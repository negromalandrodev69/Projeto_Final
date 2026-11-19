import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bitcoin = pd.read_csv("investimentos.csv",sep=";")

print(bitcoin.to_string())

id = bitcoin.groupby("id_registro").size()
print(id.to_string())

data = bitcoin.groupby("data_referencia").size()
print(data.to_string())

coin = bitcoin.groupby("moeda").size()
print(coin.to_string())
#apreviação
coin_a = bitcoin.groupby("codigo_moeda").size()
print(coin_a.to_string())


# id_registro;data_referencia;moeda;codigo_moeda;cotacao_compra;cotacao_venda;variacao_percentual;cotacao_media;indicador_economico;valor_indicador;
# unidade_medida;periodicidade;fonte_dado