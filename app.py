import streamlit as st
import joblib
import numpy as np
import pandas as pd
from collections import Counter
from datetime import datetime

st.set_page_config(page_title="Sunflower Project", page_icon="🌻", layout="centered")

st.markdown("""
    <style>
    .stButton>button { border-radius: 20px; height: 3em; font-weight: bold; }
    .stSuccess { background-color: #FFF1A1; }
    </style>
""", unsafe_allow_html=True)

@st.cache_resource
def carregar_arquivos():
    modelo = joblib.load('modelo_sunflower_naive.pkl')
    vetorizador = joblib.load('vectorizer_sunflower.pkl')
    return modelo, vetorizador

modelo_nb, vectorizer = carregar_arquivos()

if 'passo' not in st.session_state:
    st.session_state.passo = 0
    st.session_state.votos = []
    st.session_state.confiancas = []

mapeamento_ia = {
    0: "joy amusement excitement love optimism pride admiration gratitude", # Alegria
    1: "anger annoyance disgust disapproval",                               # Raiva
    2: "anxiety nervousness fear confusion",                                # Ansiedade
    3: "sadness disappointment grief remorse",                              # Tristeza
    4: "desire longing wanting craving"                                     # Inveja
}

perguntas = [
    "1. Você se sentiu feliz ou animado hoje?",
    "2. Algo te deixou com muita raiva ou bravo?",
    "3. Você se sentiu muito preocupado ou ansioso?",
    "4. Você se sentiu triste ou desanimado?",
    "5. Você queria algo que um amigo tem e você não?",
]

st.title("Sunflower 🌻")
st.caption("Tecnologia Assistiva para Reconhecimento Emocional")

if st.session_state.passo < len(perguntas):
    st.markdown(f"### Questão {st.session_state.passo + 1}")
    st.info(perguntas[st.session_state.passo])
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SIM ✅", use_container_width=True):
            frase_ref = mapeamento_ia[st.session_state.passo]
            vec = vectorizer.transform([frase_ref])
            
            predicao = modelo_nb.predict(vec)[0]
            probabilidades = modelo_nb.predict_proba(vec)
            confianca_max = np.max(probabilidades) * 100
            
            st.session_state.votos.append(predicao)
            st.session_state.confiancas.append(f"{predicao} ({confianca_max:.1f}%)")
            
            st.session_state.passo += 1
            st.rerun()

    with col2:
        if st.button("NÃO ❌", use_container_width=True):
            st.session_state.passo += 1
            st.rerun()

else:
    st.header("Resultado do Período")
    
    if not st.session_state.votos:
        resultado_final = "Alegria" 
    else:
        contagem = Counter(st.session_state.votos)
        mais_comuns = contagem.most_common()
        
        if len(mais_comuns) > 1 and mais_comuns[0][1] == mais_comuns[1][1]:
            resultado_final = "Misto"
        else:
            resultado_final = mais_comuns[0][0]

    icones = {
        "Alegria": "🌻 Amarelo Radiante",
        "Raiva": "🥀 Vermelho (Raiva)",
        "Ansiedade": "😰 Azul (Ansiedade)",
        "Tristeza": "😢 Cinza (Tristeza)",
        "Inveja": "🟢 Verde (Inveja)",
        "Misto": "🟣 Roxo (Apoio Necessário)"
    }

    st.subheader(f"Estado do Avatar: {icones.get(resultado_final)}")

    if resultado_final == "Alegria":
        st.balloons()
        st.success("O Girassol está brilhando! Você parece estar muito bem hoje.")
    else:
        st.warning("O Girassol sugere: Que tal contar como você se sente para alguém de confiança?")

    st.divider()

    with st.expander("🔬 Painel Técnico (Acesso do Especialista)"):
        st.write("### Log de Inferência em Tempo Real")
        if st.session_state.confiancas:
            log_formatado = " | ".join(st.session_state.confiancas)
            st.code(f"📊 LOG DE INFERÊNCIA: {log_formatado}")
            
            st.write("**Análise de Limiar:**")
            for conf in st.session_state.confiancas:
                valor = float(conf.split('(')[1].split('%')[0])
                if valor < 50.0:
                    st.error(f"⚠️ Alerta: Confiança em '{conf.split(' ')[0]}' abaixo de 50%. Solicitar confirmação direta.")
        else:
            st.info("Nenhuma emoção negativa detectada para análise técnica.")
            
        st.caption(f"ID da Sessão: {datetime.now().strftime('%Y%m%d%H%M')}")

    if st.button("Reiniciar Questionário"):
        st.session_state.passo = 0
        st.session_state.votos = []
        st.session_state.confiancas = []
        st.rerun()