from celery import Celery
from scrapper.scraper import run_scrapper

from producer.kafka_producer import send_kafka_topic

from utils.retry_handler import retry_scrapping_task
from utils.validations import validate_data

app = Celery(
    "tasks",
    broker = "redis://localhost:6379/0",
    backend = "redis://localhost:6379/0",
)

@app.task
def schedule_scrapping_job():
    try:
        print("starting scrapping job...")
        run_scrapper()
        
        # scrape output
        dummy_data = {"name": "Sample Product", "price": "10$", "url": "example.com"}
        
        # validation before send topic
        validated_data = validate_data(dummy_data)
        if validate_data:
            send_kafka_topic(topic="new-data-topic", data=validated_data)
    except Exception as e :
        print(f"Error scrapping job:{str(e)}")
        
@app.task
def retry_task():
    retry_scrapping_task(run_scrapper)
    send_kafka_topic(topic="new-data-topic", data={"key":"value"})
