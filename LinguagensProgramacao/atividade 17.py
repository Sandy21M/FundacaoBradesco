tipo_lavagem=int(input('Informe o tipo de lavagem desejar: 1-Para lavagem simples ou 2- Para lavagem completa'))
tipo_pagamento=int(input('Informe o tipo de pagamento: 1- A vista ou 2- no cartão de crédito'))

if tipo_lavagem==1:
    if tipo_pagamento==1:
      print('VALOR 30 REAIS')
    else:
        print('VALOR 50 REAIS')
else:
    if tipo_lavagem==2:
      print('VALOR 35 REAIS')
    else:
      print('VALOR 55 REAIS')