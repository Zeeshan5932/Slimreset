import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ai_engine.groq_client import call_groq_api

from ai_engine.groq_client import call_groq_api
import json

def generate_weight_loss_meal_plan(calories=1500, diet="balanced"):
    """AI-Based Weight Loss Meal Plan Generate Karta Hai."""
    
    prompt = (f"Create a {calories}-calorie meal plan for weight loss with a {diet} diet. "
              "Ensure meals are high in protein, fiber-rich, and balanced. "
              "Include breakfast, lunch, and dinner, with portion sizes and nutritional info.")

    return call_groq_api(prompt)

def generate_fitness_plan(goal="weight loss", activity_level="moderate"):
    """AI-Based Fitness Plan Generator - Ensures plain text response"""

    prompt = (f"Create a structured {goal} workout plan for a person with {activity_level} activity level. "
              "Include warm-ups, main exercises, reps/sets, and cool-downs in a clear text format.")

    response = call_groq_api(prompt)

    # Ensure response is valid
    if not response or "error" in response.lower():
        return "⚠️ Error: AI response was invalid. Please try again."

    return response.strip()  # Ensures clean output

