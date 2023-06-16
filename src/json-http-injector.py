#!env python3
import importlib
import json
from fastapi import FastAPI, Request
import uvicorn
import os
import requests

# Constants
VER = "/v0/"

# TEST CODE -- DANGER!

# reflection_url is another copy of this code running on port 31337 for debugging
config = {
    "libname": "spacelab.spacelab",
    "func": "spacewords",
    "src": "text",
    "dst": "nlp",
    "opensearch": "https://localhost:9200/_bulk",
    "logfile": "ner_log.txt",
    "reflection_url": "http://localhost:31337" + VER + "log/eko",
    "port": 31337,
    "timeout": 3,
}


# Initialize long term globals
app = FastAPI()
log = open(config["logfile"], "a", encoding="utf-8")


async def grok():
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    #print(json.dumps(f(config["src"], config["dst"], config["val"])))
    return {"test": f"m {type(m)} f {type(f)}"}


@app.post(VER + "map")
async def reflect(info: Request):
    req_info = await info.json()
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    req_info[config["dst"]] = f(req_info[config["src"]])
    return req_info


@app.post(VER + "reflection")
async def reflection(info: Request):
    """Assume there's another copy of this running on the reflection port

    Args:
        Post request in json dictionary format

    Returns:
        Dictionary with dst field containing the results of applying the function to src
    """
    req_info = await info.json()
    m = importlib.import_module(config["libname"])
    f = getattr(m, config["func"])
    rec = f(config["src"], config["dst"], req_info)
    r = requests.put(config["reflection_url"], data=rec, timeout=config["timeout"])
    return r


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


# Logging routes
@app.post(VER + "/log/close")
async def log_close():
    global log  # pylint: disable=global-statement disable=global-variable-not-assigned
    log.close()  # pylint: disable=global-variable-not-assigned
    return {"status": "ok"}


# test this
@app.post(VER + "/log/open")
async def log_open():
    global log  # pylint: disable=global-statement
    log = open(config["logfile"], "a", encoding="utf-8")
    return {"status": "ok"}


@app.post(VER + "/log/eko")
async def log_eko(info: Request):
    req_info = await info.json()
    log.write(f"{json.dumps(req_info)}\n")
    log.flush()
    return {"status": "ok"}


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


if __name__ == "__main__":
    if "APP_PORT" in os.environ:
        uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APP_PORT")))
    else:
        uvicorn.run(app, host="0.0.0.0", port=config["port"])
