import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA (Front-End Expandido)
st.set_page_config(
    page_title="Acervo Técnico Automotivo - IA", 
    page_icon="⚙️", 
    layout="wide"
)

# Estilização visual de alto padrão
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size:16px !important; color: #4B5563; margin-bottom: 25px; }
    .card-tecnico { background-color: #FFFFFF; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #E5E7EB; border-left: 6px solid #1E3A8A; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">⚙️ Central de Literatura Técnico Automotiva</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Garimpo Visual de Diagramas, Pontos de Sincronismo e Manuais de Engenharia</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DE VEÍCULOS TOTALMENTE EXPANDIDO E SEPARADO
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2", "2.0 16V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E", "1.4 8V Econoflex"],
        "Corsa / Classic": ["1.0 8V VHC", "1.4 8V Econoflex", "1.6 8V MPFI"],
        "Cruze": ["1.4 16V Turbo Ecotec", "1.8 16V Ecotec Flex"],
        "Meriva / Montana / Agile": ["1.4 8V Econoflex", "1.8 8V Powertrain"],
        "Onix / Prisma / Tracker (Novos)": ["1.0 3cil Aspirado (Banhada a Oleo)", "1.0 3cil Turbo (Banhada a Oleo)", "1.2 3cil Turbo CSS Prime"],
        "Onix / Prisma / Cobalt / Spin (Antigos)": ["1.0 8V SPE/4", "1.4 8V SPE/4", "1.8 8V Econoflex Econo.Flex"],
        "S10 / Trailblazer": ["2.8 16V Duramax Diesel", "2.4 8V Flexpower", "2.5 16V Ecotec SIDI Flex"],
        "Vectra / Zafira": ["2.0 8V Flexpower", "2.2 8V / 16V", "2.4 16V Flexpower"]
    },
    "Volkswagen": {
        "Amarok": ["2.0 16V Turbo/BiTurbo Diesel", "3.0 V6 Turbo Diesel"],
        "Gol / Voyage / Saveiro / Parati (G3/G4)": ["1.0 16V AT", "1.0 8V AT", "1.6 / 1.8 / 2.0 AP (Correia externa)"],
        "Gol / Voyage / Saveiro (G5/G6)": ["1.0 8V VHT EA111", "1.6 8V VHT EA111"],
        "Gol / Voyage / Saveiro (G7/G8)": ["1.0 3cil 12V EA211", "1.6 16V MSI EA211"],
        "Golf / Jetta / Tiguan": ["1.4 16V TSi EA211", "2.0 TSi EA888 (Corrente)", "2.0 TSi EA113 (Correia)", "2.5 20V 5 Cilindros"],
        "Fox / CrossFox / SpaceFox": ["1.0 8V EA111", "1.6 8V EA111", "1.6 16V MSI EA211"],
        "Polo / Virtus / Nivus / T-Cross": ["1.0 3cil 200 TSi EA211", "1.0 3cil 170 TSi", "1.6 16V MSI EA211", "1.4 250 TSi EA211"],
        "Up!": ["1.0 3cil 12V MPI EA211", "1.0 3cil 12V TSi EA211"]
    },
    "Fiat / Jeep": {
        "Argo / Cronos / Pulse / Fastback": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 3cil Turbo T200", "1.3 4cil Turbo T270"],
        "Toro / Compass / Renegade / Commander": ["1.8 16V E.torQ EVO", "2.0 16V Multijet Turbodiesel", "1.3 4cil Turbo T270", "2.0 Flex Tigershark"],
        "Uno / Palio / Siena / Strada (Motores Fire)": ["1.0 8V Fire / Fire Evo", "1.3 8V Fire", "1.4 8V Fire / Fire Evo"],
        "Palio / Grand Siena / Idea / Punto (E.torQ)": ["1.6 16V E.torQ", "1.8 16V E.torQ"],
        "Mobi": ["1.0 8V Fire Evo", "1.0 3cil Firefly"],
        "Ducato": ["2.3 16V Multijet Diesel Turbo", "2.8 Turbo Diesel"]
    },
    "Ford": {
        "Ka / EcoSport (3 Cilindros)": ["1.0 3cil Ti-VCT (Correia Banhada)", "1.5 3cil Dragon (Correia Banhada)"],
        "Fiesta / Focus / Ka / EcoSport (Sigma/Rocam)": ["1.0 8V Zetec Rocam", "1.6 8V Zetec Rocam", "1.5 16V Sigma", "1.6 16V Sigma / Sigma Ti-VCT"],
        "Focus / Fusion / EcoSport (Duratec)": ["2.0 16V Duratec HE", "2.0 16V Duratec Direct Flex (Injecao Direta)", "2.5 16V Duratec Flex"],
        "Fusion": ["2.0 16V EcoBoost Turbo", "2.3 16V Duratec", "3.0 V6 Duratec"],
        "Ranger": ["2.2 16V Duratorq Diesel", "3.2 20V Duratorq Diesel 5cil", "2.3 Duratec Flex", "3.0 NGD Eletronico Diesel"]
    },
    "Toyota": {
        "Corolla / Corolla Cross": ["1.8 16V VVT-i (1ZZ-FE)", "1.8 16V Dual VVT-i (2ZR-FBE)", "2.0 16V Dual VVT-i (3ZR-FBE)", "2.0 16V Dynamic Force (Direct Shift)"],
        "Hilux / SW4": ["2.5 16V D-4D 2KD", "2.8 16V D-4D 1GD-FTV (Corrente)", "3.0 16V D-4D 1KD-FTV (Correia)", "2.7 16V VVT-i / Dual VVT-i Flex"],
        "Etios / Yaris": ["1.3 16V Dual VVT-i", "1.5 16V Dual VVT-i"]
    },
    "Honda": {
        "Civic": ["1.7 16V VTEC (D17)", "1.8 16V i-VTEC (R18)", "2.0 16V i-VTEC (R20)", "1.5 16V VTEC Turbo (L15B)"],
        "Fit / City": ["1.4 8V i-DSI", "1.4 16V i-VTEC", "1.5 16V VTEC / i-VTEC Flex"],
        "HR-V / CR-V": ["1.8 16V i-VTEC", "2.0 16V i-VTEC", "1.5 16V Turbo"]
    },
    "Renault": {
        "Kwid / Logan / Sandero (SCe)": ["1.0 3cil 12V SCe B4D", "1.6 16V SCe H4M"],
        "Logan / Sandero / Clio / Kangoo (Antigos)": ["1.0 16V D4D", "1.6 8V Hi-Torque/Hi-Flex K7M", "1.6 16V K4M"],
        "Duster / Oroch / Captur / Fluence": ["1.6 16V SCe H4M", "2.0 16V F4R", "1.3 Flex Turbo TCe"],
        "Master": ["2.3 16V dCi Turbo Diesel (M9T)", "2.5 16V dCi Turbo Diesel"]
    },
    "Hyundai / Kia": {
        "HB20 / HB20S / Picanto": ["1.0 3cil 12V Kappa", "1.0 3cil 12V Kappa Turbo GDI", "1.6 16V Gamma"],
        "Creta / Tucson / i30 / Sportage / Cerato": ["1.6 16V Gamma", "2.0 16V Beta", "2.0 16V Nu Flex", "1.8 16V Nu", "1.6 16V Turbo GDI"],
        "HR / Bongo": ["2.5 Diesel Turbo D4CB (Euro 5/Corrente)", "2.5 Diesel Turbo D4BH (Correia)"]
    },
    "Peugeot / Citroën": {
        "206 / 207 / 208 / C3 / Hoggar": ["1.4 8V TU3JP", "1.5 8V TU4M", "1.6 16V TU5JP4", "1.2 3cil Puretech", "1.0 3cil Firefly Flex"],
        "308 / 408 / 2008 / C4 / C4 Cactus / C4 Lounge": ["1.6 16V EC5 Flex", "1.6 16V THP Turbo (Prince/Corrente)", "2.0 16V EW10A / EW10J4"]
    },
    "Nissan": {
        "March / Versa / Kicks": ["1.0 3cil 12V HR10DE", "1.6 16V HR16DE"],
        "Sentra / Tiida / Livina": ["1.8 16V MR18DE", "2.0 16V MR20DE"],
        "Frontier": ["2.5 Diesel YD25", "2.3 16V Diesel BiTurbo YS23DDTI"]
    },
    "Mitsubishi": {
        "L200 Triton / Pajero": ["3.2 DI-D Diesel 4M41", "2.4 Diesel Mivec 4N15", "3.5 V6 Flex 6G74", "2.5 Diesel 4D56"]
    }
}

# 4. MONTAGEM DO MENU LATERAL (Filtros Técnicos)
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
        "Diagrama Sincronismo Pontos", 
        "Instalacao Correia Poly-V", 
        "Torque Cabecote Ordem Aperto"
    ]
)

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Opções Adicionais")
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

# 5. ESTRUTURAÇÃO DO COMANDO RESTRITO ANTI-PAGAMENTO
exclusoes_rigidas = (
    "-scribd -issuu -slideshare -mercadolivre -olx -shopee -aliexpress "
    "-comprar -preco -venda -catalogo -login -sign -facebook"
)

# 🚨 LINHA CORRIGIDA COM O RECUO DE ESPAÇOS CORRETO PARA RODAR 🚨
if not incluir_manual_proprietario:
    exclusoes_rigidas += ' -"proprietario" -"usuario" -"condutor" -"owner"'

outras_marcas = [marca for marca in lista_fabricantes if marca != fabricante_selecionada]
for marca in outras_marcas:
    exclusoes_rigidas += f" -{marca.lower()}"

comando_pesquisa = f'"{tipo_material}" "{fabricante_selecionada} {veiculo_selecionado}" motor "{motor_selecionado}" {ano_selecionado} "esquema" OR "pontos" {exclusoes_rigidas}'

# Painel Central de Informações
col1, col2 = st.columns(2)
with col1:
    st.info(f"⚙️ **Filtro Selecionado:** **{fabricante_selecionada} {veiculo_selecionado} {motor_selecionado} ({ano_selecionado})**\n\n🛠️ *Buscar:* **{tipo_material}**")
with col2:
    st.write("")
    st.write("")
    botao_buscar = st.button("🚀 Garimpar Esquemas e Imagens Técnicas", use_container_width=True)

# 6. PROCESSAMENTO E EXIBIÇÃO EM ABAS SEPARADAS COM MINIATURAS VISUAIS
if botao_buscar:
    with st.spinner("🤖 Vasculhando acervos abertos e gerando visualizações..."):
        try:
            resposta_ia = client.search(
                query=comando_pesquisa,
                search_depth="advanced",
                max_results=10,
                include_images=True
            )
            resultados = resposta_ia.get("results", [])
            imagens_encontradas = resposta_ia.get("images", [])
        except Exception as e:
            st.error(f"❌ Falha de comunicação: {e}")
            resultados, imagens_encontradas = [], []

        if not resultados:
            st.error("❌ Nenhuma literatura oficial ou imagem livre de barreira de pagamento foi localizada para este motor.")
        else:
            lista_videos = []
            lista_manuais = []
            plataformas_video = ["youtube", "youtu.be", "tiktok", "instagram", "kwai", "video"]
            
            for item in resultados:
                titulo = item.get("title", "")
                link = item.get("url", "")
                resumo = item.get("content", "")
                
                if not incluir_manual_proprietario:
                    if any(p in titulo.lower() or p in resumo.lower() for p in ["proprietario", "usuario", "condutor", "owner"]):
                        continue
                
