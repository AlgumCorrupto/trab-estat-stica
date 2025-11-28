import pandas as pd
dados_brasil = pd.read_csv("dados.csv", sep=';', encoding='latin1')
população_campos = dados_brasil[dados_brasil["NO_MUNICIPIO_PROVA"].str.strip().str.lower() == "campos dos goytacazes"]

acertos_mt = []
acertos_cn = []
acertos_ch = []
acertos_lc = []

colunas_notas = [
    "NU_NOTA_LC",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_CN",
    "NU_NOTA_REDACAO",
]

população_campos = população_campos.dropna(subset=colunas_notas)

for _, aluno in população_campos.iterrows():
    pegarAcertos = lambda respostas, gabarito: sum(1 for i in range(len(aluno[respostas])) if aluno[respostas][i] == aluno[gabarito][i])

    acertos_mt += [pegarAcertos("TX_RESPOSTAS_MT", "TX_GABARITO_MT")]
    acertos_cn += [pegarAcertos("TX_RESPOSTAS_CN", "TX_GABARITO_CN")]
    acertos_ch += [pegarAcertos("TX_RESPOSTAS_CH", "TX_GABARITO_CH")]
    acertos_lc += [pegarAcertos("TX_RESPOSTAS_LC", "TX_GABARITO_LC")]


amostra = população_campos[["NU_NOTA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC"]]

amostra["ACERTOS_MT"] = acertos_mt
amostra["ACERTOS_CN"] = acertos_cn
amostra["ACERTOS_CH"] = acertos_ch
amostra["ACERTOS_LC"] = acertos_lc

amostra = amostra.sort_values(by='NU_NOTA_MT')

amostra.to_csv('notas-campos.csv', index=False)
