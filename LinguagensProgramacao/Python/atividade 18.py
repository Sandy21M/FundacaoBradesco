numero_macas=int(input('Quantas maçãs deseja: '))
total_m=0


if numero_macas < 12:
    print('o valor é:', 1.30 *numero_macas)
else:
    print('O valor é:', 1.00 *numero_macas)