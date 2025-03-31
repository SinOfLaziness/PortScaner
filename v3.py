import socket
import sys
from threading import Thread


def check_port(host, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)


def scan_ports(host, start_port, end_port):
    open_ports = []
    threads = []
    for port in range(start_port, end_port + 1):
        thread = Thread(target=check_port, args=(host, port, open_ports))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return open_ports


if __name__ == "__main__":
    host = 'localhost'
    start_port = 1
    end_port = 1024

    flag = True
    for i in sys.argv[1:]:
        if flag:
            if i and not (int(i) < 1 or int(i) > 65535):
                start_port = int(i)
            flag = False
        else:
            if i and not (int(i) < 1 or int(i) > 65535):
                end_port = int(i)
            break

    open_ports = scan_ports(host, start_port, end_port)
    print(f"Открытые TCP порты на {host}: {open_ports}")
