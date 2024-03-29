import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com sucesso!')

host = 'localhost'
porta = 5433
mesagem = 'Olá Servidor! Testando conexão'

try:
    print(f'Cliente: {mesagem}')
    s.sendto(mesagem.encode(), (host, porta))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print(f'Cliente: {dados}')
finally:
    print('Cliente: Fechando conexão.')
    s.close()