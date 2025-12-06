# http_client.py
import socket
import sys


def http_get_client(host, path, port=80):
    try:
        # 1. Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit(1)

    try:
        # Resolve hostname to IP address
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Hostname {host} could not be resolved.")
        client_socket.close()
        sys.exit(1)

    # 2. Connect the socket to the server
    try:
        client_socket.connect((remote_ip, port))
        print(f"Connected to {host} ({remote_ip}) on port {port}")
    except socket.error as e:
        print(f"Connection to {host}:{port} failed: {e}")
        client_socket.close()
        sys.exit(1)

    # 3. Format HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    second_request = (
    f"GET {path} HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    f"User-Agent: Mozilla/5.0 (compatible; SimpleClient/1.0)\r\n"
    f"Connection: close\r\n\r\n"
)


    try:
        # 4. Send the request
        client_socket.sendall(second_request.encode('utf-8'))
        print("--- Request Sent ---")
        print(request.strip())
        print("--------------------")
    except socket.error as e:
        print(f"Error sending data: {e}")
        client_socket.close()
        sys.exit(1)

    # 5. Receive the response
    response_data = b""
    print("--- Response Received ---")
    try:
        while True:
            chunk = client_socket.recv(4096)  # Buffer size
            if not chunk:
                break  # Connection closed by server
            response_data += chunk
    except socket.error as e:
        print(f"Error receiving data: {e}")
    finally:
        # 7. Close the socket
        client_socket.close()
        print("-----------------------")
        print("Connection closed.")

    # Try to decode and print the response
    try:
        print(response_data.decode('utf-8', errors='ignore'))
    except Exception as e:
        print(f"Could not decode response: {e}")
        print("Raw response bytes:", response_data[:500])  # Print first 500 bytes if decode fails


if __name__ == "__main__":

    http_get_client("neverssl.com", "/", 80)