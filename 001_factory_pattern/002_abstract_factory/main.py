class Frog(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name
	
	def interact_with(self, obstacle):
		print('{} the Frog interacts with {} and {}!'.format(
			self,
			obstacle,
			obstacle.action()
		))

class Bug(object):
	def __str__(self):
		return 'a bug'
	
	def action(self):
		return 'eats it'

class FrogWorld(object):
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return '\n\n\t---------- Frog World ----------'
	
	def make_character(self):
		return Frog(self.player_name)
	
	def make_obstacle(self):
		return Bug()

class Wizard(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		print('{} the wizard interacts with {} and {}!'.format(
			self, 
			obstacle,
			obstacle.action()
		))

class Ork(object):
	def __str__(self):
		return 'an ork'
	
	def action(self):
		return 'kills it'

class WizardWorld(object):
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return '\n\n\t---------- Wizard World ----------'
	
	def make_character(self):
		return Wizard(self.player_name)

	def make_obstacle(self):
		return Ork()
	
class GameEnvironment(object):
	def __init__(self, factory):
		self.hero = factory.make_character()
		self.obstacle = factory.make_obstacle()
	
	def play(self):
		self.hero.interact_with(self.obstacle)

def validate_input(name):
	try:
		age = input('Welcome {}, how old are you? '.format(name))
		age = int(age)
	except ValueErr as err:
		print('Age {} is invalid, please try again...'.format(age))
		return (False, age)
	return (True, age)

def main():
	name = input('Please enter your name: ')
	valid_age = False
	while not valid_age:
		valid_age, age = validate_input(name)
	
	game = FrogWorld if age < 17 else WizardWorld
	env = GameEnvironment(game(name))
	env.play()

if __name__ == "__main__":
		main()



