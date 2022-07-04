def main():
    sex = input("性別 男:女>>")
    age = int(input("年齢>>"))
    if sex == "男" and age >= 20:
        print("dekimasu")
    elif sex == "女" and age >= 16:
        print("出来ます")
    else:
        print("dekinai")

    score=int(input())
    if 0<= score <= 100:
        if score>=50:
            print("goukaku")
        else:
            print("hugouakku")
    else:
        print("husei")

main()
