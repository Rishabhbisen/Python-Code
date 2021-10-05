# this is dictionary funtion
from functools import update_wrapper


my_duct = {
    " hello": 454,
    'food': 'goood',
    'mark': {1, 2, 3, 4},

}
# print(my_duct)
print(my_duct['food'])
my_duct['mark'] = [2, 4]
print(my_duct)

# dictionary moduls

my_dict = {
    'fast': ' in a quice manner',
    'rishabh': 'is a good codder',
    'mark': {1, 2, 3, 4, },
    'another_dicy': {'rishabh': 'player'},
    1: 2
}
print(my_dict)
print(my_dict.keys())  # print key of the dic
print(my_dict.values())  # print value of the dic
print(my_dict.items())  # print item in dic

update_dict = {
    'rishabh': ' is a good boy ',
    'rohit ': ' ....',
    'yuvan':  ' pta nhi ',
    ' review ': ' rishabh is best ha...ha..'

}
print(update_dict)
my_dict.update(update_dict)
print(my_dict)
print(my_dict['mark'])
print(my_dict.get('mark'))
# print(my_dict['mark1'])  # this will show an error
print(my_dict.get('mark1'))  # this will show none
