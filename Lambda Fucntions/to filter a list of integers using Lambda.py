# -*- coding: utf-8 -*-
"""
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]

"""
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even=list(filter(lambda x:x%2 ==0,lst))
print("Even List :",even)
odd=list(filter(lambda x:x%2 != 0,lst))
print("Odd List :",odd)pip install sqlalchemy