def main():
    p1 = {"読書", "昼寝", "映画鑑賞", "散歩", "料理"}
    p2 = {"テニス", "将棋", "料理", "読書", "旅行"}
    common = p1 & p2
    total = p1 | p2
    rate = len(common)/len(total)*100
    print(f"愛称は{rate}％")

    food="カレー"
    if "カレー" in food:
        print("kare-")

    scores=["network":60,"database"=80,"security"=75]
    key=input("追加")


main()
