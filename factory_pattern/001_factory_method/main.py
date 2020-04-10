# In the Factory Method, we execute a single function, passing a parameter that provides information about what we want. 

import xml.etree.ElementTree as etree
import json

class JSONConnector(object):
	def __init__(self, fp):
		self.data = dict()
		with open(fp, mode='r', encoding='utf-8') as f:
			self.data = json.load(f)
	
	@property
	def parsed_data(self):
		return self.data

class XMLConnector(object):
	def __init__(self, fp):
		self.data = etree.parse(fp)
	
	@property
	def parsed_data(self):
		return self.data


def connection_factory(fp):
	if fp.endswith('.json'):
		connector = JSONConnector
	elif fp.endswith('.xml'):
		connector = XMLConnector
	else:
		raise ValueError('Cannot connect to {}'.format(fp))
	
	return connector(fp)


def connect_to(fp):
	factory = None
	try:
		factory = connection_factory(fp)
	except ValueError as ve:
		print(ve)
	return factory

def handle_persons_xml(persons):
	liars = persons.findall(".//{}[{}='{}']".format(
	'person',
	'lastName',
	'Liar'))

	print('Liars:')

	for liar in liars:
		nums = list(map(
			lambda num: '{}: {}'.format(num.attrib['type'], num.text), 
			liar.find('phoneNumbers'))
		)

		print('First Name: {}, Last Name: {}, Phone Number(s) {}'.format(
			liar.find('firstName').text,
			liar.find('lastName').text,
			', '.join(nums)
		))

def handle_donuts_json(donuts):
	for donut in donuts:
		print(donut['name'].upper())
		print('\tPrice: {}'.format(donut['ppu']))
		[print('\t\tTopping: {}'.format(topping['type'])) for topping in donut['topping']]

def main():
	sqlite_factory = connect_to('not_here.sq3')
	print()

	xml_factory = connect_to('./persons.xml')
	persons = xml_factory.parsed_data
	handle_persons_xml(persons)

	json_factory = connect_to('./donut.json')
	donuts = json_factory.parsed_data
	handle_donuts_json(donuts)

if __name__ == "__main__":
		main()