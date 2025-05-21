import streamlit as st
import random
import urllib.parse

st.set_page_config(page_title="Biscoitão da Sorte", page_icon="✨", layout="centered")

# 🎨 CSS customizado
st.markdown("""
    <style>
        body, .main {
            background: linear-gradient(120deg, #fff0f0 0%, #ffe6e6 100%);
        }
        .stApp { background: transparent; }
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
        .section-divider {
            text-align:center;
            margin: 28px 0 18px 0;
        }
        .section-divider span {
            font-size:1.8em;
            color:#d7263d;
            padding:0 14px;
            vertical-align:middle;
        }
        .section-divider:before, .section-divider:after {
            content:'';
            display:inline-block;
            width:23%;
            height:2px;
            background:linear-gradient(90deg,#ffeaea 0%,#d7263d44 100%);
            vertical-align:middle;
            margin:0 4px;
        }
        .fortune-message {
            animation: popUp 1s cubic-bezier(.39,1.99,.26,.97) 1;
            font-size: 1.4em;
            font-weight: 800;
            color: #d7263d;
            letter-spacing: 0.02em;
            text-align: center;
            margin: 38px 0 10px 0;
            background: none;
            text-shadow: 0 2px 22px #fff2f2, 0 2px 2px #d7263d11;
        }
        .extra-message {
            color: #a71b32;
            font-size: 1.08em;
            text-align: center;
            margin-bottom: 18px;
        }
        .suggestion, .challenge {
            color: #d7263d;
            font-size: 1.12em;
            text-align: center;
            margin: 0px 0 0px 0;
            font-weight: bold;
        }
        .desabafo-section {
            background: none;
            padding: 0 18% 0 18%;
            margin-top: 10px;
            margin-bottom: 10px;
            text-align: center;
        }
        .desabafo-msg {
            color: #a71b32;
            background: #fff6f6;
            border-radius: 14px;
            padding: 14px 8px;
            font-size: 1.05em;
            margin: 8px auto 0 auto;
            display: inline-block;
        }
        .share-section {
            text-align: center;
            margin-top: 18px;
        }
        .whatsapp-btn {
            background: linear-gradient(90deg, #d7263d 0%, #ff7675 100%);
            color: #fff !important;
            font-size: 1.02em;
            padding: 13px 35px;
            border: none;
            border-radius: 22px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 16px #d7263d22;
            margin-bottom: 14px;
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
# OCULTA menus, header e rodapé
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("✨ Biscoitão 🍪 da Sorte ✨")
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
            pass
        st.stop()

# Frases motivacionais
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

attitudes = [
    "Mande um bom dia para alguém querido!",
    "Respire fundo três vezes e agradeça pelo dia.",
    "Faça uma gentileza agora: sorria para alguém!",
    "Dê um elogio sincero para uma pessoa próxima.",
    "Escreva três coisas pelas quais você é grato hoje.",
    "Escute com atenção alguém que precise falar.",
    "Envie uma mensagem positiva para um amigo.",
    "Doe algo que você não usa mais.",
    "Ajude alguém sem esperar nada em troca.",
    "Tire um tempinho só para você e relaxe.",
    "Faça um carinho em um animal ou plante uma flor.",
    "Se olhe no espelho e sorria para você mesmo!",
]

challenges = [
    "Desafio do dia: sorria para três pessoas!",
    "Desafio do dia: beba um copo de água e cuide do seu corpo.",
    "Desafio do dia: liste mentalmente 3 coisas boas sobre você.",
    "Desafio do dia: faça uma caminhada curta, mesmo dentro de casa.",
    "Desafio do dia: escreva um bilhete de incentivo para alguém.",
    "Desafio do dia: repita para si mesmo: 'eu sou capaz!'",
    "Desafio do dia: tire 5 minutos para respirar fundo e relaxar.",
    "Desafio do dia: mande uma mensagem positiva para alguém.",
    "Desafio do dia: faça uma pausa e ouça sua música favorita.",
    "Desafio do dia: observe o céu e agradeça por este momento.",
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

fortune = random.choice(fortunes)
attitude = random.choice(attitudes)
challenge = random.choice(challenges)

# Mensagem motivacional
st.markdown('<div class="section-divider"><span>🍪</span></div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="fortune-message">'
    f'🎉 Sua mensagem do biscoito da sorte:<br><br>'
    f'{fortune}'
    f'</div>',
    unsafe_allow_html=True
)
if extra_message:
    st.markdown(f'<div class="extra-message">{extra_message}</div>', unsafe_allow_html=True)

# Atitude do bem
st.markdown('<div class="section-divider"><span>❤️</span></div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="suggestion">Sugestão de atitude do bem:<br>'
    f'{attitude}</div>',
    unsafe_allow_html=True
)

# Desafio do dia
st.markdown('<div class="section-divider"><span>💪</span></div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="challenge">{challenge}</div>',
    unsafe_allow_html=True
)

# Campo para desabafo anônimo (sem erro de rerun)
if "desabafo_enviado" not in st.session_state:
    st.session_state["desabafo_enviado"] = False

st.markdown('<div class="section-divider"><span>💬</span></div>', unsafe_allow_html=True)
st.markdown('<div class="desabafo-section">', unsafe_allow_html=True)
if not st.session_state["desabafo_enviado"]:
    desabafo = st.text_area("Quer desabafar algo? (opcional, só você vai ver)", max_chars=240, key="desabafo_input")
    if st.button("Enviar desabafo"):
        st.session_state["desabafo_enviado"] = True
        st.session_state["ultimo_desabafo"] = desabafo
        st.rerun()
if st.session_state.get("desabafo_enviado", False):
    st.markdown(
        "<div class='desabafo-msg'>Seu sentimento importa! Parabéns por cuidar de você. 💖</div>",
        unsafe_allow_html=True,
    )
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Link do app (ajuste para o link real quando publicar)
app_url = "https://biscoitao-malucao-da-sorte.streamlit.app/"
mensagem_whatsapp = f"Recebi uma mensagem do biscoito da sorte e lembrei de você! Clique e descubra sua mensagem especial: {app_url}"
mensagem_whatsapp_url = "https://wa.me/?text=" + urllib.parse.quote(mensagem_whatsapp)

st.markdown(f"""
<div class="share-section">
    <a href="{mensagem_whatsapp_url}" target="_blank" class="whatsapp-btn">
        📲 Compartilhe no WhatsApp com alguém especial
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;font-size:1em;color:#d7263d;'><b>🌟 Espalhe boas energias para quem você gosta! 🌟</b></div>", unsafe_allow_html=True)
