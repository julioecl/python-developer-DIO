class Veiculo:
    def __init__(self, cor, placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print("Ligando o motor.")
    
    def __str__(self):
        return f"{self.__class__.__name__} => {', '.join([f'{chave.capitalize()} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa,numero_rodas, carregado):
        super().__init__(cor, placa,numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")        

moto = Motocicleta('verde', 'abc1000', 2)

moto.ligar_motor()

truck = Caminhao('Vermelho', "qhn7888", 10, carregado=False)

truck.esta_carregado()

print(truck)