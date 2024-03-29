from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print(f'Carro: {piloto} | KM: {trajeto}')
        trajeto += velocidade
        time.sleep(0.5)
    
t_carro1 = Thread(target=carro, args=[10, 'Bruno'])
t_carro2 = Thread(target=carro, args=[12.5, 'Julio'])

t_carro1.start() # start para iniciar os processos simultâneos
t_carro2.start()