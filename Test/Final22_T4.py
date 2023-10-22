#4번
string = "apple"
alphabet = []

for i in string:
    if i not in alphabet:
        alphabet.append(i)

print(alphabet)
