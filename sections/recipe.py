import streamlit as st
from ai_engine.groq_client import call_groq_api

def get_recipe_suggestions(weight, goal_weight, diet, allergies, meal_type, cuisine, cooking_time):
    """Generates AI-based recipe suggestions based on user health insights."""
    prompt = (
        f"User weighs {weight} lbs and wants to reach {goal_weight} lbs. "
        f"They follow a {diet} diet and have these allergies: {allergies}. "
        f"Suggest a {meal_type} recipe from {cuisine} cuisine that can be prepared in {cooking_time} minutes. "
        "Provide a simple, structured response including the recipe name, ingredients, and steps."
    )
    return call_groq_api(prompt).strip()

def show():
    """Streamlit UI for AI-generated recipe suggestions."""
    st.title("AI-Powered Recipe Suggestions")
    
    weight = st.number_input("Current Weight (lbs)", min_value=50.0, step=0.1)
    goal_weight = st.number_input("Goal Weight (lbs)", min_value=50.0, step=0.1)
    diet = st.selectbox("Diet Preference", ["Balanced", "Keto", "Vegetarian", "Vegan", "Paleo"])
    allergies = st.text_area("Food Allergies/Restrictions", placeholder="E.g., nuts, dairy, gluten-free...")
    meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snacks"])
    cuisine = st.selectbox("Cuisine Preference", ["Indian", "Italian", "Asian", "Mexican", "American"])
    cooking_time = st.slider("Preferred Cooking Time (minutes)", min_value=5, max_value=60, value=30, step=5)
    
    if st.button("Generate Recipe"):
        if weight and goal_weight and meal_type:
            recipe = get_recipe_suggestions(weight, goal_weight, diet, allergies, meal_type, cuisine, cooking_time)
            st.subheader("Suggested Recipe:")
            st.write(recipe)
        else:
            st.warning("Please fill in the required details.")
