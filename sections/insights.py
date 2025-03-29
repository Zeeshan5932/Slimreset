import streamlit as st
from ai_engine.groq_client import call_groq_api

def get_progress_insight(weight_loss, water_intake, sleep_hours, symptoms):
    """Generates AI-based health insights in a simple text format."""
    prompt = (
        f"User lost {weight_loss} lbs, drank {water_intake} oz water, slept {sleep_hours} hours, "
        f"and reports symptoms: {symptoms}. Provide a human-readable response with insights on "
        "hydration, sleep quality, and overall health. No JSON, just clear text."
    )
    response = call_groq_api(prompt)
    return response.strip()  # Ensures clean text output

def show():
    """Streamlit UI for AI-generated health insights."""
    st.title("📊 AI Health & Progress Insights")
    
    st.write("🔍 **Track your health and get AI-generated insights to improve your progress.**")
    
    # Explanation
    st.subheader("🧐 How Does It Work?")
    st.write("""
    Enter your daily health details, and the AI will analyze them to give you **personalized recommendations**.
    
    **How to Use:**
    1️⃣ **Enter Weight Lost (lbs)** – How much weight did you lose today?  
    2️⃣ **Water Intake (oz)** – How much water did you drink today?  
    3️⃣ **Sleep Hours** – How many hours did you sleep last night?  
    4️⃣ **Any Symptoms?** – List any health symptoms you're experiencing.  
    5️⃣ **Click "Generate Insights"** – The AI will analyze your data and provide expert recommendations!  
    """)

    # User Inputs
    weight_loss = st.number_input("Weight Lost (lbs)", min_value=0.0, step=0.1)
    water_intake = st.number_input("Water Intake (oz)", min_value=0.0, step=1.0)
    sleep_hours = st.number_input("Sleep Hours", min_value=0.0, step=0.1)
    symptoms = st.text_area("Any Symptoms?", placeholder="E.g., fatigue, headaches...")

    if st.button("Generate Insights"):
        if weight_loss or water_intake or sleep_hours or symptoms:
            insight = get_progress_insight(weight_loss, water_intake, sleep_hours, symptoms)
            st.subheader("💡 AI Insights:")
            st.write(insight)
        else:
            st.warning("⚠ Please provide at least one input.")
