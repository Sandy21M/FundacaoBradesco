tipodeingresso=int(input('Digite a opção: 1-Para ingresso Vip ou 2-Para ingresso comum \n '))
combo= int(input('Digite a opção: 1-Com o combo ou 2-Sem o combo \n'))

if(tipodeingresso==1):
 if(combo==2):
    print('O valor é de R$80,00 reais \n')

 else:
    print('O valor é de R$ 110,00 reais\n')

else:
 if(combo==2):
     print('O valor é de R$ 40,00 reais')

 else:
  print('O valor é de R$ 70,00 reais')