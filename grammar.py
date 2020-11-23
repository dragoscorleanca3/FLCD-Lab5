'''
Created on Nov 23, 2020

@author: dragoscorleanca
'''
class Grammar:
    def __init__(self, filename):
        self.fileName = filename
        self.terminals = []
        self.non_terminals = []
        self.starting_symbol = None
        self.productions = []
        self.productions_dict = {}
    def read_in(self):
        f = open(self.fileName, 'r')
        no_of_terminals=int(f.readline()[0])

        for _ in range(no_of_terminals):
            self.terminals.append(f.readline()[:-1])
        
        no_of_non_terminals=int(f.readline()[0])
        

        for _ in range(no_of_non_terminals):
            self.non_terminals.append(f.readline()[:-1])
        
        self.starting_symbol = f.readline()[0]
        
        no_of_productions = int(f.readline()[:-1])
        
        
        for _ in range(no_of_productions):
            self.productions.append(f.readline()[:-1])
        
        
        print("terminals", self.terminals)
        
        print("non terminals", self.non_terminals)
        
        print("productions",self.productions)
        
        
        productions_dict = {}
        
        for nT in self.non_terminals:
            productions_dict[nT] = []
        
        
        print("productions_dict",productions_dict)
        
        for production in self.productions:
            nonterm_to_prod = production.split("->")
            alternatives = nonterm_to_prod[1].split("/")
            for alternative in alternatives:
                productions_dict[nonterm_to_prod[0]].append(alternative)
        
        print("productions_dict",productions_dict)
        
        
g = Grammar("grammar")
g.read_in()