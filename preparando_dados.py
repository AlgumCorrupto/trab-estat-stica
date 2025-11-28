import pandas as pd
dados_brasil = pd.read_csv("dados.csv", sep=';', encoding='latin1')
população_campos = dados_brasil[dados_brasil["NO_MUNICIPIO_ESC"].str.lower() == "campos dos goytacazes"][['NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_REDACAO']]

amostra = população_campos.dropna().sort_values(by='NU_NOTA_MT')

amostra.to_csv('notas-campos.csv', index=False)
