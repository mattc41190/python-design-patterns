# Command Pattern

## What is it?

The command pattern is a means of encapsulating commands as objects that are capable of performing the action specified in the command. This is a valuable pattern for several reasons. The book I am reading _Mastering Python Design Patterns_ talks at length about how this principle make the "undo" action possible. By containing command as objects you can preserve a history of what the client asked for and can therefore preserve a chain of commands that can potentially preserve the history of all action taken in the program.

## How do I use this?

- Read the code `cat main.py`
- Run the code `python main.py`
- Observe the output 