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

@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["students_id"]== students_id:
            return student
        return{"massage":"not found"}
        

@app.post("/students")
def add student(student_id:int,name:str,age:int,class_:int,grade:str):
    students.append(
       { "students_id":"students_id",
        "Name":"name",
        "Age":"age",
        "Class":"class",
        "Grade":"grade"}
    )
    return students
    

@app.put("/students/{student_id}")
def update_student(students_id:int,name:str,age:int,class_:int,grade:str) 
if student["students_id"]:students_id,
       student["Name"]:name
       student["Age"]:age
        student["Class"]:class_
        student[Grade]:grade
    return students
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
    if student["students_ID"]:students_id
    students.remove(student)
    return students
return {"massage":"not found"}
def start():
    uvicorn.run("assignment_01.main:app",host="127.0.0.1",port=8080,reload=True)