#!env python
import requests
url = "http://localhost:31337/alphaville/reflect"
experience = [
    {"text":"Freedonia, that country of cowards, led by Rufus T. Firefly, has committed a dastardly deed by cravenly surendering to the Librarian's Assc. of Communicado."},
    {"text":["The reign of Spain mainly affected the plains.", "The Juggalo Army occupied the state capital of Deleware, demanding twinkies."]},
]
for data in experience:
    r = requests.post(url, json=data)
    print(f"{r.json()}")
    
