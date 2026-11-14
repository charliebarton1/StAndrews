import sys
def main():
    file = get_file(sys.argv)
    lines = get_line(file)
    print(lines)

def get_file(x):
    if len(x) == 2:
        if ".py" in x[1]:
            try:
                files = open(f"{x[1]}", "r")
                return files
            except:
                sys.exit("File does not exist")
        else:
            sys.exit("No a python file")
    elif len(x)== 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def get_line(py_file):
    count = 0
    for line in py_file:
        if line.strip()== "":
            pass
        elif line.strip()[0] =="#":
            pass
        else:
            count += 1
    return count

if __name__ == "__main__":
    main()
