


def main():
    print("y/n")
    okane_aruka = input("お金に余裕がある?")
    if okane_aruka == "y":
        onaka_suiteruka = input("おなかすいてるか？")
        beer = input("ビール飲みたいか？")
        if onaka_suiteruka == "y" and beer == "y":
            print("yakinijku")
        elif onaka_suiteruka == "y":
            print("curry")
        elif beer == "y":
            print("yakitori")
        else:
            print("jopasta")
    else:
        print("ie")


main()
