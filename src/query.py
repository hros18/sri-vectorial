class Query:
    def __init__(self, idx=-1, words=""):
        self.idx = idx
        self.words = words
    def __str__(self):
        return """
            Id: {}\n
            Words: {}\n
        """.format(self.idx, self.words)
