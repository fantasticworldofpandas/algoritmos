# função que calcula o fatorial de um número
def numero_fatorial(x):
    if x == 0 or x == 1:
        return 1
    else: 
        return x * numero_fatorial(x - 1)

n = int(input('Insira um número: '))

print(f'O fatorial de {n} é: {numero_fatorial(n)}')