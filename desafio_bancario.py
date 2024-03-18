# Saque, depósito e extrato OK
# Depósito -> valor positivo OK
# Saque -> máximo de 3 saques / R$ 500,00 por saque / Caso não tenha saldo, exibir mensagem / Armazenar valor de saques OK
# Extrato -> Listar saques e depósitos  OK

menu = """

[d] => Depositar
[s] => Sacar
[e] => Extrato
[q] => Sair
 
"""

def exibir_menu(saldo, extrato, numero_saques, numero_depositos):
    saldo = 0
    extrato = ""
    numero_saques = 0
    numero_depositos = 0
    LIMITE_SAQUES = 3
    limite = 500
    while True:        
        opcao = input(menu)
        if opcao.lower() == "d":
            depositar(saldo, extrato, numero_depositos)         
        elif opcao.lower() == "s":
            sacar(numero_saques, limite, saldo, extrato, LIMITE_SAQUES)
        elif opcao.lower() == "e":
            mostrar_extrato(saldo, extrato, numero_depositos, numero_saques)
        elif opcao.lower() == "q":
            print("Sair")
            return            
        else:
            print("Opção inválida, tente novamente.")
    

def sacar(numero_saques, limite ,saldo, extrato, LIMITE_SAQUES):
    while True:            
        if numero_saques < LIMITE_SAQUES:            
            valor = int(input("Qual valor deseja sacar? "))
            if valor > 0:
                if valor <= saldo:     
                    if valor <= limite:
                        saldo -= valor                           
                        numero_saques += 1
                        print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
                        extrato += f'Saque de    R$ {valor:.2f} - \n'
                        return extrato, saldo, numero_saques
                    else:
                        print("Valor máximo por saque excedido.")                        
                else:
                    print("Valor superior ao saldo em conta.")                    
            else:
                print("Valor incorreto! Por favor digite um valor válido: ")                
        else:
            print("Quantidade de saques diários excedida. Voltando ao menu principal...")
            return

def depositar(saldo, extrato, numero_depositos):
    while True:
        valor = int(input("Qual valor deseja depositar? "))
        if valor > 0:
            saldo += valor
            print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!') 
            extrato += f'Depósito de R$ {valor:.2f} +\n'
            numero_depositos += 1
            return saldo, extrato, numero_depositos
        else:
            print("Valor incorreto! Por favor digite um valor válido: ")

def mostrar_extrato(saldo, extrato, numero_depositos, numero_saques):
    while True:
        if numero_depositos == 0 and numero_saques == 0:
            print('Sem movimentação bancária!')
        elif saldo == 0:
            extrato += f'Saldo de    R$ {saldo:.2f} *'
        else:
            extrato += f'Saldo de    R$ {saldo:.2f} +'
        print(extrato)
        break
    
def cadastrar_usuario():
    pass

saldo = 0
extrato = ""
numero_saques = 0
numero_depositos = 0

exibir_menu(saldo, extrato, numero_saques, numero_depositos)

