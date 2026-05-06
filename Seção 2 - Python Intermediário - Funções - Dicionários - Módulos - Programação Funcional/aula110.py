# Count é um iterador sem fim
from itertools import count

# -> count(inicio, step)
c1 = count()
# print(next(c1))
# print(next(c1))

for i in c1:
    if i > 200:
        break
    print(i)
