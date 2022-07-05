from msilib.schema import LaunchCondition


def main():
    name = "a"

    def eat(breakfast,lunch,dinner="curry",desserts=()):
        print("asa{}".format(breakfast))
        print("hiru{}".format(lunch))
        print("yoru{}".format(dinner))
        for i in desserts:
            print(i)

    def eat(breakfast,lunch,dinner="curry",*desserts):
        print("asa{}".format(breakfast))
        print("hiru{}".format(lunch))
        print("yoru{}".format(dinner))
        for i in desserts:
            print(i)


    def hello(name):
        print("hello"+name)
        name="b"
        return name

    def eats(**kwargs):
        for key in kwargs:
            print("{}ni{}woeat".format(key,kwargs[key]))

    name=hello(name)
    print(name)

    s=eat("pan","pasta","cu",("a","c","p"))
    s=eat("pan","pasta","cu","a","c","d")
    eats(asa="pans",tyuu="paas",yuu="cpan")

main()
