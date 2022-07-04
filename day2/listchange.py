def main():
    scores = {"network": 60, "database": 70, "security": 80}
    members = ["松田", "麻木", "工藤"]
    print(tuple(members))
    print(list(scores))
    print(set(scores.values()))
    print(dict(zip(members, scores.values())))

    matsuda_scores = {"network": 60, "database": 80, "security": 50}
    asagi_scores = {"network": 80, "databse": 75, "security": 92}
    member_scores = {
        "松田": matsuda_scores,
        "麻木": asagi_scores
    }
    print(member_scores)

    member_hobbies = {
        "松田": {"SNS", "麻雀", "自転車"},
        "浅葱": {"麻雀", "食べ歩き", "数学"}
    }
    print(member_hobbies)
    print(member_hobbies["松田"])
    print(member_hobbies["浅葱"])

    a=[1,2,3]
    b=[4,5,6]
    c=[a,b]

    print(c)
    print(c[0])
    print(c[1][2])

    print(member_hobbies["松田"]&member_hobbies["浅葱"])
    print(member_hobbies["松田"]|member_hobbies["浅葱"])
    print(member_hobbies["松田"]-member_hobbies["浅葱"])
    print(member_hobbies["松田"]^member_hobbies["浅葱"])



main()
