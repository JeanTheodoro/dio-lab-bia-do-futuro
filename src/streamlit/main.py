import streamlit as st
from service import Request

st.set_page_config(page_title="Aurora - Educadora Financeira", page_icon="🌟")

st.title("🌟 Aurora, Sua Educadora Financeira")

if "cod_conta" not in st.session_state:
    st.session_state.cod_conta = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.session_state.cod_conta is None:

    st.subheader("Informe sua conta para começar")

    cod = st.text_input("Número da conta")

    if st.button("Iniciar atendimento"):
        if cod and cod.strip():
            st.session_state.cod_conta = cod.strip()
            st.success("Conta validada! Você pode começar a conversar.")
            st.rerun()
        else:
            st.warning("Informe um número de conta válido.")

else:

    col1, col2 = st.columns([4, 1])

    with col1:
        st.write(f"Conta ativa: **{st.session_state.cod_conta}**")

    with col2:
        if st.button("Encerrar"):
            st.session_state.cod_conta = None
            st.session_state.messages = []
            st.rerun()

    st.divider()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


    question = st.chat_input("Olá! Sou Aurora como posso ajuda-lo ?")

    if question:


        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)


        with st.spinner("Aurora está analisando sua situação financeira..."):
            try:
                data = {
                    "question": question,
                    "cod_conta": st.session_state.cod_conta
                }

                response = Request.post(data)
                answer = response.get("answer") or response.get("response") or "Não foi possível obter resposta."

            except Exception as e:
                answer = f"Erro ao comunicar com a API: {str(e)}"

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        with st.chat_message("assistant"):
            st.write(answer)
