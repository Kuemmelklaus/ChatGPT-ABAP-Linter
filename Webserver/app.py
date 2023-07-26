import sys
import os
import time
import json
from apiflask import APIFlask, Schema, abort
from apiflask.fields import String
sys.path.append(os.getcwd() + "/..")
from linter import Linter

app = APIFlask(__name__, title = "Linter", version = "1.0")

@app.get("/")
def root():
    return {"message": 'use "POST /linter"'}

@app.get("/health")
def health():
    return {"message": "Server is running!"}

class Lin(Schema):
    programmingLanguage = String(required = True)
    code = String(required = True)

@app.post("/linter")
@app.input(Lin, location = "json")
def lint(json_data):
    linter = Linter(json_data["programmingLanguage"], json_data["code"])
    i = 0
    while(not linter.done):
        time.sleep(1)
        if(i < 120):
            print("Timemout!")
            return json.dumps('{"success": "False"}')
        i += 1
    return linter.getLint()