from src.get_data import get_wearable_data, get_data_from_today
from src.model import HealthData, Model, load_model
from src.health_problem_detect import HealthProblemDetect
import importlib
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