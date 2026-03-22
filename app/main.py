import streamlit as st
from model.recommender import recommend_outfit

st.title("AI Outfit Recommender 👗")

gender = st.selectbox("Gender", ["men", "women"])
weather = st.selectbox("Weather", ["summer", "winter", "rainy"])
occasion = st.selectbox("Occasion", ["casual", "formal", "party", "festive"])
style = st.selectbox("Style", ["western", "ethnic"])

if st.button("Recommend Outfit"):
    outfit, colors, explanation = recommend_outfit(gender, weather, occasion, style)

    # Outfit
    st.markdown("### 👗 Recommended Outfit")
    st.markdown(f"**{outfit}**")

    # Colors
    st.markdown("### 🎨 Suggested Colors")
    st.write(", ".join(colors))

    # Explanation (FIXED BULLETS)
    st.markdown("### 🧠 Why this works")

    if isinstance(explanation, str):
        explanation = explanation.split(" • ")

    for point in explanation:
        st.markdown(f"- {point}")