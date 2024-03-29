from phonenumbers import geocoder
import phonenumbers

phone = input('Digite o telefone no formato +551140028922: ')

phone_number = phonenumbers.parse(phone)

local = geocoder.description_for_number(phone_number, 'pt')

print(f'O telefone {phone} é de {local}.')
