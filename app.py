import streamlit as st
import requests

# 1. CONFIGURAÇÃO DA TELA (Visual Garagem Premium Integrado)
st.set_page_config(
    page_title="Garagem do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"], .stSidebar { background-color: #111827 !important; color: #FFFFFF !important; }
    .main-title { font-size:36px !important; font-weight: bold; color: #F59E0B; margin-bottom: 5px; text-shadow: 2px 2px 4px #000; }
    .sub-title { font-size:16px !important; color: #9CA3AF; margin-bottom: 25px; }
    .card-tecnico { background-color: #1F2937; padding: 18px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #374151; border-left: 6px solid #F59E0B; box-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    .stTabs [data-baseweb="tab-list"] { background-color: #1F2937; padding: 10px; border-radius: 8px; border: 1px solid #374151; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF !important; font-weight: bold !important; font-size: 15px !important; }
    .stTabs [aria-selected="true"] { color: #F59E0B !important; border-bottom-color: #F59E0B !important; }
    div[data-testid="stMarkdownContainer"] p, label, .stSelectbox label { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Módulo Remapeado de Alta Performance</b> | Caminhos encurtados com foco em Doutor-IE, Simplo e Manuais Livres! 🏁</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY (Mantida para o Garimpeiro de motores novos)
TAVILY_API_KEY = "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"

# 3. 🏁 BANCO DE DADOS DE CAMINHOS CURTOS (A memória da sua oficina!)
# Sempre que encontrarmos um link espetacular, nós travamos ele aqui dentro para o app abrir na hora!
caminhos_curtos = {
    "Chevrolet_Astra_2.0 8V Familia 2": {
        "diagramas": [
            {"title": "Esquema Técnico de Distribuição - Astra 2.0 8V", "url": "https://manualdomecanico.com.br"},
            {"title": "Pontos de Sincronismo - Família 2 Chevrolet", "url": "https://oficinabrasil.com.br"}
        ],
        "manuais": [
            {"title": "Manual de Oficina Completo - Astra / Vectra (Scribd/Livre)", "url": "https://scribd.com"}
        ],
        "foruns": [
            {"title": "Fórum Oficina Brasil: Macete do Tensionador Astra 2.0 Flex", "url": "https://oficinabrasil.com.brforum/"}
        ],
        "videos": [
            {"title": "Vídeo Passo a Passo Sincronismo Astra 2.0 8V", "url": "https://youtube.com"}
        ]
    },
    "Volkswagen_Gol_1.0 3cil EA211": {
        "diagramas": [
            {"title": "Diagrama de Sincronismo Trioval - Motor EA211 3 Cilindros", "url": "https://manualdomecanico.com.br"}
        ],
        "manuais": [
            {"title": "Apostila de Treinamento Técnico VW: Motores EA211 PDF", "url": "https://manualdomecanico.com.br"}
        ],
        "foruns": [
            {"title": "Reparador VW: Sincronismo EA211 sem ferramenta é possível?", "url": "https://oficinabrasil.com.brforum/"}
        ],
        "videos": [
            {"title": "Troca da Correia Dentada EA211 3cil - O Mecânico", "url": "https://youtube.com"}
        ]
    }
}

# 4. BANCO DE DADOS DE VEÍCULOS (Filtro em cascata limpo)
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2", "2.0 16V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E", "1.4 8V Econoflex"],
        "Corsa / Classic": ["1.0 8V VHC", "1.4 8V Econoflex"],
        "Onix / Tracker (Novos)": ["1.0 3cil Aspirado (Banhada)", "1.0 3cil Turbo (Banhada)"]
    },
    "Volkswagen": {
        "Gol": ["1.0 3cil EA211", "1.6 8V EA111", "1.6 AP"],
        "Fox": ["1.0 8V EA111", "1.6 8V EA111"],
        "Polo / Virtus": ["1.0 3cil 200 TSi EA211", "1.6 16V MSI EA211"]
    },
    "Fiat": {
        "Argo / Cronos": ["1.0 3cil Firefly", "1.3 4cil Firefly"],
        "Toro / Strada": ["1.8 16V E.torQ", "1.3 Turbo Flex T270", "1.4 8V Fire Evo"]
    },
    "Ford": {
        "Ka": ["1.0 3cil Ti-VCT (Banhada)", "1.5 3cil Dragon"],
        "Fiesta / Focus": ["1.6 Zetec Rocam", "1.6 16V Sigma"]
    }
}

# 5. MONTAGEM DO MENU LATERAL
st.sidebar.header("📋 Seleção Mecânica")
lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Fabricante:", lista_fabricantes)

lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Veículo:", lista_veiculos)

lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Motorização:", lista_motores)

tipo_material = st.sidebar.radio(
    "4. Linha de Pesquisa:",
    ["Sincronismo do Motor (Pontos e Marcas)", "Esquema de Passagem da Correia Poly-V"]
)

# Chave única para identificar se o carro está na nossa memória rápida
chave_memoria = f"{fabricante_selecionada}_{veiculo_selecionado}_{motor_selecionado}"

st.info(f"⚙️ **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ DAR A PARTIDA NO GARIMPO", use_container_width=True)

# 6. PROCESSAMENTO INTELIGENTE
if botao_buscar:
    # 🚨 PASSO 1: VERIFICA SE O CARRO ESTÁ NA MEMÓRIA DE CAMINHOS CURTOS 🚨
    if chave_memoria in caminhos_curtos:
        st.success("🏁 MEMÓRIA DE BANCADA ATIVA! Entregando caminhos curtos armazenados instantaneamente.")
        
        # Puxa os dados direto do nosso banco fixo sem buscar na web
        dados_fixos = caminhos_curtos[chave_memoria]
        
        aba_diag, aba_pdf, aba_forum, aba_video = st.tabs([
            "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
        ])
        
        for x in dados_fixos["diagramas"]:
            aba_diag.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📊 {x["title"]}</h4><a href="{x["url"]}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Abrir Caminho do Diagrama</a></div>', unsafe_allow_html=True)
            
        for x in dados_fixos["manuais"]:
            aba_pdf.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📚 {x["title"]}</h4><a href="{x["url"]}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Abrir Manual Técnico / PDF</a></div>', unsafe_allow_html=True)
            
        for x in dados_fixos["foruns"]:
            aba_forum.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">💬 {x["title"]}</h4><a href="{x["url"]}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Entrar no Fórum Mecânico</a></div>', unsafe_allow_html=True)
            
        for x in dados_fixos["videos"]:
            aba_video.markdown(f"#### 🎥 {x['title']}")
            if "youtube" in x["url"].lower(): aba_video.video(x["url"])
            else: aba_video.markdown(f'[🔗 Assistir Vídeo]({x["url"]})')

    # 🚨 PASSO 2: SE NÃO ESTIVER NA MEMÓRIA, ACIONA O GARIMPEIRO NA WEB 🚨
    else:
        with st.spinner("🤖 Carro novo na oficina! Graxinim garimpando rotas abertas na internet..."):
            # Filtro focado estritamente em domínios de mecânica confiáveis do Brasil
            comando_pesquisa = (
                f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} "
                f"\"manual de oficina\" OR \"ponto de sincronismo\" site:manualdomecanico.com.br OR site:oficinabrasil.com.br OR site:omecanico.com.br"
            )
            
            try:
                resposta_ia = requests.post("https://tavily.com", json={"api_key": TAVILY_API_KEY, "query": comando_pesquisa, "search_depth": "advanced", "max_results": 10}).json()
                resultados = resposta_ia.get("results", [])
            except:
                resultados = []

            if not resultados:
                st.error("❌ Nenhuma rota limpa foi localizada pelo Garimpeiro para este motor novo. Tente termos aproximados.")
            else:
                aba_diag, aba_pdf, aba_forum, aba_video = st.tabs([
                    "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
                ])
                
                # Distribui os resultados encontrados na web de forma segura
                for item in resultados:
                    link = item.get("url", "")
                    titulo = item.get("title", "")
                    
                    if "youtube" in link.lower() or "youtu.be" in link.lower():
                        aba_video.markdown(f"#### 🎥 {titulo}")
                        aba_video.video(link)
                        aba_video.write("---")
                    elif "forum" in link.lower() or "topico" in link.lower():
                        aba_forum.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">💬 {titulo}</h4><a href="{link}" target="_blank" style="color:#3B82F6; font-weight:bold;">🔗 Acessar Fórum</a></div>', unsafe_allow_html=True)
                    elif "pdf" in link.lower() or "manual" in titulo.lower():
                        aba_pdf.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📚 {titulo}</h4><a href="{link}" target="_blank" style="color:#3B82F6; font-weight:bold;">📥 Abrir Manual / PDF</a></div>', unsafe_allow_html=True)
                    else:
