# habit.py
# This file contains the Habit class

from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity  # in days
        self.creation_date = datetime.now()
        self.completed_dates = []

    def complete_task(self):
        # Mark habit as completed for today
        self.completed_dates.append(datetime.now())

    def to_dict(self):
        # Convert object to dictionary for JSON storage
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "creation_date": str(self.creation_date),
            "completed_dates": [str(date) for date in self.completed_dates]
        }
