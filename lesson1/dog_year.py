def main():
    dogname = input("犬の名前を入力>")
    dogage = input("犬の年齢を入力>")  # input関数の返り値はString
    humanage = int(dogage)*7
    text = dogage*7
    print(dogname, "は今", dogage, "歳で人換算すると", humanage, "です", sep="")


main()
