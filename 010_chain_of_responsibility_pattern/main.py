# A generic event type
class Event(object):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


# A generic widget (another word for Doo-Hickey).
# It implements the Chain of Command 
class Widget(object):
    def __init__(self, parent=None):
        self.parent = parent
    
    # The Chain of Command delegation lives here
    def handle(self, event: Event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)
        else:
            print('Fatal error no default handler...')
            exit(-1)


# Widget implementation
class MainWindow(Widget):
    def handle_close(self, event):
        print('{}: {}'.format(self, event))

    def handle_default(self, event):
        print('{} DEFAULT: {}'.format(self, event))

    def __str__(self):
        return 'MainWindow'


# Widget implementation
class SendDialog(Widget):
    def handle_paint(self, event):
        print('{}: {}'.format(self, event))

    def __str__(self):
        return 'SendDialog'


# Widget implementation
class MsgText(Widget):
    def handle_down(self, event):
        print('{}: {}'.format(self, event))

    def __str__(self):
        return 'MsgText'


# The application
def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for name in ('down', 'paint', 'unhandled', 'close'):
        event = Event(name)
        print('\nSending event -{}- to {}'.format(event, mw))
        mw.handle(event)
        print('\nSending event -{}- to {}'.format(event, sd))
        sd.handle(event)
        print('\nSending event -{}- to {}'.format(event, msg))
        msg.handle(event)


if __name__ == "__main__":
    main()
