from fastapi import FastAPI
import datetime
import json
app = FastAPI()

with open('date.json', 'r') as file:
        users = json.load(file)['data']

@app.get('/', status_code = 200)
def manin_page():
    return "Hello world!"

@app.get('/date', status_code = 200)
def getDate():
    todays = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return todays

@app.get('/users', status_code = 200)
def getUsers():
    user = [u for u in users]
    return user if len(users) > 0 else {"Error":" There'are no records"}
    