#list comprehension solution for squaring:
a = list(range(10))
sq = [i**2 for i in a]
print(sq)

#Mapping method for square method
sq = map(lambda x : x ** 2, a)
print(list(sq))

#only square if it is even number
even_sq = [i**2 for i in a if i % 2 == 0]
print(even_sq)

even_sq = map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, a))
print(list(even_sq))
