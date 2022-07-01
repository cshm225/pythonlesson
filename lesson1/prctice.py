def main():
    height = float(input("身長"))
    weight = float(input("体重"))
    height = height/100
    bmi = weight/height/height
    print(bmi)


main()
