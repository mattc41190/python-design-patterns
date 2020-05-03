from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restarting zombie')

class User(object):
    pass

class Process(object):
    pass

class File(object):
    pass

class Server(metaclass=ABCMeta):
    '''abstart server interface that all concrete servers must implement'''
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name
    
    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass

class FileServer(Server):
    '''server responsible for creating and destroying files'''

    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting server: {}...'.format(self.name))
        self.state = State.running

    def kill(self, restart=True):
        print('killing server: {}...'.format(self.name))
        self.state = State.restart if restart else State.zombie

    def create_file(self, file_name, user, permissions):
        '''create a file with a new and extension for a user'''
        print('trying to create the file {} for user {} with permissions {}'.format(file_name, user, permissions))

class ProcessServer(Server):
    '''server responsible for creating and destroying processes'''

    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting server: {}...'.format(self.name))
        self.state = State.running

    def kill(self, restart=True):
        print('killing server: {}...'.format(self.name))
        self.state = State.restart if restart else State.zombie

    def create_process(self, process_name, user):
        '''check user rights, generate PID, etc.'''
        print('trying to create the process {} for user {}'.format(process_name, user))

class WindowServer(object):
    pass

class NetworkServer(object):
    pass

class OperatingSystem(object):
    '''Facade over several independent but complementary services'''

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    
    def start(self):
        [server.boot() for server in (self.ps, self.fs)]


    def create_file(self, file_name, user, permissions):
        return self.fs.create_file(file_name, user, permissions)

    def create_process(self, process_name, user):
        return self.ps.create_process(process_name, user)
    

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('hello.txt', 'matt', '-rw-r-r')
    os.create_process('ls /tmp', 'ariel')

if __name__ == "__main__":
    main()
    