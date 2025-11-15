import unittest
import socket
from unittest.mock import patch
import sys


from pythonPack.workshop.NetworkApplications import setupArgumentParser


class TestArgumentParser(unittest.TestCase):



    def test_socket_ICMP(self):
        # AF_INET address type, type_properties, types connection 166 explanation PAGE 434

        """
        The ICMP header contains a fixed four-byte section with Type, Code, and Checksum fields,
        followed by a variable-length "Rest of Header" section that depends on the message ty
        # Step 1: Build header with checksum = 0
    header = struct.pack('!BBHHH', 8, 0, 0, identifier, sequence)

        # Step 2: Add payload (e.g., timestamp)
        payload = struct.pack('d', time.time())

        # Step 3: Compute checksum
        chksum = checksum(header + payload)

        # Step 4: Rebuild header with correct checksum
        header = struct.pack('!BBHHH', 8, 0, chksum, identifier, sequence)

        # Step 5: Combine
        packet = header + payload

        send_sock.sendto(packet, (destination_ip, 0))
send_time = time.time()





        """
        server_destination = "google.com"
        port = 65535
        _host_name_ipv4 = socket.gethostbyname(server_destination)
        # NEED SUDO PRIVILEDGE
        socket_interface = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.UDPLITE_RECV_CSCOV)

        # 2. Use a socket option to set the TTL in the IP header
        socket_interface.setsockopt(socket.SOL_IP, socket.IP_TTL, 2)

        result_sending = socket_interface.sendto(server_destination)
        socket_interface.settimeout(2)

    def extract_main_domain(sefl, url):
        # Remove scheme if present
        if "://" in url:
            url = url.split("://", 1)[1]

        # Remove path
        url = url.split("/", 1)[0]

        # Remove port if present
        url = url.split(":", 1)[0]

        # Split domain parts
        parts = url.split(".")

        # Return main domain (second-to-last part)
        if len(parts) >= 2:

            final_result = "".join(parts[0:-1])
            return final_result
        return parts[0]

    def test_split (self):
        content = 'GET http://neverssl.ss.tn.com/ HTTP/1.1Host: neverssl.comUser-Agent: curl/8.5.0Accept: */*Proxy-Connection: Keep-Alive'
        pa = self.extract_main_domain(content)
        assert pa == "neverssltn"
        lines = content.splitlines()
        filename = content.split()[1]
        split_again = filename.rsplit(".", 1)[0]
        split_final = split_again.split("//")[1]
        # Find the line that starts with "Host:"
        host_line = next((line for line in lines if line.startswith("Host:")), None)
        # Extract the host value
        if host_line:
            host = host_line.split(":", 1)[1].strip()
            print(host)


    def test_mtrace(self):
        test_args = ['program_name', 'mtroute', 'example.com']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.hostname, 'example.com')
            self.assertEqual(args.protocol, 'udp')

    def test_ping_default(self):
        test_args = ['program_name', 'ping', 'example.com']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.hostname, 'example.com')
            self.assertEqual(args.timeout, 2)
            self.assertEqual(args.count, 10)
            self.assertEqual(args.func.__name__, 'ICMPPing')

    def test_ping_custom_count_timeout(self):
        test_args = ['program_name', 'ping', 'example.com', '--count', '5', '--timeout', '3']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.hostname, 'example.com')
            self.assertEqual(args.count, 5)
            self.assertEqual(args.timeout, 3)
            self.assertEqual(args.func.__name__, 'ICMPPing')

    def test_traceroute_defaults(self):
        test_args = ['program_name', 'traceroute', 'example.com']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.hostname, 'example.com')
            self.assertEqual(args.timeout, 2)
            self.assertEqual(args.protocol, 'udp')
            self.assertEqual(args.func.__name__, 'Traceroute')

    def test_web_custom_port(self):
        test_args = ['program_name', 'web', '--port', '9000']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.port, 9000)
            self.assertEqual(args.func.__name__, 'WebServer')

    def test_proxy_default_port(self):
        test_args = ['program_name', 'proxy']
        with patch.object(sys, 'argv', test_args):
            args = setupArgumentParser()
            self.assertEqual(args.port, 8000)
            self.assertEqual(args.func.__name__, 'Proxy')

if __name__ == '__main__':
    unittest.main()
