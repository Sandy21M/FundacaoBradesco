numero_total=int(input('Informe o número de horas trabalhadas:'))
valor_hora= float(input('Informe o valor do salário por hora:'))


if numero_total > 160:
    sbase= 160 * valor_hora
    hora_extra= (((numero_total - 160)* valor_hora) * 1.5)
    salario_total= sbase + hora_extra
    print('O salário total é de: R$', salario_total)

else:
    sbase= 160 * valor_hora
    print('O salário total é de: R$',sbase)




