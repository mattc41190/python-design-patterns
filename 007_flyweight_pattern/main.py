import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree(object):
    # Static member
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)  # From the cls passed in - either get a value from the pool or default to None
        if not obj:
            obj = object.__new__(cls)  # new up the class forcefully by means of calling object.__new__
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj
    
    def render(self, age, x, y):
        print('rendering tree or type {} of age {} at coordinates x:{} y:{}'.format(
            self.tree_type,
            age,
            x,
            y
        ))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range (10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(
            rnd.randint(age_min, age_max),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point)
        )
        tree_counter += 1

    for _ in range (4):
        t2 = Tree(TreeType.peach_tree)
        t2.render(
            rnd.randint(age_min, age_max),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point)
        )
        tree_counter += 1

    for _ in range (7):
        t3 = Tree(TreeType.cherry_tree)
        t3.render(
            rnd.randint(age_min, age_max),
            rnd.randint(min_point, max_point),
            rnd.randint(min_point, max_point)
        )
        tree_counter += 1
    
    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))  # pool is referenced as a static member
    
    # To further illustrate this point
    t4 = Tree(TreeType.cherry_tree) 
    t5 = Tree(TreeType.cherry_tree) 
    t6 = Tree(TreeType.apple_tree) 

    print("t4({}) is equal to t5({}): {}".format(id(t4), id(t5), id(t4) == id(t5)))
    print("t4({}) is equal to t6({}): {}".format(id(t4), id(t6), id(t4) == id(t6)))


if __name__ == "__main__":
    main()