def main():
    s_n = input("会談のだんすう>")
    for i in range(int(s_n)):
        for j in range(i+1):
            print("*",end="")
        print()


main()
