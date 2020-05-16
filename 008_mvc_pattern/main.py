quotes = ('A man is not complete until he is married. Then he is finished.', 
    'As I said before, I never repeat myself.', 
    'Behind a successful man is an exhausted woman.', 
    'Black holes really suck...', 
    'Facts are stubborn things.'
)

# Model
class QuoteModel(object):
    def get(self, index):
        try:
            value = quotes[index]
        except IndexError as err:
            value = 'Not found!'
        return value

# View
class TerminalView(object):
    def show(self, quote):
        print(quote)

    def select_quote(self):
        index = input('Which quote would you like to see: ')
        return index

    def error(self, msg):
        print(msg)

# Controller 
class QuoteTerminalController(object):
    def __init__(self):
        self.model = QuoteModel()
        self.view = TerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            index = self.view.select_quote()
            try:
                index = int(index)
            except Exception as err:
                self.view.error('dats no good...')
                continue
            
            valid_input = True
        quote = self.model.get(index)
        self.view.show(quote)

# App
def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == "__main__":
    main()