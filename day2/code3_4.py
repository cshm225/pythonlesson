def main():
    month=int(input("今は何月ですか"))
    if month in [1,3,5,7,8,10,12]:
        print("31")
    else:
        if month !=2:
            print("30")

main()