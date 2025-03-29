import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai_engine.groq_client import call_groq_api

def generate_weight_loss_meal_plan(calories=1500, diet="balanced"):
    """Generate AI-based Weight Loss Meal Plan."""
    
    prompt = (f"Create a {calories}-calorie meal plan for weight loss with a {diet} diet. "
              "Ensure meals are high in protein, fiber-rich, and balanced. "
              "Include breakfast, lunch, and dinner, with portion sizes and nutritional info.")

    response = call_groq_api(prompt)
    
    return response.strip() if isinstance(response, str) else "⚠️ Error: Invalid AI response."

def generate_fitness_plan(goal="weight loss", activity_level="moderate"):
    """Generate AI-Based Fitness Plan."""
    
    prompt = (f"Create a structured {goal} workout plan for a person with {activity_level} activity level. "
              "Include warm-ups, main exercises, reps/sets, and cool-downs.")

    response = call_groq_api(prompt)

    if not response or not isinstance(response, str):
        return "⚠️ Error: AI response was invalid. Please try again."

    return response.strip()

def show():
    """📌 Streamlit UI for the Fitness Planner Section"""
    st.title("🏋️ Fitness Planner")
    st.write("Plan your workouts and fitness goals here!")

    # goal = st.selectbox("Select Your Goal:", ["Weight Loss", "Muscle Gain", "Endurance"])
    # activity_level = st.selectbox("Select Activity Level:", ["Low", "Moderate", "High"])

    # if st.button("Generate Fitness Plan"):
    #     plan = generate_fitness_plan(goal, activity_level)
    #     st.subheader("Your AI-Generated Fitness Plan:")
    #     st.write(plan)

    calories = st.slider("Set Daily Calorie Goal:", 1000, 3000, 1500, 100)
    diet = st.selectbox("Choose Diet Type:", ["Balanced", "Keto", "Vegan", "Low-Carb"])

    if st.button("Generate Meal Plan"):
        meal_plan = generate_weight_loss_meal_plan(calories, diet)
        st.subheader("Your AI-Generated Meal Plan:")
        st.write(meal_plan)
