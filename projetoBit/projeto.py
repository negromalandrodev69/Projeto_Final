import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

bitcoin = pd.read_csv("investimentos.csv",dtype = {"data_referencia": str},sep=";",error = "coerce")

print(bitcoin.as_type())

id = bitcoin.groupby("id_registro").size()
print(id.as_type())

data = bitcoin.groupby("data_referencia").size()
print(data.as_type())

coin = bitcoin.groupby("moeda").size()
print(coin.as_type())
#apreviação
coin_a = bitcoin.groupby("codigo_moeda").size()
print(coin_a.as_type())


# id_registro;data_referencia;moeda;codigo_moeda;cotacao_compra;cotacao_venda;variacao_percentual;cotacao_media;indicador_economico;valor_indicador;
# unidade_medida;periodicidade;fonte_dado