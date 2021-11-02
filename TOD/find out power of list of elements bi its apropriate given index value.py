# -*- coding: utf-8 -*-
"""
find out power of list of elements bi its apropriate given index value

"""
numbers = (1, 2, 4, 6)
indices = (2, 1, 0.5, 2)
# use map()
um=list(map(pow, numbers, indices))
print(um) #[1, 2, 2.0, 36]
# list comprehensions
lc=[pow(x, y) for x, y in zip(numbers, indices)]
print(lc)#[1, 2, 2.0, 36]


print(pow(3,2))