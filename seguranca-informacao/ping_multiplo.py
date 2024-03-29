import os
import time

with open('./seguranca-informacao/hosts.txt') as file:
    dump = file.read().splitlines()
    for ip in dump:
        print(f'Verificando o ip: {ip}')
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(5)