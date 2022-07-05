class Hero:
    hp=90;
    name="C"
    def __init__(self) -> None:
        pass

    def __init__(self,name,hp):
        self.hp=hp
        self.name=name

    def sleep(self, hours):
        print("{}ha{}neta".format(self.name, hours))
        self.hp += hours


def main():
    h = Hero("A",100)
    h.sleep(4)
    h2 = Hero("B",150)
    h2.sleep(3)

    print("{} no hp wa {}".format(h.name, h.hp))
    print("{} no hp wa {}".format(h2.name, h2.hp))

main()