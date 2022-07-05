from dataclasses import replace


def main():
    #info = input()
   # [name, blood] = info.split(",")
    #blood = blood.upper().strip()
    #print("{}{}".format(name, blood))
    name = "banana"
    name = name.replace("a", "o")
    print(name)
    count = name.count("o")
    print(count)

    def add(x, y):
        return x+y

    type(add)
    newadd = add
    print(newadd(4, 5))


main()
