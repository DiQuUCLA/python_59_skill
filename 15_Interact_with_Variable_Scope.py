# In the helper function helper, defined inside sort_priority
# It's able to see the input variable group when it needs to use it
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

# However, if you assign value to a variable inside helper function,
# Which is defined outside, it will think you are define a new variable
# in inner function
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1,x)
    numbers.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
found = sort_priority2(numbers, group)
print('Found: ', found)
print(numbers)

"""
Order to find a variable when it is referenced
1. Current function scope
2. Any enclosing scops (like other containing functions)
3. The scope of the module that contains the code (global scope)
4. The built-in scope (the scope that contains functions like len and str)
"""

# we can introduce the variable in inner scope with nonlocal
def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
found = sort_priority2(numbers, group)
print('Found: ', found)
print(numbers)

# However, nonlocal doesn't exist in python2
# so we can use list as wrapper

def sort_priority_p2(numbers, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found[0]

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
found = sort_priority2(numbers, group)
print('Found: ', found)
print(numbers)

