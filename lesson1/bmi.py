
def main():

    def body():
        if bmi >= 25:
            result = "肥満"
        if bmi >= 18.5:
            result = "標準"
        else:
            result = "やせ"
        return result

    height = input("身長を入力")
    weight = input("体重を入力")
    height = float(height)/100
    weight = float(weight)
    bmi = weight/(height*height)
    resultbody = body()
    print("bmi:", bmi, resultbody)


main()
