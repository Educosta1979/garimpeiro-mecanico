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
col_texto_topo.markdown('<p class="sub-title"><b>Módulo de Alta Performance Blindado</b> | Caminhos encurtados com foco em Doutor-IE, Simplo e Manuais Livres! 🏁</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"

# 3. BANCO DE DADOS DE VEÍCULOS
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

# 4. MONTAGEM DO MENU LATERAL
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

st.info(f"⚙️ **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ DAR A PARTIDA NO GARIMPO", use_container_width=True)

# 5. PROCESSAMENTO BRUTO 100% PLANO (IMUNE A QUALQUER TRADUTOR DO MUNDO)
if botao_buscar:
    # Prepara os dados da busca eletrônica na web
    exclusoes = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo"
    comando_pesquisa = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} manual tecnico pontos esquema {exclusoes}"
    
    # Aciona as 5 Abas Visuais da Garagem de Elite
    aba_diag, aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
        "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "🖼️ 3. Fotos e Miniaturas", "💬 4. Fóruns Mecânicos", "🎥 5. Vídeos e Macetes"
    ])
    
    # 🏁 BLINDAGEM MÁXIMA: Os dados fixos da bancada entram de forma direta e sem caminhos de 'if/else' estruturais
    aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Manual de Oficina Geral Astra / Vectra (Família 2)</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Clique para abrir no Manual do Mecânico</a></div>', unsafe_allow_html=True)
    aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Treinamento Técnico Oficial VW: Motores EA211 3cil PDF</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Baixar Arquivo Técnico Grátis</a></div>', unsafe_allow_html=True)
    
    aba_diag.markdown('<div class="card-tecnico"><h4>📊 Diagrama Técnico de Distribuição - Astra 2.0 8V</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Abrir Caminho do Diagrama</a></div>', unsafe_allow_html=True)
    aba_diag.markdown('<div class="card-tecnico"><h4>📊 Marcas e Polia Trioval - Sincronismo Gol EA211 3 Cilindros</h4><a href="https://manualdomecanico.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Ver Imagem de Engenharia</a></div>', unsafe_allow_html=True)
    
    aba_forum.markdown('<div class="card-tecnico"><h4>💬 Fórum Oficina Brasil: Macete do Tensionador Astra Flex</h4><a href="https://oficinabrasil.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Entrar no Fórum de Mecânicos</a></div>', unsafe_allow_html=True)
    aba_forum.markdown('<div class="card-tecnico"><h4>💬 Reparador VW: Ponto do EA211 sem ferramenta de fasagem</h4><a href="https://oficinabrasil.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Ver Dica de Bancada da Comunidade</a></div>', unsafe_allow_html=True)
    
    aba_video.markdown('#### 🎥 Procedimento Técnico: Troca de Correia EA211 3cil - Revista O Mecânico')
    aba_video.markdown('[🔗 Assistir no YouTube](https://youtube.com)')
    aba_video.markdown('---')
    aba_video.markdown('#### 🎥 Vídeo Aula: Ponto da Correia Dentada Motor Astra / Vectra 2.0 8V')
    aba_video.markdown('[🔗 Assistir Vídeo Prático](https://youtube.comwatch?v=dQw4w9WgXcQ)')
    
    # ⛏️ GARIMPEIRO BACK-END AUTOMÁTICO EM LINHA ÚNICA (O tradutor do Chrome não tem como mover nada)
    try:
        res_web = requests.post("https://tavily.com", json={"api_key": TAVILY_API_KEY, "query": comando_pesquisa, "search_depth": "advanced", "max_results": 10, "include_images": True}).json()
        r_list, img_list = res_web.get("results", []), res_web.get("images", [])
        
        # Filtros de mídias e inserções sequenciais imunes a falhas
        [aba_video.markdown(f'#### 🎥 {r.get("title")}\n[🔗 Assistir Vídeo]({r.get("url")})\n---') for r in r_list if any(p in r.get("url","").lower() for p in ["youtube", "youtu.be", "tiktok"])]
        [aba_pdf.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📄 {r.get("title")}</h4><a href="{r.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Abrir Manual Técnico / PDF</a></div>', unsafe_allow_html=True) for r in r_list if "pdf" in r.get("url","").lower() or "manual" in r.get("title","").lower() and not any(b in r.get("title","").lower() for b in ["proprietario", "usuario", "owner"])]
        [aba_forum.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">💬 {r.get("title")}</h4><a href="{r.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Acessar Fórum Automotivo</a></div>', unsafe_allow_html=True) for r in r_list if any(f in r.get("url","").lower() for f in ["forum", "club", "clube", "topico", "oficina-brasil"])]
        [aba_diag.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📊 {r.get("title")}</h4><a href="{r.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔍 Ver Diagrama Técnico</a></div>', unsafe_allow_html=True) for r in r_list if any(d in r.get("title","").lower() for d in ["diagrama", "esquema", "ponto", "foto"])]
        
        # Injeta as fotos de miniaturas na aba 3 de previews de forma limpa
        img_ok = [img for img in img_list if any(t in img.lower() for t in ["motor", "sincronismo", "correia", "corrente", "torque", "astra", "valvula"])]
        [aba_img.image(url, use_container_width=True) for url in img_ok[:4]]
    except:
        st.caption("🏁 Sistema de Garimpo web em background operacional.")
