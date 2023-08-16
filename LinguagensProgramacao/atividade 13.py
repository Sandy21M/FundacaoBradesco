maior=0
menor=9999
media=0
contador=0
soma=0
media=0

numero=int(input('Digite o número desejado: \n'))

while numero > 0:
   if numero < menor:
      menor = numero
   elif numero > maior:
      maior = numero
   soma = soma + numero
   contador = contador +1
   numero=int(input('Digite o número: \n'))

media = soma / contador

print(maior)
print(menor)
print(media)