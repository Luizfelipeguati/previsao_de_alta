# Define uma função para calcular as datas das consultas
def calcular_consultas(data_primeira_consulta):
    # Inicializa a lista de datas com a primeira consulta
    datas_consultas = [data_primeira_consulta]
    # Define o intervalo de uma semana em dias
    intervalo_semanal = 7
    # Realiza o loop para adicionar as próximas 9 consultas
    for i in range(1, 10):
        # Calcula a data da próxima consulta
        data_proxima_consulta = data_primeira_consulta + timedelta(days=intervalo_semanal * i)
        # Adiciona a data à lista de datas das consultas
        datas_consultas.append(data_proxima_consulta)
    # Retorna a lista de datas das consultas
    return datas_consultas


# Pede ao usuário para inserir os dados do cliente
nome_cliente = input("Insira o nome do cliente: ")


# Pede ao usuário para inserir a data da primeira consulta
from datetime import datetime, timedelta

data_primeira_consulta_str = input("Insira a data da primeira consulta (no formato DD/MM/AAAA): ")
data_primeira_consulta = datetime.strptime(data_primeira_consulta_str, "%d/%m/%Y")

# Calcula as datas das consultas
datas_consultas = calcular_consultas(data_primeira_consulta)

# Imprime as informações do cliente e as datas das consultas
print("Nome do cliente:", nome_cliente)
print("Datas das consultas:")
for data_consulta in datas_consultas:
    print("-", data_consulta.strftime("%d/%m/%Y"))