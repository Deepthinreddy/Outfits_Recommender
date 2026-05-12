# 👗 AI Outfit Recommender

An intelligent outfit recommendation system that suggests clothing combinations based on user preferences such as weather, occasion, style, and gender.

🔗 **Live Demo:** https://outfitsrecommender.streamlit.app/  

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

## 💡 Product Thinking

### Problem
Users often struggle to quickly decide outfits that match weather, occasion, and personal style. Existing fashion recommendation systems are either too generic or lack explainability.

### Goal
Build a lightweight AI-powered stylist that delivers contextual outfit recommendations while keeping the interaction simple and intuitive.

### UX Decisions
- Added explainable recommendations to improve user trust
- Added fallback logic to avoid dead-end experiences
- Reduced interaction friction through minimal inputs
- Designed a clean dark UI for clarity and focus

### Metrics I Would Track
- Recommendation acceptance rate
- Repeat usage frequency
- Most selected outfit categories
- User feedback sentiment

### Future Improvements
- Conversational AI stylist
- Personalized wardrobe memory
- Weekly outfit planning assistant
- Image-based outfit recommendations

---

## 📂 Project Structure

```text
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
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app/main.py
