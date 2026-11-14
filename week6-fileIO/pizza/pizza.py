import sys
import csv
from tabulate import tabulate
def main():
    info = []
    if get_file(sys.argv)==True:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                info.append(row)
            tab = tabulate(info, headers = "firstrow",tablefmt="grid")
            print(tab)


def get_file(x):
    if len(x) == 2:
        if ".csv" in x[1]:
            try:
                files = open(f"{x[1]}", "r")
                return True
            except:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")
    elif len(x)== 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

main()
