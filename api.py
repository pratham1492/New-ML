# python api - framework - fast api - rest api 
#api oops pip install fastapi uvicorn 
# server install uvicorn -browser - 8000 
# base model = structure and validate 
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
#fastapi oops -class 
#class inilaization  data store 
app=FastAPI() #inilalization of fast api class 

student=[] #blank lst 

class mydata(BaseModel):
    id:int
    name:str
    email:str

# get post delete - function decorder/annotation
#set of instruction 
#server properly work 
#routes /
@app.get("/")
def testing():
    return {"msg":"server is running"}

# all datafetch -get
@app.get("/alldata") 
def alldatafetch():
    return student

# data insert - post 
#insert into tba name,email id 
@app.post("/datainsert")
def datainsert(s:mydata):

    student.append(s.model_dump())

    return {"msg":"data inserted"}

#delete -put patch = data set 
#delete * from tb where id=5
# id pass = list  student  
@app.delete("/mydelete/{id}")
def datadelete(id:int):
    #== nd = 
    for s in student:
        if s["id"] == id: #4 delete 4=4

            student.remove(s)

            return {"msg":"data deleted"}
    return {"msg":"id not found"}        
# python run uvicorn 
#  uvicorn myapi:app --reload    
#common end point http://127.0.0.1:8000/mydata/4
#domain name 
#https - ssl