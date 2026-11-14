x = input("Please write in camel style: ")
new = ""
for i in x:
    if i.isupper():
        i = "_" + i.lower()
    new = new + i
print(new)


