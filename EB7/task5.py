"""
Given a list of dictionaries, each representing a person with 'name' and 'age' keys, 
use lambda functions to filter out people under 18 and then map the remaining people's 
names to a new list.
"""

# my_people = [{"name" : "Hari", "age" : 25},
#              {"name" : "Ram", "age" : 17},
#              {"name" : "Sham", "age" : 19}]


# adult = list(filter(lambda people : people['age'] >= 18, my_people))
# print(adult)

# non_adult = list(filter(lambda people : people['age'] < 18, my_people))
# print(non_adult)

# names = list(map(lambda people : people['name'], non_adult))
# print(names)


"""
2. Using lambda reduce to get the product of all numbers in a list
"""

from functools import reduce

my_list = [2, 4, 5, 6]

product = reduce(lambda x,  y : x * y, my_list)
print(product)

