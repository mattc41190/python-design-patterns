import copy
from collections import OrderedDict

class Book(object):
    def __init__(self, name, authors, price, **rest):
        '''Book objects must have a name, authors, and price
        users may add k=v attrbiutes to the book as well'''

        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)
    
    def __str__(self):
        attrs = []
        ordered_book_attrs = OrderedDict(sorted(self.__dict__.items()))
        for key in ordered_book_attrs.keys():
            attrs.append('{}: {}'.format(key, ordered_book_attrs[key]))
            if key == 'price':
                attrs.append('$')
            attrs.append('\n')
        return ''.join(attrs)

class Prototype(object):
    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def deregister(self, identifier):
        del self.objects[identifier]
    
    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Not object found for identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj

def main():
    prototype = Prototype()

    b1 = Book(
        'The C Programming Language', 
        ('Brian W. Kernighan','Dennis M.Ritchie'), 
        price=118, 
        publisher='Prentice Hall', 
        length=228, 
        publication_date='1978-02-22', 
        tags=('C', 'programming', 'algorithms', 'data structures')
    )
    
    cid = 'k&r-first'

    prototype.register(cid, b1)

    b2 = prototype.clone(
        cid, 
        name='The C Programming Language (ANSI)', 
        price=48.99, 
        length=274, 
        publication_date='1988-04-01', 
        edition=2
    )

    for i in (b1, b2):
        print(i)
    
    print('ID b1: {} != ID b2: {}'.format(id(b1), id(b2)))


if __name__ == '__main__':
    main()