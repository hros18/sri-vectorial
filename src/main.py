import sys
from text import *
from corpus import *
import math

def metrics(vector_a, vector_b):
    suma = 0
    squares_a = 0
    squares_b = 0
    for i in range(len(vector_a)):
        suma += vector_a[i] * vector_b[i]
        squares_a += vector_a[i]**2
        squares_b += vector_b[i]**2
    return suma / (math.sqrt(squares_a)*math.sqrt(squares_b))

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Missing arguments')
        print('main.py <documents_path> <query_path> <rel_path>')
        exit(1)
    documents_path = sys.argv[1]
    query_path = sys.argv[2]
    rel_path = sys.argv[3]

    #todo process files
    docs = parse_documents(documents_path)

    queries = parse_querys(query_path)

    corpus = Corpus(docs)

    normalize(corpus)

    corpus.update_global_terms()
    corpus.update_weight_vectors()

    result = []

    for q in queries:
        q.tokenize()
        normalize_query(q)
        q.update_weight_vector(corpus)
        for doc in corpus.documents:
            value = metrics(q.vector, doc.vector)
            if doc.idx:
                print('Q {}: Doc {} Res: {}'.format(q.idx, doc.idx, value))
        break

    

    # print(corpus.documents[0].vector)
    # for doc in corpus.documents:
    #     doc.stemms = stemming(doc.tokens)
    #     doc.lemmas = lemmatizing(doc.tokens)
    # for l in corpus.documents[0].lemmas:
    #     print('Lemmsa: {}'.format(l))
