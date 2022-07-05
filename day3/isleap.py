def main():
    def isleapyear(year):
        return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

    year = int(input("何年>>"))
    if isleapyear(year):
        print("{}閏年".format(year))
    else:
        print("{}閏年ではない".format(year))


main()
