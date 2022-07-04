def main():
    members = ["工藤", "松田", "麻木"]
    members.append("スガワラ")
    members.append("朝霞")
    members.append("湊")
    print(members)
    print(members[0])
    members.remove("松田")
    print(members)
    print(members[1])
    members[2]="菅原"
    print(members)
    print(members[1:3])#添え字が1異常3未満
    print(members[2:])#添え字が2以上
    print(members[:3])#添え字が3未満
    print(members[-1])
    m=members[:]#配列のコピー　新しい配列mあつかいになる
    print(m)


    scores = [88, 90, 95]
    total = sum(scores)
    ave = total/len(scores)
    print(f"合計は{total}で平均{ave}はです")


main()
