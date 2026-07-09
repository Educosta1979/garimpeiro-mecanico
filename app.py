import streamlit as st
import urllib.parse
import json

# 1. CONFIGURAÇÃO DA TELA (Visual Garagem Premium - Contraste Máximo)
st.set_page_config(
    page_title="Garagem do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

# Estilização CSS de Alto Padrão (Fundo escuro, textos brancos e detalhes em amarelo)
st.markdown("""
    <style>
    .stApp, [data-testid="stSidebar"], .stSidebar { background-color: #1A1D20 !important; color: #FFFFFF !important; }
    .main-title { font-size:36px !important; font-weight: bold; color: #F59E0B; margin-bottom: 5px; text-shadow: 2px 2px 4px #000; }
    .sub-title { font-size:16px !important; color: #E5E7EB; margin-bottom: 25px; }
    .card-tecnico { background-color: #2D3135; padding: 18px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #4B5563; border-left: 6px solid #F59E0B; box-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    .stTabs [data-baseweb="tab-list"] { background-color: #2D3135; padding: 10px; border-radius: 8px; border: 1px solid #4B5563; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF !important; font-weight: bold !important; font-size: 15px !important; }
    .stTabs [aria-selected="true"] { color: #F59E0B !important; border-bottom-color: #F59E0B !important; }
    div[data-testid="stMarkdownContainer"] p, label, .stSelectbox label { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Módulo Retificado de Links Diretos</b> | Links cirúrgicos sem depender de tokens ou chaves limitadas! 🏁</p>', unsafe_allow_html=True)

# 2. BANCO DE DADOS DE VEÍCULOS TOTALMENTE EXPANDIDO E SEPARADO (Strada e Toro divididas)
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
        "Strada": ["1.4 8V Fire Evo", "1.3 4cil Firefly", "1.0 Turbo T200"],
        "Toro": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Flex T270"],
        "Argo / Cronos / Pulse": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 Turbo T200"]
    },
    "Ford": {
        "Ka": ["1.0 3cil Ti-VCT (Banhada)", "1.5 3cil Dragon"],
        "Fiesta / Focus": ["1.6 Zetec Rocam", "1.6 16V Sigma"]
    }
}

# 3. MONTAGEM DO MENU LATERAL
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

st.info(f"⚙️ **Garimpo Ativo:** {tipo_material} | **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ CONECTAR ACERVOS AUTOMOTIVOS", use_container_width=True)

if botao_buscar:
    # Cria os termos exatos de engenharia para o buscador
    termo_busca = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado}"
    termo_url = urllib.parse.quote(termo_busca)
    
    # 🚨 SISTEMA DE LINKS DIRETOS CIRÚRGICOS: Cria os túneis sem risco de travar por chaves zeradas 🚨
    aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
        "📚 1. Manuais e PDFs", "🖼️ 2. Fotos e Imagens", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
    ])
    
    # Injeção Inteligente baseada no maior banco de dados técnico aberto do Brasil
    aba_pdf.markdown(f"""
    <div class="card-tecnico">
        <h4 style="color:#F59E0B;">📚 Acervo Completo: {fabricante_selecionada} {veiculo_selecionado} ({motor_selecionado})</h4>
        <p>Acessando a biblioteca digital aberta de engenharia automotiva para esquemas e apostilas densas.</p>
        <a href="https://manualdomecanico.com.br{termo_url}" target="_blank" style="color:#3B82F6; font-weight:bold; font-size:16px; text-decoration:underline;">📥 Clique aqui para abrir a Lista de PDFs desse motor</a>
    </div>
    <div class="card-tecnico">
        <h4 style="color:#F59E0B;">📄 Repositório de Apostilas: {motor_selecionado}</h4>
        <p>Pesquisa profunda em servidores de arquivos PDF técnicos.</p>
        <a href="https://google.com{termo_url}+filetype:pdf" target="_blank" style="color:#3B82F6; font-weight:bold; font-size:16px; text-decoration:underline;">📥 Buscar Manuais em PDF Direto no Google</a>
    </div>
    """, unsafe_allow_html=True)
    
    aba_img.markdown(f"""
    <div class="card-tecnico">
        <h4 style="color:#F59E0B;">🖼️ Diagrama e Marcas do Ponto de Sincronismo</h4>
        <p>Acessando o banco de dados visual do Google Imagens filtrado por enciclopédias técnicas (Doutor-IE / Simplo / Sabó).</p>
        <a href="https://google.com{termo_url}+%22doutor+ie%22+OR+%22simplo%22+OR+%22sabó%22" target="_blank" style="color:#3B82F6; font-weight:bold; font-size:16px; text-decoration:underline;">🔍 Clique aqui para ver as Fotos e Esquemas Técnicos de Ponto</a>
    </div>
    """, unsafe_allow_html=True)
    
    aba_forum.markdown(f"""
    <div class="card-tecnico">
        <h4 style="color:#F59E0B;">💬 Debate Técnico: Casos Resolvidos e Defeitos Crônicos</h4>
        <p>Acessando diretamente a base do maior Fórum de reparadores independentes do Brasil.</p>
        <a href="https://google.com{termo_url}+site:oficinabrasil.com.br/forum+OR+site:reparador.com.br" target="_blank" style="color:#3B82F6; font-weight:bold; font-size:16px; text-decoration:underline;">🔗 Clique aqui para abrir as discussões e macetes entre Mecânicos</a>
    </div>
    """, unsafe_allow_html=True)
    
    aba_video.markdown(f"""
    <div class="card-tecnico">
        <h4 style="color:#F59E0B;">🎥 Vídeos Práticos de Montagem e Sincronismo</h4>
        <p>Canal direto de passo a passo mecânico focado no motor selecionado.</p>
        <a href="https://youtube.com{termo_url}+procedimento+tecnico" target="_blank" style="color:#3B82F6; font-weight:bold; font-size:16px; text-decoration:underline;">🎥 Clique aqui para ver os vídeos práticos no YouTube</a>
    </div>
    """, unsafe_allow_html=True)
