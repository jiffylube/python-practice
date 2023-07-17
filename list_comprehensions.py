# offers shorter syntax when creating a list based on existing lists

# example:

fruits = ['apples', 'bananas', 'oranges', 'kiwis', 'olives']
newList = []

for i in fruits:
    newList.append(i)
print(newList)

# the same can also be achieved with a list comprehension

comprehensionList = [i for i in fruits]
print(comprehensionList)

# syntax explaination :
# new_list = [ expression for item in iterable if condition ]

# lets say we want to return a new list of fruits that contains an expression

iList = [i for i in fruits if i.startswith('o')]
print(iList)

# can also do operands and booleans
# return if length of fruit is > 5

over5 = [i for i in fruits if len(i) > 5]
print(over5)
