import os

ip_ou_host = input('Digite o Ip ou host a ser verificado: ')

os.system('ping -n 6 {}'.format(ip_ou_host))