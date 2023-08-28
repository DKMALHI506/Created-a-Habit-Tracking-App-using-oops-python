# Created-a-Habit-Tracking-App-using-oops-python

import json
from datetime import datetime, timedelta

# Define the Habit class
class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completed_dates = []

    def complete_task(self):
        self.completed_dates.append(datetime.now())

    def is_broken(self):
        today = datetime.now()
        return all((today - date).days >= self.periodicity for date in self.completed_dates)

# Save habits to a JSON file
def save_habits_to_file(habits):
    with open("habits.json", "w") as f:
        json.dump(habits, f, default=lambda habit: habit.__dict__, indent=4)

# Load habits from the JSON file
def load_habits_from_file():
    try:
        with open("habits.json", "r") as f:
            data = json.load(f)
            habits = []
            for habit_data in data:
                habit = Habit(habit_data["name"], habit_data["periodicity"])
                habit.creation_date = datetime.strptime(habit_data["creation_date"], "%Y-%m-%d %H:%M:%S.%f")
                habit.completed_dates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f") for date in habit_data["completed_dates"]]
                habits.append(habit)
            return habits
    except FileNotFoundError:
        return []

# Main program logic
def main():
    habits = load_habits_from_file()

    while True:
        print("\n1. Add Habit")
        print("2. Complete Task")
        print("3. Analyze Habits")
        print("4. Exit")
        choice = int(input("Select an option: "))

        if choice == 1:
            name = input("Enter habit name: ")
            periodicity = int(input("Enter periodicity (in days): "))
            new_habit = Habit(name, periodicity)
            habits.append(new_habit)
            save_habits_to_file(habits)
            print("Habit added!")

        elif choice == 2:
            for i, habit in enumerate(habits, start=1):
                print(f"{i}. {habit.name}")
            habit_index = int(input("Select habit to complete: ")) - 1
            habits[habit_index].complete_task()
            save_habits_to_file(habits)
            print("Task completed!")

        elif choice == 3:
            # Implement analytics functions here
            pass

        elif choice == 4:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

