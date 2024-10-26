
import requests


url = 'http://127.0.0.1:5000/generate_raport'  
data = {'id_teamu': 2}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)

