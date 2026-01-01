from fastapi import FastAPI
from db.operations import log

app = FastAPI()



@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/cpu/temperature/{temperature}")
async def log_cpu(temperature: float):
    response = log(cpu_temperature=temperature)
    if response["status"] == "success":
        return {"message": "CPU temperature logged successfully", "data": response["data"]}
    else:
        return {"message": "Failed to log CPU temperature", "error": response["message"]}

