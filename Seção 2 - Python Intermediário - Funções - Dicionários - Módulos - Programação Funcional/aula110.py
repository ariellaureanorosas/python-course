# Count is an endless iterator
from itertools import count

# -> count(start, step)
c1 = count()
# print(next(c1))
# print(next(c1))

for index in c1:
    if index > 200:
        break
    print(index)

