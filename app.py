
import streamlit as st
import random

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="VibeAI ✨",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 0, 128, 0.18), transparent 25%),
        radial-gradient(circle at 90% 15%, rgba(0, 204, 255, 0.18), transparent 25%),
        radial-gradient(circle at 50% 90%, rgba(132, 0, 255, 0.15), transparent 30%),
        linear-gradient(135deg, #080014, #10001f 50%, #020617);
    color: white;
}

/* Main title */

.hero {
    padding: 35px;
    border-radius: 28px;
    background:
        linear-gradient(
            135deg,
            rgba(255, 0, 128, 0.25),
            rgba(98, 0, 255, 0.25),
            rgba(0, 204, 255, 0.20)
        );
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 0 45px rgba(162, 0, 255, 0.25);
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 8px;
    background: linear-gradient(
        90deg,
        #ff4ecd,
        #a855f7,
        #38bdf8
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 18px;
    color: #d8d4e8;
}

/* Cards */

.card {
    padding: 24px;
    border-radius: 22px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
    margin-bottom: 20px;
}

.card:hover {
    border-color: rgba(255,255,255,0.25);
}

/* Result */

.result-card {
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    background:
        linear-gradient(
            135deg,
            rgba(255, 0, 128, 0.18),
            rgba(0, 204, 255, 0.15)
        );
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 0 40px rgba(255,0,128,0.15);
}

.result-card h2 {
    font-size: 38px;
    margin-bottom: 5px;
}

.score {
    font-size: 48px;
    font-weight: 800;
    color: #38bdf8;
}

/* Buttons */

.stButton > button {
    width: 100%;
    border-radius: 15px;
    border: none;
    padding: 13px;
    font-size: 17px;
    font-weight: 700;
    color: white;
    background: linear-gradient(
        90deg,
        #ff0080,
        #8b5cf6,
        #06b6d4
    );
    box-shadow: 0 8px 25px rgba(139,92,246,0.30);
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* Metrics */

.metric-box {
    padding: 20px;
    text-align: center;
    border-radius: 20px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
}

.metric-number {
    font-size: 30px;
    font-weight: 800;
    color: #a855f7;
}

.metric-label {
    color: #b8b3c9;
}

/* Footer */

.footer {
    text-align: center;
    margin-top: 45px;
    padding: 20px;
    color: #8f8aa0;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown("## ✨ VibeAI")

    st.write("Your tiny colorful AI-style experience.")

    st.markdown("---")

    st.markdown("### 🎨 Choose your vibe")

    vibe = st.selectbox(
        "Current mood",
        [
            "😊 Happy",
            "😎 Confident",
            "🤩 Excited",
            "😌 Calm",
            "🤔 Curious",
            "😴 Tired",
            "😢 Sad"
        ]
    )

    intensity = st.slider(
        "Vibe intensity",
        0,
        100,
        75
    )

    st.markdown("---")

    st.caption("🚀 Demo project")
    st.caption("Built with Streamlit")


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>✨ VibeAI</h1>

<p>
Discover your digital vibe through a colorful AI-inspired experience.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# MAIN INPUT
# --------------------------------------------------

col1, col2 = st.columns([1.5, 1])

with col1:

    st.markdown("""
    <div class="card">

    <h2>💭 Tell VibeAI what's on your mind</h2>

    <p style="color:#aaa">
    Write a short sentence and let the app generate a playful vibe analysis.
    </p>

    </div>
    """, unsafe_allow_html=True)

    text = st.text_area(
        "Your message",
        placeholder="Example: Today I finished my project and I'm feeling amazing! 🚀",
        height=160
    )

    analyze = st.button("✨ Analyze My Vibe")


with col2:

    st.markdown("""
    <div class="card">

    <h3>🌈 How it works</h3>

    <p>01 — Share your thoughts</p>
    <p>02 — Choose your mood</p>
    <p>03 — Analyze your vibe</p>
    <p>04 — Explore your result</p>

    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if analyze:

    if not text.strip():

        st.warning("✨ Write something first!")

    else:

        positive_words = [
            "happy", "amazing", "great", "love",
            "awesome", "excited", "good",
            "wonderful", "success", "beautiful"
        ]

        negative_words = [
            "sad", "bad", "hate", "angry",
            "tired", "stress", "stressed",
            "worried", "upset"
        ]

        words = text.lower().split()

        positive_count = sum(
            word.strip(".,!?") in positive_words
            for word in words
        )

        negative_count = sum(
            word.strip(".,!?") in negative_words
            for word in words
        )

        if positive_count > negative_count:
            mood = "Positive Energy"
            emoji = "🚀"
            score = random.randint(85, 98)

        elif negative_count > positive_count:
            mood = "Low Energy"
            emoji = "🌙"
            score = random.randint(45, 65)

        else:
            mood = "Balanced Vibe"
            emoji = "🌈"
            score = random.randint(70, 84)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card">

        <h2>{emoji} {mood}</h2>

        <p>Your Vibe Score</p>

        <div class="score">{score}%</div>

        <p style="color:#bdb8ca">
        Based on your message and selected mood.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # --------------------------------------------------
        # METRICS
        # --------------------------------------------------

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{len(words)}</div>
                <div class="metric-label">Words</div>
            </div>
            """, unsafe_allow_html=True)

        with m2:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{positive_count}</div>
                <div class="metric-label">Positive</div>
            </div>
            """, unsafe_allow_html=True)

        with m3:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{negative_count}</div>
                <div class="metric-label">Negative</div>
            </div>
            """, unsafe_allow_html=True)

        with m4:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-number">{intensity}%</div>
                <div class="metric-label">Intensity</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # --------------------------------------------------
        # INSIGHT
        # --------------------------------------------------

        st.info(
            f"💡 VibeAI detected a **{mood.lower()}** pattern "
            f"with a confidence-style score of **{score}%**."
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

✨ VibeAI — Creative Streamlit Demo

<br>

Made with Python + Streamlit 🚀

</div>
""", unsafe_allow_html=True)

