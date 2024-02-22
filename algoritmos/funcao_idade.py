from datetime import datetime, date

def data_usuario():
    data_nascimento = input('Qual a sua data de nascimento: ')
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
    hoje = date.today() # armazena a data atual
    resultado = (hoje - nascimento) // 360
    print(f'Você tem {resultado.days} anos.')

data_usuario()