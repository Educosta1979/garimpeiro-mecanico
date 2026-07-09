import streamlit as st
from tavily import TavilyClient

# 1. Configuração visual do aplicativo de produção
st.set_page_config(page_title="Garimpeiro Mecânico IA", page_icon="⚙️", layout="centered")

st.title("⚙️ Garimpeiro Mecânico IA")
st.subheader("Seu acervo automático de diagramas e manuais de sincronismo")
st.write("Digite o motor ou veículo para buscar diagramas de correias, correntes ou poly-v na internet.")

# 2. Sua chave de acesso da IA Tavily
TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

# 3. Campo de texto para digitação do mecânico
termo_busca = st.text_input("Qual motor ou veículo você quer garimpar hoje?", 
                             placeholder="Ex: Sincronismo corrente comando Ford Ka 1.0 3 cil")

# 4. Processamento da pesquisa inteligente
if st.button("🔍 Iniciar Garimpo Inteligente"):
    if not termo_busca:
        st.warning("Por favor, digite o nome de um motor antes de buscar!")
    else:
        with st.spinner("🤖 IA vasculhando a web... Aguarde alguns segundos..."):
            try:
                # Efetua a busca profunda na internet inteira
                resposta_ia = client.search(
                    query=f"{termo_busca} manual tecnico filetype:pdf diagramas",
                    search_depth="advanced",
                    max_results=5
                )
                resultados = resposta_ia.get("results", [])
            except Exception as e:
                st.error(f"❌ Erro ao conectar com o servidor de busca: {e}")
                resultados = []

            if not resultados:
                st.error("❌ Nenhum material técnico encontrado para este termo.")
            else:
                st.success(f"✨ Encontramos {len(resultados)} materiais relevantes!")
                
                # Exibe os resultados em cartões expansíveis na tela
                for i, item in enumerate(resultados):
                    titulo = item.get("title")
                    link = item.get("url")
                    resumo = item.get("content")
                    
                    with st.expander(f"📄 {i+1}. {titulo}"):
                        st.write(f"**Resumo do Conteúdo:** {resumo}")
                        st.markdown(f"[🔗 Clique aqui para abrir o link original]({link})")
