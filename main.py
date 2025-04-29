import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

request = "GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n"
client.send(request.encode('utf-8'))

response = b""
while True:
    part = client.recv(4096)
    if not part:
        break
    response += part
    
 with open("google_response.html", "w", encoding="utf-8") as f:
    f.write(response.decode('utf-8', errors='replace'))

print(response.decode('utf-8', errors='replace'))
