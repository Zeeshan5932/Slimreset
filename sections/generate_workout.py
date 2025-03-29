import streamlit as st
from sections.fitness_planner import generate_fitness_plan

def show():
    st.header("🏋️ AI-Generated Workout Plan")
    st.write("💪 Get a customized workout plan based on your fitness goal and activity level.")

    # User inputs
    goal = st.selectbox("Select Your Goal:", ["Weight Loss", "Muscle Gain", "Endurance"])
    activity_level = st.selectbox("Select Your Activity Level:", ["Sedentary", "Light", "Moderate", "Active"])
    duration = st.selectbox("Workout Duration:", ["10 mins", "20 mins", "30 mins", "45 mins", "1 hour", "1.5 hours", "2 hours"])

    intensity = st.selectbox("Select Intensity Level:", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Generate Workout Plan"):
        fitness_plan = generate_fitness_plan(goal, activity_level)  # Ensure it's text-based
        st.success("✅ Workout Plan Generated!")

        # Displaying the workout plan in a structured, readable format
        formatted_plan = f"""
        🏆 **Workout Plan Details**
        -------------------------
        **Goal:** {goal}  
        **Activity Level:** {activity_level}  
        **Duration:** {duration}  
        **Intensity:** {intensity}  

        **Your Workout Plan:**  
        {fitness_plan}
        """

        st.text(formatted_plan)  # Using text instead of st.code to avoid YAML formatting issues
