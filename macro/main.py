# pip install android-auto-play-opencv
from itertools import count
import android_auto_play_opencv as am
adbpath = "D:\\Program Files\\Nox\\bin\\"


def main():
    aapo = am.AapoManager(adbpath)

    def event():
        imgpath = "event"
        count = 0
        aapo.screencap()
        aapo.touchImg("./images/work.PNG")
        while True:
            count += 1
            aapo.sleep(3)
            aapo.screencap()
            aapo.sleep(3)
            if count == 3:
                aapo.touchPos(1710, 930)
            else:
                if count == 4:
                    result, x, y = aapo.chkImg2(
                        "./images/event/"+imgpath+str(count)+".PNG")
                    if result:
                        aapo.longTouchPos(x, y, 11000)
                else:
                    aapo.touchImg("./images/event/"+imgpath+str(count)+".PNG")
                if count == 8:
                    break
        aapo.sleep(3)
        aapo.touchImg("./images/home.PNG")
        aapo.sleep(2)
        aapo.touchImg("./images/home.PNG")

    def cafe():
        imgpath = "cafe"
        count = 0
        while True:
            count += 1
            aapo.screencap()
            aapo.sleep(4)
            aapo.touchImg("./images/cafe/"+imgpath+str(count)+".PNG")
            aapo.sleep(4)
            if count == 6:
                break

    def battle():
        aapo.screencap()
        aapo.touchImg("./images/work.PNG")
        imgpath = "battle"
        count = 0
        while True:
            count += 1
            aapo.sleep(4)
            aapo.screencap()
            aapo.sleep(4)
            if count == 3:
                aapo.touchPos(539, 698)
                aapo.sleep(3)
                aapo.touchPos(1800, 1000)
                break
            else:
                aapo.touchImg("./images/battle/"+imgpath+str(count)+".PNG")
            if count == 2:
                aapo.sleep(5)
                aapo.touchPos(1800, 1000)
        aapo.touchImg("./images/home.PNG")

    def shop():
        aapo.screencap()
        aapo.touchImg("./images/shop/shop.PNG")
        imgpath = "shop"
        count = 0
        while True:
            count += 1
            aapo.sleep(3)
            aapo.screencap()
            aapo.sleep(3)
            aapo.touchImg("./images/shop/"+imgpath+str(count)+".PNG")
            if count == 5:
                break
        aapo.touchImg("./images/home.PNG")

    cafe()
    aapo.sleep(3)
    event()
    aapo.sleep(3)
    battle()
    aapo.sleep(3)
    shop()


if __name__ == "__main__":
    main()
