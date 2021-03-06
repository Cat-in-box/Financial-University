import socket

global clients
clients = {} # Словарь где храним адреса клиентов
connectings = []

def login(sock, addr):
	if addr[0] not in clients: # Если такого клиента нету , то добавить
		sock.sendto(str.encode('Жду регистрацию'), addr)
		a = sock.recv(1024).decode()
		b = sock.recv(1024).decode()
		clients[addr[0]] = (a, b)
		sock.sendto(str.encode(a), addr)
	else:
		sock.sendto(str.encode(clients[addr[0]][0]), addr)
		flag = True
		while flag:
			sock.sendto(str.encode('Жду пароль'), addr)
			if clients[addr[0]][1] == sock.recv(1024).decode():
				flag = False
				sock.sendto(str.encode(clients[addr[0]][0]), addr)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('', 9090))
print ('Start Server')

while True:
	conn, addr = sock.recvfrom(1024)
	connectings.append(addr)
	print (addr[0], addr[1])
	if conn.decode() == 'Connect to server':
		login(sock, addr)
	else:
		for connect in connectings:
			sock.sendto(conn, connect)