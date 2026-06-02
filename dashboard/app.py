import streamlit as st
import pandas as pd
import sys
import os

# Permite importar arquivos da pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.coleta_dados import coletar_dados_nasa


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


st.set_page_config(
    page_title="SpaceGuard AI",
    page_icon="🛰️",
    layout="wide"
)

cidades = {
    "São Paulo": (-23.5505, -46.6333),
    "Uberlândia": (-18.9186, -48.2772),
    "Belo Horizonte": (-19.9167, -43.9345),
    "Brasília": (-15.7939, -47.8828),
    "Rio de Janeiro": (-22.9068, -43.1729)
}

st.title("🛰️ SpaceGuard AI")

st.subheader("Monitoramento Climático com Dados Espaciais da NASA")

st.markdown("""
O SpaceGuard AI utiliza dados climáticos obtidos por satélites da NASA
para monitorar condições ambientais e gerar alertas inteligentes de risco.
""")

cidade = st.selectbox(
    "Selecione a cidade",
    list(cidades.keys())
)

latitude, longitude = cidades[cidade]

st.info(f"📍 Localização monitorada: {cidade}")
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")
mapa_df = pd.DataFrame({
    "lat": [latitude],
    "lon": [longitude]
})

st.map(mapa_df)

with st.spinner("Consultando dados climáticos da NASA..."):
    df = coletar_dados_nasa(latitude, longitude)

if df.empty:
    st.error("Não foi possível coletar os dados da NASA.")
    st.stop()

df["Risco"] = df.apply(classificar_risco, axis=1)

st.header("Dados Climáticos")
st.dataframe(df)

ultimo = df.iloc[-1]

st.header("Última Análise")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Temperatura", f"{ultimo['Temperatura']} °C")
col2.metric("Umidade", f"{ultimo['Umidade']} %")
col3.metric("Precipitação", f"{ultimo['Precipitacao']} mm")
if ultimo["Risco"] == "ALTO":
    risco_exibicao = "🔴 ALTO"
elif ultimo["Risco"] == "MÉDIO":
    risco_exibicao = "🟡 MÉDIO"
else:
    risco_exibicao = "🟢 BAIXO"

col4.metric("Risco", risco_exibicao)

st.header("Evolução da Temperatura")

st.line_chart(
    df.set_index("Data")["Temperatura"]
)

st.header("Alerta Inteligente")

if ultimo["Risco"] == "ALTO":
    st.error("""
🚨 RISCO ALTO

As condições climáticas indicam risco elevado.
Recomenda-se monitoramento contínuo da região.
""")

elif ultimo["Risco"] == "MÉDIO":
    st.warning("""
⚠️ RISCO MÉDIO

As condições climáticas exigem atenção.
Monitoramentos preventivos são recomendados.
""")

else:
    st.success("""
✅ RISCO BAIXO

Não foram identificados riscos significativos.
""")