from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
@app.get("/hello")
def hello():
    return {"message": "Hello World"}
@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}"}
@app.get("/hello/{name}/{age}")
def hello_name_age(name: str, age: int):
    return {"message": f"Hello {name} and you are {age} years old"}
@app.get("/hello/{name}/{weight}")
def hello_name_weight(name: str, weight: int):
    return {"message": f"Hello {name} and you are {weight} kg"}
@app.get("/hello/{name}/{height}")
def hello_name_height(name: str, height: int):
    return {"message": f"Hello {name} and you are {height} cm"}
@app.get("/hello/{name}/{age}/{weight}/{height}")
def hello_name_age_weight_height(name: str, age: int, weight: int, height: int):
    return {"message": f"Hello {name} and you are {age} years old, {weight} kg and {height} cm"}
@app.get("/hello/{name}/{age}/{weight}/{height}/{hair_color}")
def hello_name_age_weight_height_hair_color(name: str, age: int, weight: int, height: int, hair_color: str):
    return {"message": f"Hello {name} and you are {age} years old, {weight} kg and {height} cm and you have {hair_color} hair"}