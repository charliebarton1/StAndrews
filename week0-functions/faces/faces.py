def convert(j):
    j = j.replace(":)", "🙂")
    j = j.replace(":(", "🙁")
    return j
def main():
    string = input("Write anything: ")
    string = convert(string)
    print(string)
    return string


main()




