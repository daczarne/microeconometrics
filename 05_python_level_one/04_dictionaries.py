
my_dict = {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key2'])


my_dict = {'key1': 123, 'key2': [12,23,33], 'key3': ['item0', 'item1', 'item2']}
print(my_dict['key3'])
print(my_dict['key3'][0])
print(my_dict['key3'][0].upper())
print(my_dict['key1'])

my_dict['key1'] = my_dict['key1'] - 123
print(my_dict['key1'])

my_dict['key1'] -= 123
print(my_dict['key1'])
print(my_dict)

# Create a new dictionary
d = {}
d['animal'] = 'Dog'
d['answer'] = 42
print(d)

## Nesting

d = {'key1': {'nestkey': {'subnestkey': 'value'}}}
print(d['key1']['nestkey']['subnestkey'])

## Dictionary methods

d = {'key1': 1, 'key2': 2, 'key3': 3}
print(d.keys())
print(d.values())
print(d.items())
