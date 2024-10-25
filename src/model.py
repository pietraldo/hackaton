import json
from datetime import datetime

class HealthData:
    def __init__(self, data):
        
        self.timestamp = datetime.now().timestamp()
        self.steps = data["steps"]
        self.heart_rate = data["heart_rate"]
        self.hrv = data["hrv"]
        self.respiratory_rate = data["respiratory_rate"]
        self.spO2 = data["spO2"]
        self.systolic_bp = data["systolic_bp"]
        self.diastolic_bp = data["diastolic_bp"]
        
    def __str__(self):
        return (f"HealthData(timestamp={self.timestamp}, "
                f"steps={self.steps}, "
                f"heart_rate={self.heart_rate}, "
                f"hrv={self.hrv}, "
                f"respiratory_rate={self.respiratory_rate}, "
                f"spO2={self.spO2}, "
                f"systolic_bp={self.systolic_bp}, "
                f"diastolic_bp={self.diastolic_bp})")
        
class EvaluatedHealthData:
    def __init__(self, is_stressed, is_asleep, good_sleep, is_exercise, is_tired):
        self.timestamp=datetime.now().timestamp()
        self.is_stressed=is_stressed
        self.is_asleep=is_asleep
        self.good_sleep=good_sleep
        self.is_exercise=is_exercise
        self.is_tired=is_tired
    
    def __str__(self):
        return (
            f"EvaluatedHealthData("
            f"is_stressed={self.is_stressed}, "
            f"is_asleep={self.is_asleep}, "
            f"good_sleep={self.good_sleep}, "
            f"is_exercise={self.is_exercise}, "
            f"is_tired={self.is_tired})"
        )

class Model:
    def __init__(self):
        pass
    def evaluate(self,healthData):
        is_stressed = healthData.heart_rate > 100 or healthData.hrv < 50
        is_asleep = healthData.heart_rate < 60 and healthData.respiratory_rate < 12
        good_sleep = healthData.hrv > 60 and healthData.spO2 >= 95
        is_exercise = healthData.steps > 1000
        is_tired = healthData.heart_rate > 80 and healthData.spO2 < 95

        return EvaluatedHealthData(is_stressed, is_asleep, good_sleep, is_exercise, is_tired)
    
def load_model():
    return Model();