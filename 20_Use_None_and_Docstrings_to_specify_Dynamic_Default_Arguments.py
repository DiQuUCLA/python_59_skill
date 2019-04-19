from datetime import datetime
import time
import json

def log(message, when=datetime.now()):
    print('%s: %s' % (when, message))

log('Hi there!')
time.sleep(0.1)
log('Hi again')

# The reason that it keeps using the same time every time you call it is because
# when the datetime.now will only be executed once, which is the time it's loaded
def log_when_None(message, when=None):
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))

log_when_None('Hi there!')
time.sleep(0.1)
log_when_None('Hi again')

# This evaluation order will cause some serious problem sometimes
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
print('Foo:', foo)
print('Bar:', bar)

# I guess the underlying structure is like when the module is loaded, it will just
# store the default value as a variable somewhere in the memory. Therefore, thie 
# memory is used over and over again

def decode_safe(data, default=None):
    default = {} if default is None else default
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode_safe('bad data')
foo['stuff'] = 5
bar = decode_safe('also bad')
print('Foo:', foo)
print('Bar:', bar)


