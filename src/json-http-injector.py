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
}


# Initialize long term globals
app = FastAPI()

# Constants
VER = "/alphaville/"


async def grok():
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    print(json.dumps(f(config["src"], config["dst"], config["val"])))


@app.post(VER + "inject")
async def reflect(info: Request):
    """Apply the current configuration to data

    Args:
        Post request in json dictionary format

    Returns:
        Dictionary with dst field containing the results of applying the function to src
    """
    req_info = await info.json()
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    return f(config["src"], config["dst"], req_info)


@app.get(VER + "_config")
async def get_config() -> dict:
    """Return current configuration

    Returns:
        Current configuration dictionary
    """
    return config


@app.post(VER + "_config")
async def post_config(new_config: dict) -> dict:
    """Set GLOBAL variable config

    Globals:
        config

    Returns:
        Configuration dictionary after update
    """
    global config  # pylint: disable=global-statement
    config = new_config
    return config


# Test routes
@app.post(VER + "eko")
async def eko(info: Request) -> dict:
    req_info = await info.json()
    return {"status": "SUCCESS", "data": req_info}


@app.get(VER + "ekopath/{q}")
def eko_path(q: str) -> str:
    return {"status": "SUCCESS", "data": q}


@app.get(VER + "ekoqs")
def eko_qs(qs: str) -> str:
    return {"status": "SUCCESS", "data": qs}


@app.get(VER + "healz")
def health() -> dict:
    """Health check"""
    return {"status": "healthy"}
