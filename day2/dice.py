import random


def main():
    num = int(input(">>"))
    dice = [random.randint(1, 6) for _ in range(num)]
    print(dice)


main()
