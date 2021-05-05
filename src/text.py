import sys
import re
from document import Document
from query import Query
from corpus import Corpus

def tokenize(corpus : Corpus):
    for doc in corpus.documents:
        for t in re.split(r'\W+', doc.author):
            doc.tokens.add(t)
        for t in re.split(r'\W+', doc.title):
            doc.tokens.add(t)
        for t in re.split(r'\W+', doc.bookmark):
            doc.tokens.add(t)
        for t in re.split(r'\W+', doc.words):
            doc.tokens.add(t)
        break

def normalize():
    pass

def stemming():
    pass

def lemmatizing():
    pass

def delete_stopwords():
    pass

def parse_documents(path):
    states = ['.I', '.T', '.A', '.B', '.W']
    current_state = 0
    to_return = []
    f = open(path)
    lines = f.readlines()
    doc = None
    text = ""
    for line in lines:
        split = line.split(' ', 1)
        # print(split)
        head = split[0].split('\n')[0]
        rest = ""
        if len(split) > 1:
            rest = split[1].split('\n')[0]
        if head in states:
            current_state = (current_state + 1)
            if current_state == 6:
                current_state = 1
            if current_state == 1:
                if doc:
                    doc.words = text
                    text = ""
                    to_return.append(doc)
                doc = Document()
                doc.idx = rest
            elif current_state == 2:
                text += rest
            elif current_state == 3:
                doc.title = text
                text = rest
            elif current_state == 4:
                doc.author = text
                text = rest
            elif current_state == 5:
                doc.bookmark = text
                text = rest
        else:
            text += " " + line.split('\n')[0] 
    return to_return


def parse_querys(path):
    states = ['.I', '.W']
    current_state = 0
    to_return = []
    f = open(path)
    lines = f.readlines()
    query = None
    text = ""
    for line in lines:
        split = line.split(' ', 1)
        # print(split)
        head = split[0].split('\n')[0]
        rest = ""
        if len(split) > 1:
            rest = split[1].split('\n')[0]
        if head in states:
            current_state = (current_state + 1)
            if current_state == 3:
                current_state = 1
            if current_state == 1:
                if query:
                    query.words = text
                    text = ""
                    to_return.append(query)
                query = Query()
                query.idx = rest
            elif current_state == 2:
                text += rest
            
        else:
            text += " " + line.split('\n')[0] 
    return to_return

def parse_rel(path):
    pass
