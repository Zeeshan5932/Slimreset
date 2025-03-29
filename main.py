import streamlit as st
from sections import home, fitness_planner, generate_workout, insights

# App Title
st.title("SlimReset AI - Weight Loss Coach 🏋️‍♀️")

# Sidebar - Navigation
st.sidebar.title("🔗 Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Fitness Planner", "Workout Plan", "AI Health Insights"])

# Load the selected section
if section == "Home":
    home.show()  # Calls the home section

elif section == "Fitness Planner":
    st.header("🍽 AI-Generated Weight Loss Meal Plan")
    st.write("🥗 Get a custom meal plan tailored for weight loss. Choose your calorie intake and diet preference.")

    calories = st.slider("Daily Calorie Goal:", min_value=1000, max_value=2500, value=1500, step=100)
    diet = st.selectbox("Choose Diet Type:", ["low-carb", "high-protein", "balanced", "plant-based"])

    if st.button("Generate Meal Plan"):
        meal_plan = fitness_planner.generate_weight_loss_meal_plan(calories, diet)
        st.success("✅ Meal Plan Generated!")
        st.code(meal_plan, language="yaml")

elif section == "Workout Plan":
    generate_workout.show()  # Calls the workout section

elif section == "AI Health Insights":
    insights.show()  # Calls the AI insights section
