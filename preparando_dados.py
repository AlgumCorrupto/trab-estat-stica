import pandas as pd
dados_brasil = pd.read_csv("dados.csv", sep=';', encoding='latin1')
população_campos = dados_brasil[dados_brasil["NO_MUNICIPIO_PROVA"].str.strip().str.lower().str.contains("goytacazes")]

print(f"Alunos inscritos no Enem {len(população_campos)}")

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

amostra_notas = população_campos.dropna(subset=colunas_notas)
amostra_presenças = população_campos[["TP_PRESENCA_LC", "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_MT"]]

for _, aluno in amostra_notas.iterrows():
    def pegarAcertosSeguro(respostas, gabarito):
        resp = aluno[respostas]
        gab = aluno[gabarito]
    
        if pd.isna(resp) or pd.isna(gab):
            return None   # ou 0, se quiser

        return sum(1 for i in range(len(resp)) if resp[i] == gab[i])
    pegarAcertos = lambda respostas, gabarito: sum(1 for i in range(len(aluno[respostas])) if aluno[respostas][i] == aluno[gabarito][i])

    acertos_mt += [pegarAcertosSeguro("TX_RESPOSTAS_MT", "TX_GABARITO_MT")]
    acertos_cn += [pegarAcertosSeguro("TX_RESPOSTAS_CN", "TX_GABARITO_CN")]
    acertos_ch += [pegarAcertosSeguro("TX_RESPOSTAS_CH", "TX_GABARITO_CH")]
    acertos_lc += [pegarAcertosSeguro("TX_RESPOSTAS_LC", "TX_GABARITO_LC")]

amostra_notas = amostra_notas[["NU_NOTA_MT", "NU_NOTA_CN", "NU_NOTA_CH", "NU_NOTA_LC"]]

amostra_notas["ACERTOS_MT"] = acertos_mt
amostra_notas["ACERTOS_CN"] = acertos_cn
amostra_notas["ACERTOS_CH"] = acertos_ch
amostra_notas["ACERTOS_LC"] = acertos_lc

amostra_notas = amostra_notas.sort_values(by='NU_NOTA_MT')

amostra_notas.to_csv('notas-campos.csv', index=False)
amostra_presenças.to_csv('presença-campos.csv', index=False)