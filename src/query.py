from corpus import Corpus
import math
import re

class Query:
    def __init__(self, idx=-1, words=""):
        self.idx = idx
        self.words = words
        self.tokens = []
        self.terms = {}
        self.lemmas = set()
        self.stemms = set()
        self.vector = []
        self.max_l = 1

    def tokenize(self):
        for t in re.split(r'\W+', self.words.replace('.', '')):
            if t != '':
                self.tokens.append(t)

    def update_weight_vector(self, corpus : Corpus, a=0.5):
        for t in corpus.terms:
            w = 0
            idf = 0
            if t in self.terms.keys():
                idf = self.terms[t]/ self.max_l
                if t in corpus.ni.keys():
                    w = (a + (1-a)*(idf))*math.log(len(corpus.documents)/corpus.ni[t])
            self.vector.append(w)

    def __str__(self):
        return """
            Id: {}\n
            Words: {}\n
        """.format(self.idx, self.words)
