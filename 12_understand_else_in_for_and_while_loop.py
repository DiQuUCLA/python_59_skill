# unlike in java or C, python can support else after while and for loop
for i in range(3):
    print("Loop %d" % i)
else:
    print("Else block!")

# However, else is not what it will goes after break
for i in range(3):
    print("Loop %d" % i)
    if i == 1:
        break
else:
    print("Else block!")

# We can think that the else block belongs to loop, when break, we are out
# of the entire loop, including the else block

# The else block also runs when while loop is on false
while False:
    print('Never')
else:
    print('Else block of While False!')

# Else sometimes is useful when you want to know you get out of the loop
# by break or run out of the iterator
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')
