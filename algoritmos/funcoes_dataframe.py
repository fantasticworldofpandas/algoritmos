import pandas as pd


dados = {
    'id': [1, 2, 3],
    'Motorista': ['Timao', 'Pumba', 'Simba'],
    'Caminhão': ['Truck', 'Volvo', 'Bi trem'],
    'Placa': ['TI1010', 'PU1011', 'SI1012'],
    'Data Viagem': ['01/01/24', '06/01/24', '10/01/24']
    }

base = pd.DataFrame(dados)

base.head()

# funcao para filtrar informacoes de um motorista

def info_motorista(df, motorista):
    nome_motorista = df[df['Motorista'] == motorista]
    return nome_motorista

# chamada da funcao
info_motorista(base, 'Timao')

# funcao filtra placa do caminhao por argumentos
def info_placa_carro(df, coluna):
    placa = df[df['Placa'] == coluna]
    return placa

# chamada da funcao
info_placa_carro(base, 'JU1013')

# Função para adicionar uma nova linha no DF

def novo_registro(dataframe, nova_linha):
    nova_linha_df = pd.DataFrame([nova_linha])
    df = pd.concat([dataframe, nova_linha_df], ignore_index=True)
    return df

base = novo_registro(base, {'id': 4, 'Motorista': 'Musafasa', 'Caminhão': 'Mercedes', 'Placa': 'MU1013', 'Data Viagem': '01/02/24'})

# Filtro com Datas

viagem_atual = base[base['Data Viagem'] >= '2024-01-10']
viagem_atual

base.dtypes
base['Data Viagem'] = pd.to_datetime(base['Data Viagem'], format='%d/%m/%y', errors='coerce')

caminho = 'C:\\Users\\freit\\OneDrive\\Documentos\\python-automacao\\relatorio.xlsx'
base.to_excel(caminho, index=False)