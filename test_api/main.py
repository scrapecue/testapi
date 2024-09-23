from fastapi import FastAPI
import random
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/random", status_code=200)
def get_random_number():
    return JSONResponse(content={"random_number": random.randint(1, 100)},
                        status_code=200)
