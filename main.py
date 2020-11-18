from fastapi import FastAPI

app = FastAPI()


@app.post('/webhook/',  status_code=200)
async def index(messages: str):
    print (messages)
    return messages