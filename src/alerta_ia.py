import pandas as pd

df = pd.read_csv("../data/dados_climaticos.csv")

ultimo_registro = df.iloc[-1]

risco = ultimo_registro["Risco"]
temperatura = ultimo_registro["Temperatura"]
umidade = ultimo_registro["Umidade"]
precipitacao = ultimo_registro["Precipitacao"]

if risco == "ALTO":
    alerta = f"""
🚨 ALERTA DE RISCO ALTO

Temperatura: {temperatura}°C
Umidade: {umidade}%
Precipitação: {precipitacao} mm

As condições climáticas indicam risco elevado.
Recomenda-se monitoramento contínuo da região.
"""

elif risco == "MÉDIO":
    alerta = f"""
⚠️ ALERTA DE RISCO MÉDIO

Temperatura: {temperatura}°C
Umidade: {umidade}%
Precipitação: {precipitacao} mm

As condições climáticas exigem atenção.
Monitoramentos preventivos são recomendados.
"""

else:
    alerta = f"""
✅ RISCO BAIXO

Temperatura: {temperatura}°C
Umidade: {umidade}%
Precipitação: {precipitacao} mm

Não foram identificados riscos significativos.
"""

print(alerta)