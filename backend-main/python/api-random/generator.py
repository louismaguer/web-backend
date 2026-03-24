import random

from fastapi import FastAPI, HTTPException

app = FastAPI()


# simple GET endpoints with query parameters
@app.get("/api/integer")
def random_integers(count: int = 3, min: int = 0, max: int = 100):
    return random.sample(range(min, max + 1), count)


@app.get("/api/float")
def some_random_floats(count: int = 3, min: float = 0, max: float = 100):
    return [random.uniform(min, max) for _ in range(count)]




# a sample POST endpoint to set the random seed
# used later on in the course to discuss POST requests with body parameters
# NOTE: this is not the simplest/most common way to pass body parameters
# but we have not covered Pydantic models yet, so this is a good intermediate step


from fastapi import Body

@app.post("/api/seed")
# with Body() we indicate that the parameter comes from the request body
# with embed=True we state that the parameter is embedded in a JSON object
# as opposed to being sent raw
def set_seed(seed_value: int=Body(..., embed=True)):
    random.seed(seed_value)
    return {"message": f"Seed set to {seed_value}"}


# exact same functionality, but leveraging Pydantic models
# using Pydantic model to parse the request body
from pydantic import BaseModel
class SeedRequest(BaseModel):
    seed_value: int

# once this is done the endpoint can be rewritten more cleanly
@app.post("/api/seed2")
def set_seed2(seed: SeedRequest):
    # extract the seed value from the request body
    seed_value = seed.seed_value
    # no need to check or convert to int, Pydantic has done it for us
    random.seed(seed_value)
    return {"message": f"Random seed set to {seed_value}"}


