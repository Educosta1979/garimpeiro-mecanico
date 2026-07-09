import streamlit as st
from tavily import TavilyClient

# 1. CONFIGURAÇÃO DA TELA PROFISSIONAL (Front-End)
st.set_page_config(
    page_title="Acervo Técnico Automotivo - IA", 
    page_icon="⚙️", 
    layout="wide" # Tela cheia para visualização profissional
)

# Estilização visual moderna (CSS para deixar o visual limpo)
st.markdown("""
    <style>
    .main-title { font-size:36px !important; font-weight: bold; color: #1E3A8A; margin-bottom: 5px; }
    .sub-title { font-size:18px !important; color: #4B5563; margin-bottom: 25px; }
    </style>
""", unsafe_allow_exists=True)

st.markdown('<p class="main-title">⚙️ Sistema Integrado de Literatura Mecânica</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Garimpo Inteligente e Inteligência Artificial para Sincronismo de Motores</p>', unsafe_allow_html=True)

# 2. CHAVE TAVILY
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. BANCO DE DADOS DE FILTROS (Dicionário em Cascata)
# Você pode aumentar essa lista adicionando mais carros e motores depois!
dados_veiculos = {
    "Volkswagen": {
        "Gol": ["1.0 3cil EA211", "1.6 8V EA111", "1.0 8V EA111"],
        "Golf": ["1.4 TSi EA211", "2.0 TSi TSi", "1.6 16V TSi"],
        "Amarok": ["2.0 16V Turbo Diesel", "3.0 V6 Diesel"]
    },
    "Ford": {
        "Ka": ["1.0 3cil Ti-VCT", "1.5 3cil Dragon", "1.5 16V Sigma"],
        "Ranger": ["2.2 Duratorq", "3.2 Duratorq", "2.0 Panther Diesel"],
        "EcoSport": ["1.6 16V Sigma", "2.0 16V Duratec"]
    },
    "Fiat": {
        "Argo": ["1.0 3cil Firefly", "1.3 4cil Firefly", "1.8 16V E.torQ"],
        "Toro": ["1.8 16V E.torQ", "2.0 16V Multijet Diesel", "1.3 Turbo Firefly"],
        "Uno": ["1.0 8V Fire", "1.0 3cil Firefly"]
    },
    "Chevrolet": {
        "Onix": ["1.0 3cil Aspirado SPE/3", "1.0 3cil Turbo CSS Prime", "1.4 8V SPE/4"],
        "S10": ["2.8 Duramax Diesel", "2.4 Flexpower", "2.5 Ecotec Flex"],
        "Cruze": ["1.4 Turbo Ecotec", "1.8 16V Ecotec"]
    }
}

# 4. CRIAÇÃO DOS CAMPOS VISUAIS EM COLUNAS (Organização do Painel)
st.sidebar.header("📋 Filtros de Seleção Técnica")

# Filtro 1: Fabricante
lista_fabricantes = sorted(list(dados_veiculos.keys()))
fabricante_selecionada = st.sidebar.selectbox("1. Escolha a Fabricante:", lista_fabricantes)

# Filtro 2: Veículo (Atualiza sozinho baseado na fabricante)
lista_veiculos = sorted(list(dados_veiculos[fabricante_selecionada].keys()))
veiculo_selecionado = st.sidebar.selectbox("2. Escolha o Veículo:", lista_veiculos)

# Filtro 3: Motorização (Atualiza sozinho baseado no veículo)
lista_motores = dados_veiculos[fabricante_selecionada][veiculo_selecionado]
motor_selecionado = st.sidebar.selectbox("3. Escolha a Motorização:", lista_motores)

# Filtro 4: Ano do Veículo
lista_anos = [str(ano) for ano in range(2000, 2027)]
ano_selecionado = st.sidebar.selectbox("4. Ano do Modelo:", lista_anos, index=len(lista_anos)-3)

# Filtro 5: Tipo de Material Procurado
tipo_material = st.sidebar.radio(
    "5. Qual componente você quer o diagrama?",
    ["Sincronismo da Correia Dentada", "Sincronismo da Corrente de Comando", "Esquema da Correia de Acessórios (Poly-V)", "Tabela de Torques de Cabeçote"]
)

# 5. MONTAGEM AUTOMÁTICA DA CONSULTA DE IA
# O próprio sistema junta as escolhas dos botões para criar a pergunta perfeita para a IA
termo_busca = f"{tipo_material} motor {motor_selecionado} {fabricante_selecionada} {veiculo_selecionado} ano {ano_selecionado}"

# Painel Central de Confirmação
col1, col2 = st.columns([2, 1])
with col1:
    st.info(f"🔍 **Parâmetro de Busca Atualizado:**\n\n*{termo_busca}*")

with col2:
    st.write("")
    st.write("")
    botao_buscar = st.button("🚀 Iniciar Busca Avançada", use_container_width=True)

# 6. PROCESSAMENTO E EXIBIÇÃO DOS RESULTADOS EM PAINÉIS MODERNOS
if botao_buscar:
    with st.spinner("🤖 Consultando acervos digitais e convertendo manuais técnicos..."):
        try:
            resposta_ia = client.search(
                query=f"{termo_busca} manual tecnico filetype:pdf diagramas",
                search_depth="advanced",
                max_results=5
            )
            resultados = resposta_ia.get("results", [])
        except Exception as e:
            st.error(f"❌ Falha de rede: {e}")
            resultados = []

        if not resultados:
            st.error("❌ Nenhuma literatura oficial ou diagrama foi localizado para essa configuração específica.")
        else:
            st.success(f"✅ Sucesso! Encontramos {len(resultados)} manuais compatíveis com a sua busca.")
            st.write("---")
            
            # Exibe os resultados usando componentes visuais de alta qualidade
            for i, item in enumerate(resultados):
                titulo = item.get("title")
                link = item.get("url")
                resumo = item.get("content")
                
                # Container visual para cada resultado
                with st.container():
                    st.markdown(f"### 📄 {i+1}. {titulo}")
                    st.write(f"**Trecho extraído do manual:** {resumo}")
                    st.markdown(f"📥 **[Clique aqui para abrir ou baixar o material completo]({link})**")
                    st.write("---")
