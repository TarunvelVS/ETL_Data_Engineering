# kafka_producer.py
from kafka import KafkaProducer
import json
import time
import random

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Function to generate sample data
def generate_data():
    return {"timestamp": time.time(), "value": random.randint(1, 100)}

# Send data to Kafka topic
topic = 'real-time-data'
while True:
    data = generate_data()
    producer.send(topic, data)
    print(f'Sent: {data}')
    time.sleep(1)  # Adjust the sleep time as needed
