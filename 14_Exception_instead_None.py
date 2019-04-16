def divide_with_None(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

result = divide_with_None(3, 0)
if result is None:
    print('Invalid inputs')

def divide_with_exception(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inpputs') from e

try:
    result = divide_with_exception(5, 0)
except ValueError:
    print('Invalid Inputs')
else:
    print('Result is %.1f' % result)


