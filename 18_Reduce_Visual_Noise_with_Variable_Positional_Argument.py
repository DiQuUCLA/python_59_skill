def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log('My numbers are', [1, 2])
log('Hi there', [])

# However, the above implementaion requires you to type [] as the second parameter.
# Seemes not beautiful if you are writing something like API

def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
log('My numbers are', [1, 2])
log('Hi there')

# Two issue of it:
# It forms all of the variables into a tuple
# It's bad for generator cause you use generator because you don't really want them in you memory

def my_generator():
    for i in range(10):
        yield i
it = my_generator()
def my_func(*args):
    print(args)

my_func(*it)

# The second issue:
# You can't add any more positional variable after it
