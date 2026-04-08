import streamlit as st
import joblib
from collections import Counter

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
    0: "I am feeling very happy and joyful",
    1: "I am angry and someone was mean to me",
    2: "I am feeling nervous and scared"
}

perguntas = [
    "1. Você sorriu ou se sentiu animado hoje?",
    "2. Alguém brigou com você ou te deixou bravo?",
    "3. Você se sentiu preocupado ou com medo de algo?"
]

st.set_page_config(page_title="Sunflower Project", page_icon="🌻")
st.title("Sunflower 🌻")

if st.session_state.passo < len(perguntas):
    st.markdown(f"### Pergunta {st.session_state.passo + 1}")
    st.info(perguntas[st.session_state.passo])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM ✅", use_container_width=True):
            frase_ref = mapeamento_ia[st.session_state.passo]
            vec = vectorizer.transform([frase_ref])
            emocao_predita = modelo_nb.predict(vec)[0]
            
            st.session_state.votos.append(emocao_predita)
            st.session_state.passo += 1
            st.rerun()

    with col2:
        if st.button("NÃO ❌", use_container_width=True):
            st.session_state.passo += 1
            st.rerun()

else:
    st.header("Resultado do Girassol")
    
    if not st.session_state.votos:
        resultado_final = "Alegria" 
        st.balloons()
        st.success("✅ O Girassol está RADIANTE!")
    else:
        contagem = Counter(st.session_state.votos)
        mais_comuns = contagem.most_common()

        if len(mais_comuns) > 1 and mais_comuns[0][1] == mais_comuns[1][1]:
            resultado_final = "Misto"
            st.warning("⚖️ O Girassol percebeu sentimentos mistos...")
            st.error("📢 Recomendamos que você procure conversar com um psicólogo.")
        else:
            resultado_final = mais_comuns[0][0]
            st.write(f"Análise concluída: O estado predominante é **{resultado_final}**")
            if resultado_final in ["Raiva", "Ansiedade", "Tristeza", 1, 2]:
                st.warning("Talvez seja bom conversar com alguém sobre isso.")
            else:
                st.balloons()

    icones = {
        "Alegria": "🌻 Amarelo Radiante",
        "Raiva": "🥀 Vermelho (Bravo)",
        "Ansiedade": "😰 Azul (Preocupado)",
        "Tristeza": "😢 Cinza (Triste)",
        "Misto": "🟣 Roxo (Falar com Psicólogo)"
    }
    
    st.subheader(f"Estado Visual: {icones.get(resultado_final, '🌻 Girassol Amarelo')}")

    if st.button("Reiniciar"):
        st.session_state.passo = 0
        st.session_state.votos = []
        st.rerun()