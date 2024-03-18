# C = int(input()) 

# numbers = []


# for i in range (C):
#     values = input()
    
#     numbers.append(values)
    
#     if int(numbers[i]) <= 8000:
#         print("Inseto!")
#     else: 
#         print("Mais de 8000!")

# T = int(input())

# garrafas = []

# for i in range(T):
  
#     n, k = input().split()
#     n = int(n)
#     k = int(k)
#     if k > n:
#         print(n)
#     else:
#         div_inteira = n // k        
#         sobra = n - (div_inteira * k)        
#         total = div_inteira + sobra
#         print(total)

a = input() 
b = input() 
c = input() 

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        elif c == 'onivoro':
            print('pomba')
    elif b == 'mamifero':
        if c == 'onivoro':
            print('homem')
        elif c == 'herbivoro':
            print('vaca')
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        elif c == 'herbivoro':
            print('lagarta')
    elif b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        elif c == 'onivoro':
            print('minhoca')