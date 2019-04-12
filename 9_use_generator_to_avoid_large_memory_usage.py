import os
import psutil
import sys

a = sys.argv

if len(a) != 2:
    print("Need to tell use generator or list: \n" + 
            "0: generator\n" +
            "1: list")
if a[1] == '0':
    it = (x for x in open('my_file.txt'))
    print(next(it))
    print(next(it))

if a[1] == '1':
    it = [x for x in open('my_file.txt')]
    print(it)

process = psutil.Process(os.getpid())
print(process.memory_info().rss)

