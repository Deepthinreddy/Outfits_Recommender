import pandas as pd
import os
import random

# Load dataset
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "outfits.csv")

df = pd.read_csv(DATA_PATH)

# 🎨 Color suggestions
COLOR_MAP = {
    "western": ["black", "white", "beige", "blue", "grey"],
    "ethnic": ["maroon", "gold", "green", "red", "cream"]
}

def generate_explanation(weather, occasion, style):
    explanation = []

    # Weather logic
    if weather == "winter":
        explanation.append("Keeps you warm and comfortable")
    elif weather == "summer":
        explanation.append("Light and breathable for hot weather")
    elif weather == "rainy":
        explanation.append("Practical and comfortable for rainy conditions")

    # Occasion logic
    if occasion == "formal":
        explanation.append("Gives a polished and professional look")
    elif occasion == "party":
        explanation.append("Stylish and eye-catching for social events")
    elif occasion == "festive":
        explanation.append("Perfect for traditional and festive vibes")
    else:
        explanation.append("Relaxed and comfortable for daily wear")

    # Style logic
    if style == "ethnic":
        explanation.append("Reflects cultural elegance")
    else:
        explanation.append("Modern and versatile styling")

    return explanation   # ✅ VERY IMPORTANT (LIST, NOT STRING)


def recommend_outfit(gender, weather, occasion, style):
    # 🎯 Exact match
    result = df[
        (df["gender"] == gender) &
        (df["weather"] == weather) &
        (df["occasion"] == occasion) &
        (df["style"] == style)
    ]

    # 🔄 Smart fallback
    if result.empty:
        result = df[
            (df["gender"] == gender) &
            (df["style"] == style)
        ]

    if result.empty:
        result = df.sample(1)

    outfit = result.iloc[0]["outfit"]

    # 🎨 Colors
    colors = random.sample(COLOR_MAP[style], 3)

    # 🧠 Explanation
    explanation = generate_explanation(weather, occasion, style)

    return outfit, colors, explanation