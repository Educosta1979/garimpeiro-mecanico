import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA (Layout Garagem de Alta Performance)
st.set_page_config(
    page_title="Garagem do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

# Estilização CSS: Visual de Oficina Premium / Garagem Noturna
st.markdown("""
    <style>
    .stApp { background-color: #111827; color: #F3F4F6; }
    .main-title { font-size:36px !important; font-weight: bold; color: #3B82F6; margin-bottom: 5px; text-shadow: 2px 2px 4px #000; }
    .sub-title { font-size:16px !important; color: #9CA3AF; margin-bottom: 25px; }
    .card-tecnico { background-color: #1F2937; padding: 18px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #374151; border-left: 6px solid #EF4444; box-shadow: 3px 3px 10px rgba(0,0,0,0.5); }
    .stTabs [data-baseweb="tab-list"] { background-color: #1F2937; padding: 10px; border-radius: 8px; }
    .stTabs [data-baseweb="tab"] { color: #9CA3AF !important; font-weight: bold; }
    .stTabs [aria-selected="true"] { color: #3B82F6 !important; border-bottom-color: #3B82F6 !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 90px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Literatura Mecânica de Precisão</b> | Analisando Doutor-IE, Simplo e Fóruns Técnicos sem enrolação eletrônica! 🔧🏁</p>', unsafe_allow_html=True)

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

# 🚨 RETIRADA A OPÇÃO DE BUSCA POR MANUAIS NO SELETOR - FOCO TOTAL EM CONJUNTO TÉCNICO 🚨
tipo_material = st.sidebar.radio(
    "5. Linha de Pesquisa:",
    [
        "Sincronismo do Motor (Pontos e Marcas)", 
        "Esquema de Passagem da Correia Poly-V"
    ]
)

# 5. MONTAGEM DO COMANDO ROBUSTO
texto_ano = "" if ano_selecionado == "Não Informar (Buscar Todos)" else f"ano {ano_selecionado}"
exclusoes_ajustadas = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo"

# Comando expandido injetando gatilhos fortes para forçar o retorno dos fóruns mecânicos
comando_pesquisa = (
    f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} {texto_ano} "
    f"manual oficina diagramas esquema \"oficina brasil\" OR \"reparador\" OR \"resolvido\" OR \"defeito\" {exclusoes_ajustadas}"
)

# Painel Central de Informações
col_info, col_btn = st.columns(2)
col_info.info(f"⚙️ **Garimpo Ativo:** {tipo_material} | **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = col_btn.button("⚡ DAR A PARTIDA NO GARIMPO", use_container_width=True)

# 6. PROCESSAMENTO
if botao_buscar:
    with st.spinner("🤖 Graxinim vasculhando as bancadas da internet..."):
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
            # Novas gavetas incluindo a separação entre diagramas e manuais
            lista_diagramas = []
            lista_manuais = []
            lista_foruns = []
            lista_videos = []
            
            plataformas_video = ["youtube", "youtu.be", "tiktok", "instagram"]
            sites_foruns = ["forum", "oficina-brasil", "mecanicos", "reparador", "club", "clube", "topico"]

            for item in resultados:
                link = item.get("url", "").lower()
                titulo = item.get("title", "").lower()
                
                # Ignora cartilhas de condutor
                if any(t in titulo for t in ["proprietario", "usuario", "condutor", "owner"]):
                    continue

                if any(p in link for p in plataformas_video):
                    lista_videos.append(item)
                elif any(f in link for f in sites_foruns) or any(f in titulo for f in sites_foruns):
                    lista_foruns.append(item)
                # 🚨 SEPARAÇÃO: Se contiver palavras de imagem ou esquema, vai para Diagramas, se for arquivo denso vai para Manuais
                elif any(d in titulo or d in link for d in ["diagrama", "esquema", "ponto", "sincronismo", "imagem", "foto"]):
                    lista_diagramas.append(item)
                else:
                    lista_manuais.append(item)
            
            # 🚨 NOVAS ABAS DA GARAGEM REORGANIZADAS 🚨
            aba_diag, aba_pdf, aba_img, aba_forum, aba_video = st.tabs([
                "📊 1. Diagramas de Ponto", 
                "📚 2. Manuais Completos", 
                "🖼️ 3. Fotos e Miniaturas", 
                "💬 4. Fóruns Mecânicos", 
                "🎥 5. Vídeos e Macetes"
            ])
            
            # Aba 1: Diagramas Rápidos
            if not lista_diagramas: aba_diag.info("Nenhum link focado em diagrama isolado foi detectado. Veja a aba de manuais.")
            for item in lista_diagramas:
                aba_diag.markdown(f'<div class="card-tecnico"><h4>📊 {item.get("title")}</h4><a href="{item.get("url")}" target="_blank">🔍 Abrir Esquema Visual</a></div>', unsafe_allow_html=True)

            # Aba 2: Manuais de Oficina
            if not lista_manuais: aba_pdf.info("Nenhum manual completo em formato PDF extenso foi localizado.")
            for item in lista_manuais:
                aba_pdf.markdown(f'<div class="card-tecnico"><h4>📚 {item.get("title")}</h4><a href="{item.get("url")}" target="_blank">📥 Abrir Manual Técnico / Scribd / PDF</a></div>', unsafe_allow_html=True)

            # Aba 3: Imagens e Previews (FILTRAGEM DE DESCRIÇÃO ANTI-GUAXINIM FESTA)
            # 🛡️ PENTE FINO: Só deixa passar a foto se na URL ou na tag tiver termos puros da mecânica automotiva
            termos_mecanicos = ["motor", "sincronismo", "correia", "corrente", "torque", "car", "auto", "mecanic", "astra", "chevrolet", "valvula", "passagem", "poly", "tensionador", "polia"]
            imagens_filtradas = [img for img in imagens_encontradas if any(t in img.lower() for t in termos_mecanicos)]
            
            if not imagens_filtradas: 
                aba_img.info("Nenhum diagrama limpo em imagem isolada foi extraído de forma direta.")
            for url_foto in imagens_filtradas[:6]:
                aba_img.image(url_foto, use_container_width=True)
                aba_img.write("---")

            # Aba 4: Fóruns Mecânicos (Combustível aditivado nos resultados)
            if not lista_foruns: aba_forum.info("Nenhum tópico de debate aberto foi localizado para este motor.")
            for item in lista_foruns:
