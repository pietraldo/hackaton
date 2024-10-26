import json
import random
from datetime import datetime, timedelta

# Set the start and end dates
start_date = datetime(2024, 10, 15)
end_date = datetime(2024, 10, 26)

# Initialize an empty list to hold all records
team_sleep_data = []

# Loop through each date within the date range
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")
    
    # Generate random averages for team sleep and good team sleep
    avg_team_sleep = round(random.uniform(6, 9), 1)  # Average team sleep (6 to 9 hours)
    avg_good_team_sleep = round(random.uniform(3, min(7, avg_team_sleep)), 1)  # Good sleep (3 to avg sleep, max 7)

    # Add the entry to the team_sleep_data list
    team_sleep_data.append({
        "date": date_str,
        "avg_team_sleep": avg_team_sleep,
        "avg_good_team_sleep": avg_good_team_sleep
    })
    
    # Move to the next day
    current_date += timedelta(days=1)

# Save data to a JSON file
with open('team_sleep_data.json', 'w') as file:
    json.dump(team_sleep_data, file, indent=4)

print("Data generation complete. Saved to 'team_sleep_data.json'.")
