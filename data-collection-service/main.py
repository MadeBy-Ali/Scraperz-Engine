from fastapi import FastAPI

from scheduler.task import schedule_scrapping_job

import asyncio

app = FastAPI(title="Data Collection Service")

@app.get("/")
async def root():
    return {"message": "Data Collection Service is Running"}

@app.post("/start-scraping")
async def start_scraping_job():
    # Trigger scraping job
    asyncio.create_task(schedule_scrapping_job())
    return {"status": "Scraping job started!"}