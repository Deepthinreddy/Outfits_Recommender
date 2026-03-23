# 👗 AI Outfit Recommender

An intelligent outfit recommendation system that suggests clothing combinations based on user preferences such as weather, occasion, style, and gender.

---

## 🚀 Features

- 🎯 Context-aware outfit recommendations  
- 🎨 Suggested color palettes for styling  
- 🧠 Explainable outputs (why the outfit works)  
- 🔄 Smart fallback logic (no empty results)  
- 💻 Interactive UI built with Streamlit  

---

## 🧠 How It Works

The system uses a rule-based recommendation approach:

1. Takes user inputs:
   - Gender
   - Weather
   - Occasion
   - Style (Ethnic / Western)

2. Matches inputs against a structured dataset

3. Applies multi-level filtering:
   - Exact match  
   - Partial match (fallback)  
   - Random selection (final fallback)

4. Enhances output with:
   - Color suggestions  
   - Explanation of recommendations  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- CSV (Dataset)

---

## 📂 Project Structure


outfit-recommender/
│
├── app/
│ └── main.py
│
├── model/
│ └── recommender.py
│
├── data/
│ └── outfits.csv
│
├── requirements.txt
└── README.md


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app/main.py
