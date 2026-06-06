# 🛰️ SpaceGuard AI

## 🎓 Global Solution 2026.1 - FIAP

### 👩‍💻 Integrante

**Michelle Guedes Cavalari**
RM564557
---
**Gustavo Zanette Martins**
RM564523
---

# 📖 Sobre o Projeto

O SpaceGuard AI é uma plataforma inteligente de monitoramento climático que utiliza dados espaciais obtidos por satélites da NASA para analisar condições ambientais e gerar alertas automáticos de risco.

A solução foi desenvolvida como Prova de Conceito (POC) para a Global Solution 2026.1 da FIAP, dentro do tema Economia Espacial, demonstrando como tecnologias de Inteligência Artificial, análise de dados e APIs espaciais podem apoiar a tomada de decisão em cenários ambientais.

---

# 🎯 Problema

Dados climáticos provenientes de satélites são fundamentais para monitoramento ambiental, prevenção de desastres e planejamento estratégico.

Entretanto, esses dados geralmente são apresentados de forma técnica, dificultando sua interpretação por usuários sem conhecimento especializado.

---

# 💡 Solução Proposta

O SpaceGuard AI consulta dados climáticos disponibilizados pela NASA e transforma essas informações em indicadores simples e acessíveis.

O sistema permite:

* Selecionar uma cidade;
* Consultar dados climáticos espaciais;
* Visualizar informações em dashboard interativo;
* Classificar automaticamente o nível de risco;
* Gerar alertas inteligentes;
* Exibir a localização monitorada em mapa.

---

# 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Requests
* NASA POWER API
* GitHub
* Inteligência Artificial aplicada à análise de risco

---

# 🛰️ Arquitetura da Solução

```text
Usuário
    ↓
Dashboard Streamlit
    ↓
Seleção de Cidade
    ↓
API NASA POWER
    ↓
Coleta de Dados
    ↓
Análise de Dados
    ↓
Classificação de Risco
    ↓
Alerta Inteligente
    ↓
Visualização em Dashboard
```

---

# 📂 Estrutura do Projeto

```text
spaceguard-ai
│
├── README.md
│
├── docs
│   ├── IDEIA_DO_PROJETO.md
│   └── ARQUITETURA.md
│
├── src
│   ├── coleta_dados.py
│   ├── analise_risco.py
│   └── alerta_ia.py
│
├── dashboard
│   └── app.py
│
├── data
│
├── assets
│   └── imagens
│
└── requirements.txt
```

---

# ⚙️ Funcionalidades

## Consulta Climática

Permite consultar dados climáticos de diferentes cidades utilizando dados espaciais fornecidos pela NASA.

## Classificação de Risco

O sistema avalia:

* Temperatura
* Umidade
* Precipitação

e classifica o risco em:

* 🟢 Baixo
* 🟡 Médio
* 🔴 Alto

## Alerta Inteligente

Com base nos dados coletados, o sistema gera mensagens automáticas para auxiliar a interpretação das condições ambientais.

## Dashboard Interativo

Exibe:

* Tabela de dados climáticos;
* Indicadores principais;
* Gráfico de temperatura;
* Mapa da localização monitorada;
* Alerta inteligente.

---

# ▶️ Como Executar

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar o Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📊 Resultados Esperados

O SpaceGuard AI demonstra como dados espaciais podem ser utilizados para apoiar processos de monitoramento climático, prevenção de riscos ambientais e análise inteligente de informações obtidas por satélites.

---

# 🚀 Futuras Evoluções

* Integração com mais cidades;
* Machine Learning preditivo;
* Integração com APIs meteorológicas adicionais;
* Alertas em tempo real;
* Aplicação mobile.

---

# 📚 Projeto Acadêmico

Projeto desenvolvido para a disciplina Global Solution 2026.1 da Graduação em Inteligência Artificial da FIAP.
