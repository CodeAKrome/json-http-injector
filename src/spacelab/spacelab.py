import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import typing
"""Do polarity, subjectivity, sentiment_assessments, NER"""

NLP = spacy.load("en_core_web_lg")
NLP.add_pipe("spacytextblob")

def ufo_to_blob(ufo: spacy.tokens.doc.Doc) -> dict:
    """Assign textblob properties polarity, subjectivity, sentiment_assessments and ents to spaCy NLP object.
    
    Args: result of running NLP() on text.
    
    Returns:
        Dictionary of polarity, subjectivity, sentiment_assessments and entities extracted from ufo text.
    """
    blob = {}
    blob['polarity'] = ufo._.blob.polarity
    blob['subjectivity'] = ufo._.blob.subjectivity
    blob['assesments'] = ufo._.blob.sentiment_assessments.assessments
    blob['ents'] = []
    for word in ufo.ents:
        blob['ents'].append({'word': word.text, 'label': word.label_})
    return blob    

def spacewords(src: str, dst: str, json_data: dict) -> dict:
    """Run json_data[src] text through spacytextblob and add/replace json_data[dst] with the results.
    
    Args:
        src: name of top level field containing data to analize.
        dst: name of top level field to hold results of analysis.
        json_data: record into which data is to be inserted.
        
    Returns:
        Dictionary with dst field populated with the results of src field spacytextblob-ification
    """
    if isinstance(json_data[src], str):
        json_data[dst] = ufo_to_blob(NLP(json_data[src]))
    else:
        out = []
        for rec in json_data[src]:
            out.append(ufo_to_blob(NLP(rec)))
        json_data[dst] = out
    return json_data
    