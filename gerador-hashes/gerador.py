import hashlib

texto = input('Digite o texto a ser gerado a hash: ')

print('''Digite em que formato deseja criar a HASH: 
                 1 - MD5
                 2 - SHA1
                 3 - SHA256
                 4 - SHA512
                 ''')

menu = int(input())

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print(resultado)
elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print(resultado)
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print(resultado)
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print(resultado)
else:
    print('Não foi possível encontrar essa opção.')