# 🌻 Sunflower NLP – Inteligência Artificial no Apoio Emocional Infantil

[](https://sunflower-npl-mvp.streamlit.app/)

O **Sunflower** é um ecossistema projetado para auxiliar crianças no reconhecimento e expressão de suas emoções. Este repositório contém o **Módulo de NLP (Processamento de Linguagem Natural)**, desenvolvido como o "motor" de análise de sentimentos do projeto.

### 🔗 Links do Projeto

  * **📍 Acesse a aplicação (MVP):** [https://sunflower-npl-mvp.streamlit.app/](https://sunflower-npl-mvp.streamlit.app/)
  * **📱 Repositório do App Base (React Native):** [https://github.com/karolynne-freire/sunflower.git](https://github.com/karolynne-freire/sunflower.git)

-----

## 📚 Sobre o Projeto

Este software é fruto de um projeto de **Iniciação Científica (PIBIC)** no IFPE. Este módulo de IA foi consolidado como trabalho prático da disciplina de **Inteligência Artificial**, focando na aplicação de Machine Learning em contextos de impacto social e saúde mental.

## ✨ Funcionalidades

  * **Interface Interativa:** Desenvolvida com Streamlit para facilitar a triagem lúdica.
  * **Conversão de Input:** Transforma a interação por botões em vetores textuais processados pela IA.
  * **Triagem Clínica:** Identificação de **5 categorias emocionais**: Alegria, Tristeza, Raiva, Ansiedade e Inveja.
  * **Data Logging (Verificação):** Gravação de logs em `historico_sunflower.csv` para auditoria clínica.
    
-----
## 📚 Metodologia de Desenvolvimento
Este modelo utiliza o dataset **GoEmotions** (Google Research) como base de conhecimento léxico. A grande diferença da nossa abordagem para os modelos padrão é a interface:

* **Input via Botões:** Em vez de exigir que a criança digite textos complexos, o sistema apresenta perguntas. Se a resposta for "SIM", o motor de IA captura o texto bruto do dataset associado àquela emoção para realizar a análise.

* **Tratamento de Dados:** Filtramos as 28 emoções originais do GoEmotions para as 5 categorias essenciais do projeto Sunflower, garantindo um modelo mais focado e eficiente.

-----

## 📊 Comparativo de Modelos

O gráfico abaixo apresenta a acurácia obtida por diferentes algoritmos testados durante a fase experimental:

<p align="center">
  <img src="https://raw.githubusercontent.com/karolynne-freire/sunflower-npl/main/comparativo_dinamico.png" alt="Comparativo de Modelos" width="600"/>
</p>

**Observa-se que, embora alguns modelos apresentem maior acurácia, o ganho não compensa o custo computacional no contexto de uso.**

-----

## 🧠 Inteligência Artificial & Desenvolvimento Próprio

**Modelo Utilizado:** `Complement Naive Bayes`
**Acurácia:** `68,4%`

 **🛡️ Justificativa Técnica (Eficiência vs. Acurácia):**
Embora outros modelos pudessem apresentar métricas superiores, a escolha do Naive Bayes com **69,0% de acurácia** foi uma decisão de engenharia focada na **viabilidade do app mobile**:

  * **Baixíssima Latência:** Crucial para o público infantil; a resposta precisa ser imediata para não quebrar o fluxo lúdico.
  * **Leveza:** O modelo ocupa pouco espaço e processa rápido, permitindo que o Sunflower rode em diversos dispositivos sem depender de hardware potente.
  * **Eficiência:** O ganho de acurácia de outros modelos não compensava o custo computacional e o aumento no tempo de resposta no contexto de uso real.

**🛡️ Decisão Ética e Pontuação:**

1.  **Neutralidade Algorítmica:** O sistema utiliza votação direta. Não foram atribuídas pontuações automáticas para evitar decisões clínicas sem embasamento.
2.  **Aguardando Validação:** O sistema está preparado para receber pesos e pontuações, mas essa implementação **só ocorrerá após o parecer de um especialista clínico (psicólogo)**.

**🛡️ Verificação e Data Logging**
Os dados coletados são armazenados para:

1. Avaliação da acurácia do modelo em cenários reais.
2.  Apoio à decisão clínica: A IA atua como ferramenta de suporte, nunca como diagnóstico isolado.
-----

## ⚙️ Tecnologias Utilizadas

  * **Python** | **Streamlit**
  * **Scikit-learn** (Pipeline de IA e TF-IDF)
  * **Pandas** (Tratamento de dados e logs)
  * **Joblib** (Persistência do modelo próprio)

-----

## ⚙️ Como Executar Localmente

1️⃣ **Clonar o repositório**

```bash
git clone https://github.com/karolynne-freire/sunflower-npl.git
```

2️⃣ **Acesse a pasta do projeto**

```bash
cd sunflower-nlp
```

3️⃣ **Instale as dependências**

```bash
pip install -r requirements.txt
```

4️⃣ **Executar o sistema**

```bash
streamlit run app.py
```

-----

## ⭐ Considerações Finais

O Sunflower demonstra como a Inteligência Artificial pode ser humanizada para servir às necessidades de quem mais precisa. Ao priorizar uma arquitetura leve e uma interface por botões, transformamos dados complexos em uma jornada acolhedora, garantindo que a tecnologia seja uma aliada segura na expressão emocional infantil.

**Desenvolvido por Karolynne Freire** 🌻

