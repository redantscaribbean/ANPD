from fastapi import FastAPI

app = FastAPI()


@app.post('/webhook/',  status_code=200)
async def index(message: dict):
    print (message)
    return message