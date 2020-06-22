# The writer of this exercise made this for more complicated than it needed to be...

class Publisher(object):
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer in self.observers:
            print('observer: {} already observing...'.format(observer))
        else:
            self.observers.append(observer)
    
    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print('observer: {} not being observed...'.format(observer))
    
    def notify(self):
        [o.notify(self) for o in self.observers]


# DefaultFormatter is the Publisher
class DefaultFormatter(Publisher):
    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0
    
    def __str__(self):
        return '{}: {} has data = {}'.format(
            type(self).__name__, 
            self.name,
            self._data 
        )
    
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as err:
            print(err)
            return
        
        self.notify()


# HexFormatter is a subscriber to Default Formatter
class HexFormatter(object):
    def notify(self, publisher):
        hex_value = hex(publisher.data)
        print('{}: {} now has hex value {}'.format(
            type(self).__name__,
            publisher.name, #  Actually this is the DefaultFormatter's name...
            hex_value
        ))

# BinaryFormatter is a subscriber to Default Formatter
class BinaryFormatter(object):
    def notify(self, publisher):
        binary_value = bin(publisher.data)
        print('{}: {} now has binary value {}'.format(
            type(self).__name__,
            publisher.name, #  Actually this is the DefaultFormatter's name...
            binary_value
        ))


def main():
    default_formatter = DefaultFormatter('test_1_name')
    print(default_formatter)

    print()
    hex_formatter = HexFormatter()
    default_formatter.add(hex_formatter)  # Couldn't either formatter add thw other? This is dumb!
    default_formatter.data = 21

    print()
    print(default_formatter)

    binary_formatter = BinaryFormatter()
    default_formatter.add(binary_formatter)
    default_formatter.data = 54

    print()
    print(default_formatter)

    default_formatter.remove(hex_formatter)

    default_formatter.data = 'hello'


    print()
    print(default_formatter)


if __name__ == '__main__':
    main()
