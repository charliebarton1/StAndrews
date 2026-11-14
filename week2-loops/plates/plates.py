def main():
    plate = input("Plate: ")
    plate = plate.strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if two_let(s) and max_min(s) and number_middle(s) and only_let_num(s):
        return True
    else:
        return False



def two_let(x):
    if x[0:2].isalpha():
        return True
    else:
        return False



def max_min(x):
    if len(x)>=2 and len(x) <= 6:
        return True
    else:
        return False


def number_middle(x):
    for i in x:
        if i.isnumeric():
            y = x.split(i,1)
            if i == "0":
                return False
            for g in y[1]:
                if g.isalpha():
                    return False
            return True

    return True


def only_let_num(x):
    if x.isalnum():
        return True
    else:
        return False



main()
