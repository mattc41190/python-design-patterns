# Insecure Class
class SensitiveInfo(object):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']
    
    def read(self):
        print('There are {} users, {}'.format(len(self.users), self.users))
    
    def add(self, user):
        self.users.append(user)
        print('added user: {}'.format(user))

# Secure Proxy Class
class Info(object):
    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'
    
    def read(self):
        self.protected.read()
    
    def add(self, name):
        password = input('Password: ')
        if password == self.secret:
            self.protected.add(name)
        else:
            print('incorrect password')

# Application
def main():
    info = Info() 

    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
           info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option')
        
if __name__ == "__main__":
    main()