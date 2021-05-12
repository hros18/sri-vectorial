import sys
import re
from document import Document
from query import Query
from corpus import Corpus
from nltk import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from spacy.lang.en.stop_words import STOP_WORDS

lemmatizer = WordNetLemmatizer()

def tokenize(corpus : Corpus):
    for doc in corpus.documents:
        for t in re.split(r'\W+', doc.title.replace('.', '')):
            if t != '':
                doc.tokens.append(t)
        for t in re.split(r'\W+', doc.author.replace('.', '')):
            if t != '':
                doc.tokens.append(t)
        for t in re.split(r'\W+', doc.title.replace('.', '')):
            if t != '':
                doc.tokens.append(t)
        for t in re.split(r'\W+', doc.bookmark.replace('.', '')):
            if t != '':
                doc.tokens.append(t)
        for t in re.split(r'\W+', doc.words.replace('.', '')):
            if t != '':
                doc.tokens.append(t)

def normalize(corpus : Corpus):
    tokenize(corpus)
    # stemming(corpus)
    lemmatizing(corpus)

def stemming(corpus):
    for doc in corpus.documents:
        snowball = SnowballStemmer(language='english')
        for t in doc.tokens:
            p = snowball.stem(t)
            if not p in STOP_WORDS:
                if not p in doc.terms.keys():
                    doc.terms.update({p: 1})
                else:
                    doc.terms[p] += 1
                doc.max_l = max(doc.max_l, doc.terms[p])
                doc.stemms.add(p)
    

def lemmatizing(corpus):
    for doc in corpus.documents:
        for t in doc.tokens:
            term = lemmatizer.lemmatize(t)
            if not term in STOP_WORDS:
                if not term in doc.terms.keys():
                    doc.terms.update({term: 1})
                else:
                    doc.terms[term] += 1
                doc.lemmas.add(term)

def normalize_query(query : Query):
    # stemming_query(query)
    lemmatizing_query(query)

def stemming_query(query):
    snowball = SnowballStemmer(language='english')
    for t in query.tokens:
        p = snowball.stem(t)
        if not p in STOP_WORDS:
            if not p in query.terms.keys():
                query.terms.update({p: 1})
            else:
                query.terms[p] += 1
            query.max_l = max(query.max_l, query.terms[p])
            query.stemms.add(p)
    

def lemmatizing_query(query):
    for t in query.tokens:
        term = lemmatizer.lemmatize(t)
        if not term in STOP_WORDS:
            if not term in query.terms.keys():
                query.terms.update({term: 1})
            else:
                query.terms[term] += 1
            query.lemmas.add(term)
    # return to_return
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
