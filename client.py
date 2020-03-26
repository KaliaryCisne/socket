import socket

from pip._vendor.distlib.compat import raw_input

HOST = '192.168.11.3'  # Endereco IP do Servidor
PORT = 5000  # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print('Para sair use CTRL+X\n')
msg = raw_input()
while msg != '\x18':
    print('Digite sua mensagem: \n')
    print("kaliary: ", msg, "\n")
    udp.sendto(msg.encode(), dest)
    msg = raw_input()
udp.close()
