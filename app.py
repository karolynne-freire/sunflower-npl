import streamlit as st
import joblib
import pandas as pd
from collections import Counter
from datetime import datetime

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
    0: "I am so happy and joyful today",           # Alegria
    1: "I am very angry and mad at someone",       # Raiva
    2: "I feel very nervous and anxious",           # Ansiedade
    3: "I am feeling so sad and depressed",        # Tristeza
    4: "I feel jealous and envy of others",         # Inveja
    5: "I am very scared and afraid"               # Medo
}

perguntas = [
    "1. Você se sentiu feliz hoje?",
    "2. Algo te deixou com muita raiva?",
    "3. Você se sentiu muito preocupado?",
    "4. Você se sentiu triste ou desanimado?",
    "5. Você sentiu inveja de algo ou alguém?",
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
        resultado_final = "joy" 
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

    df_log = pd.DataFrame([novo_dado])
    df_log.to_csv("historico_sunflower.csv", mode='a', header=False, index=False)

    icones = {
        "joy": "🌻 Amarelo Radiante (Alegria)",
        "anger": "🥀 Vermelho (Raiva)",
        "fear": "😰 Azul (Ansiedade/Medo)",
        "sadness": "😢 Cinza (Tristeza)",
        "envy": "🟢 Verde (Inveja)",
        "Misto": "🟣 Roxo (Falar com Psicólogo)"
    }

    st.subheader(f"Estado do Avatar: {icones.get(resultado_final, resultado_final)}")

    if resultado_final != "joy":
        st.error("💡 Recomendamos conversar com seu psicólogo.")
    else:
        st.success("Você está indo muito bem!")

    if st.button("Reiniciar"):
        st.session_state.passo = 0
        st.session_state.votos = []
        st.rerun()