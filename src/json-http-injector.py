#!env python
import importlib

config = {
    "libname": "spacelab.spacelab",
    "func": "test",
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

m = importlib.import_module(config["libname"])
f = getattr(m, config["func"])
print(f(config["src"], config["dst"], config["val"]))
