# 🥗 NutriAI – AI Food Nutrition Analyzer

NutriAI is an AI-powered application that helps users understand the nutritional quality of their meals. Users can simply enter food items and receive estimated calories, macronutrients, health scores, and personalized recommendations.

---

## 🚀 Features

- 🍽️ Meal nutrition analysis
- 🔥 Calorie estimation
- 💪 Protein, carbohydrates, and fat breakdown
- ⭐ Health score generation
- 💡 Personalized suggestions
- 🥗 Better meal alternatives
- 📊 Interactive nutrient distribution charts
- 🌐 Multilingual support
- 🔑 BYOK (Bring Your Own Key) support using Google Gemini
- 🏠 Architecture designed for future local AI inference

---

## 🛠 Tech Stack

### Frontend
- Streamlit
- Plotly

### Backend
- Python

### AI
- Google Gemini API
- Ollama-ready architecture for local inference

### Localization
- English
- Telugu
- Punjabi

---

## 📂 Project Structure

```text
NutriAI
│
├── backend
│   ├── locales
│   │   ├── en.py
│   │   ├── te.py
│   │   └── pa.py
│   ├── analyzer.py
│   ├── gemini_model.py
│   ├── ollama_model.py
│   ├── parser.py
│   └── prompt.py
│
├── frontend
│   ├── charts.py
│   ├── components.py
│   └── styles.py
│
├── images
├── app.py
├── requirements.txt
└── README.md
```

---

## 📸 Application Workflow

### Input

```text
2 idlis, 1 banana, 1 glass milk
```

### Output

```text
Calories: 420 kcal

Protein: 16 g

Carbohydrates: 55 g

Fat: 9 g

Health Score: 8/10

Suggestions:
✔ Good breakfast choice
✔ Add healthy fats
✔ Increase protein intake

Better Alternatives:
🥗 Add boiled eggs
🥗 Include nuts or fruits
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Varshithreddy799/NutriAI.git

cd NutriAI
```

### Create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🔑 Google Gemini API Setup

Get your API key from:

https://aistudio.google.com/apikey

Select:

```text
Gemini API (BYOK)
```

and paste your API key inside the application.

---

## 🎯 Target Users

- Students
- Working professionals
- Fitness enthusiasts
- Health-conscious individuals

---

## 🌟 Future Enhancements

- 📷 Image-based food analysis
- 🎙 Voice input support
- 📄 PDF report generation
- 📈 Meal history and tracking
- 🏃 Integration with fitness applications
- 🏠 Fully offline local AI inference

---

## 🤖 Use of Generative AI

Generative AI played a major role during development.

- ChatGPT was used for coding assistance, debugging, architecture design, and prompt engineering.
- Google Gemini powers the AI nutrition analysis.
- GenAI significantly improved productivity and accelerated feature development.

---

## 🎓 Hackathon Project

**Project Title**

### NutriAI – AI Food Nutrition Analyzer

**Theme:** Open Innovation

Built with ❤️ using Python, Streamlit, and Generative AI.

---

## 👨‍💻 Team Members

- Developer 1 – Frontend and UI Development
- Developer 2 – Backend and AI Integration

---

## 📜 License

This project is developed for educational and hackathon purposes.
