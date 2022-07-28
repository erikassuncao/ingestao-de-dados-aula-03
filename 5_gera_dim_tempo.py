# importa as bibliotecas necessrias
import pandas as pd
import csv

# realiza a leitura do arquivo unificado.csv contendo os CNPJ
dados = pd.read_csv("/home/tasks/trusted/unificado.csv",sep = ';',encoding='iso-8859-1')

csv_file =  open("/home/tasks/trusted/DIM_TEMPO.csv", 'w')
csv_writer = csv.writer(csv_file, delimiter=";")

csv_writer.writerow(["ANO","TRIMESTRE","CODIGO_TEMPO"])

for i, instituicao in dados.iterrows():
  if instituicao['CNPJ'] != " ":
    csv_writer.writerow([instituicao['Ano'],instituicao['Trimestre'],str(instituicao['Ano']) + str(instituicao['Trimestre'])[:-2]])
  else:
    continue

csv_file.close()

df = pd.read_csv("/home/tasks/trusted/DIM_TEMPO.csv", sep=";")

df.drop_duplicates(subset=None, inplace=True)
ordenado = df.sort_values(by=["CODIGO_TEMPO"], ascending=True)

# Grava o resultado no arquivo DIM_TEMPO
ordenado.to_csv("/home/tasks/trusted/DIM_TEMPO.csv", sep=";", encoding='iso-8859-1', index=False)