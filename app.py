import streamlit as st
import joblib
import pandas as pd
from collections import Counter
from datetime import datetime

st.set_page_config(page_title="Sunflower Project", page_icon="🌻")

@st.cache_resource
def carregar_arquivos():
    modelo = joblib.load('modelo_sunflower_naive.pkl')
    vetorizador = joblib.load('vectorizer_sunflower.pkl')
    return modelo, vetorizador

modelo_nb, vectorizer = carregar_arquivos()

if 'passo' not in st.session_state:
    st.session_state.passo = 0
    st.session_state.votos = []

mapeamento_ia = {
    0: "joy amusement approval excitement gratitude love admiration", #Alegria
    1: "anger annoyance disapproval",                                  #Raiva
    2: "nervousness fear",                                              #Ansiedade
    3: "sadness disappointment grief remorse",                          #Tristeza
    4: "desire longing wanting craving",                                #Inveja
    5: "fear nervousness"                                               #Medo/Ansiedade
}

perguntas = [
    "1. Você se sentiu feliz ou animado hoje?",
    "2. Algo te deixou com muita raiva ou bravo?",
    "3. Você se sentiu muito preocupado ou ansioso?",
    "4. Você se sentiu triste ou desanimado?",
    "5. Você sentiu inveja ou queria algo que não era seu?",
    "6. Você sentiu medo de alguma coisa?"
]

st.title("Sunflower 🌻")

if st.session_state.passo < len(perguntas):
    st.markdown(f"### Questão {st.session_state.passo + 1}")
    st.info(perguntas[st.session_state.passo])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM ✅", use_container_width=True):
            frase_ref = mapeamento_ia[st.session_state.passo]
            vec = vectorizer.transform([frase_ref])
            predicao = modelo_nb.predict(vec)[0]
            
            st.session_state.votos.append(predicao)
            st.session_state.passo += 1
            st.rerun()

    with col2:
        if st.button("NÃO ❌", use_container_width=True):
            st.session_state.passo += 1
            st.rerun()

else:
    st.header("Resultado Final")
    
    if not st.session_state.votos:
        resultado_final = "Alegria" 
    else:
        contagem = Counter(st.session_state.votos)
        mais_comuns = contagem.most_common()
        
        if len(mais_comuns) > 1 and mais_comuns[0][1] == mais_comuns[1][1]:
            resultado_final = "Misto"
        else:
            resultado_final = mais_comuns[0][0]

    novo_dado = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "votos": str(st.session_state.votos),
        "resultado": resultado_final
    }
    pd.DataFrame([novo_dado]).to_csv("historico_sunflower.csv", mode='a', header=False, index=False)

    icones = {
        "Alegria": "🌻 Amarelo Radiante",
        "Raiva": "🥀 Vermelho (Raiva)",
        "Ansiedade": "😰 Azul (Ansiedade)",
        "Tristeza": "😢 Cinza (Tristeza)",
        "Inveja": "🟢 Verde (Inveja)",
        "Misto": "🟣 Roxo (Falar com Psicólogo)"
    }

    estado_texto = icones.get(resultado_final, f"Detetado: {resultado_final}")
    st.subheader(f"Estado do Avatar: {estado_texto}")

    if resultado_final == "Alegria":
        st.balloons()
        st.success("Que bom! O Girassol está feliz por você.")
    else:
        st.error("💡 O Girassol sugere: Seria importante conversar com seu psicólogo.")

    if st.button("Reiniciar Questionário"):
        st.session_state.passo = 0
        st.session_state.votos = []
        st.rerun()