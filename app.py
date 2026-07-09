import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA (Layout Garagem Noturna - Tema Integrado de Fábrica)
st.set_page_config(
    page_title="Garagem do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

# Estilização CSS que amarra as cores da tela inteira (Área central e Menu Lateral)
st.markdown("""
    <style>
    /* Força o fundo escuro e texto branco no app inteiro, inclusive no menu lateral */
    .stApp, [data-testid="stSidebar"], .stSidebar { background-color: #111827 !important; color: #FFFFFF !important; }
    .main-title { font-size:36px !important; font-weight: bold; color: #F59E0B; margin-bottom: 5px; text-shadow: 2px 2px 4px #000; }
    .sub-title { font-size:16px !important; color: #9CA3AF; margin-bottom: 25px; }
    
    /* Configuração dos Cartões Técnicos */
    .card-tecnico { background-color: #1F2937; padding: 18px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #374151; border-left: 6px solid #F59E0B; box-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    
    /* Configuração e Visibilidade das Abas */
    .stTabs [data-baseweb="tab-list"] { background-color: #1F2937; padding: 10px; border-radius: 8px; border: 1px solid #374151; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF !important; font-weight: bold !important; font-size: 15px !important; }
    .stTabs [aria-selected="true"] { color: #F59E0B !important; border-bottom-color: #F59E0B !important; }
    
    /* Garante que todos os textos normais fiquem brancos para leitura */
    div[data-testid="stMarkdownContainer"] p, label, .stSelectbox label { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns([1, 6])
with col_logo:
    st.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0; text-align: center;'>🦝</h1>", unsafe_allow_html=True)
with col_texto_topo:
    st.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title"><b>O Primeiro Software Feito para Chão de Oficina</b> | Filtros limpos estilo Doutor-IE e Simplo sem enrolação comercial! 🔧🏁</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DE VEÍCULOS EXPANDIDO
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2", "2.0 16V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E", "1.4 8V Econoflex"],
        "Corsa / Classic": ["1.0 8V VHC", "1.4 8V Econoflex", "1.6 8V MPFI"],
        "Cruze": ["1.4 16V Turbo Ecotec", "1.8 16V Ecotec Flex"],
        "Meriva / Montana / Agile": ["1.4 8V Econoflex", "1.8 8V Powertrain"],
        "Onix / Tracker (Novos)": ["1.0 3cil Aspirado (Banhada)", "1.0 3cil Turbo (Banhada)", "1.2 3cil Turbo CSS Prime"],
        "S10 / Trailblazer": ["2.8 16V Duramax Diesel", "2.4 8V Flexpower", "2.5 16V Ecotec Flex"],
        "Vectra / Zafira": ["2.0 8V Flexpower", "2.2 8V / 16V", "2.4 16V Flexpower"]
    },
    "Volkswagen": {
        "Amarok": ["2.0 16V Turbo Diesel", "3.0 V6 Turbo Diesel"],
        "Gol / Voyage / Saveiro / Parati": ["1.0 16V AT", "1.0 8V AT", "1.6 / 1.8 / 2.0 AP", "1.0 8V EA111", "1.6 8V EA111", "1.0 3cil EA211", "1.6 16V MSI EA211"],
        "Golf / Jetta / Tiguan": ["1.4 16V TSi EA211", "2.0 TSi EA888 (Corrente)", "2.0 TSi EA113 (Correia)"],
        "Polo / Virtus / Nivus / T-Cross": ["1.0 3cil 200 TSi EA211", "1.6 16V MSI EA211", "1.4 250 TSi EA211"]
    },
    "Fiat": {
        "Argo / Cronos / Pulse / Fastback": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 3cil Turbo T200", "1.3 4cil Turbo T270"],
        "Toro / Mobi / Uno / Strada": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.0 8V Fire Evo", "1.4 8V Fire Evo"],
        "Ducato": ["2.3 16V Multijet Diesel", "2.8 Turbo Diesel"]
    },
    "Ford": {
        "Ka / EcoSport (3 Cilindros)": ["1.0 3cil Ti-VCT (Banhada)", "1.5 3cil Dragon (Banhada)"],
        "Fiesta / Focus / EcoSport": ["1.6 Zetec Rocam", "1.6 16V Sigma", "2.0 16V Duratec HE"],
        "Ranger": ["2.2 16V Duratorq Diesel", "3.2 20V Duratorq Diesel", "2.3 Duratec Flex"]
    }
}

# 4. MONTAGEM DO MENU LATERAL (Sidebar)
st.sidebar.header("📋 Seleção Mecânica")

lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Fabricante:", lista_fabricantes)

lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Veículo:", lista_veiculos)

lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Motorização:", lista_motores)

lista_anos = ["Não Informar (Buscar Todos)"] + [str(ano) for ano in range(2000, 2027)]
ano_selecionado = st.sidebar.selectbox("4. Ano do Modelo:", lista_anos, index=0)

tipo_material = st.sidebar.radio(
    "5. Linha de Pesquisa:",
    [
        "Sincronismo do Motor (Pontos e Marcas)", 
        "Esquema de Passagem da Correia Poly-V"
    ]
)

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Opções Adicionais")
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

# 5. MONTAGEM DO COMANDO (Injeção Regulada de Combustível)
texto_ano = "" if ano_selecionado == "Não Informar (Buscar Todos)" else f"ano {ano_selecionado}"
exclusoes_ajustadas = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo -pecas -loja -produto"

# Frase de busca calibrada para cruzar dados com esquemas e pontos de referência legítimos
comando_pesquisa = (
    f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} {texto_ano} "
    f"manual oficina esquema pontos "
    f'("doutor ie" OR "simplo" OR "dicatek" OR "mecanica 2000" OR "manualdomecanico") {exclusoes_ajustadas}'
)

# Painel Central de Informações
st.info(f"⚙️ **Garimpo Ativo:** {tipo_material} | **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ DAR A PARTIDA NO GARIMPO", use_container_width=True)

# 6. PROCESSAMENTO
if botao_buscar:
    with st.spinner("🤖 Graxinim varrendo a internet..."):
        try:
            resposta_ia = client.search(
                query=comando_pesquisa,
                search_depth="advanced",
                max_results=20,
                include_images=True
            )
            resultados = resposta_ia.get("results", [])
            imagens_encontradas = resposta_ia.get("images", [])
        except Exception as e:
            st.error(f"❌ Falha no circuito de rede: {e}")
            resultados, imagens_encontradas = [], []

        if not resultados:
            st.error("❌ Nenhuma literatura ou imagem foi localizada pelo Graxinim.")
        else:
            lista_diagramas = []
            lista_manuais = []
            lista_foruns = []
            lista_videos = []
            
            plataformas_video = ["youtube", "youtu.be", "tiktok", "instagram"]
            sites_foruns = ["forum", "oficina-brasil", "mecanicos", "reparador", "club", "clube", "topico", "comunidade"]
            termos_bloqueados = ["proprietario", "usuario", "condutor", "owner", "proprietário", "usuário"]

            for item in resultados:
                link = item.get("url", "")
                titulo = item.get("title", "")
                link_min = link.lower()
                tit_min = titulo.lower()
                
                # Bloqueio de manuais de proprietário
                if not incluir_manual_proprietario and any(t in tit_min for t in termos_bloqueados):
                    continue

                # Triagem direta por link e texto nas gavetas certas
                if any(p in link_min for p in plataformas_video):
                    lista_videos.append(item)
                elif any(f in link_min for f in sites_foruns) or any(f in tit_min for f in sites_foruns):
                    lista_foruns.append(item)
                elif any(d in tit_min or d in link_min for d in ["diagrama", "esquema", "ponto", "sincronismo", "imagem", "foto", "png", "jpg"]):
                    lista_diagramas.append(item)
                else:
                    lista_manuais.append(item)
            
            # Inicializa as Abas do Painel Principal
            aba_diag, aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
                "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "🖼️ 3. Fotos e Miniaturas", "💬 4. Fóruns Mecânicos", "🎥 5. Vídeos e Macetes"
            ])
            
            # Injeta dados de forma simples e direta (Totalmente livre de erros visuais e à prova de tradutor)
            if not lista_diagramas:
                aba_diag.info("Nenhum diagrama rápido isolado detectado.")
            for item in lista_diagramas:
                aba_diag.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📊 {item.get("title")}</h4><a href="{item.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Abrir Esquema Visual do Ponto</a></div>', unsafe_allow_html=True)

            if not lista_manuais:
                aba_pdf.info("Nenhum manual de oficina completo listado.")
            for item in lista_manuais:
                aba_pdf.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📚 {item.get("title")}</h4><a href="{item.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Abrir Apostila Técnica / PDF</a></div>', unsafe_allow_html=True)

            # Injeta as imagens encontradas na Aba 3
            termos_mecanicos = ["motor", "sincronismo", "correia", "corrente", "torque", "car", "auto", "mecanic", "astra", "chevrolet", "valvula", "passagem", "poly", "tensionador", "polia"]
