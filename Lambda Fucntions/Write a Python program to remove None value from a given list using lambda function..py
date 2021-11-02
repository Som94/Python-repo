
''' Write a Python program to remove None value from a given list using lambda function.'''


nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

act=list(filter(lambda v: v is not None,nums))

print(act)