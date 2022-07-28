# importa as bibliotecas necessrias
import pandas as pd
import csv

# realiza a leitura do arquivo dados_api.csv contendo os dados
dados = pd.read_csv("/home/tasks/trusted/dados_api.csv",sep = ';',encoding='iso-8859-1')

csv_file =  open("/home/tasks/trusted/DIM_SERVICO.csv", 'w')
csv_writer = csv.writer(csv_file, delimiter=";")

csv_writer.writerow(["CODIGO_SERVICO","SERVICO"])

for i, servico in dados.iterrows():
    csv_writer.writerow([servico['CodigoServico'],servico['Servico']])

csv_file.close()

df = pd.read_csv("/home/tasks/trusted/DIM_SERVICO.csv", sep=";")

df.drop_duplicates(subset=["CODIGO_SERVICO","SERVICO"], inplace=True)
ordenado = df.sort_values(by=["CODIGO_SERVICO"], ascending=True)

# Write the results to a different file
ordenado.to_csv("/home/tasks/trusted/DIM_SERVICO.csv", sep=";", index=False,encoding='iso-8859-1')