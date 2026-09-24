import socket 

print("Port Scanner Project V-1.0")

ip = input("Enter the IP: ")
try:
    port = (input("Enter the port number: "))
    port = int(port)
except:
    print("Invalid port")
    exit()

print("The IP to be scanned is: ", ip, " and the port is: ", port )

if (port < 1 or port > 65535):
    print("Invalid Port number")
    exit()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.settimeout(1)
        s.connect((ip,port))
        print("Port is open.")
    except socket.error:
        print("Port is closed.")