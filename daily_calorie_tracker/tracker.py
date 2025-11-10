# ==========================================================
# Name: Your Name
# Date: 10-Nov-2025
# Project Title: Daily Calorie Tracker CLI
# Course: Programming for Problem Solving using Python
# Description:
#   A command-line tool to log daily meals and calories,
#   compute total & average intake, compare with a daily limit,
#   and optionally save the session summary to a text file.
# ==========================================================

from datetime import datetime

# ------------------- Task 1: Introduction -------------------
print("=====================================")
print(" Welcome to the Daily Calorie Tracker ")
print("=====================================")
print("Track your daily meals and calories easily!\n")

# ------------------- Task 2: Data Collection -------------------
# Ask how many meals user wants to log
num_meals = int(input("How many meals would you like to log today? "))

# Create empty lists to store meal names and calories
meal_names = []
meal_calories = []

# Loop to collect meal details
for i in range(num_meals):
    print(f"\n--- Meal #{i+1} ---")
    meal = input("Enter meal name: ")
    calories = float(input(f"Enter calories for {meal}: "))
    meal_names.append(meal)
    meal_calories.append(calories)

# ------------------- Task 3: Calculations -------------------
# Calculate total and average calories
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)

# Ask user for daily calorie limit
daily_limit = float(input("\nEnter your daily calorie limit: "))

# ------------------- Task 4: Limit Check -------------------
if total_calories > daily_limit:
    status_message = "⚠️ WARNING: You have exceeded your daily calorie limit!"
else:
    status_message = "✅ Great job! You are within your daily calorie limit."

# ------------------- Task 5: Formatted Output -------------------
print("\n=======================================")
print("           DAILY CALORIE SUMMARY       ")
print("=======================================")
print("Meal Name\t\tCalories")
print("---------------------------------------")

# Print each meal entry
for i in range(len(meal_names)):
    print(f"{meal_names[i]:15}\t{meal_calories[i]}")

print("---------------------------------------")
print(f"Total:\t\t\t{total_calories}")
print(f"Average per meal:\t{average_calories:.2f}")
print(f"Daily Limit:\t\t{daily_limit}")
print("---------------------------------------")
print(status_message)

# ------------------- Task 6 (Bonus): Save Session -------------------
save_option = input("\nWould you like to save this session? (yes/no): ").lower()

if save_option == "yes":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"

    with open(filename, "w") as file:
        file.write(f"Calorie Tracker Log - {timestamp}\n")
        file.write("=====================================\n")
        file.write("Meal Name\tCalories\n")
        file.write("-------------------------------------\n")
        for i in range(len(meal_names)):
            file.write(f"{meal_names[i]:15}\t{meal_calories[i]}\n")
        file.write("-------------------------------------\n")
        file.write(f"Total:\t\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Daily Limit:\t{daily_limit}\n")
        file.write(f"Status:\t\t{status_message}\n")
        file.write("=====================================\n")

    print(f"✅ Session saved successfully to '{filename}'!")
else:
    print("Session not saved. Goodbye!")

# ------------------- End of Program -------------------
