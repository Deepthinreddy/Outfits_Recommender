import os
import random
import csv

# ---------------- PATH SETUP ---------------- #

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "outfits.csv")


# ---------------- LOAD DATA ---------------- #

def load_data():

    data = []

    with open(DATA_PATH, newline='', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:
            data.append(row)

    return data


df = load_data()


# ---------------- COLOR MAP ---------------- #

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

    # WEATHER REASONING

    if weather == "winter":

        explanation.append(
            "Keeps you warm and comfortable"
        )

    elif weather == "summer":

        explanation.append(
            "Light and breathable for hot weather"
        )

    elif weather == "rainy":

        explanation.append(
            "Practical and comfortable for rainy conditions"
        )

    # OCCASION REASONING

    if occasion == "formal":

        explanation.append(
            "Gives a polished and professional look"
        )

    elif occasion == "party":

        explanation.append(
            "Stylish and eye-catching for social events"
        )

    elif occasion == "festive":

        explanation.append(
            "Perfect for traditional and festive vibes"
        )

    else:

        explanation.append(
            "Relaxed and comfortable for daily wear"
        )

    # STYLE REASONING

    if style == "ethnic":

        explanation.append(
            "Reflects cultural elegance"
        )

    else:

        explanation.append(
            "Modern and versatile styling"
        )

    return explanation


# ---------------- MAIN RECOMMENDER ---------------- #

def recommend_outfit(gender, weather, occasion, style):

    # ---------------- EXACT MATCH ---------------- #

    result = [

        row for row in df

        if row["gender"] == gender
        and row["weather"] == weather
        and row["occasion"] == occasion
        and row["style"] == style
    ]

    # ---------------- FALLBACK 1 ---------------- #
    # Match gender + occasion

    if not result:

        result = [

            row for row in df

            if row["gender"] == gender
            and row["occasion"] == occasion
        ]

    # ---------------- FALLBACK 2 ---------------- #
    # Match gender + style

    if not result:

        result = [

            row for row in df

            if row["gender"] == gender
            and row["style"] == style
        ]

    # ---------------- FINAL RANDOM FALLBACK ---------------- #

    if not result:

        result = [random.choice(df)]

    # ---------------- SELECT OUTFIT ---------------- #

    selected = random.choice(result)

    outfit = selected["outfit"]

    outfit_lower = outfit.lower()

    # =========================================================
    # WEATHER-BASED INTELLIGENT OVERRIDES
    # =========================================================

    # ---------------- SUMMER ---------------- #

    if weather == "summer":

        # Heavy outfits

        if (
            "hoodie" in outfit_lower
            or "jacket" in outfit_lower
            or "coat" in outfit_lower
        ):

            if gender == "women":

                outfit = "cotton crop shirt + linen pants + sneakers"

            else:

                outfit = "oversized t-shirt + linen pants + sneakers"

        # Hot-weather discomfort outfits

        elif (
            "bodycon" in outfit_lower
            or "boots" in outfit_lower
        ):

            if gender == "women":

                outfit = "sleeveless midi dress + sandals + sling bag"

            else:

                outfit = "cotton shirt + chinos + loafers"

    # ---------------- WINTER ---------------- #

    elif weather == "winter":

        if (
            "shorts" in outfit_lower
            or "mini skirt" in outfit_lower
            or "midi dress" in outfit_lower
        ):

            if gender == "women":

                outfit = "turtleneck + trench coat + boots"

            else:

                outfit = "sweater + wool trousers + boots"

        elif (
            "sleeveless" in outfit_lower
            or "tank top" in outfit_lower
        ):

            if gender == "women":

                outfit = "full sleeve sweater + jeans + ankle boots"

            else:

                outfit = "hooded sweatshirt + denim jeans + sneakers"

    # ---------------- RAINY ---------------- #

    elif weather == "rainy":

        # ETHNIC RAINY LOOKS

        if style == "ethnic":

            if gender == "women":

                outfit = "layered kurta set + leggings + closed flats"

            else:

                outfit = "kurta + straight pants + loafers"

        # WESTERN RAINY LOOKS

        else:

            if (
                "heels" in outfit_lower
                or "suede" in outfit_lower
                or "shorts" in outfit_lower
            ):

                # FORMAL RAINY LOOKS

                if occasion == "formal":

                    if gender == "women":

                        outfit = "formal trench coat + straight pants + waterproof loafers"

                    else:

                        outfit = "formal jacket + tailored pants + waterproof shoes"

                # CASUAL RAINY LOOKS

                else:

                    if gender == "women":

                        outfit = "oversized shirt + joggers + waterproof sneakers"

                    else:

                        outfit = "hoodie + joggers + waterproof sneakers"

    # =========================================================
    # FORMALITY CHECKS
    # =========================================================

    if occasion == "formal":

        if (
            "shorts" in outfit.lower()
            or "sandals" in outfit.lower()
            or "hoodie" in outfit.lower()
        ):

            if style == "ethnic":

                if gender == "women":

                    outfit = "elegant kurta set + straight pants + flats"

                else:

                    outfit = "formal kurta + trousers + loafers"

            else:

                if gender == "women":

                    outfit = "blazer + straight trousers + loafers"

                else:

                    outfit = "formal shirt + tailored pants + oxford shoes"

    # =========================================================
    # COLOR LOGIC
    # =========================================================

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

        colors = random.sample(
            COLOR_MAP[style],
            3
        )

    # =========================================================
    # EXPLANATIONS
    # =========================================================

    explanation = generate_explanation(
        weather,
        occasion,
        style
    )

    # WEATHER CONTEXT

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

    # FORMAL CONTEXT

    if occasion == "formal":

        explanation.append(
            "Structured outfit pieces improve professional appearance"
        )

    # ETHNIC CONTEXT

    if style == "ethnic":

        explanation.append(
            "Styling maintains traditional aesthetics while staying practical"
        )

    return outfit, colors, explanation
