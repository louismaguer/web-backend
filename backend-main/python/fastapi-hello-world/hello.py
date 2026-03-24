# dans hello.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.api_route("/ping", methods=["GET", "POST"])
def ping():
    return {"message": "pong"}
