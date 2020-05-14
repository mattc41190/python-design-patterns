# Flyweight Pattern

## What is this?

The flyweight pattern allows you to create several items based on the same object. It is used when you need to preserve memory and have lots of highly similar generally static objects.

In this scenario we create several tree renders, but actually on ever create 3 tree objects. We just "reuse" their representation.

Somethings we see in this example are usages of `__new__` and `Enum`

## How do I use this?

- Read the code in `main.py`
- Run the code in `main.py` (`python main.py`) 
- Observe output

## Resources

- https://realpython.com/python-metaclasses/