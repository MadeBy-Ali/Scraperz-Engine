from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop = stop_after_attempt(3), wait = wait_fixed (5))
def retry_scrapping_task(task):
    print("Retrying task....")
    return task()