import json
import random
from datetime import datetime, timedelta

# Set the start and end dates
start_date = datetime(2024, 10, 15)
end_date = datetime(2026, 10, 26)

# Define the number of employees and initialize an empty list to hold all records
num_employees = 8
sleep_data = []

# Loop through each date within the date range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    
    # Generate data for each employee for the current date
    for emp_id in range(1, num_employees + 1):
        total_sleep = round(random.uniform(4, 10), 1)  # Total sleep hours (4 to 10)
        good_sleep = round(random.uniform(0, min(8, total_sleep)), 1)  # Good sleep (0 to total sleep, max 8)
        
        # Add the entry to the sleep_data list
        sleep_data.append({
            "data": date_str,
            "hours_of_good_sleep": good_sleep,
            "hours_of_sleep": total_sleep,
            "id_pracownika": emp_id
        })
    
    # Move to the next day
    current_date += timedelta(days=1)

# Save data to a JSON file
with open('sleep_data.json', 'w') as file:
    json.dump(sleep_data, file, indent=4)

print("Data generation complete. Saved to 'sleep_data.json'.")
