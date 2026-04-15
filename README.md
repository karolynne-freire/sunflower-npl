# 🌻 Sunflower NLP – Inteligência Artificial no Apoio Emocional Infantil

O **Sunflower** é um ecossistema projetado para auxiliar crianças no reconhecimento e expressão de suas emoções. Este repositório contém o **Módulo de NLP (Processamento de Linguagem Natural)**, desenvolvido como o "motor" de análise de sentimentos do projeto.

### 🔗 Links do Projeto

  * **📍 Acesse a aplicação (MVP):** [https://sunflower-npl-mvp.streamlit.app/](https://sunflower-npl-mvp.streamlit.app/)
  * **📱 Repositório do App Base (React Native):** [https://github.com/karolynne-freire/sunflower.git](https://github.com/karolynne-freire/sunflower.git)

-----

## 📚 Sobre o Projeto

Este software é fruto de um projeto de **Iniciação Científica (PIBIC)** no IFPE. Este módulo de IA foi consolidado como trabalho prático da disciplina de **Inteligência Artificial**, focando na aplicação de Machine Learning em contextos de impacto social e saúde mental.

## ✨ Funcionalidades

  * **Interface Interativa:** Desenvolvida com Streamlit para facilitar a triagem lúdica.
  * **Visão Dual-View:** Interface simplificada para a criança e **Painel do Especialista** com logs técnicos para o profissional.
  * **Triagem Clínica:** Identificação de **5 categorias emocionais**: Alegria, Tristeza, Raiva, Ansiedade e Inveja.
  * **Data Logging (Verificação):** Gravação de logs em `historico_sunflower.csv` para auditoria clínica e suporte à decisão.

-----

## 📚 Metodologia de Desenvolvimento

Este modelo utiliza o dataset **GoEmotions** (Google Research) como base de conhecimento léxico. A grande diferença da nossa abordagem para os modelos padrão é a interface:

  * **Input via Botões:** Em vez de exigir que a criança digite textos complexos, o sistema apresenta perguntas. Se a resposta for "SIM", o motor de IA captura o texto bruto do dataset associado àquela emoção (mapeamento taxonômico) para realizar a análise.
  * **Tratamento de Dados:** Filtramos as 28 emoções originais do GoEmotions para as 5 categorias essenciais do projeto Sunflower. Aplicamos **undersampling** (teto de 8.000 frases por classe) e vetorização por **trigramas** para garantir equidade na detecção.

-----

## 📊 Comparativo de Modelos

O gráfico abaixo apresenta a acurácia obtida por diferentes algoritmos testados durante a fase experimental, comparados aos benchmarks da literatura:

<p align="center">
  <img src="https://raw.githubusercontent.com/karolynne-freire/sunflower-npl/main/comparativo_dinamico.png" alt="Comparativo de Modelos" width="600"/>
</p>

**Observa-se que, embora alguns modelos apresentem maior acurácia, o ganho não compensa o custo computacional no contexto de uso.**

-----

## 🧠 Inteligência Artificial & Desenvolvimento Próprio

**Modelo Utilizado:** `Complement Naive Bayes`
**Acurácia Final (Fase 2):** `62,42%`

🛡️ **Justificativa Técnica (Eficiência vs. Acurácia):**
Embora modelos como SVM (**65,42%**) e Regressão Logística (**65,38%**) apresentem métricas superiores, a escolha do Naive Bayes foi uma decisão de engenharia focada na **viabilidade do app mobile**:

  * **Baixíssima Latência:** Crucial para o público infantil; a resposta é imediata (0,8ms) para não quebrar o fluxo lúdico.
  * **Leveza:** O modelo serializado ocupa poucos KB, permitindo execução em diversos dispositivos sem depender de hardware potente.
  * **Ganho em Classes Minoritárias:** O refinamento com trigramas e balanceamento elevou o F1-Score da **Inveja (+9 p.p.)** e **Ansiedade (+5 p.p.)**.

🛡️ **Decisão Ética e Segurança:**

1.  **Mecanismo de Confirmação:** Se a confiança da IA for inferior a **50%**, o sistema solicita que a criança **confirme seu sentimento com o especialista de forma direta**.
2.  **Neutralidade Algorítmica:** O sistema utiliza votação direta, evitando decisões clínicas automáticas sem o parecer de um psicólogo.

-----

## ⚙️ Tecnologias Utilizadas

  * **Python | Streamlit**
  * **Scikit-learn** (Naive Bayes, TF-IDF Trigrams)
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

O Sunflower demonstra como a Inteligência Artificial pode ser humanizada para servir às necessidades de quem mais precisa. Ao priorizar uma arquitetura leve e uma interface por botões, transformamos dados complexos em uma jornada acolhedora.

**Desenvolvido por Karolynne Freire** 🌻
*ADS – Instituto Federal de Pernambuco (IFPE)*

-----

