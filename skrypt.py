from src.get_data import get_wearable_data, get_data_from_today
from src.model import HealthData, Model, load_model
from src.health_problem_detect import HealthProblemDetect
import importlib
import requests
#importlib.reload(src.model)

data=get_wearable_data()
healthData = HealthData(data)
model=load_model()
evaluated_data=model.evaluate(healthData)
print(evaluated_data)

today_data=get_data_from_today()
print(today_data)

problem=HealthProblemDetect.detectProblem(evaluated_data, today_data)
print(problem)



url = 'http://127.0.0.1:5000/get_ai_recomendation'  
data = {'health_problems': problem}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)

#saving data to db
url = 'http://127.0.0.1:5000/save_data'  
data = {'health_data': str(healthData)}
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)

