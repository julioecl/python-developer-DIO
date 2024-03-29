import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco)

ip2 = '192.168.0.1/24'

rede = ipaddress.ip_network(ip)

print(rede)