# importa as bibliotecas necessrias
import pandas as pd
import csv

# realiza a leitura do arquivo unificado.csv contendo os dados
dados = pd.read_csv("/home/tasks/trusted/unificado.csv",sep = ';',encoding='iso-8859-1')

csv_file =  open("/home/tasks/trusted/FATO_RECL.csv", 'w')
csv_writer = csv.writer(csv_file, delimiter=";")
csv_writer.writerow(["CODIGO_TEMPO","CNPJ","INDICE","QTD_RECLAMACOES_PROCEDENTES","QTD_RECLAMACOES_OUTRAS","QTD_RECLAMACOES_NAO_REGULADAS","QTD_RECLAMACOES","QTD_CLIENTES","QTD_CLIENTES_CCS","QTD_CLIENTES_SCR"])

#print(dados.columns.tolist())

for i, instituicao in dados.iterrows():
  if instituicao['CNPJ'] != " ":
    if instituicao['Indice'] == " ": 
      instituicao['Indice'] = 0
    if instituicao['Quantidade de clientes CCS'] == " ": 
      instituicao['Quantidade de clientes CCS'] = 0
    if instituicao['Quantidade de clientes SCR'] == " ": 
      instituicao['Quantidade de clientes SCR'] = 0  
    if instituicao['Quantidade total de clientes CCS e SCR'] == " ":
      instituicao['Quantidade total de clientes CCS e SCR'] = 0
    csv_writer.writerow([str(instituicao['Ano']) + str(instituicao['Trimestre'])[:-2],instituicao['CNPJ'],str(instituicao['Indice']).replace(".","").replace(",","."),instituicao['Quantidade de reclamaÃ§Ãµes reguladas procedentes'],instituicao['Quantidade de reclamaÃ§Ãµes reguladas - outras'],instituicao['Quantidade de reclamaÃ§Ãµes nÃ£o reguladas'],instituicao['Quantidade total de reclamaÃ§Ãµes'],instituicao['Quantidade total de clientes CCS e SCR'],instituicao['Quantidade de clientes CCS'],instituicao['Quantidade de clientes SCR']])
  else:
    continue

csv_file.close()
df = pd.read_csv("/home/tasks/trusted/FATO_RECL.csv", sep=";")

# remove duplicados
df.drop_duplicates(subset=None, inplace=True)

# faz a ordenacao
ordenado = df.sort_values(by=["CODIGO_TEMPO"], ascending=True)

# Grava o resultado no arquivo FATO_RECL
ordenado.to_csv("/home/tasks/trusted/FATO_RECL.csv", sep=";", encoding='iso-8859-1', index=False)