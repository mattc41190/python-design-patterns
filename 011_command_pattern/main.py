import os

Verbose = True

# RenameFile Command Class
class RenameFile(object):
    
    # State of the command
    def __init__(self, src, dest):
        self.src, self.dest = src, dest
    
    # The actual execution of the command
    def execute(self):
        if Verbose:
            print(f'renaming {self.src} to {self.dest}')
        os.rename(self.src, self.dest)
    
    # The ability to manage the command after the fact
    def undo(self):
        if Verbose:
            print(f'undoing rename of {self.src} to {self.dest}')
        os.rename(self.dest, self.src)


# Demonstration of how to not use the command pattern?
# It was in the book and I am fine pupil -- meh
def delete_file(path):
    if Verbose:
        print(f'deleting {path}')
    os.remove(path)


# CreateFile Command Class
class CreateFile(object):
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt
     
    def execute(self):
        if Verbose:
            print('creating file "{}"'.format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
    
    def undo(self):
        delete_file(self.path)

# ReadFile Command Class
class ReadFile(object):
    def __init__(self, path):
        self.path = path
    
    def execute(self):
        if Verbose:
            print('reading file {}'.format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as read_file:
            print(read_file, end='')

def main():
    orig_name, new_name = 'file1', 'file2'

    commands = [CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name)]

    for cmd in commands:
        cmd.execute()
    
    answer = input('reverse the executes commands? [y/n] ')

    if answer not in 'yY':
        print('the result is {}'.format(new_name))
        exit()
    
    for cmd in reversed(commands):
        try: 
            cmd.undo()
        except AttributeError as e:
            pass

if __name__ == '__main__':
    main()
