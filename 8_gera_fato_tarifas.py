# importa as bibliotecas necessrias
import pandas as pd
import zlib
import csv

# realiza a leitura do arquivo dados_api.csv contendo os dados
dados = pd.read_csv("/home/tasks/trusted/dados_api.csv",sep = ';',encoding='iso-8859-1')

csv_file =  open("/home/tasks/trusted/FATO_TARIFAS.csv", 'w')
csv_writer = csv.writer(csv_file, delimiter=";")
csv_writer.writerow(["CNPJ","CODIGO_SERVICO","CODIGO_UNIDADE","DATA_VIGENCIA","VALOR_MAXIMO","CODIGO_TIPO_VALOR"])

for i, instituicao in dados.iterrows():
  if instituicao['CNPJ'] != " ":
    codigo_tipo_valor = 1 if instituicao["TipoValor"] == "Real" else 2
    csv_writer.writerow([instituicao["CNPJ"],zlib.crc32(instituicao["Servico"].encode()),zlib.crc32(instituicao["Unidade"].encode()),instituicao["DataVigencia"],instituicao["ValorMaximo"],codigo_tipo_valor])
  else:
    continue

csv_file.close()

# remove duplicados
df = pd.read_csv("/home/tasks/trusted/FATO_TARIFAS.csv", sep=";")
df.drop_duplicates(subset=None, inplace=True)

# Grava resultado tratado
df.to_csv("/home/tasks/trusted/FATO_TARIFAS.csv", sep=";", encoding='iso-8859-1', index=False)