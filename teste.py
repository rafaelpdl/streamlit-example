import streamlit as st


st.markdown("<h1 style='text-align: center;'>Concurso Potencial 📚🎓</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Faça parte da nova maneira de estudar para concursos!</h2>", unsafe_allow_html=True)


if st.button('Say hello'):
    st.write('Hello, Streamlit!')

option = st.selectbox(
    'Escolha uma questão:',
    (1, 2, 3, 4, 5))

st.write('Your favorite number is ', option)


"""
O que achou? Nos mande uma mensagem ou preencha esse formulário com a sua opinião.

"""