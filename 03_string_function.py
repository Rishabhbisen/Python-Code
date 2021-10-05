st1 = " hello my name is Rishabh bisen i am from balaghat which is an mp , currantly i am persuing btech from ies college of technolgy"
print(len(st1))
print(st1.count('c'))
print(st1.replace('h', 'r'))
print(st1.capitalize())
print(st1.find('my'))

# this is an example
latter = ''' hello good mourning
        <|name|>
        you are selected in our company 
        <|date|> 
        thank you for intresting in our compant'''
name = input(" enter your name \n")
date = input(" enter date\n")
latter = latter.replace("<|name|>", name)
latter = latter.replace("<|date|> ", date)
print(latter)

st = "hello  good   morning   ok"
st = st.replace(' ', '  ')
print(st)
double_space = st.find(" ")
print(double_space
)
