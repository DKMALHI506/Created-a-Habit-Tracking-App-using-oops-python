# main.py
# Main program for Habit Tracking App

import json
from datetime import datetime
from habit import Habit

DATA_FILE = "../data/habits.json"

# Load habits from file
def load_habits():
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            habits = []

            for item in data:
                habit = Habit(item["name"], item["periodicity"])
                habit.creation_date = datetime.fromisoformat(item["creation_date"])
                habit.completed_dates = [
                    datetime.fromisoformat(d) for d in item["completed_dates"]
                ]
                habits.append(habit)

            return habits
    except FileNotFoundError:
        return []

# Save habits to file
def save_habits(habits):
    with open(DATA_FILE, "w") as file:
        json.dump([habit.to_dict() for habit in habits], file, indent=4)

def main():
    habits = load_habits()

    while True:
        print("\n--- Habit Tracking App ---")
        print("1. Add Habit")
        print("2. Complete Habit")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter habit name: ")
            days = int(input("Enter periodicity (days): "))
            habits.append(Habit(name, days))
            save_habits(habits)
            print("Habit added successfully!")

        elif choice == "2":
            if not habits:
                print("No habits available.")
                continue

            for i, habit in enumerate(habits, start=1):
                print(f"{i}. {habit.name}")

            index = int(input("Select habit number: ")) - 1
            habits[index].complete_task()
            save_habits(habits)
            print("Habit marked as completed!")

        elif choice == "3":
            if not habits:
                print("No habits found.")
            else:
                for habit in habits:
                    print(f"\nHabit: {habit.name}")
                    print(f"Created on: {habit.creation_date}")
                    print(f"Times completed: {len(habit.completed_dates)}")

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
