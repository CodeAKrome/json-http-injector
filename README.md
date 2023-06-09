# micro-gp

# FastAPI based microservice using dyna-loaded libraries to perform operations on JSON encoded data with optional HTTP result forwarding.

## Version: v0

## :skull: **Danger Will Robinson, danger!**

## Gamma code, Reality level: 64:1 against, and falling. Under no circumstances use this for anything ... yet

## FYI

Json doesn't return the same values as python's print command. Instead of `None` it returns `null` as one of the `assesments` values. This will cause issues if you, as I, try to cut and paste things.

### Exempli Gratia

```sh
sample/curl_json.sh
```

```text
{"text":"The reign of Spain mainly affected the plains.","nlp":{"polarity":0.16666666666666666,"subjectivity":0.3333333333333333,"assesments":[[["mainly"],0.16666666666666666,0.3333333333333333,null]],"ents":[{"word":"Spain","label":"GPE"}]}}
```

Pretty JSON

```json
{
   "nlp" : {
      "assesments" : [
         [
            [
               "mainly"
            ],
            0.166666666666667,
            0.333333333333333,
            null
         ]
      ],
      "ents" : [
         {
            "label" : "GPE",
            "word" : "Spain"
         }
      ],
      "polarity" : 0.166666666666667,
      "subjectivity" : 0.333333333333333
   },
   "text" : "The reign of Spain mainly affected the plains."
}
```

I can't show a python `json_pp` example because, aside from complaining about single quotes, it rejects `None` as a valid value. Simply be aware.

```sh
sample/requests_json.py
```

```json
{'text': 'The reign of Spain mainly affected the plains.', 'nlp': {'polarity': 0.16666666666666666, 'subjectivity': 0.3333333333333333, 'assesments': [[['mainly'], 0.16666666666666666, 0.3333333333333333, None]], 'ents': [{'word': 'Spain', 'label': 'GPE'}]}}
```

## Lab notes

Containerization begins.

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
