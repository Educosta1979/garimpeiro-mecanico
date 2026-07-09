import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA PROFISSIONAL (Front-End)
st.set_page_config(
    page_title="Acervo Técnico Automotivo - IA", 
    page_icon="⚙️", 
    layout="wide" # Tela cheia para visualização profissional
)

# Estilização visual moderna (CSS para deixar o visual limpo)
st.markdown("""
    <style>
    .main-title { font-size:36px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size:18px !important; color: #4B5563; margin-bottom: 25px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">⚙️ Sistema Integrado de Literatura Mecânica</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Garimpo Inteligente e Inteligência Artificial para Sincronismo de Motores</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DE FILTROS SUPER EXPANDIDO
dados_veiculos = {
    "Volkswagen": {
        "Gol / Voyage / Saveiro": ["1.0 3cil EA211", "1.6 8V EA111", "1.0 8V EA111", "1.6 16V MSI EA211"],
        "Golf / Jetta / Tiguan": ["1.4 TSi EA211", "2.0 TSi EA888 (Corrente)", "2.0 TSi EA113 (Correia)"],
        "Amarok": ["2.0 16V Turbo Diesel", "3.0 V6 Diesel"],
        "Polo / Virtus / Nivus / T-Cross": ["1.0 200 TSi EA211", "1.0 TSi 170 TSi", "1.6 16V MSI"]
    },
    "Fiat / Jeep": {
        "Argo / Cronos / Pulse": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 Turbo Turbo 200"],
        "Toro / Compass / Renegade": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Flex T270"],
        "Uno / Palio / Mobi": ["1.0 8V Fire Evo", "1.4 8V Fire Evo", "1.0 3cil Firefly"],
        "Siena / Strada (Antiga)": ["1.4 8V Fire", "1.6 16V E.torQ", "1.8 8V Powertrain"]
    },
    "Ford": {
        "Ka / EcoSport (Modernos)": ["1.0 3cil Ti-VCT (Correia Banhada)", "1.5 3cil Dragon", "1.5 16V Sigma"],
        "Ranger": ["2.2 Duratorq Diesel", "3.2 Duratorq Diesel", "2.3 Duratec Flex", "3.0 NGD Diesel"],
        "Fiesta / Focus / EcoSport": ["1.6 16V Sigma", "2.0 16V Duratec Direct Flex", "1.0 Rocam", "1.6 Rocam"]
    },
    "Chevrolet": {
        "Onix / Prisma / Tracker (Novos)": ["1.0 3cil Aspirado (Correia Banhada)", "1.0 3cil Turbo (Correia Banhada)"],
        "S10 / Trailblazer": ["2.8 Duramax Diesel Turbodiesel", "2.4 Flexpower", "2.5 Ecotec SIDI Flex"],
        "Cruze": ["1.4 Turbo Ecotec", "1.8 16V Ecotec Flex"],
        "Celta / Corsa / Classic / Astra / Vectra": ["1.0 8V VHC/VHC-E", "1.4 8V Econoflex", "1.8 8V Família 1", "2.0 8V Família 2"]
    },
    "Toyota": {
        "Corolla / Corolla Cross": ["1.8 16V Dual VVT-i (1ZZ/2ZR)", "2.0 16V Dynamic Force", "2.0 16V Dual VVT-i (3ZR)"],
        "Hilux / SW4": ["2.8 D-4D 1GD-FTV (Corrente)", "3.0 D-4D 1KD-FTV (Correia)", "2.7 16V Flex Dual VVT-i"],
        "Etios / Yaris": ["1.3 16V Dual VVT-i", "1.5 16V Dual VVT-i"]
    },
    "Honda": {
        "Civic": ["1.8 16V i-VTEC (R18)", "2.0 16V i-VTEC (R20)", "1.5 16V Turbo (L15)", "1.7 16V (D17)"],
        "Fit / City / WR-V": ["1.4 8V/16V i-VTEC", "1.5 16V i-VTEC Flex"],
        "HR-V": ["1.8 16V i-VTEC", "1.5 16V Turbo VTEC"]
    },
    "Hyundai / Kia": {
        "HB20 / HB20S / Picanto": ["1.0 3cil Kappa 12V Kappa", "1.0 3cil Turbo Kappa", "1.6 16V Gamma"],
        "Creta": ["1.6 16V Gamma", "2.0 16V Nu Flex", "1.0 3cil Turbo Kappa"],
        "Tucson / i30 / Sportage": ["2.0 16V Beta", "2.0 16V Nu", "1.6 Turbo GDI"]
    },
    "Renault": {
        "Kwid / Sandero / Logan": ["1.0 3cil SCe B4D (Corrente)", "1.6 16V SCe H4M (Corrente)"],
        "Duster / Oroch / Captur": ["2.0 16V F4R (Correia)", "1.6 16V Hi-Flex K4M", "1.3 Turbo TCe"],
        "Master": ["2.3 dCi Turbo Diesel (G9U/M9T)"]
    },
    "Peugeot / Citroën": {
        "208 / 2008 / C3 / C4 Cactus": ["1.2 3cil Puretech", "1.6 16V EC5 Flex", "1.6 16V THP (Prince)"],
        "308 / 408 / C4 Lounge": ["1.6 16V THP Turbo", "2.0 16V EW10"]
    },
    "Premium (BMW / Mercedes / Audi)": {
        "BMW 320i / X1 / 120i": ["2.0 Turbo ActiveFlex N20", "2.0 Turbo B48 (Corrente)", "2.0 Aspirado N46"],
        "Mercedes-Benz C180 / C200 / GLA": ["1.6 Turbo M270", "1.8 Turbo M271 (Corrente)", "2.0 Turbo M274"],
        "Audi A3 / A4 / Q3": ["1.4 TFSI EA211", "2.0 TFSI EA888", "1.8 TFSI EA888"]
    }
}

# 4. CRIAÇÃO DOS CAMPOS VISUAIS EM COLUNAS (Organização do Painel)
st.sidebar.header("📋 Filtros de Seleção Técnica")

# Filtro 1: Fabricante
lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Escolha a Fabricante:", lista_fabricantes)

# Filtro 2: Veículo (Atualiza sozinho baseado na fabricante)
lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Escolha o Veículo:", lista_veiculos)

# Filtro 3: Motorização (Atualiza sozinho baseado no veículo)
lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Escolha a Motorização:", lista_motores)

# Filtro 4: Ano do Veículo
lista_anos = [str(ano) for ano in range(2000, 2027)]
ano_selecionado = st.sidebar.selectbox("4. Ano do Modelo:", lista_anos, index=len(lista_anos)-1)

# Filtro 5: Tipo de Material Procurado
tipo_material = st.sidebar.radio(
    "5. Qual componente você quer o diagrama?",
    [
        "Sincronismo da Correia Dentada", 
        "Sincronismo da Corrente de Comando", 
        "Esquema da Correia de Acessórios (Poly-V)", 
        "Tabela de Torques de Cabeçote e Bielas"
    ]
)

# 5. MONTAGEM AUTOMÁTICA DA CONSULTA DE IA
termo_busca = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} ano {ano_selecionado}"

# Painel Central de Confirmação
col1, col2 = st.columns([3, 1])
with col1:
    st.info(f"🔍 **Parâmetro de Busca Inteligente Atualizado:**\n\n*{termo_busca}*")

with col2:
    st.write("")
    st.write("")
    botao_buscar = st.button("🚀 Iniciar Busca Avançada", use_container_width=True)

# 6. PROCESSAMENTO E EXIBIÇÃO DOS RESULTADOS EM PAINÉIS MODERNOS
if botao_buscar:
    with st.spinner("🤖 Consultando acervos digitais e convertendo manuais técnicos..."):
        try:
            resposta_ia = client.search(
                query=f"{termo_busca} manual tecnico filetype:pdf diagramas pontos sincronismo",
                search_depth="advanced",
                max_results=5
            )
            resultados = resposta_ia.get("results", [])
        except Exception as e:
            st.error(f"❌ Falha de rede: {e}")
            resultados = []

        if not resultados:
            st.error("❌ Nenhuma literatura oficial ou diagrama foi localizado para essa configuração específica.")
        else:
            st.success(f"✅ Sucesso! Encontramos {len(resultados)} manuais compatíveis com a sua busca.")
            st.write("---")
            
            # Exibe os resultados usando componentes visuais de alta qualidade
            for i, item in enumerate(resultados):
                titulo = item.get("title")
                link = item.get("url")
                resumo = item.get("content")
                
                with st.container():
                    st.markdown(f"### 📄 {i+1}. {titulo}")
                    st.write(f"**Trecho extraído do manual:** {resumo}")
                    st.markdown(f"📥 **[Clique aqui para abrir ou baixar o material completo]({link})**")
                    st.write("---")
