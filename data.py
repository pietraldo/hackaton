import json


with open('stress_activity_sleep_rest_dataset.json', 'r') as file:
    dane = json.load(file)

sorted_data = sorted(dane, key=lambda x: (x['date'], x['time']))
for a in sorted_data:
    print(a)