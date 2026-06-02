import requests
import pandas as pd


def coletar_dados_nasa(latitude, longitude):
    url = (
        f"https://power.larc.nasa.gov/api/temporal/daily/point"
        f"?parameters=T2M,RH2M,PRECTOTCORR"
        f"&community=RE"
        f"&longitude={longitude}"
        f"&latitude={latitude}"
        f"&start=20260101"
        f"&end=20260107"
        f"&format=JSON"
    )

    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()

        temperatura = dados["properties"]["parameter"]["T2M"]
        umidade = dados["properties"]["parameter"]["RH2M"]
        precipitacao = dados["properties"]["parameter"]["PRECTOTCORR"]

        df = pd.DataFrame({
            "Data": temperatura.keys(),
            "Temperatura": temperatura.values(),
            "Umidade": umidade.values(),
            "Precipitacao": precipitacao.values()
        })

        return df

    else:
        print("Erro ao acessar API:", response.status_code)
        return pd.DataFrame()