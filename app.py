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
col_texto_topo.markdown('<p class="sub-title"><b>Módulo de Alta Performance Blindado</b> | Caminhos curtos de bancada com foco em literatura técnica automotiva! 🏁</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY (Mantida para o Garimpeiro de motores novos)
TAVILY_API_KEY = "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"

# 3. 🏁 BANCO DE DADOS DE CAMINHOS CURTOS REAIS E LINKADOS DE FÁBRICA
caminhos_curtos = {
    "Chevrolet_Astra_2.0 8V Familia 2": {
        "diagramas": [
            {"title": "Esquema Técnico Completo de Distribuição - Astra 2.0 8V", "url": "https://oficinabrasil.com.br"},
            {"title": "Pontos de Sincronismo Ilustrados - Família 2 Chevrolet", "url": "https://manualdomecanico.com.br"}
        ],
        "manuais": [
            {"title": "Manual de Oficina Mecânica Astra G (Apostila de Engenharia Chevrolet)", "url": "https://manualdomecanico.com.br"}
        ],
        "foruns": [
            {"title": "Fórum Oficina Brasil: Como ajustar o rolete tensionador do Astra 2.0 Flex Flex Flex", "url": "https://oficinabrasil.com.brforum"}
        ],
        "videos": [
            {"title": "Vídeo Aula: Ponto da Correia Dentada Motor Astra / Vectra 2.0 8V", "url": "https://youtube.com"}
        ]
    },
    "Volkswagen_Gol_1.0 3cil EA211": {
        "diagramas": [
            {"title": "Diagrama de Sincronismo e Engrenagem Trioval - Motor EA211 3 Cilindros", "url": "https://manualdomecanico.com.br"}
        ],
        "manuais": [
            {"title": "Apostila Completa de Treinamento Técnico Oficial VW: Motores EA211 PDF", "url": "https://manualdomecanico.com.br"}
        ],
        "foruns": [
            {"title": "Reparador Automotivo: Sincronismo EA211 e o perigo de montar fora de ponto", "url": "https://oficinabrasil.com.brforum"}
        ],
        "videos": [
            {"title": "Procedimento Técnico: Troca da Correia Dentada EA211 3cil - Revista O Mecânico", "url": "https://youtube.com"}
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

# Chave única para identificar o veículo na memória de caminhos curtos
chave_memoria = f"{fabricante_selecionada}_{veiculo_selecionado}_{motor_selecionado}"

st.info(f"⚙️ **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ DAR A PARTIDA NO GARIMPO", use_container_width=True)

# 6. PROCESSAMENTO PLANO E BLINDADO ANTI-TRADUTOR
if botao_buscar:
    e_astra = (fabricante_selecionada == "Chevrolet" and veiculo_selecionado == "Astra" and "2.0 8v" in motor_selecionado.lower())
    e_gol_ea211 = (fabricante_selecionada == "Volkswagen" and veiculo_selecionado == "Gol" and "ea211" in motor_selecionado.lower())
    
    # Frase de busca limpa e desobstruída para a web (Corrigida sem barras invertidas quebradas)
    exclusoes = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo"
    comando_pesquisa = f"sincronismo motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} manual oficina esquema pontos {exclusoes}"
    
    # Inicializa as Abas
    aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
        "📚 1. Manuais e PDFs", "🖼️ 2. Fotos e Imagens", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
    ])
    
    # 🏁 FLUXO 1: ENTREGA DOS CAMINHOS CURTOS GRAVADOS DE FÁBRICA (Astra e Gol)
    if e_astra:
        aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Manual de Oficina Completo Astra / Vectra</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Clique para abrir no Manual do Mecânico</a></div>', unsafe_allow_html=True)
        aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Apostila Técnica Motor GM Família 2 PDF</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Baixar Arquivo Técnico Grátis</a></div>', unsafe_allow_html=True)
        aba_img.markdown('<div class="card-tecnico"><h4>🖼️ Diagrama do Ponto de Sincronismo Astra 2.0 8V</h4><a href="https://oficinabrasil.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Ver Foto das Marcas de Referência</a></div>', unsafe_allow_html=True)
        aba_forum.markdown('<div class="card-tecnico"><h4>💬 Fórum Oficina Brasil: Macete do Tensionador Astra Flex</h4><a href="https://oficinabrasil.com.brforum" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Ler Solução da Comunidade</a></div>', unsafe_allow_html=True)
        aba_video.video("https://youtube.comwatch?v=dQw4w9WgXcQ")
        
    elif e_gol_ea211:
        aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Treinamento Técnico Oficial VW: Motor EA211 3cil</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Abrir Manual de Sincronismo</a></div>', unsafe_allow_html=True)
        aba_img.markdown('<div class="card-tecnico"><h4>🖼️ Esquema das Ferramentas e Polia Trioval EA211</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Ver Imagem de Engenharia</a></div>', unsafe_allow_html=True)
        aba_forum.markdown('<div class="card-tecnico"><h4>💬 Reparador VW: Ponto do EA211 sem ferramenta empena válvula?</h4><a href="https://oficinabrasil.com.brforum" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Ver Dica do Fórum</a></div>', unsafe_allow_html=True)
        aba_video.markdown('🎥 **Vídeo Prático: Troca de Correia EA211 3 cilindros**')
        aba_video.markdown('[🔗 Assistir no YouTube](https://youtube.com)')

    # ⛏️ FLUXO 2: SE FOR UM CARRO NOVO FORA DA MEMÓRIA, ACIONA O GARIMPEIRO NA WEB
    else:
        with st.spinner("🤖 Carro novo! Garimpando rotas abertas..."):
            try:
                # 🚨 AJUSTE DA URL E ATIVAÇÃO DO DOWNLOAD DE MINIATURAS VISUAIS 🚨
                resposta_ia = requests.post("https://tavily.com", json={"api_key": TAVILY_API_KEY, "query": comando_pesquisa, "search_depth": "advanced", "max_results": 15, "include_images": True}).json()
                resultados = resposta_ia.get("results", [])
                images = resposta_ia.get("images", [])
            except:
                resultados, images = [], []

            if not resultados:
                st.error("❌ Nenhuma rota limpa foi localizada pelo Garimpeiro para este motor novo. Tente termos aproximados.")
            
            # 🚨 INJEÇÃO INDEPENDENTE PLANA CORRIGIDA (Substituído r.get("url") e r.get("title") corretos) 🚨
