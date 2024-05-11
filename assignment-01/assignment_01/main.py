
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import uvicorn

app = FastAPI()

students:list=[
    {"Student_ID":1, "Name":"Naeem","Age":17,"Class_":8,"Grade":"A"},
    {"Student_ID":2, "Name":"Saleem","Age":16,"Class_":7,"Grade":"A+"}, 
    {"Student_ID":3, "Name":"Faheem","Age":15,"Class_":6,"Grade":"B"},
    {"Student_ID":4, "Name":"Nadeem","Age":18,"Class_":9,"Grade":"D"},
    {"Student_ID":5, "Name":"Safder","Age":19,"Class_":10,"Grade":"F"},
    {"Student_ID":6, "Name":"Akber","Age":20,"Class_":11,"Grade":"A"}
]

@app.get("/students")
def student_list():
    return students
@app.get("/student/{id}")
def students_id(id:int=0):
    return id

@app.get("/students/{student_id}")
def studends_id():{}
def get_student(student_id: int=0):
    for student in students:
        if student_id:
            student["student_id"]=student_id
            return student
        else:
            return {"massage":"not found"}
        return (get_student)
    
@app.post("/add")
def add(a:int=1,b:int=2):
    c=a+b
    return (c)
    
    
     

@app.post("/students")
def add_student(student_id:int=0,name:str="none",age:int=0,class_:int=0,grade:str="none"):
    students.append(
       { "student_id":"",
        "Name":"",
        "Age":"",
        "class_":"",
        "Grade":""
      }
    )
    return students
    

@app.put("/update_students")
def update_students(student_id:int=0,name:str="none",age:int=0,class_:int=0,grade:str="none"):

       {students.students_id :"studends_id",
        students.name:"name",
        students.Age:"age",
        students.class_:"class_",
        students.Grade:"grade"
      }
       return students
    
def start():
    uvicorn.run("assignment_01.main:app",host="127.0.0.1",port=8080,reload=True)