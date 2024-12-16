from celery import Celery
from scrapper.scraper import run_scrapper

from producer.kafka_producer import send_kafka_topic

from utils.retry_handler import retry_scrapping_task
from utils.validations import validate_data

app = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

@app.task
def schedule_scrapping_job():
    try:
        print("Starting scraping job...")
        
        # Simulate scraper output
        run_scrapper()  # Your scraping logic
        dummy_data = {"name": "Sample Product", "price": "10$", "url": "example.com"}
        
        # Validate scraped data
        validated_data = validate_data(dummy_data)
        if validated_data:
            print("Sending data to Kafka...")
            send_kafka_topic(topic="new-data-topic", data=validated_data)
        else:
            print("Data validation failed.")
    except Exception as e:
        print(f"Error during scraping job: {str(e)}")
        
@app.task
def retry_task():
    retry_scrapping_task(run_scrapper)
    send_kafka_topic(topic="new-data-topic", data={"key":"value"})
