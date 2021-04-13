from random import *
#Rede Neural Perceptron
#Usando a função degrau unitário como parametro (1 se x >= 1 e 0 para outros casos)

#Pesos randômicos
peso1 = random()
peso2 = random()

entrada1 = int(input('Digite a primeira entrada (0 ou 1)\n'))
entrada2 = int(input('Digite a segunda entrada (0 ou 1)\n'))

erro = 1
taxaAprendizado = 0.1

while (erro != 0):
    if (entrada1 == 1) and (entrada2 == 1):
        resultadoEsperado = 1
    else:
        resultadoEsperado = 0

    print(f'O Peso 1 é  {peso1}')
    print(f'O Peso 2 é  {peso2}')

    somatorio = (entrada1 * peso1) + (entrada2 * peso2)
    print(f'Somatorio é {somatorio}')

    #Aplica a lógica da função degrau para obter o resultado
    if (somatorio < 1):
        resultado = 0
    elif (somatorio >= 1):
        resultado = 1

    print(f'O resultado é {resultado}')
    erro = resultadoEsperado - resultado
    print(f'O erro é {erro}')

    #Recalcula pesos para nova tentativa
    peso1 += taxaAprendizado * erro * entrada1
    peso2 += taxaAprendizado * erro * entrada2
    print(f'O Peso 1 agora vale {peso1}')
    print(f'O Peso 2 agora vale  {peso2}')
