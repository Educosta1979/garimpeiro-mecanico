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
st.markdown('<p class="sub-title">Garimpo Inteligente Separado por Vídeos Práticos e Materiais Didáticos de Engenharia</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DETALHADO POR CARRO INDIVIDUAL
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
    }
}

# 4. CRIAÇÃO DOS CAMPOS VISUAIS (Barra Lateral)
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

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Configurações Extra")
# 🚨 NOVA REGULAGEM: Manual do proprietário desmarcado por padrão (Filtro Inteligente)
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

# 5. MONTAGEM DA CONSULTA DINÂMICA COM EXCLUSÕES
exclusoes = (
    "-site:mercadolivre.com.br -site:olx.com.br -site:shopee.com.br -site:aliexpress.com "
    "-site:americanas.com.br -site:magazineluiza.com.br -site:autodoc.pt -site:pecasauto.pt"
)

if not incluir_manual_proprietario:
    exclusoes += ' -"manual do proprietario" -"manual de usuario" -"manual do condutor"'

comando_pesquisa = (
    f'"{tipo_material}" motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} '
    f'ano {ano_selecionado} "manual técnico" OR "esquema técnico" OR "pontos" OR "youtube.com" {exclusoes}'
)

# Painel Central de Informações
col1, col2 = st.columns(2)
with col1:
    st.info(f"⚙️ **Filtro Selecionado:**\n\n*{fabricante_selecionada} {veiculo_selecionado} {motor_selecionado} ({ano_selecionado})*\n\n🛠️ *Componente: {tipo_material}*")
with col2:
    st.write("")
    st.write("")
    botao_buscar = st.button("🚀 Garimpar Literatura Avançada", use_container_width=True)

# 6. PROCESSAMENTO E EXIBIÇÃO EM ABAS SEPARADAS
if botao_buscar:
    with st.spinner("🤖 Vasculhando acervos de engenharia e plataformas didáticas..."):
        try:
            resposta_ia = client.search(
                query=comando_pesquisa,
                search_depth="advanced",
                max_results=8 # Aumentado para trazer mais opções visuais
            )
            resultados = resposta_ia.get("results", [])
        except Exception as e:
            st.error(f"❌ Falha de comunicação: {e}")
            resultados = []

        if not resultados:
            st.error("❌ Nenhuma literatura ou vídeo foi localizado para essa configuração de motor.")
        else:
            # Separa os resultados em listas de mídias diferentes
            lista_videos = []
            lista_manuais = []
            
            for item in resultados:
                link = item.get("url", "")
                if "youtube.com" in link.lower() or "youtu.be" in link.lower():
                    lista_videos.append(item)
                else:
                    lista_manuais.append(item)
            
            # 🚨 SISTEMA DE ABAS PROFISSIONAIS NO PAINEL PRINCIPAL 🚨
            aba_manuais, aba_videos = st.tabs(["📚 Literaturas e Manuais Didáticos", "🎥 Vídeos Práticos e Macetes"])
            
            # Exibição na Aba de Manuais
            with aba_manuais:
                if not lista_manuais:
                    st.info("Nenhum arquivo de manual em PDF foi encontrado para este termo.")
                else:
                    st.success(f"Encontramos {len(lista_manuais)} esquemas técnicos didáticos:")
                    for i, item in enumerate(lista_manuais):
                        with st.container():
                            st.markdown(f"#### 📄 {i+1}. {item.get('title')}")
                            st.write(f"**Trecho do Material:** {item.get('content')}")
                            st.markdown(f"📥 **[Abrir Literatura / Esquema Técnico]({item.get('url')})**")
                            st.write("---")
            
            # Exibição na Aba de Vídeos
            with aba_videos:
                if not lista_videos:
                    st.info("Nenhum vídeo técnico explicativo foi encontrado para este motor.")
                else:
                    st.success(f"Encontramos {len(lista_videos)} vídeos com o procedimento prático:")
                    for i, item in enumerate(lista_videos):
                        with st.container():
                            st.markdown(f"#### 🎥 {i+1}. {item.get('title')}")
                            st.write(f"**Dica do vídeo:** {item.get('content')}")
                            # Renderiza o reprodutor de vídeo do YouTube direto na tela da oficina!
                            st.video(item.get('url'))
                            st.write("---")
