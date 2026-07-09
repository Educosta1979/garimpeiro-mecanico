import streamlit as st
import requests

# 1. CONFIGURAÇÃO DA TELA (Visual Garagem Premium - Contraste Máximo)
st.set_page_config(
    page_title="Garagem do Graxinim - IA Automotiva", 
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
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim IA</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Módulo de Varredura Restrita com Google Gemini</b> | Buscando direto nas maiores enciclopédias mecânicas do Brasil! 🏁</p>', unsafe_allow_html=True)

# 🚨 CHAVES DE ACESSO (MÓDULO DE INTELIGÊNCIA ARTIFICIAL) 🚨
GEMINI_API_KEY = "SUA_CHAVE_DO_GEMINI_AQUI"
TAVILY_API_KEY = "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"

# 3. BANCO DE DADOS DE VEÍCULOS EXPANDIDO
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
botao_buscar = st.button("⚡ DAR A PARTIDA NO SCANNER AUTOMOTIVO POR IA", use_container_width=True)

# 5. PROCESSAMENTO COM FILTRO DE DOMÍNIO TÉCNICO PROTEGIDO
if botao_buscar:
    with st.spinner("🤖 Graxinim ativando varredura restrita nos portais de engenharia mecânica..."):
        
        # 🔥 AQUI ESTÁ O SEGREDO: Travamos a pesquisa APENAS dentro dos domínios oficiais de mecânica brasileira
        comando_pesquisa = (
            f'"{tipo_material}" motor "{motor_selecionado}" "{fabricante_selecionada} {veiculo_selecionado}" '
            f'site:manualdomecanico.com.br OR site:oficinabrasil.com.br OR site:omecanico.com.br OR site:reparadorfiat.com.br'
        )
        
        try:
            url_tavily = "https://tavily.com"
            resposta_busca = requests.post(url_tavily, json={"api_key": TAVILY_API_KEY, "query": comando_pesquisa, "search_depth": "advanced", "max_results": 15, "include_images": True}).json()
            resultados = resposta_busca.get("results", [])
            images = resposta_busca.get("images", [])
        except:
            resultados, images = [], []

        if not resultados:
            st.error("❌ Nenhuma literatura oficial foi localizada nesses acervos. Verifique se o veículo ou motorização estão corretos.")
        else:
            # Consolida os dados limpos encontrados para a IA Gemini ler e formatar
            texto_bruto_mecanico = ""
            for item in resultados:
                texto_bruto_mecanico += f"\nFONTE: {item.get('url')}\nCONTEUDO TÉCNICO: {item.get('content')}\n---"

            # Chamada para o cérebro do Google Gemini Pro organizar tudo de forma mastigada [1]
            url_gemini = f"https://googleapis.com{GEMINI_API_KEY}"
            prompt_ia = (
                f"Você é a central de engenharia automotiva Doutor-IE. Com base nas informações coletadas da web para o motor {motor_selecionado} "
                f"do {fabricante_selecionada} {veiculo_selecionado}, monte um manual de sincronismo ou instruções de montagem extremamente direto, "
                f"curto e focado em tópicos para o mecânico usar na bancada. Evite qualquer texto comercial ou enrolação.\n\n"
                f"DADOS COLETADOS:\n{texto_bruto_mecanico}"
            )
            
            try:
                resposta_gemini = requests.post(url_gemini, json={"contents": [{"parts": [{"text": prompt_ia}]}]}).json()
                analise_gemini = resposta_gemini['candidates']['content']['parts']['text']
            except:
                analise_gemini = "📝 Rota de dados estabelecida. Links diretos dos acervos disponíveis nas abas ao lado."

            # Inicializa as Abas da Garagem
            aba_diag, aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
                "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "🖼️ 3. Fotos e Miniaturas", "💬 4. Fóruns Mecânicos", "🎥 5. Vídeos e Macetes"
            ])
            
            # 📚 Injeção Direta da Análise da IA na Aba 1
            aba_diag.subheader("📊 Guia Técnico de Fasagem por IA")
            aba_diag.write(analise_gemini)
            
            # Distribui os links oficiais de engenharia de forma plana e indestrutível nas abas certas
            [aba_pdf.markdown(f'<div class="card-tecnico"><h4>📄 {r.get("title")}</h4><a href="{r.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">📥 Abrir Manual de Oficina / PDF</a></div>', unsafe_allow_html=True) for r in resultados if "pdf" in r.get("url","").lower() or "manual" in r.get("title","").lower()]
            [aba_forum.markdown(f'<div class="card-tecnico"><h4>💬 {r.get("title")}</h4><a href="{r.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold; text-decoration:underline;">🔗 Acessar Tópico do Fórum de Oficina</a></div>', unsafe_allow_html=True) for r in resultados if any(f in r.get("url","").lower() for f in ["forum", "club", "clube", "topico"])]
            [aba_video.markdown(f'#### 🎥 {r.get("title")}\n[🔗 Assistir Vídeo Prático]({r.get("url")})\n---') for r in resultados if any(p in r.get("url","").lower() for p in ["youtube", "youtu.be", "tiktok"])]
            
            # Fotos e miniaturas na aba 3
            termos_img = ["motor", "sincronismo", "correia", "corrente", "torque", "astra", "valvula"]
            img_filtradas = [img for img in images if any(t in img.lower() for t in termos_img)]
            [aba_img.image(url, use_container_width=True) for url in img_filtradas[:4]]
