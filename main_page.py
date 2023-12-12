import streamlit as st
# from openai import OpenAI
import langchain
from langchain import PromptTemplate
from langchain.llms import OpenAI

openai_api_key = st.secrets["openai_api_key"]

st.markdown("<h1 style='text-align: center;'>Futuro Aprovado 📚🎓</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Faça parte da criação da nova maneira de estudar para concursos!</h2>", unsafe_allow_html=True)


template = """
Sua tarefa é avaliar uma resposta para a seguinte questão. Essa é uma questão discursiva de um
concurso para Analista de Gestão e Políticas Públicas da Prefeitura de São Paulo.

Enunciado:

Você é um Analista de Gestão e Políticas Públicas trabalhando para a Prefeitura de São Paulo.
Atualmente, a cidade enfrenta desafios significativos relacionados ao crescimento urbano desordenado,
que resultou em problemas como trânsito intenso, poluição e desigualdade social. Com base em seus
conhecimentos e experiência, elabore um plano estratégico que aborde os seguintes pontos:

1) Análise de Problemas: Identifique e descreva três problemas urbanos críticos resultantes do
crescimento desordenado em São Paulo.
2) Estratégias de Intervenção: Proporcione soluções inovadoras e viáveis para cada um dos problemas 
identificados. Suas soluções devem considerar fatores como sustentabilidade, inclusão social e 
viabilidade econômica.
3) Implementação e Avaliação: Descreva como você implementaria essas soluções, incluindo os
stakeholders envolvidos, recursos necessários e um plano de avaliação contínua para medir o
sucesso das intervenções.

Avalie a seguinte resposta:
{input}
"""

prompt = PromptTemplate(
    input_variables=["input"], ## "target"],
    template=template
)

def load_LLM():
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    return llm

llm = load_LLM()

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

        # prompt_with_text = prompt.format(input=input, target=target)
        prompt_with_text = prompt.format(input=user_input)

        converted = llm(prompt_with_text)
        st.write (converted)
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

