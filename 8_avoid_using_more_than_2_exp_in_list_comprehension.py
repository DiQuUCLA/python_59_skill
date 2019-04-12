matrix = [[1,2,3], [4,5,6], [7,8,9]]

#The below one seems cool, but not hard to read
filtered = [[x for x in row if x % 3 == 0]
        for row in matrix if sum(row) > 10]
print(filtered)

filtered = []
for row in matrix:
    if sum(row) > 10:
        new_l = []
        for n in row:
            if n % 3 == 0:
                new_l.append(n)
        if new_l:
            filtered.append(new_l)
print(filtered)
