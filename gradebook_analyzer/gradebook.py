"""
GradeBook Analyzer
Course: Programming for Problem Solving using Python
Assignment: Analysing and Reporting Student Grades
Student Name: HARSH
Roll No. : 2501730062
Date: 25 Nov 2025
"""

import csv
import statistics

# ----------------------------------------------------
# TASK 1 — MENU + INITIALIZATION
# ----------------------------------------------------

def print_menu():
    print("\n===================================")
    print("         GRADEBOOK ANALYZER")
    print("===================================")
    print("1. Enter student data manually")
    print("2. Load data from CSV file")
    print("3. Exit")
    print("===================================")

# ----------------------------------------------------
# TASK 2 — MANUAL INPUT + CSV IMPORT
# ----------------------------------------------------

def manual_input():
    marks = {}
    print("\nEnter student marks (type 'done' to finish):\n")

    while True:
        name = input("Enter student name: ").strip()
        if name.lower() == "done":
            break

        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid input! Enter a number for marks.")

    return marks


def load_csv():
    marks = {}
    filename = input("\nEnter CSV filename (with .csv): ")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        marks[name] = float(row[1])
                    except:
                        pass
        print("CSV loaded successfully!\n")
    except FileNotFoundError:
        print("Error: File not found.\n")

    return marks

# ----------------------------------------------------
# TASK 3 — STATISTICS FUNCTIONS
# ----------------------------------------------------

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

def find_min_score(marks_dict):
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

# ----------------------------------------------------
# TASK 4 — GRADE ASSIGNMENT + DISTRIBUTION
# ----------------------------------------------------

def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
            grade, score
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade
    return grades


def grade_distribution(grades_dict):
    dist = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades_dict.values():
        dist[g] += 1
    return dist

# ----------------------------------------------------
# TASK 5 — PASS/FAIL USING LIST COMPREHENSION
# ----------------------------------------------------

def pass_fail_lists(marks_dict):
    passed = [name for name, m in marks_dict.items() if m >= 40]
    failed = [name for name, m in marks_dict.items() if m < 40]
    return passed, failed

# ----------------------------------------------------
# TASK 6 — RESULT TABLE + LOOP
# ----------------------------------------------------

def print_results_table(marks_dict, grades_dict):
    print("\n===================================")
    print("             RESULTS TABLE")
    print("===================================")
    print(f"{'Name':15} {'Marks':10} {'Grade'}")
    print("-" * 35)

    for name in marks_dict:
        print(f"{name:15} {marks_dict[name]:<10} {grades_dict[name]}")

    print("-" * 35)


def analyze(marks):
    if not marks:
        print("No data to analyze!")
        return

    # --- Statistics ---
    avg = calculate_average(marks)
    med = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)

    # --- Grades ---
    grades = assign_grades(marks)
    dist = grade_distribution(grades)

    # --- Pass/Fail ---
    passed, failed = pass_fail_lists(marks)

    # --- Print everything ---
    print("\n============ STATISTICAL SUMMARY ============")
    print(f"Average Score: {avg:.2f}")
    print(f"Median Score: {med}")
    print(f"Highest Score: {max_name} ({max_score})")
    print(f"Lowest Score: {min_name} ({min_score})")

    print("\n============ GRADE DISTRIBUTION ============")
    for grade, count in dist.items():
        print(f"{grade}: {count}")

    print("\n============ PASS / FAIL ============")
    print(f"Passed ({len(passed)}): {', '.join(passed) if passed else 'None'}")
    print(f"Failed ({len(failed)}): {', '.join(failed) if failed else 'None'}")

    print_results_table(marks, grades)


# ----------------------------------------------------
# MAIN PROGRAM LOOP
# ----------------------------------------------------

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            marks = manual_input()
            analyze(marks)

        elif choice == "2":
            marks = load_csv()
            analyze(marks)

        elif choice == "3":
            print("\nExiting GradeBook Analyzer... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")

# Run the project
if __name__ == "__main__":
    main()
