a = 13
if a == 2:
    print('yes')    # if first condition is true other case will not be run
elif a < 12:
    print('no this is wrong value')
elif a > 3:
    print(' a is greter than 3')
else:
    print('no')

age = int(input(' Enter your age\n'))
if a > 18:
    print(' yes ! you can vote ')
else:
    print(' no ! you can not vote')

# logocal oprater
age1 = int(input(' Enter your age \n'))
if (age > 18 or age < 60):
    print(' yes you can work with us')
else:
    print(' no , you can not work with us')

mark = int(input(' Enter your mark \n'))
if mark >= 33:
    print(' pass')
elif (mark > 33):
    print('fail')
elif(mark >= 70):
    print(' pass, with firsr devizion')
else:
    print(' you get grade f ')


a = [1, 2, 3, 4]
print(1 in a)

text = input(' enter text\n')
if (' make a money lot ' in text):
    spam = True
elif (' hello' in text):
    spam = True
elif (' good ' in text):
    spam = True
else:
    spam = False
if (spam):
    print(' this is text spam ')
else:
    print(' this is not text spam')


names = ['rishabh', 'rohit', 'yuvan', 'vikash']
name = input(" enter name and check\n")
if name in names:
    print(' your name is here')
else:
    print(' your name is not here')
