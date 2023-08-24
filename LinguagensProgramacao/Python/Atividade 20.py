operacao = int(input('Digite um número: 1-Para soma \n 2-Para subração\n 3-Para subtração\n 4-Para divisão\n 0-Para sair'))
 
while operacao !=0:
    if operacao >=0 and operacao <4:
        num1 = float(input('Digite um número:'))
        num2 = float(input('Digite um número:'))
        if operacao==1:
            resultado =  num1 + num2
        elif operacao == 2: 
            resultado = num1 - num2
        elif operacao == 3:
            resultado = num1 * num2
        elif operacao == 4:
            resultado = num1 / num2
        print ('O resultado é:', resultado )    
        operacao = int(input('Digite um número: 1-Para soma \n 2-Para subração\n 3-Para subtração\n 4-Para divisão \n 0-Para sair'))
    else:
        print('Operação invalida.')
        operacao = int(input('Digite um número: 1-Para soma \n 2-Para subração\n 3-Para subtração\n 4-Para divisão\n 0-Para sair '))
print('Opção de saída realizada com sucesso.')
             
