from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/gettodos")
def gettodos():
    print("Ramdan Mubark")
    return"Ramdan Mubarak"
@app.get("/getSingleTodos")
def getsingletodos():
    print ("Advance Eid Mubarak")
    return "getSingleTodos"

def start():
    uvicorn.run("hello_world.main:app",host="127.0.0.1",port=8000,reload=True)