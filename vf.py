#importando a biblioteca phonenumbers
import phonenumbers
#importando o método geocoder
from phonenumbers import  geocoder
#pedindo ao usuário  a entrada de um número válido;
phone = input("Digite o telefone no formato +(código do país/código da região/número do telefone:  ")
#transformando a string da variavel phone em um numero de telefone
phone_number = phonenumbers.parse(phone)
#printando a localização do número passado em portugues
print(geocoder.description_for_number(phone_number, 'pt'))