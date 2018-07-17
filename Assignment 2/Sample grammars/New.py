__author__ = 'alexanderkwok'

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

MICH = 'Michigan'
print(states)
print(MICH)
MICH = states[MICH]
print(MICH)
MICH = 'Michigan'
# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states[MICH])
print("Florida's abbreviation is: ", states['Florida'])
