def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('my_file.txt')
percentages = normalize(it)
print(percentages) # This will return []

'''
The reason is that the line:
    sum(numbers)
has runs out the generator
So it will yields nothing after this line
'''

# Use a function that will return a generator instead

def normalize_func(get_iter):
    total = sum(get_iter()) #return a new iterator
    result = []
    for value in get_iter():
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits('my_file.txt'))
print(percentages)

# Or we can write a iterator protocol: a container
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits('my_file.txt')
percentages = normalize(visits)
print(percentages)

# To make our function defensive to normaliz_defensize(numbers):
def  normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
print(normalize_defensive(visits))
visits = ReadVisits('my_file.txt')
print(normalize_defensive(visits))

it = iter(visits)
normalize_defensive(it)
