from src.model import HealthData, Model, load_model, EvaluatedHealthData

def get_wearable_data():
    return {
    "steps":23,
    "heart_rate":56,
    "hrv":75,
    "respiratory_rate":18.86,
    "spO2":97.1,
    "systolic_bp": 111,
    "diastolic_bp": 90
    };
    
def get_data_from_today():
    return [
        {'timestamp': 1728079200.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079260.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079320.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079380.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079440.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079500.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079560.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': True, 'is_tired': False},
        {'timestamp': 1728079620.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': True, 'is_tired': False},
        {'timestamp': 1728079680.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': True, 'is_tired': False},
        {'timestamp': 1728079740.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': True, 'is_tired': False},
        {'timestamp': 1728079800.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': False, 'is_exercise': True, 'is_tired': False},
        {'timestamp': 1728079860.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': False, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079920.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728079980.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': False, 'is_tired': True},
        {'timestamp': 1728080040.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': False, 'is_tired': True},
        {'timestamp': 1728080100.0, 'is_stressed': True, 'is_asleep': True, 'good_sleep': True, 'is_exercise': False, 'is_tired': True},
        {'timestamp': 1728080160.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': True},
        {'timestamp': 1728080220.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': True},
        {'timestamp': 1728080280.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': False},
        {'timestamp': 1728080340.0, 'is_stressed': True, 'is_asleep': False, 'good_sleep': True, 'is_exercise': False, 'is_tired': True}
    ]
    
