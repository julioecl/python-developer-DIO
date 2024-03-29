import hashlib

arq1 = './comparar-hashes/a.txt'
arq2 = './comparar-hashes/b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arq1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arq2, 'rb').read())

print(f'O conteúdo do arquivo arquivo 1 é: {(hash1).hexdigest()}')
print(f'O conteúdo do arquivo arquivo 2 é: {(hash2).hexdigest()}')

if hash1.digest() == hash2.digest():
    print('São conteúdos iguais')
else:
    print('São conteúdos diferentes')