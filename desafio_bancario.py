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

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
      
    if opcao.lower() == "d":
        while True:
            valor = int(input("Qual valor deseja depositar? "))
            if valor > 0:
                saldo += valor
                print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!') 
                extrato += f'Depósito de R$ {valor:.2f} +\n'
                break
            else:
                print("Valor incorreto! Por favor digite um valor válido: ")
    elif opcao.lower() == "s":        
        while True:            
            if numero_saques < 3:            
                valor = int(input("Qual valor deseja sacar? "))
                if valor > 0:
                    if valor <= saldo:     
                        if valor <= limite:
                            saldo -= valor                           
                            numero_saques += 1
                            print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
                            extrato += f'Saque de    R$ {valor:.2f} - \n'
                            break
                        else:
                            print("Valor máximo por saque excedido.")                        
                    else:
                        print("Valor superior ao saldo em conta.")                    
                else:
                    print("Valor incorreto! Por favor digite um valor válido: ")                
            else:
                print("Quantidade de saques diários excedida. Voltando ao menu principal...")
                break          
    elif opcao.lower() == "e":
        if saldo == 0:
            extrato += f'Saldo de    R$ {saldo:.2f} *'
        else:
            extrato += f'Saldo de    R$ {saldo:.2f} +'
        print(extrato)
        break
    elif opcao.lower() == "q":
        print("Sair")
        break
    else:
        print("Opção inválida, tente novamente.")
