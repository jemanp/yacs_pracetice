from time import timezone
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone: str
    
@app.get("/")
    def root():
        return {"hello": "world"}

@app.get('/cities')
def get_cities():
    result = []
    for city in db:
        strs = "http://worldtimeapi.org/api/timezone/America/New_York"
        r = requests.get(strs) # get ip address 
    
    return result #return city created


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    
@app.get('/cities')
def create_city(city_id: int):

@app.get('/cities/{city_id}')
def delete_city(city_id: int):
    
    