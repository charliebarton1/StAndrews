

def main():
    short = shorten()
    print(short)

def shorten():
    word = ""
    l = ["a","o","u","i","e"]
    try:
        x = input("Write whatever you want: ")
        for i in x:
            if i.lower() in l:
                i = ""
            word += i
    except:
        print("There was an error in the input")


if __name__ == "__main__":
    main()
