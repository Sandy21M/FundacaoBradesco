sabor=int(input('Informe o tipo de sorvete desejado: 1-Para chocolate ou 2-Para morango:\n'))
quantidade=int(input('Informe a quantidade desejada:\n'))

if sabor==1:
   if quantidade>=3:
       print('VOCÊ TEM O DESCONTO DE 10% \n')

   else:
    print('VOCÊ TEM O DESCONTO DE 5% \n')
elif sabor==2:
    print('VOCÊ NÃO TEM DESCONTO NENHUM- \n')
