#!/usr/bin/env python3
"""
Simple traceroute implemented in pure Python using raw ICMP echo requests.
Run as root (sudo python3 this_file.py).
"""

import socket
import struct
import time
import select

ICMP_ECHO_REQUEST = 8
ICMP_ECHO_REPLY   = 0
ICMP_TIME_EXCEEDED = 11

def checksum(data: bytes) -> int:
    """Compute the Internet Checksum for the given data.
    Returns a 16-bit checksum as an integer.
    """
    if len(data) % 2:
        data += b'\x00'
    s = 0
    # sum 16-bit words, high byte first (network order)
    for i in range(0, len(data), 2):
        word = data[i] << 8 | data[i+1]
        s += word
        s &= 0xffffffff  # keep within 32 bits
    # add carries
    while (s >> 16):
        s = (s & 0xffff) + (s >> 16)
    # one's complement
    s = ~s & 0xffff
    return s

def make_icmp_packet(identifier: int, sequence: int, payload: bytes = b'') -> bytes:
    """Build an ICMP echo request packet with correct checksum."""
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, identifier, sequence)
    body = payload
    chksum = checksum(header + body)
    # pack again with correct checksum
    header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, chksum, identifier, sequence)
    return header + body

def traceroute(dst_host: str, max_hops: int = 30, timeout: float = 2.0, tries_per_hop: int = 3):
    dst_addr = socket.gethostbyname(dst_host)
    print(f"traceroute to {dst_host} ({dst_addr}), {max_hops} hops max")

    # We'll use a single raw socket for receiving ICMP (listening for responses)
    # and a separate UDP/ICMP socket for sending while changing TTL.
    recv_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    recv_sock.settimeout(timeout)

    # We'll identify our ICMP packets with PID & changing sequence
    pid = (os.getpid() & 0xFFFF)
    sequence = 0

    for ttl in range(1, max_hops + 1):
        print(f"{ttl:2d} ", end='', flush=True)
        hop_addr = None
        hop_name = None
        elapsed_list = []

        for attempt in range(tries_per_hop):
            # Create a new sending socket so we can set TTL per send.
            send_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            send_sock.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
            # Optional: set non-blocking send timeout
            send_sock.settimeout(timeout)

            sequence += 1
            payload = struct.pack("d", time.time())  # send timestamp in body
            pkt = make_icmp_packet(pid, sequence, payload)
            send_time = time.time()
            try:
                send_sock.sendto(pkt, (dst_addr, 0))
            except PermissionError:
                send_sock.close()
                recv_sock.close()
                raise

            # Wait for a reply on recv_sock
            addr = None
            try:
                # We use select to allow timeout across platforms
                ready = select.select([recv_sock], [], [], timeout)
                if ready[0]:
                    data, addr = recv_sock.recvfrom(65535)
                    recv_time = time.time()
                else:
                    # timeout
                    recv_time = None
            except socket.timeout:
                recv_time = None
            except Exception as e:
                recv_time = None
                # continue to next attempt

            send_sock.close()

            if not addr or recv_time is None:
                print("  *", end='', flush=True)
                elapsed_list.append(None)
                continue

            icmp_header_offset = 20  # assume IPv4 header with no options
            icmp_header = data[icmp_header_offset:icmp_header_offset+8]
            icmp_type, icmp_code, icmp_chksum, icmp_id, icmp_seq = struct.unpack('!BBHHH', icmp_header)

            # record hop address
            hop_addr = addr[0]
            # Try reverse DNS once
            if hop_name is None:
                try:
                    hop_name = socket.gethostbyaddr(hop_addr)[0]
                except Exception:
                    hop_name = hop_addr

            # If the reply is "time exceeded" (type 11), the ICMP payload contains
            # the original IP header + first 8 bytes of the original datagram.
            # For simplicity we just report the responding address and RTT.
            if icmp_type == ICMP_TIME_EXCEEDED:
                rtt = (recv_time - send_time) * 1000.0
                elapsed_list.append(rtt)
                print(f"  {hop_name} ({hop_addr})  {rtt:.1f} ms", end='', flush=True)
            elif icmp_type == ICMP_ECHO_REPLY and icmp_id == pid:
                # we've reached destination
                rtt = (recv_time - send_time) * 1000.0
                elapsed_list.append(rtt)
                print(f"  {hop_name} ({hop_addr})  {rtt:.1f} ms", end='', flush=True)
                # print newline then return
                print()
                recv_sock.close()
                return
            else:
                # other ICMP types (e.g., destination unreachable) — still report
                rtt = (recv_time - send_time) * 1000.0
                elapsed_list.append(rtt)
                print(f"  {hop_name} ({hop_addr})  {rtt:.1f} ms", end='', flush=True)

        # after tries for this ttl
        print()
    recv_sock.close()
    print("Reached max hops without receiving a final echo-reply.")

if __name__ == "__main__":
    import os, sys
    if len(sys.argv) < 2:
        print("Usage: sudo python3 traceroute_icmp.py <destination> [max_hops]")
        sys.exit(1)
    dest = sys.argv[1]
    maxh = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    traceroute(dest, max_hops=maxh)
