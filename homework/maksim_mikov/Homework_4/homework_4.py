my_dict = {'tuple': (11, 12, 13, 14, 15), 'list': [6, 7, 8, 9, 10],
           'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
           'set': {'Philadelphia Flyers', 'Washington Capitals', 'Minnesota Wild', 'Tampa Bay Lightning',
                   'New York Rangers'}}

print(my_dict['tuple'][-1])

my_dict['list'].append(25)
my_dict['list'].pop(1)
# print(my_dict['list'])

my_dict['dict'][('i am a tuple',)] = 555
del my_dict['dict']['two']
# print(my_dict['dict'])

my_dict['set'].add('Florida Panthers')
my_dict['set'].remove('Minnesota Wild')
# print(my_dict['set'])

print(my_dict)
