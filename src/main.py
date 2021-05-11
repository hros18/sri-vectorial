import sys
from text import *
from corpus import *

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

    tokenize(corpus)

    for doc in corpus.documents:
        doc.stemms = stemming(doc.tokens)
        doc.lemmas = lemmatizing(doc.tokens)
    for l in corpus.documents[0].lemmas:
        print('Lemmsa: {}'.format(l))
