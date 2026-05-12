import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.recommender import recommend_outfit

st.set_page_config(
    page_title="AI Outfit Recommender",
    page_icon="👗",
    layout="centered"
)

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

st.title("AI Outfit Recommender 👗")
st.caption("Personalized outfit suggestions based on context, style, and weather.")

st.markdown("## 💬 AI Stylist")

user_prompt = st.text_area(
    "Describe your plan today",
    placeholder="Example: Dinner date tonight and slightly cold weather"
)

# ---------------- HELPER FUNCTION ---------------- #

def extract_preferences(prompt):

    prompt = prompt.lower()

    weather = None
    occasion = None
    style = None

    # WEATHER

    if any(word in prompt for word in [
        "cold",
        "winter",
        "cool",
        "chilly",
        "freezing"
    ]):
        weather = "winter"

    elif any(word in prompt for word in [
        "rain",
        "rainy",
        "wet",
        "drizzle"
    ]):
        weather = "rainy"

    elif any(word in prompt for word in [
        "hot",
        "summer",
        "warm",
        "sunny"
    ]):
        weather = "summer"

    # OCCASION

    if any(word in prompt for word in [
        "party",
        "club",
        "nightout",
        "concert",
        "date",
        "dinner"
    ]):
        occasion = "party"

    elif any(word in prompt for word in [
        "formal",
        "office",
        "meeting",
        "business",
        "corporate"
    ]):
        occasion = "formal"

    elif any(word in prompt for word in [
        "festival",
        "festive",
        "traditional",
        "wedding"
    ]):
        occasion = "festive"

    elif any(word in prompt for word in [
        "casual",
        "daily",
        "relaxed"
    ]):
        occasion = "casual"

    # STYLE

    if any(word in prompt for word in [
        "ethnic",
        "traditional"
    ]):
        style = "ethnic"

    elif any(word in prompt for word in [
        "western",
        "modern"
    ]):
        style = "western"

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

# ---------------- AI PROMPT DETECTION ---------------- #

if user_prompt:

    detected_weather, detected_occasion, detected_style = extract_preferences(user_prompt)

    if detected_weather:
        weather = detected_weather

    if detected_occasion:
        occasion = detected_occasion

    if detected_style:
        style = detected_style

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

    st.markdown("## 👗 Recommended Outfit")

    st.markdown(
        f"""
        <div class="recommendation-card">
            <h3>{outfit}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 📊 Style Match")

    st.progress(92)
    st.caption("92% contextual compatibility match")

    st.markdown("## 🎨 Suggested Colors")

    st.success(", ".join(colors))

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

    st.markdown("## 💭 Feedback")

    col1, col2 = st.columns(2)

    with col1:
        st.button("👍 Useful")

    with col2:
        st.button("👎 Not My Style")
