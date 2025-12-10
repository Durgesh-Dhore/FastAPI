from fastapi import FastAPI, Request
from datetime import datetime

app = FastAPI()

hit_count = 0     # Track hit number


@app.get("/")
async def read_root(request: Request):
    global hit_count
    hit_count += 1  # Increase hit count for every request

    # Get visitor IP
    client_ip = request.client.host

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print in EC2 terminal only
    print(f"Hit No: {hit_count} | IP: {client_ip} | Time: {timestamp}")

    # Show only message to the user
    return {"message": "Hello World"}
