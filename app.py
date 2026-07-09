# 1. Instala as ferramentas essenciais
!pip install streamlit tavily-python -q

# 2. Cria o arquivo do aplicativo atualizado e leve
with open('app.py', 'w', encoding='utf-8') as f:
    f.write('''
import streamlit as st
from tavily import TavilyClient

st.set_page_config(page_title="Garimpeiro Mecânico IA", page_icon="⚙️")

st.title("⚙️ Garimpeiro Mecânico IA")
st.subheader("Seu acervo automático de diagramas de sincronismo")

TAVILY_API_KEY = "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"
client = TavilyClient(api_key=TAVILY_API_KEY)

termo_busca = st.text_input("Qual motor ou veículo você quer garimpar hoje?", 
                             placeholder="Ex: Sincronismo corrente comando Ford Ka 1.0 3 cil")

if st.button("🔍 Iniciar Garimpo Inteligente"):
    if not termo_busca:
        st.warning("Por favor, digite o nome de um motor!")
    else:
        with st.spinner("🤖 IA vasculhando a web..."):
            try:
                resposta_ia = client.search(
                    query=f"{termo_busca} manual tecnico filetype:pdf diagramas",
                    search_depth="advanced",
                    max_results=5
                )
                resultados = resposta_ia.get("results", [])
            except Exception as e:
                st.error(f"❌ Erro na busca: {e}")
                resultados = []

            if not resultados:
                st.error("❌ Nenhum material técnico encontrado.")
            else:
                st.success(f"✨ Encontramos {len(resultados)} materiais relevantes!")
                for i, item in enumerate(resultados):
                    with st.expander(f"📄 {i+1}. {item.get('title')}"):
                        st.write(f"**Resumo:** {item.get('content')}")
                        st.markdown(f"[🔗 Abrir Link Original]({item.get('url')})")
''')

# 3. Liga o servidor com configurações de segurança e leveza
import subprocess
subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"])

# 4. Abre a janela oficial do Google
from google.colab import output
output.serve_kernel_port_as_window(8501)
