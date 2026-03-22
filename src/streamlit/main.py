import os
import streamlit as st
import tempfile
from streamlit_mic_recorder import mic_recorder
from openai import OpenAI
from service import Request

# ========================
# CONFIG
# ========================
st.set_page_config(page_title="Aurora", page_icon="🌟")
st.title("🌟 Aurora, Sua Educadora Financeira")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ========================
# SESSION STATE
# ========================
if "modo" not in st.session_state:
    st.session_state.modo = None

if "cod_conta" not in st.session_state:
    st.session_state.cod_conta = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================
# ETAPA 1: ESCOLHER MODO
# ========================
if st.session_state.modo is None:

    st.subheader("Como você quer interagir?")

    if st.button("💬 Texto"):
        st.session_state.modo = "texto"
        st.rerun()

    if st.button("🎤 Voz"):
        st.session_state.modo = "voz"
        st.rerun()

# ========================
# ETAPA 2: INFORMAR CONTA
# ========================
elif st.session_state.cod_conta is None:

    st.subheader("Informe sua conta")
    cod = st.text_input("Número da conta")

    if st.button("Entrar"):
        if cod and cod.strip().isdigit():
            st.session_state.cod_conta = cod.strip()
            st.rerun()
        else:
            st.warning("Digite apenas números.")

# ========================
# ETAPA 3: CHAT
# ========================
else:

    col1, col2, col3 = st.columns([3, 1, 1])

    with col1:
        st.write(f"Conta: **{st.session_state.cod_conta}**")

    with col2:
        st.write(f"Modo: **{st.session_state.modo}**")

    with col3:
        if st.button("🔄 Trocar"):
            st.session_state.modo = None
            st.session_state.cod_conta = None
            st.session_state.messages = []
            st.rerun()

    st.divider()

    # ========================
    # HISTÓRICO
    # ========================
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    question = None

    # ========================
    # INPUT TEXTO
    # ========================
    if st.session_state.modo == "texto":
        question = st.chat_input("Digite sua pergunta...")

    # ========================
    # INPUT VOZ (OpenAI)
    # ========================
    elif st.session_state.modo == "voz":

        audio = mic_recorder(
            start_prompt="🎙️ Falar",
            stop_prompt="⏹️ Parar",
            key="recorder"
        )

        if audio and "bytes" in audio:

            # cria arquivo temporário
            with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
                tmp.write(audio["bytes"])
                tmp_path = tmp.name

            st.audio(audio["bytes"])

            with st.spinner("Transcrevendo áudio..."):
                try:
                    with open(tmp_path, "rb") as f:
                        transcript = client.audio.transcriptions.create(
                            model="gpt-4o-mini-transcribe",
                            file=f
                        )

                    question = transcript.text

                except Exception as e:
                    st.error(f"Erro na transcrição: {e}")
                    st.stop()

            st.write(f"🗣️ Você disse: {question}")

            os.remove(tmp_path)

    # ========================
    # PROCESSAMENTO (FASTAPI)
    # ========================
    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)

        with st.spinner("Aurora analisando..."):
            try:
                data = {
                    "question": question,
                    "cod_conta": st.session_state.cod_conta
                }

                response = Request.post(data)

                if not isinstance(response, dict):
                    answer = "Resposta inválida da API."
                else:
                    answer = (
                        response.get("answer")
                        or response.get("response")
                        or "Sem resposta."
                    )

            except Exception as e:
                answer = f"Erro: {str(e)}"

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        with st.chat_message("assistant"):
            st.write(answer)
