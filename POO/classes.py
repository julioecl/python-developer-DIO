class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def correr(self):
        print('Vrummmmm...')
    
    def parar(self):
        print(f'Parando a bicicleta {self.modelo}...')
        print(f'Bicicleta {self.modelo} parada!')
    
    def buzinar(self):
        print('Plim plim...')    
        
    def mostrar_infos(self):
        print(f'Cor: {self.cor.capitalize()}')
        print(f'Modelo: {self.modelo.capitalize()}')
        print(f'Ano: {self.ano}')
        print(f'Valor: R${self.valor:.2f}')
    
    # def __str__(self) -> str:
    #     return f'{self.__class__.__name__} | Cor: {self.cor.capitalize()} | Modelo: {self.modelo.capitalize()} | Ano: {self.ano} | Valor: R${self.valor:.2f}'
    
    def __str__(self):
        return f"{self.__class__.__name__} => {', '.join([f'{chave.capitalize()} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)

print(b1)
    

