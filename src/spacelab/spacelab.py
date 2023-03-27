import spacy
from spacytextblob.spacytextblob import SpacyTextBlob  # pylint: disable=unused-import

NLP = spacy.load("en_core_web_lg")
NLP.add_pipe("spacytextblob")


def ufo_to_blob(ufo: spacy.tokens.doc) -> dict:
    """Assign textblob properties polarity, subjectivity,
       sentiment_assessments and ents to spaCy NLP object.

    Args: result of running NLP() on text.

    Returns:
        Dictionary of polarity, subjectivity, sentiment_assessments
        & entities extracted from ufo text.
    """
    blob = {}
    blob["polarity"] = ufo._.blob.polarity
    blob["subjectivity"] = ufo._.blob.subjectivity
    blob["assesments"] = ufo._.blob.sentiment_assessments.assessments
    blob["ents"] = []
    for word in ufo.ents:
        blob["ents"].append({"word": word.text, "label": word.label_})
    return blob


def spacewords(text: str | list) -> str:
    """Run text through spacytextblob and return results.

    Args:
        text: What to process. Full sentence.

    Returns:
        Dictionary with fields populated with the results or processing text
    """
    if isinstance(text, str):
        return ufo_to_blob(NLP(text))
    else:
        out = []
        for sent in text:
            out.append(ufo_to_blob(NLP(sent)))
        return out


def loopback(src: str, dst: str, json_data: dict) -> dict:
    if isinstance(json_data[src], str):
        json_data[dst] = f"touché - {json_data[src]}"
    else:
        out = []
        for rec in json_data[src]:
            out.append(f"touché - {rec}")
        json_data[dst] = out
    return json_data
