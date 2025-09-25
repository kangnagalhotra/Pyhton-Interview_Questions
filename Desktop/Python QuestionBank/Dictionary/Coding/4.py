# Invert a dictionary (values → keys).

my_dict = {'a': 1, 'b': 2, 'c': 3}
inverted = {value: key for key, value in my_dict.items()}
print(inverted)
