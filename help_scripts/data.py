import json

with open('stress_activity_sleep_rest_dataset.json', 'r') as file:
    dane = json.load(file)

# Sort data by 'date' and 'time'
sorted_data = sorted(dane, key=lambda x: (x['date'], x['time']))
# for a in sorted_data:
#     print(a)

# Initialize an empty dictionary
dic = {}

# Loop through sorted data and count occurrences of each date-time combination
for a in sorted_data:
    key = a["date"] +" "+ a['time']  # Concatenate 'date' and 'time' to create a unique key
    if key in dic:
        dic[key] += 1  # Increment count if the key exists
    else:
        dic[key] = 1   # Initialize count if the key doesn't exist

for key, value in dic.items():
    print(key + ": " + str(value))

