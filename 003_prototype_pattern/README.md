# Prototype Pattern

## What is this?

This is a demonstration of the prototype object creation pattern in Python.

the prototype pattern is used to create objects based on other objects. I.e. cloning objects.

Using a deeply copied prototype pattern we can maintain a chain of clones while not affecting the prototype. 

A good example is recipes sharing software.

Ex:

- Bob finds a recipe on recipes.com
- He makes it and decides it can be improved 
- He copies recipe, maintaining a reference to the original recipe while at the same time so that the original can always be found even as it independently evolves over time.
- He modifies his local copy and loves the new flavor
- Sarah finds Bobs recipe, decides _it_ can be improved and copies it.
- Now Sarah's recipes refs Bob's, and Bob's ref the original; however all three are still allowed to grow independently of each other.

__Note: Maintaining reference is something I did to demonstrate the relationship between the prototypes. IT is not required. All that is required is that the object be copied either deeply or shallowly.__

## How do I use this?

- Read the code in `main.py`
- Run the code in `main.py` (`python main.py`) 
- Observe output