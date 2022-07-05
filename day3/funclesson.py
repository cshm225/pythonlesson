name = "M"
def main():

    def change_name():
        global name
        name="asa"
        print(name)

    def hello():
        print("a"+name)


    hello()
    change_name()
    hello()

main()
