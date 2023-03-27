# json-http-injector

[![Alphaville](https://github.com/CodeAKrome/json-http-injector/actions/workflows/main.yml/badge.svg)](https://github.com/CodeAKrome/json-http-injector/actions/workflows/main.yml)

# Version: ![alphaville](https://user-images.githubusercontent.com/44734955/227808001-3c82808d-3909-488a-bb6f-385c8c19edb8.png)
## Inject data into a json encoded http data stream using local or network python modules which may be used to shim 3rd party REST APIs.

## :skull: ** Danger Will Robinson, danger! **

## Gamma code, Reality level: 64:1 against, and falling. Under no circumstances use this for anything ... yet.

## Curl problem
Curl doesn't return the same values as python's requests library. Instead of `None` it returns `null` as one of the `assesments` values.

### E.g.

```sh
sample/curl_json.sh
```

```text
{"text":"The reign of Spain mainly affected the plains.","nlp":{"polarity":0.16666666666666666,"subjectivity":0.3333333333333333,"assesments":[[["mainly"],0.16666666666666666,0.3333333333333333,null]],"ents":[{"word":"Spain","label":"GPE"}]}}
```

```sh
sample/requests_json.py
```

```text
{"text": "The reign of Spain mainly affected the plains.", "nlp": {"polarity": 0.16666666666666666, "subjectivity": 0.3333333333333333, "assesments": [[["mainly"], 0.16666666666666666, 0.3333333333333333, null]], "ents": [{"word": "Spain", "label": "GPE"}]}}
```


## Lab notes

Currently copying over code to support [SpaCy](https://spacy.io/) [spacytextblob](https://spacy.io/universe/project/spacy-textblob)

### Testing

```zsh
function jpcurl {
    curl -H "Accept: application/json" -H "Content-Type: application/json" -X POST -d $2 $1
}
```

```sh
curl http://localhost:31337/alphaville/healz
```

```text
{"status":"healthy"}
```

```sh
jpcurl http://localhost:31337/alphaville/reflect "{\"text\":\"Freedonia, that country of cowards, led by Rufus T. Firefly, has committed a dastardly deed by cravenly surendering to the Librarian's Assc. of Communicado.\"}"
```

```json
{"text":"Freedonia, that country of cowards, led by Rufus T. Firefly, has committed a dastardly deed by cravenly surendering to the Librarian's Assc. of Communicado.","nlp":{"polarity":0.0,"subjectivity":0.0,"assesments":[],"ents":[{"word":"Freedonia","label":"GPE"},{"word":"Rufus T. Firefly","label":"PERSON"},{"word":"Communicado","label":"ORG"}]}}
```


###  Sample

### configuration:

```python
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
```

### input:

```json
{"_id": "3l337", "text": ["The reign of Spain mainly affected the plains.", "The Juggalo Army occupied the state capital of Deleware, demanding twinkies."]}
```

### output:

```json
{"_id": "3l337", "text": ["The reign of Spain mainly affected the plains.", "The Juggalo Army occupied the state capital of Deleware, demanding twinkies."], "nlp": [{"polarity": 0.16666666666666666, "subjectivity": 0.3333333333333333, "assesments": [[["mainly"], 0.16666666666666666, 0.3333333333333333, null]], "ents": [{"word": "Spain", "label": "GPE"}]}, {"polarity": 0.0, "subjectivity": 0.0, "assesments": [], "ents": [{"word": "The Juggalo Army", "label": "ORG"}, {"word": "Deleware", "label": "PRODUCT"}]}]}
```

