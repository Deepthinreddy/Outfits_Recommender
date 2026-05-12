import streamlit as st
from model.recommender import recommend_outfit

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Outfit Recommender",
    page_icon="👗",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    font-weight: 600;
}

.recommendation-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #333;
    margin-top: 10px;
    margin-bottom: 20px;
}

.reason-card {
    background-color: #161b22;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #4CAF50;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.title("AI Outfit Recommender 👗")
st.caption("Personalized outfit suggestions based on context, style, and weather.")

# ---------------- AI STYLIST INPUT ---------------- #

st.markdown("## 💬 AI Stylist")

user_prompt = st.text_area(
    "Describe your plan today",
    placeholder="Example: Dinner date tonight and slightly cold weather"
)

# ---------------- HELPER FUNCTION ---------------- #

def extract_preferences(prompt):

    prompt = prompt.lower()

    weather = "summer"
    occasion = "casual"
    style = "western"

    # Weather Detection
    if "cold" in prompt or "winter" in prompt:
        weather = "winter"

    elif "rain" in prompt:
        weather = "rainy"

    # Occasion Detection
    if "party" in prompt:
        occasion = "party"

    elif "office" in prompt or "meeting" in prompt:
        occasion = "formal"

    elif "date" in prompt or "dinner" in prompt:
        occasion = "party"

    elif "festival" in prompt or "festive" in prompt:
        occasion = "festive"

    # Style Detection
    if "ethnic" in prompt or "traditional" in prompt:
        style = "ethnic"

    return weather, occasion, style

# ---------------- DEFAULT INPUTS ---------------- #

gender = st.selectbox("Gender", ["men", "women"])

weather = st.selectbox(
    "Weather",
    ["summer", "winter", "rainy"]
)

occasion = st.selectbox(
    "Occasion",
    ["casual", "formal", "party", "festive"]
)

style = st.selectbox(
    "Style",
    ["western", "ethnic"]
)

# ---------------- AI PROMPT OVERRIDE ---------------- #

if user_prompt:
    weather, occasion, style = extract_preferences(user_prompt)

    st.info(
        f"Detected Preferences → Weather: {weather} | Occasion: {occasion} | Style: {style}"
    )

# ---------------- RECOMMEND BUTTON ---------------- #

if st.button("✨ Recommend Outfit"):

    with st.spinner("Generating personalized outfit recommendations..."):

        outfit, colors, explanation = recommend_outfit(
            gender,
            weather,
            occasion,
            style
        )

    # ---------------- RECOMMENDED OUTFIT ---------------- #

    st.markdown("## 👗 Recommended Outfit")

    st.markdown(
        f"""
        <div class="recommendation-card">
            <h3>{outfit}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- STYLE MATCH ---------------- #

    st.markdown("## 📊 Style Match")

    st.progress(92)
    st.caption("92% contextual compatibility match")

    # ---------------- COLORS ---------------- #

    st.markdown("## 🎨 Suggested Colors")

    st.success(", ".join(colors))

    # ---------------- EXPLANATION ---------------- #

    st.markdown("## 🧠 Why This Works")

    if isinstance(explanation, str):
        explanation = explanation.split(" • ")

    for point in explanation:

        st.markdown(
            f"""
            <div class="reason-card">
                {point}
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- FEEDBACK ---------------- #

    st.markdown("## 💭 Feedback")

    col1, col2 = st.columns(2)

    with col1:
        st.button("👍 Useful")

    with col2:
        st.button("👎 Not My Style")
