import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA (Front-End)
st.set_page_config(
    page_title="Central do Graxinim - Literatura Automotiva", 
    page_icon="🦝", 
    layout="wide"
)

# Estilização visual limpa e direta
st.markdown("""
    <style>
    .main-title { font-size:32px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size:16px !important; color: #4B5563; margin-bottom: 25px; }
    .card-tecnico { background-color: #FFFFFF; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #E5E7EB; border-left: 6px solid #1E3A8A; }
    </style>
""", unsafe_allow_html=True)

# LOGO DO GRAXINIM COM ÍCONE DO SISTEMA
col_logo, col_texto_topo = st.columns()
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">⚙️ Central de Literatura Técnica Automotiva</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Mascote Oficial:</b> Graxinim Chefe - Buscando manuais e diagramas técnicos automotivos! 🛠️🚘</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DE VEÍCULOS TOTALMENTE EXPANDIDO
dados_veiculos = {
    "Chevrolet": {
        "Astra": ["2.0 8V Familia 2", "1.8 8V Familia 2", "2.0 16V Familia 2"],
        "Celta": ["1.0 8V VHC / VHC-E", "1.4 8V Econoflex"],
        "Corsa / Classic": ["1.0 8V VHC", "1.4 8V Econoflex", "1.6 8V MPFI"],
        "Cruze": ["1.4 16V Turbo Ecotec", "1.8 16V Ecotec Flex"],
        "Meriva / Montana / Agile": ["1.4 8V Econoflex", "1.8 8V Powertrain"],
        "Onix / Tracker (Novos)": ["1.0 3cil Aspirado (Banhada)", "1.0 3cil Turbo (Banhada)", "1.2 3cil Turbo CSS Prime"],
        "Onix / Cobalt / Spin (Antigos)": ["1.0 8V SPE/4", "1.4 8V SPE/4", "1.8 8V Econoflex"],
        "S10 / Trailblazer": ["2.8 16V Duramax Diesel", "2.4 8V Flexpower", "2.5 16V Ecotec Flex"],
        "Vectra / Zafira": ["2.0 8V Flexpower", "2.2 8V / 16V", "2.4 16V Flexpower"]
    },
    "Volkswagen": {
        "Amarok": ["2.0 16V Turbo Diesel", "3.0 V6 Turbo Diesel"],
        "Gol / Voyage / Saveiro / Parati": ["1.0 16V AT", "1.0 8V AT", "1.6 / 1.8 / 2.0 AP", "1.0 8V EA111", "1.6 8V EA111", "1.0 3cil EA211", "1.6 16V MSI EA211"],
        "Golf / Jetta / Tiguan": ["1.4 16V TSi EA211", "2.0 TSi EA888 (Corrente)", "2.0 TSi EA113 (Correia)", "2.5 20V 5 Cilindros"],
        "Fox / CrossFox / SpaceFox": ["1.0 8V EA111", "1.6 8V EA111", "1.6 16V MSI EA211"],
        "Polo / Virtus / Nivus / T-Cross": ["1.0 3cil 200 TSi EA211", "1.0 3cil 170 TSi", "1.6 16V MSI EA211", "1.4 250 TSi EA211"],
        "Up!": ["1.0 3cil 12V MPI EA211", "1.0 3cil 12V TSi EA211"]
    },
    "Fiat": {
        "Argo / Cronos / Pulse / Fastback": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.0 3cil Turbo T200", "1.3 4cil Turbo T270"],
        "Toro / Mobi / Uno / Strada": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.0 8V Fire / Fire Evo", "1.4 8V Fire Evo", "1.3 Firefly"],
        "Ducato": ["2.3 16V Multijet Diesel", "2.8 Turbo Diesel"]
    },
    "Jeep": {
        "Renegade / Compass / Commander": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Flex T270", "2.0 Flex Tigershark"]
    },
    "Ford": {
        "Ka / EcoSport (3 Cilindros)": ["1.0 3cil Ti-VCT (Banhada)", "1.5 3cil Dragon (Banhada)"],
        "Fiesta / Focus / EcoSport": ["1.0 Zetec Rocam", "1.6 Zetec Rocam", "1.6 16V Sigma", "2.0 16V Duratec HE"],
        "Ranger": ["2.2 16V Duratorq Diesel", "3.2 20V Duratorq Diesel", "2.3 Duratec Flex"]
    },
    "Toyota": {
        "Corolla / Corolla Cross": ["1.8 16V VVT-i", "2.0 16V Dual VVT-i", "2.0 16V Dynamic Force"],
        "Hilux / SW4": ["2.5 16V D-4D", "2.8 D-4D 1GD-FTV", "3.0 D-4D 1KD-FTV", "2.7 16V VVT-i Flex"],
        "Etios / Yaris": ["1.3 16V Dual VVT-i", "1.5 16V Dual VVT-i"]
    },
    "Honda": {
        "Civic": ["1.7 16V VTEC", "1.8 16V i-VTEC", "2.0 16V i-VTEC", "1.5 16V Turbo"],
        "Fit / City / HR-V": ["1.4 8V i-DSI", "1.5 16V i-VTEC Flex", "1.8 16V i-VTEC"]
    },
    "Renault": {
        "Kwid / Logan / Sandero": ["1.0 3cil 12V SCe", "1.6 16V SCe H4M", "1.0 16V D4D", "1.6 16V K4M"],
        "Duster / Oroch / Captur": ["2.0 16V F4R", "1.6 16V SCe", "1.3 Flex Turbo TCe"],
        "Master": ["2.3 16V dCi Turbo Diesel"]
    },
    "Hyundai / Kia": {
        "HB20 / HB20S / Creta": ["1.0 3cil Kappa", "1.0 3cil Kappa Turbo GDI", "1.6 16V Gamma", "2.0 16V Nu Flex"],
        "HR / Bongo / Tucson": ["2.5 Diesel Turbo D4CB", "2.5 Diesel Turbo D4BH", "2.0 16V Beta"]
    }
}

# 4. MONTAGEM DO MENU LATERAL
st.sidebar.header("📋 Filtros de Seleção Técnica")

lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Escolha a Fabricante:", lista_fabricantes)

lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Escolha o Veículo:", lista_veiculos)

lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Escolha a Motorização:", lista_motores)

lista_anos = ["Não Informar (Buscar Todos)"] + [str(ano) for ano in range(2000, 2027)]
ano_selecionado = st.sidebar.selectbox("4. Ano do Modelo (Opcional):", lista_anos, index=0)

tipo_material = st.sidebar.radio(
    "5. Tipo de Literatura Exigida:",
    [
        "Diagrama Sincronismo Pontos", 
        "Instalacao Correia Poly-V", 
        "Torque Cabecote Ordem Aperto"
    ]
)

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Opções Adicionais")
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

# 5. MONTAGEM DO COMANDO (Calibrado e Otimizado para não falhar)
texto_ano = "" if ano_selecionado == "Não Informar (Buscar Todos)" else f"ano {ano_selecionado}"
exclusoes_ajustadas = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo"

# Busca limpa e direta, garantindo que o servidor da IA encontre dados
comando_pesquisa = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} {texto_ano} manual mecânico esquema pontos"

# Painel Central de Informações
col_info, col_btn = st.columns(2)
col_info.info(f"⚙️ **Buscando:** {tipo_material} | **Carro:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = col_btn.button("🚀 Garimpar Literatura Total (Mão na Massa)", use_container_width=True)

# 6. PROCESSAMENTO
if botao_buscar:
    with st.spinner("🤖 Graxinim varrendo a internet..."):
        try:
            resposta_ia = client.search(
                query=comando_pesquisa,
                search_depth="advanced",
                max_results=25, # Aumentado para trazer o máximo de mídias possíveis
                include_images=True
            )
            resultados = resposta_ia.get("results", [])
            imagens_encontradas = resposta_ia.get("images", [])
        except Exception as e:
            st.error(f"❌ Falha de comunicação: {e}")
            resultados, imagens_encontradas = [], []

        if not resultados:
            st.error("❌ Nenhuma literatura foi localizada na web para esta configuração.")
        else:
            lista_pdfs = []
            lista_foruns = []
            lista_videos = []
            lista_portais = []
            
            plataformas_video = ["youtube", "youtu.be", "tiktok", "instagram", "kwai", "video"]
            sites_foruns = ["forum", "oficina-brasil", "mecanicos", "reparador", "club", "clube", "injetronic"]
            termos_bloqueados_manuais = ["proprietario", "usuario", "condutor", "owner", "proprietário", "usuário"]

            for item in resultados:
                link = item.get("url", "")
                titulo = item.get("title", "")
                
                if not incluir_manual_proprietario and any(termo in titulo.lower() for termo in termos_bloqueados_manuais):
                    continue

                if any(p in link.lower() for p in plataformas_video) or "video" in titulo.lower():
                    lista_videos.append(item)
                elif link.lower().endswith(".pdf") or "pdf" in titulo.lower() or "manualdomecanico" in link.lower():
                    lista_pdfs.append(item)
                elif any(f in link.lower() for f in sites_foruns) or any(f in titulo.lower() for f in sites_foruns):
                    lista_foruns.append(item)
                else:
                    lista_portais.append(item)
            
            # Abas principais
            aba_pdf, aba_img, aba_forum, aba_video, aba_portais = st.tabs([
                "📚 1. Manuais em PDF", "🖼️ 2. Fotos e Imagens", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes", "🌐 5. Portais Técnicos (Scribd/Gerais)"
            ])
            
            # Injeta dados na Aba 1
            if not lista_pdfs:
                aba_pdf.info("Nenhum arquivo PDF direto detectado nesta pesquisa.")
            for item in lista_pdfs:
                aba_pdf.markdown(f'<div class="card-tecnico"><h4>📄 {item.get("title")}</h4><a href="{item.get("url")}" target="_blank">📥 Abrir Literatura Técnica / Download</a></div>', unsafe_allow_html=True)

            # Injeta dados na Aba 2 (Imagens - Puxa tudo o que encontrar sobre o motor)
            if not imagens_encontradas:
                aba_img.info("A IA não extraiu fotos diretas isoladas. Verifique os manuais na Aba 1 ou Aba 5 que possuem fotos internas.")
            else:
                aba_img.success(f"Encontramos {len(imagens_encontradas)} diagramas e fotos na rede:")
                for img_url in imagens_encontradas[:8]:
                    aba_img.image(img_url, use_container_width=True)
                    aba_img.write("---")

            # Injeta dados na Aba 3 (Fóruns)
            if not lista_foruns:
