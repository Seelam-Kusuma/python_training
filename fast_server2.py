from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Item(BaseModel):
    name: str 
    description:str|None=None
    price : float 
    tax:float|None=None

d1={1:'kusuma',2:'ganesh',3:'rakesh'}
items:dict[int,Item]={}
@app.get("/list/{item_id}")
async def read_query(item_id:int|None =None, limit:int|None=None):
    if item_id in items :
        return d1[item_id]
    else:
        return d1







