import sys
import csv
def main():
    if get_files(sys.argv)==True:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            data = [["first", "last", "house"]]

            for row in reader:
                try:
                    names = (row[0].split(", "))
                    new = [names[1],names[0]]
                    new.append(row[1])
                    data.append(new)
                except:
                    pass
            # data[0] = ["first", "last", "house"]
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            for row in data:
                writer.writerow({"first": row[0], "last": row[1], "house": row[2]})






def get_files(x):
    if len(x) == 3:
        if ".csv" in x[1]:
            try:
                files = open(f"{x[1]}", "r")
                valid1 = True
                pass
            except:
                sys.exit("First file does not exist")
        else:
            sys.exit("First file was not a CSV file")
        if ".csv" in x[2]:
            try:
                files = open(f"{x[1]}", "r")
                valid2 = True
                pass
            except:
                sys.exit("Second file does not exist")
        else:
            sys.exit("Second file is not a CSV file")
    elif len(x)== 1:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")
    if valid1 and valid2 ==True:
        return True

main()
