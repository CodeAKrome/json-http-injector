#!env python
import pytest
from src.spacelab.spacelab import loopback, spacewords

rec = {"text": "The bubble-headed booby said it was horrible that Freedonia had annexed Communicado to the Ninny."}
res_test = {'text': 'The bubble-headed booby said it was horrible that Freedonia had annexed Communicado to the Ninny.', 'nlp': 'touché - The bubble-headed booby said it was horrible that Freedonia had annexed Communicado to the Ninny.'}
res_spacewords = {'text': 'The bubble-headed booby said it was horrible that Freedonia had annexed Communicado to the Ninny.', 'nlp': {'polarity': -1.0, 'subjectivity': 1.0, 'assesments': [(['horrible'], -1.0, 1.0, None)], 'ents': [{'word': 'Freedonia', 'label': 'GPE'}, {'word': 'Communicado', 'label': 'ORG'}, {'word': 'Ninny', 'label': 'PERSON'}]}}
src = "text"
dst = "nlp"

def test_loopback():
    res = loopback(src, dst, rec)
    assert res == res_test
    
def test_spacewords():
    res = spacewords(src, dst, rec)
    assert res == res_spacewords