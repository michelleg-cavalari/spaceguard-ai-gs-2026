import pandas as pd

df = pd.read_csv("../data/dados_climaticos.csv")

def classificar_risco(linha):
    temperatura = linha["Temperatura"]
    umidade = linha["Umidade"]
    precipitacao = linha["Precipitacao"]

    if temperatura >= 30 and umidade <= 50 and precipitacao <= 1:
        return "ALTO"
    elif temperatura >= 25 and umidade <= 70:
        return "MÉDIO"
    else:
        return "BAIXO"

df["Risco"] = df.apply(classificar_risco, axis=1)

print(df)

df.to_csv("../data/dados_climaticos.csv", index=False)

print("\nClassificação de risco concluída com sucesso!")