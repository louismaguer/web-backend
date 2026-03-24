# support code for notebook 302 - FastAPI basics

from fastapi import FastAPI

app = FastAPI()


# GET

"""
http ":8000/une/route/donnee?name=Basile&age=32"
"""
@app.get("/une/route/donnee")
async def get_parameters(
        name: str,
        age: int):
    return {"name": name, "age": age}


# GET avec paramètres dans l'URL

"""
http :8000/ma/route/12/
"""
@app.get("/ma/route/{parametre}")
async def url_parameter(parametre: int):
    return {"square": parametre**2}

"""
http :8000/le/debut/du/chemin/qui/peut/etre/long
"""
@app.get("/le/debut/du/chemin/{full_path:path}")
def path_parameter(full_path):
    return {"full_path": full_path}


# GET avec gestion d'erreur
import random
from fastapi import HTTPException

"""
http :8000/api/integer-check min==20 max==10
"""
@app.get("/api/integer-check")
def random_integers_with_check(n: int = 2, min: int = 0, max: int = 100):
    print(f"n={n}, min={min}, max={max}")
    if min >= max:
        raise HTTPException(status_code=400, detail="min must be smaller than max")
    return random.sample(range(min, max + 1), n)


# POST
from fastapi import Body


# un exemple de POST pour modifier l'état du serveur
"""
http :8000/api/seed seed_value:=42
"""

@app.post("/api/seed")
def set_seed(seed_value: int=Body(..., embed=True)):
    random.seed(seed_value)
    return {"message": f"Seed set to {seed_value}"}
