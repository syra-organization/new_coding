# for loops

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

users = {'Avinash': 'active', 'Yogesh': 'not active', 'Sharath': 'not active'}

# loop may modifies the collections while itirating so we need to itirate with the copy of it.

for user, status in users.copy().items():
    if status == 'active':
        print(user + ' is active')
    else:
        print(user + ' is not active')

# using of range in for loops

for i in range(5):
    print(i)  # will print the index

# If we want to traverse the array using index

for i in range(len(words)):
    print(i, words[i])

# while loop

i = 0

while i < len(words):
    print(words[i], 'from while loop')
    i += 1
