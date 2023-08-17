names = [
    'Hazard',
    'Mbappe',
    'Kane'
]

# List comprehension
length = [len(name) for name in names]

# Dictionary comprehension
length_dict = {name:len(name) for name in names}

print(length)
print(length_dict)