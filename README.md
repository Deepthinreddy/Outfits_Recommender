# 👗 AI Outfit Recommender

An intelligent outfit recommendation system that suggests clothing combinations based on user preferences such as weather, occasion, style, and gender.

🔗 **Live Demo:** Coming Soon  

---

## 🚀 Features

- 🎯 Context-aware outfit recommendations  
- 🎨 Suggested color palettes for styling  
- 🧠 Explainable outputs (why the outfit works)  
- 🔄 Smart fallback logic (ensures no empty results)  
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
   - Color suggestions 🎨  
   - Explanation of recommendations 🧠  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- CSV (Dataset)  

---

## 📂 Project Structure


Outfits_Recommender/
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
├── screenshots/
│ ├── overview1.png
│ ├── overview2.png
│ ├── overview3.png
│ └── overview4.png
│
├── requirements.txt
├── runtime.txt
└── README.md


---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
