# funcao que cria um arquivo txt e classifica uma lista de 100 números por ímpar e par.
def impar_par():
    # arquivo gerado salvo no diretorio 'arquivos'
    with open('arquivos/classificador.txt', 'w') as folder: 
        numeros_pares = []
        numeros_impares = []
        for x in range(1, 101):
            if x % 2 == 0:
                numeros_pares.append(str(x))
            else:
                numeros_impares.append(str(x))
        folder.write('Números pares:\n')
        folder.write(', '.join(numeros_pares) + '\n\n')
        folder.write('Números impares: \n')
        folder.write(', '.join(numeros_impares) + '\n\n')

#chamada da funcao
impar_par()