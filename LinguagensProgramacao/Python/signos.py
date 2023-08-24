
signos = ['Macaco', 'Gaio', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'DragãO', 'Serpente', 'Cavalo', 'Carneiro']
ano = int(input('Digite o ano em que nasceu:'))
indice = ano % 12
print(signos[indice])