from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

# The Gate class is a simple abstraction of an automatic gate door system
class Gate(object):

    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'
    
    def open(self):
        print('opening the gate...')
        self.is_open = True
    
    def close(self):
        print('closing the gaate...')
        self.is_open = False

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()

    tests = ('open -> gate')

    # did not finish because this is a very bad exercise... come on