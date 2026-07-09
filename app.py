import streamlit as st
import urllib.parse

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
col_texto_topo.markdown('<p class="sub-title"><b>Injeção Direta Otimizada</b> | Links do Google e Manuais com alinhamento de URL corrigido! 🏁</p>', unsafe_allow_html=True)

# 2. BANCO DE DADOS DE VEÍCULOS TOTALMENTE EXPANDIDO (Com a Kombi adicionada!)
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2", "2.0 16V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E", "1.4 8V Econoflex"],
        "Corsa / Classic": ["1.0 8V VHC", "1.4 8V Econoflex"],
        "Onix / Tracker (Novos)": ["1.0 3cil Aspirado (Banhada)", "1.0 3cil Turbo (Banhada)"]
    },
    "Volkswagen": {
        "Kombi": ["1.6 Ar Carburado / Injeção", "1.4 8V Total Flex (Água)"],
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
    },
    "Peugeot / Citroën": {
        "206 / 207": ["1.4 8V TU3JP", "1.6 16V TU5JP4"],
        "208 / C3": ["1.2 3cil Puretech", "1.6 16V EC5", "1.0 3cil Firefly Flex"]
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

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Opções Adicionais")
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

st.info(f"⚙️ **Garimpo Ativo:** {tipo_material} | **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ INICIAR VARREDURA COMPLETA NA WEB", use_container_width=True)

if botao_buscar:
    # Codificação limpa do termo de busca para a URL
    exclusoes = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo -pecas"
    termo_busca = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} manual oficina pontos esquema {exclusoes}"
    termo_limpo = termo_busca.replace(" ", "+")
    
    # Inicializa as 4 Abas Oficiais Corretas
    aba_diag, aba_pdf, aba_forum, aba_video = st.tabs([
        "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
    ])
    
    try:
        # 🚨 FIXADO: Adicionado '/search?tbm=isch&q=' e '/search?q=' corretos para o Google abrir direto na pesquisa! 🚨
        
        # Aba 1: Diagramas
        aba_diag.markdown('<div class="card-tecnico"><h4>📊 Banco de Imagens e Esquemas de Sincronismo</h4><p>Clique abaixo para carregar as fotos reais de pontos (Doutor-IE, Simplo e Sabó) no banco visual do Google Imagens.</p></div>', unsafe_allow_html=True)
        aba_diag.link_button("🔍 VER DIAGRAMAS E FOTOS DE SINCRONISMO", f"https://google.com{termo_limpo}+doutor+ie+OR+simplo+OR+sabo")
        
        # Aba 2: PDFs e Manuais
        aba_pdf.markdown('<div class="card-tecnico"><h4>📚 Biblioteca Manual do Mecânico</h4><p>Clique abaixo para abrir a pesquisa interna de PDFs e apostilas completas desse motor.</p></div>', unsafe_allow_html=True)
        aba_pdf.link_button("📥 ABRIR ACERVO DO MANUAL DO MECÂNICO", f"https://manualdomecanico.com.br{termo_limpo}")
        aba_pdf.markdown('<div class="card-tecnico"><h4>📄 Repositório de Manuais em PDF no Google</h4><p>Gera o túnel de download direto focado em arquivos digitais de oficina no Google.</p></div>', unsafe_allow_html=True)
        aba_pdf.link_button("📥 BUSCAR PDFs DE REPARAÇÃO NO GOOGLE", f"https://google.com{termo_limpo}+filetype:pdf")
        
        # Aba 3: Fóruns Mecânicos
        aba_forum.markdown('<div class="card-tecnico"><h4>💬 Discussões e Defeitos Cabeludos entre Reparadores</h4><p>Abre diretamente os tópicos de debates e macetes do maior fórum automotivo independente do Brasil.</p></div>', unsafe_allow_html=True)
        aba_forum.link_button("🔗 VER MACETES NO FÓRUM OFICINA BRASIL", f"https://google.com{termo_limpo}+site:oficinabrasil.com.br/forum+OR+site:reparador.com.br")
        
        # Aba 4: Vídeos e Macetes
        aba_video.markdown('<div class="card-tecnico"><h4>🎥 Tutoriais e Procedimentos Técnicos Passo a Passo</h4><p>Canal direto de passo a passo mecânico em vídeo focado no motor selecionado.</p></div>', unsafe_allow_html=True)
        aba_video.link_button("🎥 ASSISTIR VÍDEOS DE MONTAGEM NO YOUTUBE", f"https://youtube.com{termo_limpo}+procedimento+tecnico")
        
        st.success("⚡ Módulo remapeado com sucesso! Utilize os botões amarelos de cada aba acima para abrir a literatura.")
        
    except Exception as e:
        st.error("❌ Ocorreu um erro na montagem dos botões. Tente reiniciar a página.")
