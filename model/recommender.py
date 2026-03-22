import os
import random
import csv

# Load dataset without pandas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "outfits.csv")

def load_data():
    data = []
    with open(DATA_PATH, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

df = load_data()

# 🎨 Color suggestions
COLOR_MAP = {
    "western": ["black", "white", "beige", "blue", "grey"],
    "ethnic": ["maroon", "gold", "green", "red", "cream"]
}

def generate_explanation(weather, occasion, style):
    explanation = []

    if weather == "winter":
        explanation.append("Keeps you warm and comfortable")
    elif weather == "summer":
        explanation.append("Light and breathable for hot weather")
    elif weather == "rainy":
        explanation.append("Practical and comfortable for rainy conditions")

    if occasion == "formal":
        explanation.append("Gives a polished and professional look")
    elif occasion == "party":
        explanation.append("Stylish and eye-catching for social events")
    elif occasion == "festive":
        explanation.append("Perfect for traditional and festive vibes")
    else:
        explanation.append("Relaxed and comfortable for daily wear")

    if style == "ethnic":
        explanation.append("Reflects cultural elegance")
    else:
        explanation.append("Modern and versatile styling")

    return explanation


def recommend_outfit(gender, weather, occasion, style):
    # Exact match
    result = [
        row for row in df
        if row["gender"] == gender
        and row["weather"] == weather
        and row["occasion"] == occasion
        and row["style"] == style
    ]

    # Fallback
    if not result:
        result = [
            row for row in df
            if row["gender"] == gender and row["style"] == style
        ]

    if not result:
        result = [random.choice(df)]

    outfit = result[0]["outfit"]

    colors = random.sample(COLOR_MAP[style], 3)
    explanation = generate_explanation(weather, occasion, style)

    return outfit, colors, explanation