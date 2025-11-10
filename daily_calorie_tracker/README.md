# 🥗 Daily Calorie Tracker CLI

## 📘 Course Information
**Course:** Programming for Problem Solving using Python  
**Assignment Type:** Individual Mini Project  
**Submission Date:** 10th November 2025  
**Weightage:** 5 Marks  

---

## 💡 Project Overview
The **Daily Calorie Tracker CLI** is a Python-based console application that helps users log their meals and calorie intake throughout the day. It calculates total and average calories, compares the intake with a user-defined daily calorie limit, and optionally saves the session log to a text file.

This tool encourages mindful eating and basic health awareness while strengthening core Python programming skills such as I/O, loops, conditionals, and file handling.

---

## 🎯 Learning Objectives
By completing this mini-project, you will learn to:

- Use `input()`, type conversion, and basic I/O operations in Python  
- Manage user data using lists and basic data structures  
- Perform arithmetic and comparison operations  
- Use f-strings and escape characters for formatted output  
- Implement simple file I/O operations  
- Build a working Command Line Interface (CLI) tool  

---

## 🧩 Project Features
✔️ User-friendly command-line interface  
✔️ Input and store multiple meals and calorie values  
✔️ Calculate total and average calories  
✔️ Compare with a daily calorie limit  
✔️ Show status message (within limit / exceeded)  
✔️ Bonus: Save summary to a timestamped `.txt` file  

---

## 🗂️ Project Structure
daily_calorie_tracker/
│
├── tracker.py # Main Python script
├── calorie_log.txt # Session log file (auto-created if user chooses to save)
└── README.md # Project description and documentation

yaml
Copy code

---

## ⚙️ How to Run

1. **Clone or Download** this repository from GitHub.
2. Open the folder in your IDE (VS Code / PyCharm / etc.).
3. Run the script in a terminal or command prompt:
   ```bash
   python tracker.py
Follow the on-screen instructions:

Enter the number of meals

Input meal names and calorie values

Provide your daily calorie limit

Optionally save the session log to a file

**🧮 Sample Runs**
Sample Run 1 (Within Limit)
pgsql
Copy code
How many meals would you like to log today? 3
Enter meal name: Breakfast
Enter calories for Breakfast: 300
Enter meal name: Lunch
Enter calories for Lunch: 600
Enter meal name: Dinner
Enter calories for Dinner: 500
Enter your daily calorie limit: 1600

✅ Great job! You are within your daily calorie limit.
Sample Run 2 (Exceed Limit)
pgsql
Copy code
How many meals would you like to log today? 2
Enter meal name: Lunch
Enter calories for Lunch: 900
Enter meal name: Dinner
Enter calories for Dinner: 850
Enter your daily calorie limit: 1500

**⚠️ WARNING: You have exceeded your daily calorie limit!
Sample Run 3 (Save Session Log)
pgsql
Copy code
Would you like to save this session? (yes/no): yes
✅ Session saved successfully to 'calorie_log.txt'!
🗒️ Example Output File (calorie_log.txt)
markdown
Copy code
Calorie Tracker Log - 2025-11-10 21:42:35
=====================================
Meal Name   Calories
-------------------------------------
Breakfast   350
Lunch       600
Dinner      550
-------------------------------------
Total:      1500
Average:    500.00
Daily Limit:1500
Status:     ✅ Within daily limit**
=====================================
🧠 Concepts Demonstrated
Variables, loops, and conditionals

Lists and data aggregation

Type casting (int, float)

Arithmetic and comparison operators

String formatting using f-strings

File handling using open(), write(), and context managers

📜 Academic Integrity
This project is an individual assignment.
All code is original and written for academic purposes only.
Any external references used are limited to official Python documentation and basic tutorials.

🧑‍💻 Author
Name: Harsh

Email: 2501730062@krmangalam.edu.in

Date: 10-Nov-2025

github repository link: https://github.com/Harshkrmu/PPS-with-Python/

Instructor: Sameer Farooq
