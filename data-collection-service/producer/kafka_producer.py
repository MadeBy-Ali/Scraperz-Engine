from kafka import KafkaProducer
import json

def get_kafka_producer():
    return KafkaProducer(
        bootsrap_servers = ["localhost:9092"],
        value_serializer = lambda v: json.dumps(v).encode("utf-8") 
    )
    
def send_kafka_topic(topic, data):
    producer = get_kafka_producer()
    producer.send(topic, value = data)
    producer.flush()
    print(f"Data Pushed to topic: {topic}")