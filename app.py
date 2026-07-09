import streamlit as st
import requests
from bs4 import BeautifulSoup
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
    .stLinkButton button { background-color: #F59E0B !important; color: #111827 !important; font-weight: bold !important; border-radius: 8px !important; width: 100% !important; }
    </style>
""", unsafe_allow_html=True)

# CABEÇALHO DA GARAGEM
col_logo, col_texto_topo = st.columns(2)
col_logo.markdown("<h1 style='font-size: 80px; margin: 0; padding: 0;'>🦝</h1>", unsafe_allow_html=True)
col_texto_topo.markdown('<p class="main-title">🛠️ Garagem do Graxinim</p>', unsafe_allow_html=True)
col_texto_topo.markdown('<p class="sub-title"><b>Módulo Supercharger Inquebrável</b> | Varredura em tempo real sem limite de tokens ou chaves! 🏁</p>', unsafe_allow_html=True)

# 2. BANCO DE DADOS DE VEÍCULOS TOTALMENTE EXPANDIDO
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

st.sidebar.write("---")
st.sidebar.subheader("⚙️ Opções Adicionais")
incluir_manual_proprietario = st.sidebar.checkbox("Incluir Manual do Proprietário", value=False)

st.info(f"⚙️ **Garimpo Ativo:** {tipo_material} | **Alvo:** {fabricante_selecionada} {veiculo_selecionado} {motor_selecionado}")
botao_buscar = st.button("⚡ INICIAR VARREDURA COMPLETA NA WEB", use_container_width=True)

if botao_buscar:
    # Cria a frase limpa e otimizada de busca mecânica
    exclusoes = "-mercadolivre -olx -shopee -comprar -preco -venda -catalogo -pecas"
    termo_busca = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} manual oficina pontos {exclusoes}"
    
    # Inicializa as Abas do painel
    aba_diag, aba_pdf, aba_forum, aba_video = st.tabs([
        "📊 1. Diagramas de Ponto", "📚 2. Manuais Completos", "💬 3. Fóruns Mecânicos", "🎥 4. Vídeos e Macetes"
    ])
    
    with st.spinner("🤖 Graxinim acionando o Módulo Supercharger... Varrendo bancos de dados..."):
        try:
            # ⛏️ ENGENHARIA DE SCRAPING DIRETO (Sem depender de APIs de tokens ou limites)
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
            url_busca = f"https://duckduckgo.com{urllib.parse.quote(termo_busca)}"
            resposta = requests.get(url_busca, headers=headers, timeout=10)
            soup = BeautifulSoup(resposta.text, "html.parser")
            
            # Coleta os links e títulos reais da internet
            links_coletados = soup.find_all("a", class_="result__url")
            titulos_coletados = soup.find_all("a", class_="result__snippet")
            
            total_achados = min(len(links_coletados), 15)
            
            if total_achados == 0:
                st.error("❌ O garimpeiro não localizou dados abertos neste segundo. Tente clicar no botão novamente para restabelecer a pressão.")
            else:
                st.success(f"⚡ Mistura calibrada! Encontramos {total_achados} fontes de literatura técnica.")
                
                termos_bloqueados = ["proprietario", "usuario", "condutor", "owner", "proprietário", "usuário"]
                
                # Varre os resultados e joga nas gavetas certas sem correr risco de quebra pelo tradutor
                for i in range(total_achados):
                    try:
                        link_real = links_coletados[i]["href"]
                        # Limpa o link de redirecionamento interno do DuckDuckGo se houver
                        if "//://duckduckgo.com" in link_real:
                            link_real = urllib.parse.unquote(link_real.split("uddg=")[1])
                        
                        titulo_real = links_coletados[i].text.strip()
                        link_lower = link_real.lower()
                        titulo_lower = titulo_real.lower()
                        
                        # Filtro rígido contra manuais de proprietário invasores
                        if not incluir_manual_proprietario and any(t in titulo_lower for t in termos_bloqueados):
                            continue
                            
                        # Gaveta 1: Vídeos (YouTube, TikTok, Instagram)
                        if any(p in link_lower for p in ["youtube.com", "youtu.be", "tiktok.com", "instagram.com"]):
                            aba_video.markdown(f'<div class="card-tecnico"><h4>🎥 {titulo_real}</h4><p>Tutorial em vídeo do procedimento prático na oficina.</p></div>', unsafe_allow_html=True)
                            aba_video.link_button("🎥 ASSISTIR VÍDEO COMPLETO", link_real)
                            aba_video.write("---")
                            
                        # Gaveta 2: Manuais e PDFs
                        elif link_lower.endswith(".pdf") or "pdf" in titulo_lower or "manual" in link_lower or "manualdomecanico" in link_lower:
                            aba_pdf.markdown(f'<div class="card-tecnico"><h4>📚 {titulo_real}</h4><p>Apostila técnica estruturada ou manual digital de engenharia.</p></div>', unsafe_allow_html=True)
                            aba_pdf.link_button("📥 BAIXAR MANUAL / PDF", link_real)
                            aba_pdf.write("---")
                            
                        # Gaveta 3: Fóruns de Mecânicos reais (Oficina Brasil, Reparador, etc)
                        elif any(f in link_lower for f in ["forum", "club", "clube", "topico", "oficina-brasil", "reparador"]):
                            aba_forum.markdown(f'<div class="card-tecnico"><h4>💬 {titulo_real}</h4><p>Macetes de montagem e debates reais entre mecânicos no chão de oficina.</p></div>', unsafe_allow_html=True)
                            aba_forum.link_button("🔗 VER DISCUSSÃO NO FÓRUM", link_real)
                            aba_forum.write("---")
                            
                        # Gaveta 4: Diagramas e Esquemas Visuais
                        else:
                            aba_diag.markdown(f'<div class="card-tecnico"><h4>📊 {titulo_real}</h4><p>Esquema de referência rápida para bater o olho e ver o ponto.</p></div>', unsafe_allow_html=True)
                            aba_diag.link_button("🔍 ABRIR DIAGRAMA TÉCNICO", link_real)
                            aba_diag.write("---")
                    except:
                        continue
        except Exception as e:
            st.error(f"❌ Pressão de rede oscilando: {e}. Dê a partida no botão novamente.")
