from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index_1():
    return {"FIO": "Подъяпольская Алёна Александровна"}

@app.get('/users')
async def index_2():
    return {"Phone number": "+7-999-888-55-44"}

@app.get('/tools')
async def index_2():
    return {"Skills": "I can make a simple app on FastAPI"}


