#!env python
import importlib
import json
from fastapi import FastAPI, Request

# TEST CODE -- DANGER!

config = {
    "libname": "spacelab.spacelab",
    "func": "spacewords",
    "src": "text",
    "dst": "nlp",
    "val": {
        "_id": "3l337",
        "text": [
            "The reign of Spain mainly affected the plains.",
            "The Juggalo Army occupied the state capital of Deleware, demanding twinkies.",
        ],
    },
}


# Initialize long term globals
app = FastAPI()

# Constants
VER = "/alphaville/"


async def grok():
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    print(json.dumps(f(config["src"], config["dst"], config["val"])))


# Test routes
@app.post("/eko")
async def eko(info: Request):
    req_info = await info.json()
    return {"status": "SUCCESS", "data": req_info}


@app.get(VER + "ekopath/{q}")
def eko_path(q: str):
    return q


@app.get(VER + "ekoqs")
def eko_qs(qs: str):
    return qs


@app.get(VER + "healz")
def health():
    """Health check"""
    return {"status": "healthy"}
