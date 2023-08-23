notas = []
soma = 0
media= 0

i = 0
while i<20:
    notas.append(float(input('Digite a nota: ')))
    soma = soma + notas[i]
    i = i + 1
media=(soma)/i

print(media)
10
    
i = 0
print('notas > 7,5')
while i<20:
    if notas[i]> media:
        print(notas[i])
    i = i + 1