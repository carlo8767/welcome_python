#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import argparse
import socket
import os
import sys
import struct
import time
import random
import traceback
import threading

#  NOTE: Do NOT import other libraries!

UDP_CODE = socket.IPPROTO_UDP
ICMP_ECHO_REQUEST = 8
MAX_DATA_RECV = 65535
MAX_TTL = 30


def setupArgumentParser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='A collection of Network Applications developed for SCC.231.')
    parser.set_defaults(func=ICMPPing, hostname='lancaster.ac.uk')
    subparsers = parser.add_subparsers(help='sub-command help')

    parser_p = subparsers.add_parser('ping', aliases=['p'], help='run ping')
    parser_p.set_defaults(timeout=2, count=10)
    parser_p.add_argument('hostname', type=str, help='host to ping towards')
    parser_p.add_argument('--count', '-c', nargs='?', type=int,
                          help='number of times to ping the host before stopping')
    parser_p.add_argument('--timeout', '-t', nargs='?',
                          type=int,
                          help='maximum timeout before considering request lost')
    parser_p.set_defaults(func=ICMPPing)

    parser_t = subparsers.add_parser('traceroute', aliases=['t'],
                                     help='run traceroute')
    parser_t.set_defaults(timeout=2, protocol='udp')
    parser_t.add_argument('hostname', type=str, help='host to traceroute towards')
    parser_t.add_argument('--timeout', '-t', nargs='?', type=int,
                          help='maximum timeout before considering request lost')
    parser_t.add_argument('--protocol', '-p', nargs='?', type=str,
                          help='protocol to send request with (UDP/ICMP)')
    parser_t.set_defaults(func=Traceroute)

    parser_m = subparsers.add_parser('mtroute', aliases=['mt'],
                                     help='run traceroute')
    parser_m.set_defaults(timeout=2, protocol='udp')
    parser_m.add_argument('hostname', type=str, help='host to traceroute towards')
    parser_m.add_argument('--timeout', '-t', nargs='?', type=int,
                          help='maximum timeout before considering request lost')
    parser_m.add_argument('--protocol', '-p', nargs='?', type=str,
                          help='protocol to send request with (UDP/ICMP)')
    parser_m.set_defaults(func=MultiThreadedTraceRoute)

    parser_w = subparsers.add_parser('web', aliases=['w'], help='run web server')
    parser_w.set_defaults(port=8080)
    parser_w.add_argument('--port', '-p', type=int, nargs='?',
                          help='port number to start web server listening on')
    parser_w.set_defaults(func=WebServer)

    parser_x = subparsers.add_parser('proxy', aliases=['x'], help='run proxy')
    parser_x.add_argument('--portx', '-px', type=int, nargs='?',
                          help='port number to start proxy')
    parser_x.set_defaults(portx=8085)
    parser_x.set_defaults(func=Proxy)

    parser_x.add_argument('--port', '-p', type=int, nargs='?',
                          help='port number to begin web server')
    parser_x.set_defaults(port=8080)
    parser_x.set_defaults(func=Proxy)

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    return args


class NetworkApplication:

    def checksum(self, dataToChecksum: bytes) -> int:
        csum = 0
        countTo = (len(dataToChecksum) // 2) * 2
        count = 0

        while count < countTo:
            thisVal = dataToChecksum[count + 1] * 256 + dataToChecksum[count]
            csum = csum + thisVal
            csum = csum & 0xffffffff
            count = count + 2

        if countTo < len(dataToChecksum):
            csum = csum + dataToChecksum[len(dataToChecksum) - 1]
            csum = csum & 0xffffffff

        csum = (csum >> 16) + (csum & 0xffff)
        csum = csum + (csum >> 16)
        answer = ~csum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)

        answer = socket.htons(answer)

        return answer

    # Print Ping output
    def printOneResult(self, destinationAddress: str, packetLength: int, time: float, seq: int, ttl: int,
                       destinationHostname=''):
        if destinationHostname:
            print("%d bytes from %s (%s): icmp_seq=%d ttl=%d time=%.3f ms" % (packetLength, destinationHostname,
                                                                              destinationAddress, seq, ttl, time))
        else:
            print("%d bytes from %s: icmp_seq=%d ttl=%d time=%.3f ms" % (packetLength, destinationAddress, seq, ttl,
                                                                         time))

    def printAdditionalDetails(self, host, numPacketsTransmitted, rtts):
        if len(rtts) > 0:
            print(f'--- {host} ping statistics ---')
            lossPercent = int((100.0 - 100.0 * (len(rtts) / numPacketsTransmitted)))
            print(f'{numPacketsTransmitted} packets transmitted, {len(rtts)} received, {lossPercent}% packet loss')
            avgRTT = sum(rtts) / len(rtts)
            deviations = [abs(rtt - avgRTT) for rtt in rtts]
            mdev = sum(deviations) / len(deviations)
            minRTT = min(rtts)
            maxRTT = max(rtts)
            print("rtt min/avg/max/mdev = %.3f/%.3f/%.3f/%.3f ms" % (1000 * minRTT, 1000 * avgRTT, 1000 * maxRTT,
                                                                     1000 * mdev))

    # Print one line of traceroute output
    def printMultipleResults(self, ttl: int, pkt_keys: list, hop_addrs: dict, rtts: dict, destinationHostname=''):
        if pkt_keys is None:
            print(str(ttl) + '   * * *')
            return
        # Sort packet keys (sequence numbers or UDP ports)
        pkt_keys = sorted(pkt_keys)
        output = str(ttl) + '   '
        last_hop_addr = None
        last_hop_name = None

        for pkt_key in pkt_keys:
            # If packet key is missing in hop addresses, this means no response received: print '*'
            if pkt_key not in hop_addrs.keys():
                output += '* '
                continue
            hop_addr = hop_addrs[pkt_key]

            # Get the RTT for the probe
            rtt = rtts[pkt_key]
            if last_hop_addr is None or hop_addr != last_hop_addr:
                hostName = None
                try:
                    # Get the hostname for the hop
                    hostName = socket.gethostbyaddr(hop_addr)[0]
                    if last_hop_addr is None:
                        output += hostName + ' '
                    else:
                        output += ' ' + hostName + ' '
                except socket.herror:
                    output += hop_addr + ' '
                last_hop_addr = hop_addr
                last_hop_name = hostName
                output += '(' + hop_addr + ') '

            output += str(round(1000 * rtt, 3))
            output += ' ms  '

        print(output)


class ICMPPing(NetworkApplication):

    def __init__(self, args):
        host = None
        # 1. Look up hostname, resolving it to an IP address
        try:
            host = socket.gethostbyname(args.hostname)
        except socket.gaierror:
            print('Invalid hostname: ', args.hostname)
            return

        print('Ping to: %s (%s)...' % (args.hostname, host))

        # 1. Create an ICMP socket
        try:
            self.icmpSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        except socket.error as err:
            traceback.print_exception(err)
            exit(1)

        # 2. Set a timeout on the socket
        self.icmpSocket.settimeout(args.timeout)

        # 3. Send ping probes and collect responses
        numPings = args.count
        seq_num = 0
        numPingsSent = numPings
        rtts = []
        while (numPings > 0):

            # 4. Do one ping approximately every second
            rtt, ttl, packetSize, seq = self.doOnePing(host, args.timeout, seq_num)

            # 5. Print out the RTT (and other relevant details) using the printOneResult method
            if rtt is not None:
                self.printOneResult(host, packetSize, rtt * 1000, seq, ttl)
                rtts.append(rtt)

            # 6. Sleep for a second
            time.sleep(1)

            # 7. Update sequence number and number of pings
            seq_num += 1
            numPings -= 1

        # 8. Print loss and RTT statistics (average, max, min, etc.)
        self.printAdditionalDetails(args.hostname, numPingsSent, rtts)

        # 9. Close ICMP socket
        self.icmpSocket.close()

    # Receive Echo ping reply
    def receiveOnePing(self, destinationAddress, packetID, sequenceNumSent, timeout):

        # 1. Wait for the socket to receive a reply
        echoReplyPacket = None
        isTimedout = False
        try:
            echoReplyPacket, addr = self.icmpSocket.recvfrom(MAX_DATA_RECV)
        except socket.timeout as e:
            isTimedout = True

        # 2. Once received, record time of receipt, otherwise, handle a timeout
        timeRecvd = time.time()
        if isTimedout:  # timeout
            return None, None, None, None

        # 3. Extract the IP header:

        # The first 20 bytes is the IP header:
        # (see: https://en.wikipedia.org/wiki/IPv4#/media/File:IPv4_Packet-en.svg):
        # 0          4             8          16          24           32 bits
        #  |  Version | IP Hdr  Len |     TOS   |      Total Length     |
        # |         Identification             |Flag |  Fragment offset|
        # |        TTL             |  Protocol |     Header Checksum   |
        # |           Source IP  Address(32 bits, i.e., 4 bytes)       |
        # |           Destination IP Address (32 bits, i.e., 4 bytes)  |
        # |     Option (up to 40 bytes) this is an optional field      |

        ip_header = echoReplyPacket[:20]
        version_ihl, tos, total_length, identification, flags_offset, ttl, proto, checksum, src_ip, dest_ip = struct.unpack(
            '!BBHHHBBH4s4s', ip_header)

        # Read the IP Header Length (using bit masking)
        ip_header_len_field = (version_ihl & 0x0F)

        # This field contains the length of the IP header in terms of
        # the number of 4-byte words. So value 5 indicates 5*4 = 20 bytes.
        ip_header_len = ip_header_len_field * 4

        payloadSize = total_length - ip_header_len

        # Now parse the ICMP header:
        # 0         8           16         24          32 bits
        #     Type  |    Code   |       Checksum       |
        #     Packet Identifier |       Sequence num   |
        #        <Optional timestamp (8 bytes) for     |
        #        a stateless ping>                     |
        icmpHeader = echoReplyPacket[ip_header_len:ip_header_len + 8]
        icmpType, code, checksum, p_id, sequenceNumReceived = struct.unpack('!BBHHH', icmpHeader)

        # 5. Check that the ID and sequence numbers match between the request and reply
        if packetID != p_id or sequenceNumReceived != sequenceNumSent:
            return None, None, None, None

        # 6. Return the time of Receipt
        return timeRecvd, ttl, payloadSize, sequenceNumReceived

    # NOTE: This method can be re-used by ICMP traceroute
    # Send Echo Ping Request
    def sendOnePing(self, destinationAddress, packetID, sequenceNumber, ttl=None, dataLength=0):
        # 1. Build ICMP header
        header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, packetID, sequenceNumber)

        # 2. Checksum ICMP packet using given function
        # include some bytes 'AAA...' in the data (payload) of ping
        data = str.encode(dataLength * 'A')
        my_checksum = self.checksum(header + data)

        # 3. Insert checksum into packet
        # NOTE: it is optional to include an additional 8-byte timestamp (time when probe is sent)
        # in which case, a stateless ping can be implemented: the response will contain
        # the sending time so no need to keep that state,
        # but we don't do that here (instead, we record sending time state in step 5)
        packet = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), packetID, sequenceNumber)

        if ttl is not None:
            self.icmpSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # 4. Send packet using socket
        self.icmpSocket.sendto(packet + data, (destinationAddress, 1))

        # 5. Record time of sending (state)
        timeSent = time.time()
        return timeSent

    def doOnePing(self, destinationAddress, timeout, seq_num):

        # 3. Call sendOnePing function
        packetID = random.randint(1, 65535)
        timeSent = self.sendOnePing(destinationAddress, packetID, seq_num, dataLength=48)

        # 4. Call receiveOnePing function
        timeReceipt, ttl, packetSize, seq = self.receiveOnePing(destinationAddress, packetID, seq_num, timeout)

        # 5. Compute RTT
        rtt = None
        if timeReceipt is None:
            print("Error receiveOnePing() has timed out")
        else:
            rtt = timeReceipt - timeSent

        # 6. Return total network delay, ttl, size and sequence number
        return rtt, ttl, packetSize, seq


# A partially implemented traceroute
class Traceroute(ICMPPing):

    def __init__(self, args):
        args.protocol = args.protocol.lower()

        # 1. Look up hostname, resolving it to an IP address
        self.dstAddress = None
        try:
            self.dstAddress = socket.gethostbyname(args.hostname)
            # socket.getaddrinfo(args.hostname, None, socket.AF_INET6)
        except socket.gaierror:
            print('Invalid hostname: ', args.hostname)
            return
        print('%s traceroute to: %s (%s) ...' % (args.protocol, args.hostname, self.dstAddress))

        # 2. Initialise instance variables
        self.isDestinationReached = False

        # 3. Create a raw socket bound to ICMP protocol
        self.icmpSocket = None
        try:
            self.icmpSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        except socket.error as err:
            traceback.print_exception(err)
            exit(1)

        # 4. Set a timeout on the socket
        self.icmpSocket.settimeout(args.timeout)

        # 5. Run traceroute
        self.runTraceroute()

        # 6. Close ICMP socket
        self.icmpSocket.close()

    def runTraceroute(self):

        hopAddr = None
        pkt_keys = []
        hop_addrs = dict()
        rtts = dict()
        ttl = 1

        while (ttl <= MAX_TTL and self.isDestinationReached == False):
            if args.protocol == "icmp":
                self.sendIcmpProbesAndCollectResponses(ttl)

            elif args.protocol == "udp":
                self.sendUdpProbesAndCollectResponses(ttl)
            else:
                print(f"Error: invalid protocol {args.protocol}. Use udp or icmp")
                sys.exit(1)
            ttl += 1

    # TODO: send 3 ICMP traceroute probes per TTL and collect responses
    def sendIcmpProbesAndCollectResponses(self, ttl):
        seq_num = 0
        rtts = dict()
        hop_addrs = dict()
        pkt_keys = []
        packetID = random.randint(1, 65535)
        # set TTL on socket for this hop UNDERSTAND WHAT IS DOINT
        self.icmpSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        for _ in range(3):
            seq_num += 1
            header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, packetID, seq_num)

            # 2. Checksum ICMP packet using given function
            data = str.encode(48 * 'A')
            my_checksum = self.checksum(header + data)
            header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, my_checksum, packetID, seq_num)
            packet = header + data
            timeSent = time.time()
            receive = self.icmpSocket.sendto(packet, (self.dstAddress, 0))

            trReplyPacket, hopAddr, timeRecvd = self.receiveOneTraceRouteResponse()

            pkt_keys.append(seq_num)
            if trReplyPacket is None:
                continue
            icmpType, src_ip = self.parseICMPTracerouteResponse(trReplyPacket)
            # 5. Check if we reached the destination
            if self.dstAddress == hopAddr and icmpType == 0:
                self.isDestinationReached = True
                # 6. If the response matches the request, record the rtt and the hop address
                # type, code, identifier, and sequence number
                rtts[seq_num] = timeRecvd - timeSent
                hop_addrs[seq_num] = hopAddr
            # print the intermediate hop
            elif icmpType == 11:
                rtts[seq_num] = timeRecvd - timeSent
                hop_addrs[seq_num] = hopAddr

        # 7. Print one line of the results for the 3 probes PKT_KEYS arrive empty
        self.printMultipleResults(ttl, pkt_keys, hop_addrs, rtts, args.hostname)

    # Send 3 UDP traceroute probes per TTL and collect responses
    def sendUdpProbesAndCollectResponses(self, ttl):

        hopAddr = None
        icmpType = None
        pkt_keys = []
        hop_addrs = dict()
        rtts = dict()

        numBytes = 52
        dstPort = 33439

        for _ in range(3):
            # 1. Send one UDP traceroute probe
            dstPort += 1
            timeSent = self.sendOneUdpProbe(self.dstAddress, dstPort, ttl, numBytes)

            # 2. Record a unique key (UDP destination port) associated with the probe
            pkt_keys.append(dstPort)

            # 3. Receive the response (if one arrives within the timeout)
            trReplyPacket, hopAddr, timeRecvd = self.receiveOneTraceRouteResponse()
            if trReplyPacket is None:
                # Nothing is received within the timeout period
                continue

            # 4. Extract destination port from the reply
            dstPortReceived, icmpType = self.parseUDPTracerouteResponse(trReplyPacket)

            # 5. Check if we reached the destination
            if self.dstAddress == hopAddr and icmpType == 3:
                self.isDestinationReached = True

            # 6. If the response matches the request, record the rtt and the hop address
            if dstPort == dstPortReceived:
                rtts[dstPort] = timeRecvd - timeSent
                hop_addrs[dstPort] = hopAddr

        # 7. Print one line of the results for the 3 probes
        self.printMultipleResults(ttl, pkt_keys, hop_addrs, rtts, args.hostname)

    # Parse the response to UDP probe
    def parseUDPTracerouteResponse(self, trReplyPacket):

        # 1. Parse the IP header
        dst_port = None
        #  Extract the first 20 bytes
        ip_header = struct.unpack("!BBHHHBBH4s4s", trReplyPacket[:20])

        # 2. Read the IP Header Length (using bit masking)
        ip_header_len_field = (ip_header[0] & 0x0F)

        # 3. Compute the IP header length
        # This field contains the length of the IP header in terms of
        # the number of 4-byte words. So value 5 indicates 5*4 = 20 bytes.
        ip_header_len = ip_header_len_field * 4

        # 4. Parse the outermost ICMP header which is 8 bytes long:
        # 0         8           16         24          32 bits
        #     Type  |    Code   |       Checksum       |
        #     Packet Identifier |       Sequence num   |
        # This header contains type, Code and Checksum + 4 bytes of padding (0's)
        # We only care about type field
        icmpType, _, _, _, _ = struct.unpack("!BBHHH", trReplyPacket[ip_header_len:ip_header_len + 8])

        # 5. Parse the ICMP message if it has the expected type
        if icmpType == 3 or icmpType == 11:
            ip_header_inner = struct.unpack("!BBHHHBBH4s4s", trReplyPacket[ip_header_len + 8:ip_header_len + 28])

            # This is the original IP header sent in the probe packet
            # It should be 20 bytes, but let's not assume anything and extract the length
            # of the header
            ip_header_len_field = (ip_header_inner[0] & 0x0F)
            ip_header_inner_len = ip_header_len_field * 4

            # Extract the destination port and match using source port (UDP)
            _, dst_port, _, _ = struct.unpack('!HHHH', trReplyPacket[
                ip_header_len + 8 + ip_header_inner_len: ip_header_len + 8 + ip_header_inner_len + 8])

        return dst_port, icmpType

    # TODO: parse the response to the ICMP probe
    def parseICMPTracerouteResponse(self, trReplyPacket):
        # Parsing the ip Header
        ip_header = struct.unpack("!BBHHHBBH4s4s", trReplyPacket[:20])
        ip_header_len = (ip_header[0] & 0x0F) * 4
        # Extract Icmp Header
        icmp_header = trReplyPacket[ip_header_len:ip_header_len + 8]
        icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack("!BBHHH", icmp_header)
        if icmp_type == 0:
            icmp_desc = "Echo Reply (destination reached)"
        elif icmp_type == 8:
            icmp_desc = "Echo Request"
        elif icmp_type == 11:
            icmp_desc = "Time Exceeded (intermediate hop)"
        elif icmp_type == 3:
            icmp_desc = "Destination Unreachable"
        else:
            icmp_desc = f"ICMP type {icmp_type} (unknown)"

        # Extract IP
        src_ip = socket.inet_ntoa(ip_header[8])
        return icmp_type, src_ip

    def receiveOneTraceRouteResponse(self):

        timeReceipt = None
        hopAddr = None
        pkt = None

        # 1. Receive one packet or timeout
        try:
            pkt, addr = self.icmpSocket.recvfrom(MAX_DATA_RECV)
            timeReceipt = time.time()
            hopAddr = addr[0]

        # 2. Handler for timeout on receive
        except socket.timeout as e:
            timeReceipt = None

        # 3. Return the packet, hop address and the time of receipt
        return pkt, hopAddr, timeReceipt

    def sendOneUdpProbe(self, destAddress, port, ttl, dataLength):

        # 1. Create a UDP socket
        udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, UDP_CODE)

        # 2. Use a socket option to set the TTL in the IP header
        udpSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # 3. Send the UDP traceroute probe
        udpSocket.sendto(str.encode(dataLength * '0'), (destAddress, port))

        # 4. Record the time of sending
        timeSent = time.time()

        # 5. Close the UDP socket
        udpSocket.close()

        return timeSent


""""
The program run in multithreading the sending and receiving
The result of the traceroute are printed only when an internal 
flag is set up with true.
The packet send are stored in a dictionary with a tuple
(packet_id, seq_num_probes). The key is used to verify that 
a packet is receiving back.
The output is not collected in one line because I wanted to illustrates
the fact I send three probes for ttl.
"""





# TODO: A multi-threaded traceroute implementation
class MultiThreadedTraceRoute(Traceroute):

    def __init__(self, args):
        # 1. Initialise instance variables (add others if needed)
        self.args = args
        self.ttl_flag = 0
        # ICMP THREAD VARIABLE
        self.pkt_keys_thread_send = dict()
        self.seq_num_packet_probes = 1
        self.probes_unique = 339
        self.packet_id = 999
        self.packet_received_ready = dict()
        self.list_probes = list()
        self.ttl_count = 0
        self.isDestinationReached_Thread = False

        try:
            self.dstAddress = socket.gethostbyname(args.hostname)
        except socket.gaierror:
            print('Invalid hostname: ', args.hostname)
            return
        print('%s traceroute to: %s (%s) ...' % (args.protocol, args.hostname, self.dstAddress))

        self.isDestinationReached = False
        self.icmpSocket = None
        try:
            self.icmpSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        except socket.error as err:
            traceback.print_exception(err)
            exit(1)

        self.icmpSocket.settimeout(args.timeout)
        args.protocol = args.protocol.lower()
        self.timeout = args.timeout
        self.lock = threading.Lock()

        if args.protocol == "icmp":
            self.send_complete = threading.Event()
            self.receiving_complete = threading.Event()
            self.send_thread = threading.Thread(target=self.send_probes)
            self.recv_thread = threading.Thread(target=self.receive_responses)
            self.print_thread = threading.Thread(target=self.print_packet)
            self.send_thread.start()
            self.recv_thread.start()
            self.print_thread.start()
            self.send_thread.join()
            self.recv_thread.join()
            self.print_thread.join()

        elif args.protocol == "udp":
            # UDP PART
            print("UDP IS NOT MANDATORY")

        self.icmpSocket.close()

        # Thread to send probes (to be implemented, a skeleton is provided)

    def send_probes(self):
        ttl = 1
        while ttl <= MAX_TTL and self.isDestinationReached_Thread == False:
            # Send three probes per TTL
            for _ in range(3):
                if args.protocol == "icmp":
                    self.sendIcmpProbessThread(ttl)
                elif args.protocol == "udp":
                    print("UDP IS NOT MANDATORY")
                time.sleep(0.05)
            ttl += 1
            self.probes_unique += 1
            self.list_probes.clear()
        time.sleep(2)
        with self.lock:
            self.send_complete.set()
            time.sleep(2)
            self.receiving_complete.set()

    def sendIcmpProbessThread(self, ttl):
        self.ttl_flag = ttl
        self.icmpSocket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)
        seq_num_probes = self.seq_num_packet_probes  # CAN SUBSTITUTE WITH TTL
        packet_id = self.packet_id
        header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, 0, packet_id, seq_num_probes)
        data = str.encode(48 * 'A')
        checksum = self.checksum(header + data)
        header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, 0, checksum, packet_id, seq_num_probes)
        packet = header + data
        send_time = time.time()
        self.icmpSocket.sendto(packet, (self.dstAddress, 0))
        with self.lock:
            self.pkt_keys_thread_send[(packet_id, seq_num_probes)] = (packet_id, seq_num_probes, send_time,
                                                                      self.ttl_flag)
        self.seq_num_packet_probes += 1

    def receive_responses(self):
        while not (self.send_complete.is_set() and not self.pkt_keys_thread_send):
            list_pkt = []
            if args.protocol == "icmp":
                try:
                    replyPacket, hopAddr, timeRecvd = self.receiveOneTraceRouteResponse()
                except socket.timeout:
                    continue
                if replyPacket is None:
                    break
                icm_code, src_ip, icmp_id, icmp_seq = self.parseICMPTracerouteResponseThread(replyPacket)
                with self.lock:
                    if (icmp_id, icmp_seq) not in self.pkt_keys_thread_send:
                        continue
                    else:
                        packet_id, seq_num_probes, send_time, ttl = self.pkt_keys_thread_send.pop((icmp_id, icmp_seq))
                        list_pkt.append((packet_id, seq_num_probes))

                        rtt = timeRecvd - send_time
                        self.packet_received_ready[(packet_id, seq_num_probes)] = (src_ip, icm_code, ttl,
                                                                                   list_pkt.copy(), packet_id, hopAddr,
                                                                                   rtt, args.hostname)
            elif args.protocol == "udp":
                continue

    def print_packet(self):
        self.receiving_complete.wait()
        rtts_thread = dict()
        hop_addrs_thread = dict()
        ttl_no_answer = 1
        ttl_loop = False
        count_loop = 3
        for key, values in sorted(self.packet_received_ready.items(), key=lambda kv: kv[1][2]):

            src_ip, icm_code, ttl, list_pkt, id_packet, hop_address, rtt, hosting_names = self.packet_received_ready[
                key]
            while ttl_no_answer < ttl:
                listV = [0]
                hop_addrs_thread_fake = dict()
                for _ in range(3):
                    self.printMultipleResults(ttl_no_answer, listV, hop_addrs_thread_fake,
                                              rtts_thread, hosting_names)
                ttl_loop = True
                ttl_no_answer += 1
            if src_ip == self.dstAddress and icm_code == 0:
                self.isDestinationReached = True
                rtts_thread[key] = rtt
                hop_addrs_thread[key] = hop_address
            elif icm_code == 11:
                rtts_thread[key] = rtt
                hop_addrs_thread[key] = hop_address
            count_loop -= 1
            self.printMultipleResults(ttl, list_pkt, hop_addrs_thread,
                                      rtts_thread, hosting_names)
            if ttl_loop:
                ttl_loop = False
            elif count_loop == 0:
                count_loop = 3
                ttl_no_answer = ttl + 1

    # TODO: parse the response to the ICMP probe

    def parseICMPTracerouteResponseThread(self, trReplyPacket):

        ip_header = struct.unpack("!BBHHHBBH4s4s", trReplyPacket[:20])

        # CALCULATION IP HEADER SIZE OFFSET BECAUSE CAN VARY
        ip_header_len = (ip_header[0] & 0x0F) * 4
        src_ip = socket.inet_ntoa(ip_header[8])

        # Icmp hearder
        icmp_type, icmp_code, _, _, _ = struct.unpack("!BBHHH", trReplyPacket[ip_header_len:ip_header_len + 8])

        orig_id = orig_seq = None

        if icmp_type == 11 or icmp_type == 3:  # Time Exceeded or Dest Unreachable
            inner_ip_offset = ip_header_len + 8
            inner_ip_header = struct.unpack("!BBHHHBBH4s4s", trReplyPacket[inner_ip_offset:inner_ip_offset + 20])
            inner_ip_len = (inner_ip_header[0] & 0x0F) * 4

            inner_icmp_offset = inner_ip_offset + inner_ip_len
            _, _, _, orig_id, orig_seq = struct.unpack("!BBHHH", trReplyPacket[inner_icmp_offset:inner_icmp_offset + 8])
        elif icmp_type == 0:  # Echo Reply
            _, _, _, orig_id, orig_seq = struct.unpack("!BBHHH", trReplyPacket[ip_header_len:ip_header_len + 8])
            self.isDestinationReached_Thread = True
        return icmp_type, src_ip, orig_id, orig_seq


# A basic multi-threaded web server implementation

# You can test the web server as follows:
# First, run the server in the terminal: python3 NetworkApplications.py web
# Then, copy the following and paste to a browser's address bar: 127.0.0.1:8080/index.html
# NOTE: the index.html file needs to be downloaded from the Moodle (Dummy HTML file)
# and copied to the folder where you run this code
class WebServer(NetworkApplication):

    def __init__(self, args, stop_web_server_proxy):
        self.port_web_server = args.port
        self.connection_web_server = ""
        self.stop_event = stop_web_server_proxy
        print('> Web Server starting on port: %i...' % args.port)

        # 1. Create a TCP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2. Bind the TCP socket to server address and server port
        server_socket.bind(("", args.port))
        # 3. Continuously listen for connections to server socket
        server_socket.listen(100)
        print(">> Server listening on port", args.port)

        try:
            while not self.stop_event.is_set():
                try:
                    # 4. Accept incoming connections connection socket_repressent the conncetion
                    connection_socket, addr = server_socket.accept()
                    print(f">>> Connection established with {addr}")
                except OSError:
                    break
                self.connection_web_server = connection_socket
                # 5. Create a new thread to handle each client request
                thread_web_server = threading.Thread(target=self.handleRequest, args=(connection_socket,), daemon=True)
                thread_web_server.start()
        except Exception as e:
            print(f"Error web server handling request: {e}")
        finally:
            server_socket.close()

    def extracting_path(self, url):
        if "://" in url:
            url = url.split("://", 1)[1]
        if url.startswith("www."):
            url = url[4:]

        if "/" in url:
            host, path = url.split("/", 1)
            path = "/" + path
        else:
            path = "/"
        return host, path

    def handleRequest(self, connection_socket):
        try:
            message = connection_socket.recv(MAX_DATA_RECV).decode()
            hostname, path_extraction = self.extracting_path(message.split()[1])
            # HTTP REQUEST
            remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname(hostname)
            remote_socket.connect((remote_ip, 80))
            # verify HOW TO EXTRACT PATH
            request_with_agent = (
                f"GET {path_extraction} HTTP/1.1\r\n"
                f"Host: {hostname}\r\n"
                f"User-Agent: Mozilla/5.0 (compatible; SimpleClient/1.0)\r\n"
                f"Connection: close\r\n\r\n")
            # ADD USER AGENT OTHERWISE IS NOT POSSIBLE AUTHENTICATE"
            "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent"
            remote_socket.sendall(request_with_agent.encode('utf-8'))
            response_data = b""
            try:
                while True:
                    chunk = remote_socket.recv(4096)  # Buffer size
                    if not chunk:
                        break  # Connection closed by server
                    response_data += chunk
            except socket.error as e:
                print(f"Error receiving data: {e}")

            connection_socket.send(response_data)

        except IOError as e:

            # Handle file not found error
            print(f'the error is {e}')
            error_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            error_response += "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
            connection_socket.send(error_response.encode())

        except Exception as e:
            print(f"Error webserver: {e}")

        finally:
            # Close the connection socket
            connection_socket.close()


""""
Every request coming from the client 
will be forward from the Proxy to the WebServer if the cache
is not present.
When the Webserve is retrieve properly the page with HTTP status 200 ok, 
the content ist stored in a cache that match the host name.
The content of the cache it will erase when the application stop. 
Further, there is the change to run the application with 
two optional argument : -px , which set the proxy port 
and -p , which set the webserver port.
Alternatively, the default port are : proxy 8085 
web server: 8080
"""

#  TODO: A proxy implementation
class Proxy(NetworkApplication):

    def __init__(self, args):
        print('> Proxy starting on port: %i...' % args.portx)
        self.path = "./cache_page"
        self.args = args
        self.stop_web_server_proxy = threading.Event()
        server_socket_proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket_proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket_proxy.bind(("", args.portx))
        server_socket_proxy.listen(100)
        print(">> Server proxy listening on port", args.portx)
        self.server_memo_page = dict()
        # START UP WEB SERVER
        web_server_thread = threading.Thread(target=WebServer, args=(args, self.stop_web_server_proxy), daemon=True)
        web_server_thread.start()

        try:
            while not self.stop_web_server_proxy.is_set():
                try:
                    # ACCEPT INCOMING REQUEST
                    connection_socket_proxy, addr_proxy = server_socket_proxy.accept()

                except OSError:
                    break
                # CREATE A NEW THREAD FOR EVERY CLIENT REQUEST
                print(f">>> Connection established with {addr_proxy}")
                proxy_thread = threading.Thread(target=self.handleRequest_request_proxy,
                                                args=(connection_socket_proxy,), daemon=True)
                proxy_thread.start()
        except Exception as e:
            print(f"Error proxy request: {e}")
        finally:
            self.clear_cache_directory()
            server_socket_proxy.close()

    def extracts_main_domain(sefl, url):
        if "://" in url:
            url = url.split("://", 1)[1]
        url = url.split("/", 1)[0]
        url = url.split(":", 1)[0]
        parts = url.split(".")
        if len(parts) >= 2:
            final_result = "".join(parts[0:-1])
            return final_result
        return parts[0]

    def clear_cache_directory(self):
        if not os.path.isdir(self.path):
            return
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print("Error removing file:", file_path, e)

    def reading_cache(self, path):
        content = b''
        try:
            with open(path, 'rb') as r:
                content = r.read()
        except FileNotFoundError:
            return content
        return content

    def writing_in_cache(self, path, data_receive):
        try:
            with open(path, 'wb') as w:
                w.write(data_receive)
        except Exception as e:
            print(f'error in writing {e}')

    def handleRequest_request_proxy(self, connection_socket_proxy):
        try:
            message = connection_socket_proxy.recv(MAX_DATA_RECV).decode()
            name_file = self.extracts_main_domain(message)
            self.server_memo_page[name_file] = b''
            # READ THE CACHE
            search_file = self.path + "/" + name_file + ".txt"
            cache_present = self.reading_cache(search_file)

            if cache_present.decode() == "":
                print(">>>> Contact the web server")
                # CALL THE SERVER
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ws_sock:
                    # ENTER THE PORT OF THE WEB SERVER CARLO
                    ws_sock.connect(("127.0.0.1", args.port))
                    # 2. Send the message
                    ws_sock.sendall(message.encode())
                    # 3. Receive response
                    response_content = ws_sock.recv(MAX_DATA_RECV)
                    print(f'The response contains:{response_content}')
                    # WRITE THE CACHE IF 200
                    if  "200 OK" in response_content.decode():
                        self.writing_in_cache(search_file, response_content)
                    else:
                        raise Exception

                    response = b'HTTP/1.1 200 OK\r\n\r\n'
                    response += response_content
                connection_socket_proxy.sendall(response)
                print(">>>>> Answer is completed")

            else:
                print(">>> Retrieve from the cache...")
                response = b'HTTP/1.1 200 OK\r\n\r\n'
                response += cache_present
                connection_socket_proxy.sendall(response)
                print(">>>>> Answer is completed")


        except IOError:
            # Handle file not found error
            print(">>> error proxy")
            error_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            error_response += "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
            connection_socket_proxy.send(error_response.encode())

        except Exception as e:
            print(f"Error handling request: {e}")
            print(">>> error proxy")
            error_response = "HTTP/1.1 404 Not Found\r\n\r\n"
            error_response += "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n"
            connection_socket_proxy.send(error_response.encode())

        finally:
            # Close the connection socket
            connection_socket_proxy.close()


# NOTE: Do NOT delete the code below
if __name__ == "__main__":
    args = setupArgumentParser()
    args.func(args)