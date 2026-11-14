def main():
    names_list = names()
    print(names_list)
    new = ""
    if len(names_list) == 1:
        new = names_list[0]
    elif len(names_list) == 2:
        new = names_list[0] + " and " + names_list[1]

    else:
        for name in names_list[:-1]:
            new = new + name + ", "
        new = new + "and " + names_list[-1]
    print("Adieu, adieu, to " + new)


def names():
    name = []
    while True:
        try:
            x = input("Enter a name: ")
            if len(x.split()) == 1:
                name.append(x.strip())
        except EOFError:
            break
        except:
            pass
    return name


main()
