
# Advanced AI Health & Fitness Coach  
### Powered by Google Gemini (Multimodal Vision + Text)

[![Built with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red?style=flat&logo=streamlit)](https://streamlit.io)
[![Powered by Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-blue?style=flat&logo=google)](https://deepmind.google/technologies/gemini/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg?style=flat&logo=python)](https://www.python.org/)

A **next-generation AI-powered personal health and fitness companion** that goes far beyond basic planners. Built with **Streamlit** and the official **Google Gemini SDK**, this app leverages cutting-edge **multimodal AI** (vision + language) to deliver truly hyper-personalized, real-time coaching.

 ## output screen 

<img width="1055" height="853" alt="Screenshot 2025-12-24 143351" src="https://github.com/user-attachments/assets/697c03a9-45e3-4b3c-9806-89c54d7efc23" />

## ✨ Key Features

### Multimodal AI Vision Capabilities

- **🍽️ Food Photo Recognition & Logging**  
  Upload a photo of your meal → Gemini instantly identifies foods, estimates portions, calculates calories & macros, and logs it toward your daily target with smart, personalized feedback.

- **💪 Exercise Form Check**  
  Upload a photo or short video of your squat, deadlift, push-up, etc. → AI analyzes posture, detects form errors, rates your technique (1–10), and provides specific corrections + injury risk alerts.

- **📸 Body Progress Tracking**  
  Upload "before" and "after" photos → Gemini compares changes, estimates visible fat loss/muscle gain, highlights improved areas, and delivers motivational insights.

### Smart Personalized Planning

- Calorie-aware diet & workout plans using **BMR/TDEE calculations** (Mifflin-St Jeor formula)
- Fully tailored to age, weight, height, sex, activity level, dietary preferences, and fitness goals
- Beautifully structured plan display with goals, routines, tips, and important considerations

### Daily Tracking Dashboard

- Real-time calorie intake progress bar
- Logged meals with timestamps and AI-generated feedback
- Session-persistent logging (ready for future backend integration)

### Safety & Professionalism

- Prominent disclaimer emphasizing this is **not medical advice**
- Encouraging, constructive, and realistic AI feedback

## 🚀 Tech Stack

- **Frontend/UI**: Streamlit – fast, beautiful, interactive web apps
- **AI Engine**: Google Gemini 1.5 Flash – excellent vision + reasoning, fast & cost-effective
- **Image Handling**: Pillow (PIL)
- **Future-Ready**: Designed for easy extension (wearables, chat coach, progress charts, etc.)

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdShakil2004/LLM-projects-Store.git
   cd Advanced_ai_model/Health_and_Fintness_ai

   #Create a virtual environment 
    (recommended)
    Bash 
    python -m venv venv
    source venv/bin/activate        # On Windows: venv\Scripts\activate 
   
   #to run use 
    streamlit run app.py
    #or 
     python.py 

Get your Gemini API Key
Visit: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey?referrer=mdShakil2004)
Create a new API key (free tier available with generous limits)

## Future Roadmap
Persistent user accounts & history (Supabase/Firebase)
Wearables integration (Apple Health, Google Fit via Terra API)
Full AI Chatbot Coach with conversation history
Interactive progress charts (weight, calories, macros over time)
Weekly adaptive plan regeneration based on progress
PDF plan export & easy sharing
Recipe generator with AI-suggested visuals

⚠️ Important Disclaimer
This application uses artificial intelligence for educational, motivational, and informational purposes only.
It is not a substitute for professional medical advice, diagnosis, or treatment.
Always consult qualified healthcare providers, registered dietitians, or certified trainers before making changes to your diet or exercise routine — especially if you have pre-existing health conditions
