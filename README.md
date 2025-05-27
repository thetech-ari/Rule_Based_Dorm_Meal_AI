# Dorm Meal Recommender 🍳🥘

This is a simple **rule-based AI system** written in Python that helps users decide what to cook in a dorm room based on ingredients they have on hand.

## 📌 Project Objective

This project was created as part of an assignment to understand how AI systems worked before the rise of machine learning. The system uses logical rules (IF-THEN statements) to make decisions, rather than learning from data.

## 💡 How It Works

The user enters a list of ingredients they currently have. The program then uses predefined rules to suggest a meal that can be made from those ingredients. If no match is found, the system suggests getting takeout or having a snack.

### 🧠 Sample Rules
- If the input contains `"eggs"` and `"bread"` → Suggest **French Toast**
- If the input contains `"rice"` and `"beans"` → Suggest **Rice and Beans Bowl**
- If the input contains `"ramen"` and `"cheese"` → Suggest **Cheesy Ramen**
- If the input contains `"tortilla"` and `"cheese"` → Suggest **Quesadilla**

## 🚀 How to Run

1. Clone or download the repo
2. Run the script using Python 3:

```bash
python dorm_meal_recommender.py
