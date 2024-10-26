import json


with open('heart_rate_data.json', 'r') as file:
    dane = json.load(file)


min=200
max=0
for a in dane:
    heart_rate=a['heart_rate']
    if heart_rate>max:
        max=heart_rate
    if heart_rate<min:
        min=heart_rate

print(min)
print(max)