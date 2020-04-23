import external

class Computer(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} computer'.format(self.name)
    
    def execute(self):
        return 'executes a program'

class Adapter(object):
    # All the juice is right here...
    # Not a great example IMO
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)
    
    def __str__(self):
        return str(self.obj)


def main():
    c  = Computer('Asus')
    synth = external.Synthesizer('moog')
    human = external.Human('Jeff')
    objects = [
        c, 
        Adapter(synth, dict(execute=synth.play)), # We "adapt" the play method to the execute method
        Adapter(human, dict(execute=human.speak)) # We "adapt" the speak method to the execute method
    ]

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

if __name__ == "__main__":
    main()




