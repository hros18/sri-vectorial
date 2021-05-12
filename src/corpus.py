import math

class Corpus:
    def __init__(self, documents):
        self.documents = documents
        self.terms = {}
        self.ni = {}

    def update_global_terms(self):
        for doc in self.documents:
            for key in doc.terms.keys():
                value = doc.terms[key]
                if not key in self.terms.keys():
                    self.terms.update({ key: value})
                else:
                    self.terms[key] += value 
                if not key in self.ni.keys():
                    self.ni.update({ key: 1})
                else:
                    self.ni[key] += 1
    
    def update_weight_vectors(self):
        for doc in self.documents:
            for t in self.terms.keys():
                tf = 0
                if t in doc.terms.keys():
                    tf = doc.terms[t] / doc.max_l
                idf = 0
                if t in self.ni.keys():
                    idf = math.log(len(self.documents)/self.ni[t])
                w = tf * idf
                doc.vector.append(w)
