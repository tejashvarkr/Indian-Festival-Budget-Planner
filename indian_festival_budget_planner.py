# -*- coding: utf-8 -*-
"""Indian Festival Budget Planner.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_7Gk67O42Pc7aLj2amzdxmTu3sA-qGgr
"""

# Predefined list of common items for festivals across different zones
festival_items = {
    "Diwali": {
        "North": {
            "Decorations": [("Rangoli Kit", 500), ("Diyas", 300), ("Fairy Lights", 800)],
            "Gifts": [("Sweets Box", 1000), ("Handicrafts", 1500), ("Gift Hampers", 2000)],
            "Food": [("Homemade Snacks", 2000), ("Sweets", 1500), ("Dry Fruits", 1000)]
        },
        "South": {
            "Decorations": [("Torans", 400), ("Kuthu Vilakku", 600), ("Pookalam", 700)],
            "Gifts": [("Pongal Rice Pack", 1200), ("Traditional Wear", 1500), ("Sweets Box", 1300)],
            "Food": [("Sundal", 800), ("Adai", 1000), ("Sweets", 900)]
        }
    },
    "Holi": {
        "North": {
            "Decorations": [("Color Powder", 400), ("Flowers", 600), ("Water Balloons", 300)],
            "Gifts": [("Gujiyas", 800), ("Traditional Sweet Box", 1200), ("Clothing", 1500)],
            "Food": [("Thandai", 500), ("Sweets", 1000), ("Chaat", 700)]
        },
        "South": {
            "Decorations": [("Pichkaris", 200), ("Color Pack", 300), ("Water Balloons", 250)],
            "Gifts": [("Traditional Gifts", 900), ("Handmade Sweets", 1100), ("T-shirts", 1300)],
            "Food": [("Buttermilk", 500), ("Snacks", 700), ("Chutney", 400)]
        }
    },
    "Pongal": {
        "South": {
            "Decorations": [("Kolam Kit", 700), ("Sugarcane", 300), ("Flower Rangoli", 500)],
            "Gifts": [("Sugarcane", 300), ("Pongal Rice", 500), ("Sweets Box", 800)],
            "Food": [("Traditional Feast", 2500), ("Pongal Dish", 1500), ("Sweets", 1000)]
        },
        "North": {
            "Decorations": [("Clay Lamps", 400), ("Saree", 800), ("Torans", 600)],
            "Gifts": [("Pongal Box", 1000), ("Decorative Lantern", 1200)],
            "Food": [("Halwa", 1000), ("Pongal", 1200), ("Traditional Sweets", 800)]
        }
    },
    "Navratri": {
        "North": {
            "Decorations": [("Garba Lights", 800), ("Diyas", 600), ("Torans", 500)],
            "Gifts": [("Sweets Box", 1000), ("Traditional Wear", 1500), ("Puja Items", 1200)],
            "Food": [("Pithla", 700), ("Sabudana Khichdi", 500), ("Kachori", 800)]
        },
        "South": {
            "Decorations": [("Flowers", 500), ("Kumkum", 300), ("Bells", 400)],
            "Gifts": [("Silk Saree", 2500), ("Traditional Gifts", 1800)],
            "Food": [("Chana Masala", 700), ("Vada", 600), ("Kesari", 1000)]
        }
    },
    "Onam": {
        "South": {
            "Decorations": [("Pookalam", 600), ("Banana Leaves", 200), ("Elephant Figurines", 400)],
            "Gifts": [("Onam Sweets", 1000), ("Memento", 800), ("Traditional Wear", 1500)],
            "Food": [("Sadya", 2500), ("Pappadam", 500), ("Payasam", 1000)]
        }
    },
    # More festivals can be added similarly
}

# Function to generate budget suggestions
def generate_budget_plan(festival, zone, budget, user_preferences):
    if festival not in festival_items or zone not in festival_items[festival]:
        return f"Sorry, no suggestions available for the festival {festival} in zone {zone}."

    # Customize suggestions based on user preferences
    items = festival_items[festival][zone]
    total_cost = 0
    suggestions = f"Suggested Budget Plan for {festival} Celebration in {zone} (Total Budget: ₹{budget}):\n"

    for category, items_list in items.items():
        if category not in user_preferences or not user_preferences[category]:
            continue
        suggestions += f"\nCategory: {category}\n"
        category_total = 0
        for item, cost in items_list:
            if category_total + cost <= budget:
                suggestions += f"- {item} (₹{cost})\n"
                category_total += cost

        total_cost += category_total

    if total_cost <= budget:
        suggestions += f"\nTotal Cost: ₹{total_cost}\nRemaining Budget: ₹{budget - total_cost}"
    else:
        suggestions += f"\nTotal Cost exceeds your budget. Try reducing some items."

    return suggestions

# Function to add new festival dynamically
def add_new_festival():
    festival_name = input("\nEnter the name of the new festival: ")
    zone = input("Enter the zone (e.g., North, South): ")
    decorations = input("Enter decoration items and their costs (comma separated, e.g., 'Rangoli Kit,500'): ").split(',')
    gifts = input("Enter gift items and their costs (comma separated, e.g., 'Sweets Box,1000'): ").split(',')
    food = input("Enter food items and their costs (comma separated, e.g., 'Homemade Snacks,2000'): ").split(',')

    if festival_name not in festival_items:
        festival_items[festival_name] = {}

    festival_items[festival_name][zone] = {
        "Decorations": [(decorations[i], int(decorations[i+1])) for i in range(0, len(decorations), 2)],
        "Gifts": [(gifts[i], int(gifts[i+1])) for i in range(0, len(gifts), 2)],
        "Food": [(food[i], int(food[i+1])) for i in range(0, len(food), 2)]
    }

    print(f"New festival '{festival_name}' in zone '{zone}' has been added successfully!")

# Function to personalize the experience
def personalize_preferences():
    user_preferences = {}
    categories = ["Decorations", "Gifts", "Food"]

    print("\nLet's customize your preferences!")
    for category in categories:
        response = input(f"Do you want suggestions for {category}? (yes/no): ").strip().lower()
        user_preferences[category] = response == 'yes'

    return user_preferences

# Main interaction loop
def main():
    print("Welcome to the Indian Festival Budget Planner!")
    festivals = list(festival_items.keys()) + ["Add New Festival"]  # Allow users to add new festivals
    print(f"\nAvailable Festivals: {', '.join(festivals)}")

    festival = input("\nEnter the festival you are celebrating (or choose 'Add New Festival' to add a new one): ").strip()

    if festival == "Add New Festival":
        add_new_festival()
        festival = input("\nEnter the festival you are celebrating: ").strip()

    zones = ["North", "South"]
    zone = input(f"Select your zone (Options: {', '.join(zones)}): ").strip()

    if zone not in zones:
        print("Invalid zone selection. Please choose either 'North' or 'South'.")
        return

    budget = int(input("Enter your budget (₹): "))

    # Personalize suggestions based on user preferences
    user_preferences = personalize_preferences()

    # Generate customized budget plan
    print("\n--- Budget Plan ---")
    plan = generate_budget_plan(festival, zone, budget, user_preferences)
    print(plan)

if __name__ == "__main__":
    main()

# Import necessary libraries
!pip install groq

!pip install python-dotenv

from groq import Groq #type:ignore
import os

# Set  Groq API key as an environment variable
os.environ["grokapikeyllama"] = "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"

# Initialize Groq client using API key
client = Groq(api_key=os.environ.get("grokapikeyllama"))

# Festival Budget Planner Function with Detailed Debugging
def generate_festival_budget(festival, budget):
    # Creating a dynamic system prompt based on user input
    system_prompt = f"festival budget planner\nTell me about the {festival} and plan a {festival} celebration with a budget of ₹{budget}"

    # Messages for the assistant
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"I want to celebrate {festival} within a budget of ₹{budget}. Please provide a breakdown for decorations, gifts, food, etc."
        },
        {
            "role": "assistant",
            "content": "I will generate a festival budget based on your inputs."
        }
    ]

    try:
        # Request completion from the Groq API
        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Model name (can be replaced with other models available)
            messages=messages,
            temperature=1,  # Adjust the creativity of the assistant's responses
            max_tokens=1024,  # Set max tokens for completion
            top_p=1,  # Control diversity
            stream=False,  # Disabled streaming for better debugging
            stop=None  # No specific stop condition
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"


# Interactive User Inputs for Festival and Budget
def get_user_input():
    # Get custom festival choice from user
    festival = input("Enter the name of the festival you want to celebrate: ")

    # Get budget input from user
    budget = int(input("Enter your budget for the celebration (in ₹): "))

    return festival, budget


# Main execution flow
if __name__ == "__main__":
    # Welcome message
    print("Welcome to the Festival Budget Planner Bot!\n\n")

    # Get user input
    festival, budget = get_user_input()

    # Call the function to get the budget breakdown
    response = generate_festival_budget(festival, budget)


    print(response)
    formatted_output = f"{response}\n\n"
    print(formatted_output)
    # Create output file
    with open("festival_budget_plan.txt", "w") as file:
        file.write("Welcome to the Festival Budget Planner Bot!\n\n")
        file.write(f"Festival: {festival}\n")
        file.write(f"Budget: ₹{budget}\n\n")
        file.write("Budget Breakdown:\n")
        file.write(str(response))
        file.write("\n\nThank you for using the Festival Budget Planner Bot. Have a great celebration!")

    # Print response for user
    print(f"Your budget breakdown has been saved to 'festival_budget_plan.txt'.")
    print("Thank you for using the Festival Budget Planner Bot. Have a great celebration!")