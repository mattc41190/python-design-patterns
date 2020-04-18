import time
from enum import Enum 

PizzaProgress =  Enum('PizzaProgress', 'queued preperation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')

STEP_DELAY = 3

# Base Pizza Class
class Pizza(object):
    def __init__(self, name):
        self.name = name
        self.dough = None 
        self.sauce = None 
        self.toppings = []
    
    def __str__(self):
        return self.name
    
    def prepare_dough(self, dough):
        self.dough = dough 
        print('preparing the {} dough of your {}...'.format(
            self.dough.name,
            self
        ))
        time.sleep(STEP_DELAY)
        print('done preparing the {} dough...'.format(self.dough.name))


# Below are two very ham fisted example of creating pizza builders... 

# Margarita Pizza Builder
class MargaritaBuilder(object):
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preperation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        sauce = PizzaSauce.tomato
        print('adding {} sauce to your {} pizza...'.format(sauce, self.pizza))
        self.pizza.sauce = sauce
        time.sleep(STEP_DELAY)
        print('done adding {} to your {} pizza'.format(self.pizza.sauce, self.pizza))
    
    def add_topping(self):
        toppings = [PizzaTopping.double_mozzarella.name, PizzaTopping.oregano.name]
        print('adding toppings {} to your {} pizza...'.format(toppings, self.pizza))
        self.pizza.toppings = toppings
        time.sleep(STEP_DELAY)
        print('done adding toppings {} to your {} pizza...'.format(toppings, self.pizza))

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your {} pizza for {} seconds...'.format(self.pizza, self.baking_time))
        time.sleep(self.baking_time)
        print('done baking your {} pizza for {} seconds...'.format(self.pizza, self.baking_time))
        self.progress = PizzaProgress.ready
        print('your {} pizza is ready...'.format(self.pizza))

# Creamy Bacon Pizza Builder
class CreamyBaconBuilder(object):
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preperation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        sauce = PizzaSauce.creme_fraiche
        print('adding {} sauce to your {} pizza...'.format(sauce, self.pizza))
        self.pizza.sauce = sauce
        time.sleep(STEP_DELAY)
        print('done adding {} to your {} pizza'.format(self.pizza.sauce, self.pizza))
    
    def add_topping(self):
        toppings = [PizzaTopping.mozzarella.name,
            PizzaTopping.bacon.name,
            PizzaTopping.ham.name,
            PizzaTopping.mushrooms.name,
            PizzaTopping.red_onion.name,
            PizzaTopping.oregano.name
        ]
        print('adding toppings {} to your {} pizza...'.format(toppings, self.pizza))
        self.pizza.toppings = toppings
        time.sleep(STEP_DELAY)
        print('done adding toppings {} to your {} pizza...'.format(toppings, self.pizza))

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your {} pizza for {} seconds...'.format(self.pizza, self.baking_time))
        time.sleep(self.baking_time)
        print('done baking your {} pizza for {} seconds...'.format(self.pizza, self.baking_time))
        self.progress = PizzaProgress.ready
        print('your {} pizza is ready...'.format(self.pizza))


class Waiter(object):
    def __init__(self):
        self.builder = None
    
    def construct_pizza(self, builder):
        self.builder = builder
        
        steps = [builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake
        ]

        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [m]argarita or [c]reamy bacon? ')
        builder = builders[pizza_style]()
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)

    valid_input = False 
    while not valid_input:
        valid_input, builder = validate_style(builders)

    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print('\nEnjoy your {} pizza...'.format(pizza))


if __name__ == "__main__":
    main()
