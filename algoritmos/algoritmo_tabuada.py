# esse algoritmo solicita um numero para o usuario e retorna sua tabuada de 1 a 10
n = int(input('Insira um numero: '))
print(f'\nA tabuada do n° ({n})')

lista_tabuada = range(1,11)

for x in lista_tabuada:
    resultado = x * n
    print(f'{n} x {x} = {resultado}')