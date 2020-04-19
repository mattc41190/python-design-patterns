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

my_book = Book('Silver Chair', 'C.S. Lewis', 15, publisher='harper')

print(my_book)
