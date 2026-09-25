import socket 
import time
import threading


print("Port Scanner Project V-1.0")

ip = input("Enter the IP: ")
try:
    start_port = (input("Enter the starting port number: "))
    start_port = int(start_port)
    last_port = input("Enter the last port number: ")
    last_port = int(last_port)
except:
    print("Invalid port")
    exit()

print("The IP to be scanned is: ", ip, " and the ports to be scanned are: ", start_port, last_port )

if (start_port < 1 or start_port > 65535):
    print("Invalid start Port number")
    exit()

if (last_port < 1 or last_port > 65535):
    print("Invalid last Port number ")
    exit()

if (start_port > last_port):
    print("Invalid range")
    exit()

open_ports = []
def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(1)
            s.connect((ip,port))
            try:
                service_name = socket.getservbyport(port, "tcp")
            except OSError:
                service_name = "Unknown"
            port_info = (port, service_name)
            open_ports.append(port_info)
        except socket.error:
            # print("Port", port,  "is closed.")
            pass


threads=[]

for port in range(start_port, last_port + 1):
    t = threading.Thread(target = scan_port, args = (port,))
    threads.append(t)

start_time = time.perf_counter()

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.perf_counter()
elapsed_time = end_time - start_time


if open_ports:
    print("\nOpen Ports:")
    for port, service in open_ports:
        print(f"  {port}/tcp  →  {service}")
else:
    print("\nNo open ports found.")

print(f"Scan completed in: {elapsed_time:.2f} seconds")