# Adapter Pattern

## What is this?

The adapter pattern allows to to "adapt" an interface that may live outside fo your control to meet the criteria of an interface that you do control. 

There are many examples of this, think ports and adapters, but imagine you are building an application with a database and you want to swap one database out for another. If you were programming to an adaptable interface then swapping the database is simply a matter of writing the new database implementation to meet the spec that your application is already consuming from.

In the case presented here we have an application that wants to consume a variety of objects and invoke their functionality via the same method.

## How do I use this?

- Read the code in `main.py`
- Run the code in `main.py` (`python main.py`) 
- Observe output