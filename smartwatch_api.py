import time
import random
from datetime import datetime
from lib.utils import get_producer

if __name__ == "__main__":
    producer = get_producer()

    while True:
        data = {'timestamp': [datetime.now().strftime("%d/%m/%Y %H:%M:%S")], 'heart_rate': [random.randint(60, 120)],
                'steps': [random.randint(0, 10)], 'sleep': [random.randint(0, 4)],
                'calories': [random.uniform(100, 1000)]}
        producer.send('health_data', value=data)
        producer.flush()
        time.sleep(15)
