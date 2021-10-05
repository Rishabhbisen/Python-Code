for i in range(2, 21):
    with open('multification table of {i}.txt', 'w')as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}\n")
        break

# we can use this function for replce file word
# in this case we can use if else statemant

# with open('sample.txt')as f:
#     data = f.read()
# data = data.replace("monkey", "#$^&")
# with open("sample.txt", 'w')as f:
#     f.write(data)

word = ["hello", "gello", "pello"]

with open("sample.txt")as f:
    data = f.read()

for word in word:
    data = data.replace(word, "$^%&^")
    with open("sample.txt", "w")as f:
        f.write(data)
