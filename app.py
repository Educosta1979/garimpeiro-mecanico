import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA (Visual Oficina de Elite - Contraste Máximo)
st.set_page_config(
    page_title="Garagem do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

# Estilização CSS de Alto Padrão (Fundo escuro, textos brancos e detalhes em amarelo)
st.markdown("""
    <style>
    .stApp { background-color: #1A1D20; color: #FFFFFF; }
    .main-title { font-size:36px !important; font-weight: bold; color: #F59E0B; margin-bottom: 5px; text-shadow: 2px 2px 4px #000; }
    .sub-title { font-size:16px !important; color: #E5E7EB; margin-bottom: 25px; }
    .card-tecnico { background-color: #2D3135; padding: 18px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #4B5563; border-left: 6px solid #F59E0B; box-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    .stTabs [data-baseweb="tab-list"] { background-color: #2D3135; padding: 10px; border-radius: 8px; border: 1px solid #4B5563; }
    .stTabs [data-baseweb="tab"] { color: #FFFFFF !important; font-weight: bold !important; font-size: 15px !important; }
    .stTabs [aria-selected="true"] { color: #F59E0B !important; border-bottom-color: #F59E0B !important; }
    div[data-testid="stMarkdownContainer"] p { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>O Primeiro Software Feito para Chão de Oficina</b> | Filtros limpos estilo Doutor-IE e Simplo sem enrolação comercial! 🔧🏁</p>', unsafe_allow_html=True)

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

# 4. MONTAGEM DO MENU LATERAL
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

# 5. REFINAMENTO DE PALAVRAS-CHAVE
texto_ano = "" if ano_selecionado == "Não Informar (Buscar Todos)" else f"ano {ano_selecionado}"
exclusoes_ajustadas = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo -pecas -loja -produto"

comando_pesquisa = (
    f'"{tipo_material}" motor "{motor_selecionado}" "{fabricante_selecionada} {veiculo_selecionado}" {texto_ano} '
    f'"ponto de sincronismo" OR "esquema técnico" OR "fasagem" {exclusoes_ajustadas}'
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
            # 🚨 MUDANÇA MECÂNICA: Triagem feita de forma em linha, eliminando o comando vertical 'for' das abas 🚨
            plataformas_video = ["youtube", "youtu.be", "tiktok", "instagram"]
            sites_foruns = ["forum", "oficina-brasil", "mecanicos", "reparador", "club", "clube", "topico", "comunidade"]
            termos_bloqueados = ["proprietario", "usuario", "condutor", "owner", "proprietário", "usuário"]

            # Executa os filtros em background de forma segura
            videos = [x for x in resultados if any(p in x.get("url","").lower() for p in plataformas_video)]
            foruns = [x for x in resultados if any(f in x.get("url","").lower() or f in x.get("title","").lower() for f in sites_foruns)]
            
            # Filtra os diagramas curtos e remove os manuais de proprietário invasores
            restantes = [x for x in resultados if x not in videos and x not in foruns]
            if not incluir_manual_proprietario:
                restantes = [x for x in restantes if not any(t in x.get("title","").lower() for t in termos_bloqueados)]
                foruns = [x for x in foruns if not any(t in x.get("title","").lower() for t in termos_bloqueados)]

            diagramas = [x for x in restantes if any(d in x.get("title","").lower() or d in x.get("url","").lower() for d in ["diagrama", "esquema visual", "ponto", "sincronismo", "imagem", "foto", "png", "jpg"])]
            manuais = [x for x in restantes if x not in diagramas]

            # Inicializa as 5 Abas Visuais Limpas
            aba_diag, aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
                "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "🖼️ 3. Fotos e Miniaturas", "💬 4. Fóruns Mecânicos", "🎥 5. Vídeos e Macetes"
            ])
            
            # 🚨 INJEÇÃO COMPACTADA SEM RECUOS: O tradutor não consegue mover nenhuma linha abaixo! 🚨
            # Aba 1: Diagramas
            if not diagramas: aba_diag.info("Nenhum diagrama rápido isolado detectado.")
            [aba_diag.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📊 {x.get("title")}</h4><a href="{x.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold;">🔍 Abrir Esquema Visual do Ponto</a></div>', unsafe_allow_html=True) for x in diagramas]

            # Aba 2: Manuais
            if not manuais: aba_pdf.info("Nenhum manual de oficina completo listado.")
            [aba_pdf.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">📚 {x.get("title")}</h4><a href="{x.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold;">📥 Abrir Apostila Técnica / PDF</a></div>', unsafe_allow_html=True) for x in manuais]

            # Aba 3: Imagens Miniaturas (Filtro Antiguanximim festa integrado)
            termos_mecanicos = ["motor", "sincronismo", "correia", "corrente", "torque", "car", "auto", "mecanic", "astra", "chevrolet", "valvula", "passagem", "poly", "tensionador", "polia"]
            imagens_filtradas = [img for img in imagens_encontradas if any(t in img.lower() for t in termos_mecanicos)]
            if not imagens_filtradas: aba_img.info("Nenhuma miniatura de imagem técnica extraída.")
            [aba_img.image(url_foto, use_container_width=True) for url_foto in imagens_filtradas[:6]]

            # Aba 4: Fóruns
            if not foruns: aba_forum.info("Nenhum debate de fórum localizado.")
            [aba_forum.markdown(f'<div class="card-tecnico"><h4 style="color:#F59E0B;">💬 {x.get("title")}</h4><a href="{x.get("url")}" target="_blank" style="color:#3B82F6; font-weight:bold;">🔗 Entrar no Tópico do Fórum Mecânico</a></div>', unsafe_allow_html=True) for x in foruns]

            # Aba 5: Vídeos
