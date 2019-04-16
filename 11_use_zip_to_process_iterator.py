names = ["Trump", "Obama", "Jinping"]
letters = [len(name) for name in names]

# We want to iterate both list at the same time

max_name = ""
max_letter = 0
for i, name in enumerate(names):
    if letters[i] > max_letter:
        max_letter, max_name = letters[i], name
print(max_name)

# The above way is little long and feels not beautiful
# The below one use zip to perform same actions

max_name = ""
max_letter = 0

for letter, name in zip(letters, names):
    if letter > max_letter:
        max_letter, max_name = letter, name
print(max_name)

names.append("Bush")
# Now the names has one more element to letters
for letter, name in zip(letters, names):
    print(name + ": {}".format(letter))
