from scanner import Scanner

class Parser:
    def __init__(self):
        self.sym = 0
        self.source = None
        self.scanner = None
    
    # expression = factor 
    # factor = term | term opr term
    # term = int
    def get_sym(self):
        for line in self.source:
            print(line)

    def read_file(self, file):
        with open(file) as source:
            self.source = source.readlines()
    
    def factor(self):
        ...
    
    def scan(self):
        ...
    
    def skip_blank(self):
        ...
    
    def expression(self):
        self.factor()