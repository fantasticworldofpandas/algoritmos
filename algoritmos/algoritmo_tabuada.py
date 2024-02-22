# solicita um numero para o usuario e retorna sua tabuada de 1 a 10
n = int(input('Insira um numero: '))
print(f'\nA tabuada do n° ({n})')

lista_tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in lista_tabuada:
    resultado = x * n
    print(f'{n} x {x} = {resultado}')