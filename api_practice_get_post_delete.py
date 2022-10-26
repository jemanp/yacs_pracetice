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
        cur_time = r.json()['datatime']
        results.append({'name':city['name'],'timezone':city['timezone'] , 'current_time':cur_time})
    
    return result #return city created


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city  = db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/America/New_York/{city['timezone']}"
    r = requests.get(strs) # get ip address 
    cur_time = r.json()['datatime']
    return {'name':city['name'],'timezone':city['timezone'] , 'current_time':cur_time}
    #return the list of dictionary 
    
@app.get('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1] 

#@app.get('/cities/{city_id}')
#def delete_city(city_id: int):
    
    