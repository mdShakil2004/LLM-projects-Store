import streamlit as st
import google.generativeai as genai
from PIL import Image
import json
import datetime

st.set_page_config(
    page_title="Advanced AI Health & Fitness Coach",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; }
    .disclaimer { background-color: #ffeeee; padding: 1rem; border-radius: 0.5rem; border: 1px solid red; margin-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="disclaimer">
    <strong>IMPORTANT DISCLAIMER:</strong> This app uses AI for educational and motivational purposes only. 
    It is <strong>NOT medical advice</strong>. Always consult a qualified healthcare professional or certified trainer 
    before starting any diet or exercise program, especially if you have health conditions. AI analysis of photos/videos 
    is approximate and not a substitute for professional evaluation.
    </div>
""", unsafe_allow_html=True)

# Initialize session state
if 'daily_logs' not in st.session_state:
    st.session_state.daily_logs = []  # List of {"date": "", "meals": [], "total_calories": 0, "target": 0}
if 'plans_generated' not in st.session_state:
    st.session_state.plans_generated = False
if 'calorie_target' not in st.session_state:
    st.session_state.calorie_target = 0

def analyze_with_gemini(contents, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Upgrade to 'gemini-3-flash-preview' if available
    response = model.generate_content(contents + [prompt])
    return response.text

def main():
    st.title("🏋️‍♂️ Advanced AI Health & Fitness Coach (Powered by Gemini)")

    with st.sidebar:
        st.header("🔑 Gemini API Key")
        api_key = st.text_input("Enter your Gemini API Key", type="password", help="Get it from https://aistudio.google.com/apikey")
        if api_key:
            genai.configure(api_key=api_key)
            st.success("API Key configured!")
        else:
            st.warning("Please enter your API key to enable AI features")
            st.stop()

        st.header("Your Profile (for Plans)")
        # (Keep your existing profile inputs here - age, weight, etc. from previous code)
        # For brevity, reusing logic from prior version
        # ... (insert profile inputs + BMR/TDEE calculation as before)

    tab1, tab2, tab3, tab4 = st.tabs(["📋 Generate Plans", "🍽️ Food Logging & Analysis", "💪 Exercise Form Check", "📸 Body Progress"])

    with tab1:
        # (Keep your existing plan generation code here - updated to use official SDK if needed)
        st.header("Generate Personalized Plans")
        # ... (profile inputs, generate button, display plans)

    with tab2:
        st.header("🍽️ Log Meals with Photo Analysis")
        uploaded_food = st.file_uploader("Upload a photo of your meal", type=["jpg", "jpeg", "png"], key="food")
        meal_description = st.text_input("Optional: Describe the meal or add notes")

        if uploaded_food and st.button("Analyze & Log Meal"):
            with st.spinner("Analyzing your meal with Gemini vision..."):
                image = Image.open(uploaded_food)
                st.image(image, caption="Your meal photo")

                prompt = f"""
                Analyze this food photo carefully:
                - Identify all foods and estimate portion sizes.
                - Calculate approximate calories and macros (protein, carbs, fat).
                - User's daily calorie target: {st.session_state.get('calorie_target', 'unknown')} kcal.
                - Suggest if this fits a balanced diet.
                Return response in JSON format:
                {{
                  "foods": ["item1 (portion)", "item2"],
                  "estimated_calories": number,
                  "macros": {{"protein_g": num, "carbs_g": num, "fat_g": num}},
                  "feedback": "brief advice"
                }}
                """
                contents = [image, meal_description, prompt]
                try:
                    result = analyze_with_gemini(contents, "")
                    data = json.loads(result)
                except:
                    data = {"foods": ["Analysis failed"], "estimated_calories": 0, "feedback": result}

                st.success("Meal Analyzed!")
                st.json(data)

                if st.button("Add to Today's Log"):
                    today = datetime.date.today().isoformat()
                    log_entry = {
                        "time": datetime.datetime.now().strftime("%H:%M"),
                        "foods": data.get("foods", []),
                        "calories": data.get("estimated_calories", 0),
                        "feedback": data.get("feedback", "")
                    }
                    # Find or create today's log
                    found = False
                    for log in st.session_state.daily_logs:
                        if log["date"] == today:
                            log["meals"].append(log_entry)
                            log["total_calories"] += log_entry["calories"]
                            found = True
                            break
                    if not found:
                        st.session_state.daily_logs.append({
                            "date": today,
                            "meals": [log_entry],
                            "total_calories": log_entry["calories"],
                            "target": st.session_state.calorie_target
                        })
                    st.success("Meal logged!")

        # Daily Log Dashboard
        st.header("📊 Today's Intake")
        today = datetime.date.today().isoformat()
        for log in st.session_state.daily_logs:
            if log["date"] == today:
                progress = min(log["total_calories"] / log["target"], 1.0) if log["target"] > 0 else 0
                st.progress(progress)
                st.write(f"**{log['total_calories']} / {log['target']} kcal**")
                for meal in log["meals"]:
                    st.markdown(f"- {meal['time']}: {', '.join(meal['foods'])} ({meal['calories']} kcal) — {meal['feedback']}")
                break

    with tab3:
        st.header("💪 Exercise Form Check")
        uploaded_exercise = st.file_uploader("Upload photo or short video of your exercise", type=["jpg", "jpeg", "png", "mp4", "mov"], key="exercise")
        exercise_name = st.text_input("Exercise name (e.g., Squat, Deadlift)")

        if uploaded_exercise and st.button("Check My Form"):
            with st.spinner("Analyzing form with Gemini multimodal..."):
                if uploaded_exercise.type.startswith("image"):
                    media = Image.open(uploaded_exercise)
                    st.image(media, caption="Your exercise photo")
                else:
                    st.video(uploaded_exercise)

                prompt = f"""
                Analyze this {uploaded_exercise.type} of a {exercise_name}:
                - Detect posture and form issues.
                - Provide specific corrections (e.g., 'Straighten back', 'Knees over toes').
                - Rate form 1-10 and highlight injury risks.
                - Suggest improvements.
                Be constructive and encouraging.
                """
                contents = [uploaded_exercise, prompt] if uploaded_exercise.type.startswith("image") else [uploaded_exercise, prompt]
                result = analyze_with_gemini(contents, "")
                st.markdown(result)

    with tab4:
        st.header("📸 Track Body Progress")
        col1, col2 = st.columns(2)
        with col1:
            before = st.file_uploader("Upload 'Before' photo", type=["jpg", "jpeg", "png"], key="before")
        with col2:
            after = st.file_uploader("Upload 'After' photo", type=["jpg", "jpeg", "png"], key="after")

        if before and after and st.button("Compare Progress"):
            with st.spinner("Estimating changes with Gemini vision..."):
                img1 = Image.open(before)
                img2 = Image.open(after)
                st.image([img1, img2], caption=["Before", "After"], width=300)

                prompt = """
                Compare these two body progress photos (same person):
                - Estimate visible changes in body composition (fat loss, muscle gain).
                - Highlight areas of improvement (e.g., arms, abs).
                - Provide motivational feedback and next steps.
                Be realistic and positive.
                """
                result = analyze_with_gemini([img1, img2, prompt], "")
                st.markdown(result)

if __name__ == "__main__":
    main()