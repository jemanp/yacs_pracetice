from re import template
from time import timezone
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from pydantic import BaseModel

import  requests

app = FastAPI()

db = []

#===============#===============#===============
# dats model
#===============#===============#===============

class City(BaseModel):
    name: str
    timezone: str
    
template = Jinja2Templates(directory="templates")
    
@app.get("/")
def root():
    return {"hello": "world"}

@app.get('/cities', response_class=HTMLResponse)
def get_cities(request: Request):
    context = {}
    rsCity = []
    for city in db:
        strs = "http://worldtimeapi.org/api/timezone/America/New_York"
        r = requests.get(strs) # get ip address 
        cur_time = r.json()['datatime']
        rsCity.append({'name':city['name'],'timezone':city['timezone'] , 'current_time':cur_time})
    
    context['request'] = request
    context['rsCity'] = rsCity
    return template.TemplateResponse('city_list.html', context)

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city  = db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/America/New_York/{city['timezone']}"
    r = requests.get(strs) # get ip address 
    cur_time = r.json()['datatime']
    return {'name':city['name'],'timezone':city['timezone'] , 'current_time':cur_time}
    #return the list of dictionary 
    
@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1] 

#append list and delete pop
@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
    