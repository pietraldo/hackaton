
import random
from datetime import datetime, timedelta

def generate_health_status(num_records):
    health_status_records = []
    base_timestamp = datetime(2024, 10, 5, 0, 0)  # Starting timestamp
    current_stress = False
    current_asleep = False
    current_good_sleep = True
    current_exercise = False
    current_tired = False

    for i in range(num_records):
        # Increment the timestamp by one minute for each record
        timestamp = (base_timestamp + timedelta(minutes=i)).timestamp()

        # Randomly change states with low probability to avoid rapid changes
        if random.random() < 0.1:  # 10% chance to change state
            current_stress = not current_stress
        if random.random() < 0.1:
            current_asleep = not current_asleep
        if random.random() < 0.1:
            current_good_sleep = not current_good_sleep
        if random.random() < 0.1:
            current_exercise = not current_exercise
        if random.random() < 0.1:
            current_tired = not current_tired

        # Create the health status record
        record = {
            'timestamp': timestamp,
            'is_stressed': current_stress,
            'is_asleep': current_asleep,
            'good_sleep': current_good_sleep,
            'is_exercise': current_exercise,
            'is_tired': current_tired
        }
        
        health_status_records.append(record)

    return health_status_records

# Generate 20 health status records
health_status_records = generate_health_status(20)

# Print the generated records
for record in health_status_records:
    print(record)
