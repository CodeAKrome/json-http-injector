# json-http-injector
# :skull: ** Danger Will Robinson, danger! **

## Gamma code, Reality level: 64:1 against, and falling. Under no circumstances use this for anything ... yet.

## Inject data into a json encoded http data stream using local or network python modules which may be used to shim 3rd party REST APIs.

## Status

```sh
curl http://localhost:8000/alphaville/healz
```

```text
{"status":"healthy"}
```

Currently copying over code to support [SpaCy](https://spacy.io/) [spacytextblob](https://spacy.io/universe/project/spacy-textblob)

## Sample

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

