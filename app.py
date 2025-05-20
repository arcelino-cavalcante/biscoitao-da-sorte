import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="Biscoitão da Sorte", page_icon="✨", layout="centered")

# 🎨 CSS customizado: vermelho moderno, efeito suave, nada de retângulo no resultado!
st.markdown("""
    <style>
        body, .main {
            background: linear-gradient(120deg, #fff0f0 0%, #ffe6e6 100%);
        }
        .stApp {
            background: transparent;
        }
        h1, .stTitle {
            color: #d7263d;
            text-shadow: 1px 2px 10px #ffeaea;
            font-weight: 900;
        }
        .stRadio > label, .stMarkdown p, .stTextInput label {
            color: #a71b32 !important;
            font-size: 1.13em;
        }
        .stButton>button {
            background: linear-gradient(90deg, #d7263d 0%, #ff7675 100%);
            color: white;
            font-weight: bold;
            border-radius: 22px;
            padding: 10px 32px;
            margin: 16px 0 8px 0;
            font-size: 1.1em;
            box-shadow: 0 4px 16px #d7263d22;
            border: none;
            transition: 0.15s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #ff7675 0%, #d7263d 100%);
            color: #fff5f5;
            box-shadow: 0 4px 32px #ff7a7a55;
            scale: 1.04;
        }
        .fortune-message {
            animation: popUp 1s cubic-bezier(.39,1.99,.26,.97) 1;
            font-size: 1.6em;
            font-weight: 800;
            color: #d7263d;
            letter-spacing: 0.02em;
            text-align: center;
            margin: 48px 0 16px 0;
            background: none;
            text-shadow: 0 2px 22px #fff2f2, 0 2px 2px #d7263d11;
        }
        .extra-message {
            color: #a71b32;
            font-size: 1.1em;
            text-align: center;
            margin-bottom: 24px;
        }
        .share-section {
            text-align: center;
            margin-top: 22px;
        }
        .whatsapp-btn {
            background: linear-gradient(90deg, #d7263d 0%, #ff7675 100%);
            color: #fff !important;
            font-size: 1.05em;
            padding: 14px 38px;
            border: none;
            border-radius: 22px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 16px #d7263d22;
            margin-bottom: 18px;
            text-decoration: none;
            display: inline-block;
            transition: 0.17s;
        }
        .whatsapp-btn:hover {
            background: linear-gradient(90deg, #ff7675 0%, #d7263d 100%);
            color: #fff7f7 !important;
            scale: 1.05;
            box-shadow: 0 8px 24px #ff7a7a55;
            text-decoration: none;
        }
        @keyframes popUp {
            0% { transform: scale(0.7); opacity: 0; }
            70% { transform: scale(1.08); opacity: 1; }
            100% { transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Biscoito da Sorte Interativo ✨")
st.markdown(
    "<div style='font-size:1.18em;color:#a71b32;margin-bottom:18px;'>"
    "Responda o quiz e veja sua mensagem especial no final!"
    "</div>",
    unsafe_allow_html=True,
)

# Perguntas e escolhas
questions = [
    {
        "q": "Como você está se sentindo hoje?",
        "options": ["Animado(a)", "Cansado(a)", "Curioso(a)", "Tranquilo(a)"]
    },
    {
        "q": "Qual dessas palavras mais combina com seu momento?",
        "options": ["Gratidão", "Mudança", "Superação", "Esperança"]
    },
    {
        "q": "Se pudesse ganhar algo agora, o que escolheria?",
        "options": ["Um abraço", "Um elogio", "Uma boa notícia", "Uma surpresa"]
    }
]

# Armazena as escolhas do usuário
if 'answers' not in st.session_state:
    st.session_state.answers = [None] * len(questions)

# Exibe perguntas sequencialmente
for idx, q in enumerate(questions):
    if st.session_state.answers[idx] is None:
        st.session_state.answers[idx] = st.radio(q["q"], q["options"], key=f"q{idx}")
        if st.button("Próxima", key=f"btn{idx}"):
            pass  # Vai para a próxima pergunta
        st.stop()

# Lista de frases motivacionais (mais de 30)
fortunes = [
    "Você é mais forte do que imagina e mais querido(a) do que pensa. 😊",
    "Acredite: hoje é o dia perfeito para recomeçar algo incrível!",
    "Seu sorriso pode transformar o dia de alguém. Compartilhe-o!",
    "Você faz diferença no mundo só por ser quem é.",
    "A coragem mora em cada pequeno passo que você dá.",
    "Permita-se ser feliz, você merece todas as alegrias do universo.",
    "Grandes coisas acontecem para quem nunca desiste!",
    "Cada desafio é uma chance de crescer e brilhar ainda mais.",
    "Você espalha luz por onde passa, continue assim!",
    "As pessoas ao seu redor têm muita sorte de ter você por perto.",
    "Nunca subestime o poder da sua gentileza.",
    "Hoje você é o protagonista da sua própria história.",
    "Mesmo que o dia esteja nublado, sua presença traz sol.",
    "A vida te reserva surpresas lindas. Confie no processo.",
    "Você já venceu tantas batalhas, olhe com orgulho para sua trajetória.",
    "Lembre-se: você inspira mais pessoas do que imagina.",
    "Seja sempre seu maior apoiador, você merece o melhor.",
    "Permita-se sonhar alto e acreditar no impossível.",
    "Seu valor não está no que você faz, mas em quem você é.",
    "Você é a razão do sorriso de alguém hoje!",
    "Espalhe amor, colha felicidade. Isso é lei da vida.",
    "Gratidão por existir, o mundo precisa de pessoas como você.",
    "A felicidade sempre encontra quem planta gentileza.",
    "Continue, os melhores dias ainda estão por vir!",
    "Seu brilho é único. Nunca apague essa luz.",
    "Você tem dentro de si tudo que precisa para vencer.",
    "A sua presença faz diferença onde você estiver.",
    "Valorize cada conquista, por menor que seja.",
    "Acredite: você é capaz de surpreender até a si mesmo(a).",
    "O que faz seu coração vibrar deve ser prioridade na sua vida.",
    "Permita-se errar, aprender e recomeçar sempre que necessário.",
    "Ser gentil nunca sai de moda. E você faz isso muito bem.",
    "Você é inspiração para quem te observa em silêncio.",
    "Alegria compartilhada é alegria dobrada. Compartilhe sempre.",
    "Um simples gesto seu pode iluminar o dia de alguém.",
    "Você é merecedor(a) de tudo o que há de bom no universo.",
]

# Mensagem personalizada
resposta_1 = st.session_state.answers[0]
resposta_2 = st.session_state.answers[1]
resposta_3 = st.session_state.answers[2]

extra_message = ""

if resposta_1 == "Cansado(a)":
    extra_message = "Respire fundo, descanse seu coração. Você merece paz e leveza! 🌱"
elif resposta_2 == "Superação":
    extra_message = "Tudo o que você já venceu é motivo de orgulho. Continue avançando, campeão(ã)!"
elif resposta_3 == "Um abraço":
    extra_message = "Sinta-se abraçado(a) por todo o carinho dessa mensagem. 🤗"
elif resposta_2 == "Gratidão":
    extra_message = "A gratidão transforma pequenos momentos em grandes bênçãos."

# Mostra a mensagem final com animação, sem retângulo, só destaque no texto
st.markdown(
    f'<div class="fortune-message">'
    f'🎉 Sua mensagem do biscoito da sorte:<br><br>'
    f'{random.choice(fortunes)}'
    f'</div>',
    unsafe_allow_html=True
)
if extra_message:
    st.markdown(f'<div class="extra-message">{extra_message}</div>', unsafe_allow_html=True)

st.markdown("---")

# Link do app (ajuste o endereço para seu Streamlit Cloud quando publicar!)
app_url = "https://seu-app-biscoito.streamlit.app/"

mensagem_whatsapp = f"Recebi uma mensagem do biscoito da sorte e lembrei de você! Clique e descubra sua mensagem especial: {app_url}"
mensagem_whatsapp_url = "https://wa.me/?text=" + urllib.parse.quote(mensagem_whatsapp)

# Botão estilizado para WhatsApp
st.markdown(f"""
<div class="share-section">
    <a href="{mensagem_whatsapp_url}" target="_blank" class="whatsapp-btn">
        📲 Compartilhe no WhatsApp com alguém especial
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;font-size:1em;color:#d7263d;'><b>🌟 Espalhe boas energias para quem você gosta! 🌟</b></div>", unsafe_allow_html=True)
