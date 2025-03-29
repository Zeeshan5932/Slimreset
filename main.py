import streamlit as st
from sections import home, fitness_planner, generate_workout, insights, recipe  # Import recipe

# App Title
st.title("SlimReset AI - Weight Loss Coach 🏋️‍♀️")

# Sidebar - Navigation
st.sidebar.title("🔗 Navigation")
section = st.sidebar.radio("Go to:", ["Home", "Fitness Planner", "Workout Plan", "AI Health Insights", "Recipe Suggestions"])

# Load the selected section
if section == "Home":
    home.show()

elif section == "Fitness Planner":
    fitness_planner.show()

elif section == "Workout Plan":
    generate_workout.show()

elif section == "AI Health Insights":
    insights.show()

elif section == "Recipe Suggestions":  # ✅ Add Recipe Section
    recipe.show()
