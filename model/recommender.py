import os
import random
import csv

# ---------------- LOAD DATASET ---------------- #

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "outfits.csv")

def load_data():

    data = []

    with open(DATA_PATH, newline='', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:
            data.append(row)

    return data


df = load_data()

# ---------------- COLOR PALETTES ---------------- #

COLOR_MAP = {

    "western": [
        "black",
        "white",
        "beige",
        "blue",
        "grey"
    ],

    "ethnic": [
        "maroon",
        "gold",
        "green",
        "red",
        "cream"
    ]
}

# ---------------- EXPLANATION GENERATOR ---------------- #

def generate_explanation(weather, occasion, style):

    explanation = []

    # Weather Logic
    if weather == "winter":
        explanation.append("Keeps you warm and comfortable")

    elif weather == "summer":
        explanation.append("Light and breathable for hot weather")

    elif weather == "rainy":
        explanation.append("Practical and comfortable for rainy conditions")

    # Occasion Logic
    if occasion == "formal":
        explanation.append("Gives a polished and professional look")

    elif occasion == "party":
        explanation.append("Stylish and eye-catching for social events")

    elif occasion == "festive":
        explanation.append("Perfect for traditional and festive vibes")

    else:
        explanation.append("Relaxed and comfortable for daily wear")

    # Style Logic
    if style == "ethnic":
        explanation.append("Reflects cultural elegance")

    else:
        explanation.append("Modern and versatile styling")

    return explanation

# ---------------- MAIN RECOMMENDER ---------------- #

def recommend_outfit(gender, weather, occasion, style):

    # -------- EXACT MATCH -------- #

    result = [

        row for row in df

        if row["gender"] == gender
        and row["weather"] == weather
        and row["occasion"] == occasion
        and row["style"] == style
    ]

    # -------- FALLBACK MATCH -------- #

    if not result:

        result = [

            row for row in df

            if row["gender"] == gender
            and row["style"] == style
        ]

    # -------- FINAL RANDOM FALLBACK -------- #

    if not result:
        result = [random.choice(df)]

    selected = random.choice(result)

    outfit = selected["outfit"]

    outfit_lower = outfit.lower()

    # ---------------- SMART WEATHER ADJUSTMENTS ---------------- #

    # SUMMER
    if weather == "summer":

        if "hoodie" in outfit_lower or "jacket" in outfit_lower:

            outfit = "oversized t-shirt + linen pants + sneakers"

        elif "bodycon" in outfit_lower:

            outfit = "sleeveless midi dress + sandals + sling bag"

        elif "boots" in outfit_lower:

            outfit = "cotton dress + flats + tote bag"

    # WINTER
    elif weather == "winter":
        if (
        "shorts" in outfit_lower
        or "midi dress" in outfit_lower
        or "mini skirt" in outfit_lower
    ):

        outfit = "turtleneck + trench coat + boots"

        elif (
        "sleeveless" in outfit_lower
        or "tank top" in outfit_lower
    ):

        outfit = "full sleeve sweater + jeans + ankle boots"

    # RAINY
    elif weather == "rainy":

        if "heels" in outfit_lower or "suede" in outfit_lower:

            outfit = "oversized shirt + joggers + waterproof sneakers"

    # ---------------- SMART COLOR LOGIC ---------------- #

    if weather == "summer":

        colors = [
            "white",
            "beige",
            "light blue"
        ]

    elif weather == "winter":

        colors = [
            "black",
            "brown",
            "navy"
        ]

    elif weather == "rainy":

        colors = [
            "grey",
            "olive",
            "black"
        ]

    else:

        colors = random.sample(COLOR_MAP[style], 3)

    # ---------------- GENERATE EXPLANATIONS ---------------- #

    explanation = generate_explanation(
        weather,
        occasion,
        style
    )

    # Additional contextual reasoning

    if weather == "summer":

        explanation.append(
            "Chosen fabrics and styling help reduce heat discomfort"
        )

    elif weather == "winter":

        explanation.append(
            "Layer-friendly outfit for better warmth and comfort"
        )

    elif weather == "rainy":

        explanation.append(
            "Selected pieces are easier to wear in wet conditions"
        )

    # ---------------- RETURN RESULTS ---------------- #

    return outfit, colors, explanation
