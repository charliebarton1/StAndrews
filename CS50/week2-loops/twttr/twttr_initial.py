x = input("Write whatever you want: ")
word = ""
l = ["a","o","u","i","e"]
for i in x:
    if i.lower() in l:
        i = ""
    word += i
print(word)
