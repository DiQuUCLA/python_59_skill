# a[::-1] might break for unicode encoded byte string with character not in 
# ascii table

w = "愛情公寓"
c = w.encode("utf-8")
print(c)
d = c[::-1]
print(d)
d.decode("utf-8")
