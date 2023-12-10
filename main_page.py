import streamlit as st

st.markdown("<h1 style='text-align: center;'>Futuro Aprovado 📚🎓</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Faça parte da criação da nova maneira de estudar para concursos!</h2>", unsafe_allow_html=True)


option = st.selectbox(
    'Escolha uma questão:',
    (1, 2, 3, 4, 5))

# Text input
st.write("Sua resposta deve ter no mínimo 100 e no máximo 500 palavras.")

user_input = st.text_area("Insira sua resposta:", height=100)

# Submit button
if st.button('Enviar'):
    word_count = len(user_input.split())

    # Check word count limits
    if 100 <= word_count <= 500:
        # Proceed with processing the submission
        # (e.g., sending it to a server or processing it further)
        st.success("Resposta enviada com sucesso!")
    else:
        # Display an error message
        st.error("Erro: O texto deve ter entre 100 e 500 palavras. Seu texto possui " + str(word_count) + " palavra(s).")


st.markdown(
    "Nossa equipe está empenhada em aumentar a velocidade de aprendizado \
    de quem estuda para concursos, utilizando as <b>mais recentes técnicas de inteligência artificial</b>. \n\n"

    "Nosso projeto está em fase de testes iniciais, e <b>sua opinião é muito importante</b> para adaptarmos \
    a plataforma as suas necessidades. [Deixe aqui](https://forms.gle/tWjz7d89J8qpCieC8) seu comentário sobre como podemos melhorar.",
    unsafe_allow_html=True
)