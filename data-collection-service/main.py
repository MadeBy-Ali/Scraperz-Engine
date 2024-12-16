from fastapi import FastAPI

from scheduler.task import schedule_scrapping_job

import asyncio

app = FastAPI(title="Data Collection Service")

@app.get("/")
async def root():
    return {"message": "Data Collection Service is Running"}

@app.post("/start-scraping")
async def start_scraping_job():
    try:
        print("Triggering scraping job...")
        # Trigger Celery task (asynchronously)
        schedule_scrapping_job.delay()
        return {"status": "Scraping job started!"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}