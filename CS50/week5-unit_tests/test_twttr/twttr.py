import sys
def main():
    print(shorten(12))
    short = shorten(input("Write whatever you want: "))
    print(short)

def shorten(x):
    word = ""
    l = ["a","o","u","i","e"]
    if not isinstance(x,str):
        raise TypeError
    for i in x:
        if i.lower() in l:
            i = ""
        word += i
    return word




if __name__ == "__main__":
    main()
