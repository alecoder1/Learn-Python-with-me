""" for loop iterate over a collection of items such as list or dict"""

for i in [0, 1, 2, 3, 4]:
    print(i)


""" range is a fucntion that returns a series of numbers under an iterable form"""

for i in range(5):
    print(i)
"""Note: 5 is not printed as the range here is the first five numbers counting
    from 0"""


"""ITERATING OVER LISTS USING FOR LOOPS"""

for x in ['one', 'two', 'three', 'four']:
    print(x)



for x in range(1, 6):
    print(x)


"""Loop through elements of a list and have index for elements as well using enumerate function"""

for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)



"""Iterating over a list with value manipulation using map and lambda:
    Apply lambda function on each element in the list"""


x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

"""In python 3.x map returns an iterator instead of a list so incase you
    eed a list you have to cast the result print(list(x))"""