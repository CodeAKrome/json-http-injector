#!env python3
import importlib
from fastapi import FastAPI, Request
import uvicorn
import os
import requests

VER = "/v0/"

default_config = {
    "inject_libname": "lib.spacelab",
    "inject_func": "spacewords",
    "inject_src": "text",
    "inject_dst": "nlp",
    "inject_port": 31337,
    "inject_timeout": 3,
}

app = FastAPI()


def configure(new_config: dict) -> dict:
    ints = ["inject_port", "inject_timeout"]
    for key in new_config.keys():
        uppercase_key = key.upper()
        if uppercase_key in os.environ:
            if key in ints:
                new_config[key] = int(os.environ[uppercase_key])
            else:
                new_config[key] = os.environ[uppercase_key]
    if "inject_logfile" in new_config:
        new_config["log_fh"] = open(new_config["inject_logfile"], "a", encoding="utf-8")
    return new_config


def load_function(new_config: dict) -> dict:
    module = importlib.import_module(new_config["inject_libname"])
    new_config["function"] = getattr(module, new_config["inject_func"])
    return new_config


@app.get(VER + "configure")
async def get_config() -> dict:
    return config


@app.post(VER + "configure")
async def post_config(new_config: dict) -> dict:
    config = new_config
    return config


# ----- Exec Function -----


@app.put(VER + "f")
async def exec_function(req: Request):
    data = await req.json()
    return config["function"](data)


@app.post(VER + "f")
async def fwd(req: Request):
    data = await req.json()
    result = config["function"](data)
    if "inject_fwd" in config:
        ip = config["inject_fwd"]
    else:
        if "inject_fwd" in result:
            ip = data["inject_fwd"]
        else:
            raise ValueError("No forwarding address.")
    return requests.put(ip, data=result, timeout=config["inject_timeout"])


# ----- Logging -----


@app.post(VER + "log")
async def open_log(req: Request):
    logfile = await req.text()
    config["log_fh"] = open(logfile, "a", encoding="utf-8")
    config["inject_logfile"] = logfile
    return {"status": "ok", "logfile": config["inject_logfile"]}

# fix 
@app.put(VER + "log")
async def set_logging(req: Request):
    data = await req.json()
    config["log_fh"].flush()
    if "log" in data:
        config["log"] = data["log"]
    return {"status": "ok", "log": config["log"]}


@app.delete(VER + "log")
async def close_log():
    config["log_fh"].flush()
    config["log_fh"].close()  # pylint: disable=global-variable-not-assigned
    return {"status": "ok"}


# ----- Test -----


@app.get(VER + "health")
def eko_health() -> dict:
    return {"status": "ok"}


@app.post(VER + "eko")
async def eko_post(req: Request) -> dict:
    data = await req.json()
    return {"status": "ok", "data": data}


@app.get(VER + "ekopath/{data}")
def eko_pathdata(data: str) -> dict:
    return {"status": "ok", "data": data}


@app.get(VER + "ekoqs")
def eko_querystring(querystring: str) -> dict:
    return {"status": "ok", "data": querystring}


# ----- MAIN -----

if __name__ == "__main__":
    config = load_function(configure(default_config))
    uvicorn.run(app, host="0.0.0.0", port=config["inject_port"])
