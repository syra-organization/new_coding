# dictionary is nothin but objects
# key should always should be immutable value
data = {
    'name': 'Avinash',
    'hobbie': 'sports'
}

print(data['name'])  # Avinash
print(data['hobbie'])  # sports

print(data.get('name'))  # Avinash

# IF we don't have the key in my object

# it will prints age is not mentioned because we don't have the key age.
print(data.get('age', 'Age is not mentioned'))

# If we want to create a object by using the two arrays

keys = ['name', 'hobbie']
values = ['Avinash', 'sports']

obj = dict(zip(keys, values))
print(obj)  # will print the object or dictionary

# If we want to add a new key or value

obj['age'] = 25
print(obj)

# If we want to delete a key or value

del obj['age']
print(obj)

# Nested dictionary

persons = {
    'person1': {
        'name': 'Avinash',
        'age': 25
    },
    'person2': {
        'name': 'Yogesh',
        'age': 25
    }
}

print(persons.get('person1').get('name'))  # Avinash
