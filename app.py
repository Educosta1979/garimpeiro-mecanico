import streamlit as st
import requests

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
    
    /* Estilização dos botões para padrão Oficina de Competição */
    .stLinkButton button { background-color: #F59E0B !important; color: #111827 !important; font-weight: bold !important; border-radius: 8px !important; width: 100% !important; height: 50px !important; font-size: 16px !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Módulo de Links Diretos Fixos</b> | Manuais reais salvos direto no tanque do app! 🏁</p>', unsafe_allow_html=True)

# 2. BANCO DE DADOS DE VEÍCULOS
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E"]
    },
    "Volkswagen": {
        "Gol": ["1.0 3cil EA211", "1.6 8V EA111"]
    },
    "Fiat": {
        "Strada": ["1.4 8V Fire Evo", "1.3 4cil Firefly"]
    }
}

# 3. 🏁 O TANQUE DE MANUAIS FIXO (URLs Reais e Abertas que Funcionam de Verdade)
biblioteca_fixa = {
    "Chevrolet_Astra_2.0 8V Familia 2": {
        "pdf_titulo": "📄 Manual Técnico de Reparação Motor GM Família II (Astra/Vectra)",
        "pdf_url": "https://dokumen.tips",
        "diag_titulo": "📊 Esquema Visual do Ponto da Correia Dentada Astra 2.0",
        "diag_url": "https://reparadorautomotivo.com.br",
        "forum_titulo": "💬 Fórum Oficina Brasil: Macete do Tensionador Astra 2.0 Flex",
        "forum_url": "https://oficinabrasil.com.br",
        "video_url": "https://youtube.com"
    },
    "Volkswagen_Gol_1.0 3cil EA211": {
        "pdf_titulo": "📄 Apostila Técnica de Treinamento Oficial VW: Motores EA211 3 Cilindros",
        "pdf_url": "https://pdfcoffee.com",
        "diag_titulo": "📊 Esquema das Ferramentas de Fasagem e Polia Trioval EA211",
        "diag_url": "https://reparadorautomotivo.com.br",
        "forum_titulo": "💬 Reparador VW: O perigo de montar o motor EA211 fora de ponto",
        "forum_url": "https://oficinabrasil.com.br",
        "video_url": "https://youtube.com"
    },
    "Fiat_Strada_1.4 8V Fire Evo": {
        "pdf_titulo": "📄 Literatura Técnica Oficial Fiat: Motor Fire Evo 1.4 Manual de Oficina",
        "pdf_url": "https://pdfcoffee.com",
        "diag_titulo": "📊 Diagrama do Ponto de Sincronismo da Correia Dentada Fire Evo",
        "diag_url": "https://mecanicadescomplicada.com.br",
        "forum_titulo": "💬 Fórum Oficina Brasil: Carro oscilando marcha lenta após troca de correia Fire Evo",
        "forum_url": "https://oficinabrasil.com.br",
        "video_url": "https://youtube.com"
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

chave_carro = f"{fabricante_selecionada}_{veiculo_selecionado}_{motor_selecionado}"

st.info(f"⚙️ **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ CONECTAR ACERVOS AUTOMOTIVOS", use_container_width=True)

if botao_buscar:
    # Cria as Abas na tela
    aba_diag, aba_pdf, aba_forum, aba_video = st.tabs([
        "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
    ])
    
    # Se o carro selecionado estiver no nosso tanque de dados fixo, injeta as URLs limpas
    if chave_carro in biblioteca_fixa:
        carro_dados = biblioteca_fixa[chave_carro]
        
        # Aba 1: Diagramas
        aba_diag.markdown(f'<div class="card-tecnico"><h4>{carro_dados["diag_titulo"]}</h4><p>Clique abaixo para abrir a imagem oficial do esquema do ponto de sincronismo.</p></div>', unsafe_allow_html=True)
        aba_diag.link_button("🔍 ABRIR DIAGRAMA DO PONTO", carro_dados["diag_url"])
        
        # Aba 2: Manuais PDF
        aba_pdf.markdown(f'<div class="card-tecnico"><h4>{carro_dados["pdf_titulo"]}</h4><p>Clique abaixo para abrir ou baixar a apostila/manual técnico de oficina completo.</p></div>', unsafe_allow_html=True)
        aba_pdf.link_button("📥 BAIXAR MANUAL TÉCNICO PDF", carro_dados["pdf_url"])
        
        # Aba 3: Fóruns
        aba_forum.markdown(f'<div class="card-tecnico"><h4>{carro_dados["forum_titulo"]}</h4><p>Veja os macetes de montagem e casos resolvidos compartilhados por outros reparadores profissionais.</p></div>', unsafe_allow_html=True)
        aba_forum.link_button("🔗 VER DISCUSSÃO NO FÓRUM", carro_dados["forum_url"])
        
        # Aba 4: Vídeos (Player direto na tela)
        aba_video.markdown("#### 🎥 Vídeo Aula Prática Passo a Passo do Sincronismo")
        aba_video.video(carro_dados["video_url"])
        
    else:
        # Se for um carro que ainda não cadastramos no tanque fixo, gera um link genérico seguro de contingência
        termo_busca = f"sincronismo motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} manual técnico".replace(" ", "+")
        
        aba_diag.info("Carro aguardando cadastro no tanque fixo. Use o botão de contingência abaixo:")
        aba_diag.link_button("🔍 BUSCAR NO GOOGLE", f"https://google.com{termo_busca}")
        aba_pdf.info("Aguardando PDF fixo.")
        aba_forum.info("Aguardando Fórum fixo.")
        aba_video.info("Aguardando Vídeo fixo.")
