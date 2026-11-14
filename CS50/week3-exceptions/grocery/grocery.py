def main():
    while True:
        try:
            x = input()
            if type(x) == str:
                if x in groceries:
                    n = groceries[x] + 1
                    groceries.update({x:n})
                else:
                    groceries[x] = 1

        except TypeError:
            pass
        except EOFError:
            break
    for i in sorted(groceries):
        print(groceries[i],i.upper())
groceries = {


}
main()
