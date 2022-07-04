def main():
    scores = {"network": 60, "database": 80, "security": 50}
    print(scores)
    print(scores["network"])
    scores["network"]=65
    scores["programming"]=70
    print(scores)
    total=sum(scores.values())
    print(total)
    del scores["database"]
    print(scores)


main()
