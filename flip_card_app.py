import streamlit as st

# Initialize session state for flip state of each card
if "flipped_cards" not in st.session_state:
    st.session_state.flipped_cards = [False] * 30  # 30 unique cards

# Function to toggle flip state for a specific card
def flip_card(index):
    st.session_state.flipped_cards[index] = not st.session_state.flipped_cards[index]

# CSS for flip effect and spacing with background image fix
flip_css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');

    /* Background Wrapper */
    .blurred-bg-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('https://i.ibb.co/4S11L6M/Ice-Breaker-Design-2.jpg') no-repeat center center/cover;
        filter: blur(5px); /* Apply blur effect */
        z-index: -1; /* Ensure it stays behind content */
    }

    /* Fix Streamlit content position */
    .stApp {
        background: none !important; /* Remove Streamlit's default background */
    }

    /* Card Layout */
    .flip-card-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }

    .flip-card {
        background-color: transparent;
        width: 220px;
        height: 130px;
        perspective: 1000px;
        margin: 10px;
        cursor: pointer;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
    }

    .flipped .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 13px;
        font-family: 'Tajawal', sans-serif;
        font-weight: bold;
        border-radius: 14px;
        padding: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
        text-align: center;
        color: black;
    }

    .flip-card-front {
        background: #d8d9da;
        color: black;
        font-size: 40px;
    }

    .flip-card-back {
        background: #3acddf;
        color: black;
        transform: rotateY(180deg);
    }
</style>

<div class="blurred-bg-container"></div>

"""

st.markdown(flip_css, unsafe_allow_html=True)
cards = [
    ("🐧 01 🐧", "وش تسمع وانت رايح الدوام؟"),
    ("🐧 02 🐧", "لو قدرت تغير لون السماء ليوم واحد، ايش اللون اللي تختاره؟ "),
    ("🐧 03 🐧", "شي اعجبك او لفت انتباهك اليوم في طويق؟)"),
    ("🐧 04 🐧", "غشيت في مقابلات طويق ولا لا؟"),
    ("🐧 05 🐧", "اوصف نفسك بثلاث كلمات"),
    ("🐧 06 🐧", "ايش اكثر شيء محرج صار لك؟"),
    ("🐧 07 🐧", "مين اللي قابلك من المدربين و ايش كان انطباعك عنه؟"),
    ("🐧 08 🐧", "ألف لنا قصة قصيرة مع اللي معاه نفس كرتك وكل واحد يكمل جملة بعض"),
    ("🐧 09 🐧", "وش احساسك الان بصدق"),
    ("🐧 10 🐧", "سوي مقابلة مع اللي معاه نفس كرتك"),
    ("🐧 11 🐧", "رياضات تمارسها؟"),
    ("🐧 12 🐧", "كم تعطي برودة أعصابك من 10؟"),
    ("🐧 13 🐧", "لو كنت بلد ايش راح تكون؟"),
    ("🐧 14 🐧", "تقدر تعيش مع نسخة ثانية منك؟"),
    ("🐧 15 🐧", "اكثر شي تبدع فيه؟"),
    ("🐧 16 🐧", "تكتشف الفضاء ولا المحيط؟ وليش؟"),
    ("🐧 17 🐧", "أشياء تحسن مزاجك؟"),
    ("🐧 18 🐧", "هل البكاء ضعف؟"),
    ("🐧 19 🐧", "ارسم هوايتك"),
    ("🐧 20 🐧", "اقوى كذبة كذبتها"),
    ("🐧 21 🐧", "معروف في العائلة انك…؟"),
    ("🐧 22 🐧", "اكثر شيء تصرف عليه فلوسك؟"),
    ("🐧 23 🐧", "سوي مقابلة مع اللي معاه نفس كرتك"),
    ("🐧 24 🐧", "تحب العمل الفردي او الجماعي"),
    ("🐧 25 🐧", "أكثر شي تشوف انه مطبل له(فلم , مسلسل ,أكله ...)"),
    ("🐧 26 🐧", "لو علقت في جزيرة وتقدر تاخذ معك شيء واحد ايش راح يكون؟"),
    ("🐧 27 🐧", "إيش أول كلمة تقولها لما تطيح فجأة؟"),
    ("🐧 28 🐧", "لو العالم كله تحول زومبي ايش اول مكان راح تتوجه له؟"),
    ("🐧 29 🐧", "لو انطردت من البيت وين بتروح، تكلم مين؟"),
    ("🐧 30 🐧", "ألف لنا قصة قصيرة مع اللي معاه نفس كرتك وكل واحد يكمل جملة بعض"),
]

# Display Cards in Rows with Proper Margins
for i in range(0, 30, 5):  # 5 cards per row
    cols = st.columns(5)
    for j in range(5):
        index = i + j
        if index < len(cards):
            front_text, back_text = cards[index]
            flip_class = "flipped" if st.session_state.flipped_cards[index] else ""

            # Display Flip Card inside a container for spacing
            with cols[j]:
                st.markdown(f"""
                <div class="flip-card-container">
                    <div class="flip-card {flip_class}">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                {front_text}
                            </div>
                            <div class="flip-card-back">
                                {back_text}
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Button to flip the card (Ensures unique state for each)
                if st.button(f"🧊 أكسر 🧊", key=f"btn_{index}"):
                    flip_card(index)
                    st.rerun()  # Forces UI update to reflect state changes