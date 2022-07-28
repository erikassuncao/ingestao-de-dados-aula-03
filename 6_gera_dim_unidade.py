# importa as bibliotecas necessrias
import pandas as pd
import zlib
import csv

# realiza a leitura do arquivo dados_api.csv contendo os dados
dados = pd.read_csv("/home/tasks/trusted/dados_api.csv",sep = ';',encoding='iso-8859-1')

csv_file =  open("/home/tasks/trusted/DIM_UNIDADE.csv", 'w')
csv_writer = csv.writer(csv_file, delimiter=";")
csv_writer.writerow(["CODIGO_UNIDADE","UNIDADE"])

#print(dados.columns.tolist())
for i, instituicao in dados.iterrows():
  if instituicao['CNPJ'] != " ":
    csv_writer.writerow([zlib.crc32(instituicao["Unidade"].encode()),instituicao['Unidade']])
  else:
    continue

csv_file.close()
df = pd.read_csv("/home/tasks/trusted/DIM_UNIDADE.csv", sep=";")

# remove duplicados
df.drop_duplicates(subset='UNIDADE', inplace=True)
# faz a ordenacao
ordenado = df.sort_values(by=["CODIGO_UNIDADE"], ascending=True)

# Grava o resultado no arquivo DIM_UNIDADE
ordenado.to_csv("/home/tasks/trusted/DIM_UNIDADE.csv", sep=";", encoding='iso-8859-1', index=False)