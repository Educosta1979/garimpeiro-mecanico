import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA PROFISSIONAL (Front-End)
st.set_page_config(
    page_title="Acervo Técnico Automotivo - IA", 
    page_icon="⚙️", 
    layout="wide"
)

# Estilização visual moderna
st.markdown("""
    <style>
    .main-title { font-size:36px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size:18px !important; color: #4B5563; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">⚙️ Central de Literatura Técnica Automotiva</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Garimpo de Diagramas de Sincronismo, Manuais de Reparação e Tabelas de Torque</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS 100% SEPARADO (Um único carro por linha)
dados_veiculos = {
    "Volkswagen": {
        "Gol": ["1.0 3cil EA211", "1.6 8V EA111", "1.0 8V EA111", "1.6 16V MSI EA211"],
        "Voyage": ["1.0 3cil EA211", "1.6 8V EA111", "1.6 16V MSI EA211"],
        "Saveiro": ["1.6 8V EA111", "1.6 16V MSI EA211"],
        "Polo": ["1.0 200 TSi EA211", "1.0 TSi 170 TSi", "1.6 16V MSI", "2.0 TSi GTS"],
        "Virtus": ["1.0 200 TSi EA211", "1.6 16V MSI"],
        "Nivus": ["1.0 200 TSi EA211"],
        "T-Cross": ["1.0 200 TSi EA211", "1.4 TSi EA211"],
        "Jetta": ["1.4 TSi EA211", "2.0 TSi EA888 (Corrente)", "2.0 TSi EA113 (Correia)"],
        "Golf": ["1.4 TSi EA211", "2.0 TSi EA888", "1.6 8V EA111"],
        "Tiguan": ["1.4 TSi EA211", "2.0 TSi EA888", "2.0 TDi Diesel"],
        "Amarok": ["2.0 16V Turbo Diesel", "3.0 V6 Diesel"]
    },
    "Fiat": {
        "Argo": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 Turbo Turbo 200"],
        "Cronos": ["1.3 4cil Firefly", "1.8 16V E.torQ"],
        "Pulse": ["1.3 Firefly", "1.0 Turbo Turbo 200"],
        "Toro": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Flex T270"],
        "Uno": ["1.0 8V Fire Evo", "1.4 8V Fire Evo", "1.0 3cil Firefly"],
        "Mobi": ["1.0 8V Fire Evo", "1.0 3cil Firefly"],
        "Palio": ["1.0 8V Fire", "1.4 8V Fire", "1.6 16V E.torQ"],
        "Strada": ["1.4 8V Fire", "1.3 Firefly", "1.0 Turbo Turbo 200"]
    },
    "Jeep": {
        "Renegade": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Flex T270"],
        "Compass": ["2.0 Flex Tigershark", "2.0 Multijet Diesel", "1.3 Turbo Flex T270"],
        "Commander": ["1.3 Turbo Flex T270", "2.0 Multijet Diesel"]
    },
    "Ford": {
        "Ka": ["1.0 3cil Ti-VCT (Correia Banhada)", "1.5 3cil Dragon", "1.5 16V Sigma"],
        "Fiesta": ["1.6 16V Sigma", "1.0 Rocam", "1.6 Rocam"],
        "Focus": ["1.6 16V Sigma", "2.0 16V Duratec Direct Flex"],
        "EcoSport": ["1.6 16V Sigma", "2.0 16V Duratec", "1.5 3cil Dragon"],
        "Ranger": ["2.2 Duratorq Diesel", "3.2 Duratorq Diesel", "2.3 Duratec Flex"]
    },
    "Chevrolet": {
        "Onix": ["1.0 3cil Aspirado (Correia Banhada)", "1.0 3cil Turbo (Correia Banhada)", "1.0 8V SPE/4", "1.4 8V SPE/4"],
        "Prisma": ["1.0 8V SPE/4", "1.4 8V SPE/4"],
        "Tracker": ["1.0 3cil Turbo", "1.2 3cil Turbo", "1.4 Turbo Ecotec", "1.8 16V Ecotec"],
        "Cruze": ["1.4 Turbo Ecotec", "1.8 16V Ecotec Flex"],
        "S10": ["2.8 Duramax Diesel Turbodiesel", "2.4 Flexpower", "2.5 Ecotec SIDI Flex"],
        "Celta": ["1.0 8V VHC/VHC-E"],
        "Astra": ["2.0 8V Família 2"]
    },
    "Toyota": {
        "Corolla": ["1.8 16V Dual VVT-i", "2.0 16V Dynamic Force", "2.0 16V Dual VVT-i (3ZR)"],
        "Corolla Cross": ["2.0 16V Dynamic Force"],
        "Hilux": ["2.8 D-4D 1GD-FTV (Corrente)", "3.0 D-4D 1KD-FTV (Correia)", "2.7 16V Flex Dual VVT-i"],
        "SW4": ["2.8 D-4D 1GD-FTV", "3.0 D-4D 1KD-FTV"],
        "Etios": ["1.3 16V Dual VVT-i", "1.5 16V Dual VVT-i"],
        "Yaris": ["1.5 16V Dual VVT-i"]
    },
    "Honda": {
        "Civic": ["1.8 16V i-VTEC (R18)", "2.0 16V i-VTEC (R20)", "1.5 16V Turbo (L15)", "1.7 16V (D17)"],
        "Fit": ["1.4 8V/16V i-VTEC", "1.5 16V i-VTEC Flex"],
        "City": ["1.5 16V i-VTEC Flex"],
        "HR-V": ["1.8 16V i-VTEC", "1.5 16V Turbo VTEC"]
    },
    "Hyundai": {
        "HB20": ["1.0 3cil Kappa 12V", "1.0 3cil Turbo Kappa", "1.6 16V Gamma"],
        "Creta": ["1.6 16V Gamma", "2.0 16V Nu Flex", "1.0 3cil Turbo Kappa"],
        "i30": ["2.0 16V Beta", "1.8 16V Nu", "1.6 Turbo GDI"],
        "Tucson": ["2.0 16V Beta", "1.6 Turbo GDI"]
    },
    "Renault": {
        "Kwid": ["1.0 3cil SCe B4D (Corrente)"],
        "Sandero": ["1.0 3cil SCe", "1.6 16V SCe H4M", "1.6 16V Hi-Flex K4M"],
        "Logan": ["1.0 3cil SCe", "1.6 16V SCe H4M"],
        "Duster": ["2.0 16V F4R", "1.6 16V SCe", "1.3 Turbo TCe"],
        "Master": ["2.3 dCi Turbo Diesel"]
    },
    "Peugeot": {
        "208": ["1.2 3cil Puretech", "1.6 16V EC5 Flex", "1.0 Firefly Flex"],
        "2008": ["1.6 16V EC5", "1.6 16V THP Turbo"],
        "308": ["1.6 16V THP Turbo", "2.0 16V EW10"]
    },
    "Citroën": {
        "C3": ["1.2 3cil Puretech", "1.6 16V EC5", "1.0 Firefly Flex"],
        "C4 Cactus": ["1.6 16V EC5", "1.6 16V THP Turbo"],
        "C4 Lounge": ["1.6 16V THP Turbo"]
    }
}

# 4. CRIAÇÃO DOS CAMPOS VISUAIS EM COLUNAS
st.sidebar.header("📋 Filtros de Seleção Técnica")

lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Escolha a Fabricante:", lista_fabricantes)

lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Escolha o Veículo:", lista_veiculos)

lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Escolha a Motorização:", lista_motores)

lista_anos = [str(ano) for ano in range(2000, 2027)]
ano_selecionado = st.sidebar.selectbox("4. Ano do Modelo:", lista_anos, index=len(lista_anos)-1)

tipo_material = st.sidebar.radio(
    "5. Tipo de Literatura Exigida:",
    [
        "Diagrama de Sincronismo e Pontos de Referência", 
        "Esquema de Instalação da Correia Poly-V", 
        "Tabela de Torque de Cabeçote e Ordem de Aperto"
    ]
)

# 5. CONFIGURAÇÃO DA CONSULTA RESTRITA (Bloqueando sites de vendas e focando em manuais)
# Adicionado filtros negativos (-site) para banir e-commerce e focar em esquemas estilo Doutor IE e Simplo
comando_pesquisa = (
    f'"{tipo_material}" motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} '
    f'ano {ano_selecionado} "manual técnico" OR "esquema técnico" OR "ponto de sincronismo" '
    f'-site:mercadolivre.com.br -site:olx.com.br -site:shopee.com.br -site:aliexpress.com '
    f'-site:americanas.com.br -site:magazineluiza.com.br -site:autodoc.pt -site:pecasauto.pt'
)

# Painel Central de Confirmação
col1, col2 = st.columns()
with col1:
    st.info(f"⚙️ **Configuração Mecânica Atualizada:**\n\n*{fabricante_selecionada} {veiculo_selecionado} {motor_selecionado} ({ano_selecionado})* \n\n🔹 *Buscando: {tipo_material}*")

with col2:
    st.write("")
    st.write("")
    botao_buscar = st.button("🚀 Garimpar Literatura Técnica", use_container_width=True)

# 6. PROCESSAMENTO E FILTRAGEM DOS RESULTADOS
if botao_buscar:
    with st.spinner("🤖 Vasculhando bancos de dados técnicos e manuais de reparação..."):
        try:
            resposta_ia = client.search(
                query=comando_pesquisa,
                search_depth="advanced",
                max_results=5
            )
            resultados = resposta_ia.get("results", [])
        except Exception as e:
            st.error(f"❌ Falha de comunicação: {e}")
            resultados = []

        if not resultados:
            st.error("❌ Nenhuma literatura técnica oficial ou imagem de ponto de referência foi localizada para este motor.")
        else:
            st.success(f"✅ Sucesso! Encontramos {len(resultados)} literaturas compatíveis para a montagem.")
            st.write("---")
            
            for i, item in enumerate(resultados):
                titulo = item.get("title")
                link = item.get("url")
                resumo = item.get("content")
                
                # Exibição limpa em cartões focados em conteúdo técnico
                with st.container():
                    st.markdown(f"### 📄 {i+1}. {titulo}")
                    st.write(f"**Especificações Extraídas:** {resumo}")
                    st.markdown(f"📥 **[Clique aqui para abrir o Diagrama / Manual de Reparação]({link})**")
                    st.write("---")
