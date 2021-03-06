class Document:
    
    def __init__(self, idx=-1, title="", author="", bookmark="", words=""):
        self.idx = idx
        self.title = title
        self.author = author
        self.bookmark = bookmark
        self.words = words
        self.tokens = []
        self.stemms = set()
        self.lemmas = set()
        self.terms = {}
        self.max_l = 1
        self.vector = []

    def __str__(self):
        return """
        Id: {}\n
        Title: {}\n
        Author: {}\n
        B: {}\n
        Words: {}\n
        """.format(self.idx, self.title, self.author, self.bookmark, self.words)
