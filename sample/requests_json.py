#!env python
import requests
url = "http://localhost:31337/alphaville/reflect"
data = {"text":"The reign of Spain mainly affected the plains."}
r = requests.post(url, json=data)
print(f"{r.json()}")
