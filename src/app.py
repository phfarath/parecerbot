import streamlit as st

from src.agent import get_collection_stats, get_documents_list, query_stream
from src.config import EMBEDDING_MODEL, MODEL_NAME, RETRIEVAL_TOP_K

st.set_page_config(page_title="ParecerBot - PX Ativos", page_icon=":scale:", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "history" not in st.session_state:
    st.session_state.history = []

QUICK_ACTIONS = [
    "Qual o criterio de triagem para acoes trabalhistas?",
    "Compare o fluxo de due diligence entre acoes civis e trabalhistas",
    "Gere um rascunho de parecer para uma acao consumidor de R$ 200mil",
    "Quais os principais red flags na analise de viabilidade?",
    "Resuma a politica de compliance em topicos",
]


def render_sources(sources: list[dict]):
    if not sources:
        return
    with st.expander(f"Fontes ({len(sources)})", expanded=False):
        for src in sources:
            st.markdown(f"**{src['source']}** > {src['section']}")
            st.caption(src["content"])
            st.divider()


def check_environment():
    from src.config import ANTHROPIC_API_KEY

    if not ANTHROPIC_API_KEY:
        st.error("ANTHROPIC_API_KEY nao configurada. Adicione ao arquivo .env")
        st.code("echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env")
        return False
    stats = get_collection_stats()
    if stats["chunks"] == 0:
        st.warning("Base de conhecimento vazia. Indexe os documentos primeiro.")
        if st.button("Indexar agora", type="primary"):
            with st.spinner("Indexando documentos..."):
                from src.ingest import ingest

                ingest()
            st.success("Documentos indexados!")
            st.rerun()
        return False
    return True


def main():
    st.title("ParecerBot")
    st.caption("Agente interno - PX Ativos Judiciais")

    with st.sidebar:
        st.header("Base de Conhecimento")
        stats = get_collection_stats()
        st.metric("Chunks indexados", stats["chunks"])
        docs = get_documents_list()
        if docs:
            st.subheader("Documentos")
            for doc in docs:
                st.text(f"  {doc}")
        if st.button("Re-indexar documentos"):
            with st.spinner("Re-indexando..."):
                from src.ingest import ingest

                ingest()
            st.success("Re-indexado!")
            st.rerun()
        st.divider()
        st.subheader("Sobre")
        st.caption(f"Modelo: {MODEL_NAME}")
        st.caption(f"Embeddings: {EMBEDDING_MODEL}")
        st.caption(f"Top-K: {RETRIEVAL_TOP_K}")
        st.divider()
        if st.button("Exportar conversa (.txt)"):
            lines = []
            for msg in st.session_state.messages:
                prefix = "Usuario" if msg["role"] == "user" else "ParecerBot"
                lines.append(f"{prefix}:\n{msg['content']}\n")
            text = "\n---\n\n".join(lines)
            st.download_button(
                "Download",
                data=text,
                file_name="parecerbot_conversa.txt",
                mime="text/plain",
            )

    for msg in st.session_state.messages:
        avatar = None if msg["role"] == "user" else "AI"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            if "sources" in msg and msg["sources"]:
                render_sources(msg["sources"])

    cols = st.columns(len(QUICK_ACTIONS))
    for i, action in enumerate(QUICK_ACTIONS):
        with cols[i]:
            label = action[:25] + "..." if len(action) > 25 else action
            if st.button(label, key=f"qa_{i}", use_container_width=True):
                st.session_state.pending_query = action

    if prompt := st.chat_input("Faca uma pergunta sobre os processos da PX..."):
        st.session_state.pending_query = prompt

    if "pending_query" in st.session_state and st.session_state.pending_query:
        query = st.session_state.pending_query
        del st.session_state.pending_query
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)
        with st.chat_message("assistant", avatar="AI"):
            response_placeholder = st.empty()
            full_response = ""
            sources = []
            for event in query_stream(query, st.session_state.history):
                if event["type"] == "token":
                    full_response += event["content"]
                    response_placeholder.markdown(full_response + " ")
                elif event["type"] == "done":
                    response_placeholder.markdown(full_response)
                    sources = event.get("sources", [])
                    render_sources(sources)
        st.session_state.messages.append({
            "role": "assistant",
            "content": full_response,
            "sources": sources,
        })
        st.session_state.history.append({"role": "user", "content": query})
        st.session_state.history.append({"role": "assistant", "content": full_response})
        st.rerun()


if __name__ == "__main__":
    env_ok = check_environment()
    if env_ok or get_collection_stats()["chunks"] > 0:
        main()
    else:
        st.info("Configure o ambiente e indexe os documentos para comecar.")
