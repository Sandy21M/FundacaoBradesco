notas = []

i = 0
while i<20:
    notas.append(float(input('Digite a nota: ')))
    i = i+1
i = 0
while i<20:
    if notas[i]> 7.5:
        print(notas[i])
    i = i+1
