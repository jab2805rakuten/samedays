#!/usr/local/bin/python3
import calendar
import datetime

# Print calendar for January 2024
print(calendar.month(2025, 1))

# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Format date and time
formatted_date = now.strftime("%Y-%m-%d")
print("Formatted date:", formatted_date)

