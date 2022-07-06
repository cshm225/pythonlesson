# pip install android-auto-play-opencv
from itertools import count
import android_auto_play_opencv as am
adbpath = "D:\\Program Files\\Nox\\bin\\"


def main():
    aapo = am.AapoManager(adbpath)

    def event():
        imgs = [
            "event1.PNG",
            "event2.PNG",
            "event3.PNG",
            "event4.PNG",
            "event5.PNG",
            "event6.PNG",
            "event7.PNG",
            "event8.PNG"
        ]

        aapo.screencap()
        aapo.touchImg("./images/work.PNG")
        aapo.sleep(1)

        for imgpath in imgs:
            while True:
                aapo.screencap()
                if imgpath == imgs[2]:
                    if aapo.chkImg("./images/event/"+imgpath):
                        aapo.touchPos(1710, 930)
                        break
                elif imgpath == imgs[3]:
                    result, x, y = aapo.chkImg2("./images/event/"+imgpath)
                    if result:
                        aapo.longTouchPos(x, y, 10000)
                        break
                elif imgpath == imgs[7]:
                    if aapo.chkImg("./images/event/"+imgpath):
                        aapo.sleep(1)
                        aapo.touchPos(1615.5, 145)
                        break
                else:
                    if aapo.chkImg("./images/event/"+imgpath):
                        aapo.sleep(1)
                        aapo.touchImg("./images/event/"+imgpath)
                        break
        aapo.screencap()
        aapo.touchImg("./images/home.PNG")
        aapo.sleep(2)
        aapo.touchImg("./images/home.PNG")

    def cafe():
        cafepath = "./images/cafe/"
        imgs = [
            "cafe1.PNG",
            "cafe2.PNG",
            "cafe3.PNG",
            "cafe4.PNG",
            "cafe5.PNG",
            "cafe6.PNG",
        ]

        # 処理開始
        aapo.screencap()
        aapo.touchImg("./images/cafe.PNG")
        while True:
            aapo.screencap()
            if aapo.chkImg(cafepath+"cafein.PNG"):
                break
        aapo.sleep(3)

        # cafeに入ってからの処理
        for imgpath in imgs:
            while True:
                aapo.screencap()
                if imgpath == imgs[0]:
                    aapo.sleep(5)
                    if aapo.chkImg(cafepath+imgpath):
                        aapo.touchPos(600, 600)
                        break
                    else:
                        break
                else:
                    if aapo.chkImg(cafepath+imgpath):
                        aapo.touchImg(cafepath+imgpath)
                        break

    def battle():
        battlepath = "./images/battle/"
        imgs = [
            "battle1.PNG",
            "battle2.PNG",
            "battle3.PNG",
        ]

        # 処理開始
        aapo.screencap()
        aapo.touchImg("./images/work.PNG")
        for imgpath in imgs:
            while True:
                aapo.screencap()
                if aapo.chkImg(battlepath+imgpath):
                    if imgpath == imgs[1]:
                        aapo.touchImg(battlepath+imgpath)
                        aapo.sleep(3)
                        aapo.touchPos(1800, 1000)
                        break
                    elif imgpath == imgs[2]:
                        aapo.touchPos(539, 598)
                        aapo.sleep(3)
                        aapo.touchPos(1800, 1000)
                        break
                    else:
                        aapo.touchImg(battlepath+imgpath)
                        break
        aapo.screencap()
        aapo.touchImg("./images/home.PNG")

    def shop():
        shoppath = "./images/shop/"
        imgs = [
            "shop1.PNG",
            "shop2.PNG",
            "shop3.PNG",
            "shop4.PNG",
            "shop5.PNG",
        ]
        aapo.screencap()
        aapo.touchImg("./images/shop.PNG")

        for imgpath in imgs:
            while True:
                aapo.screencap()
                if aapo.chkImg(shoppath+imgpath):
                    aapo.touchImg(shoppath+imgpath)
                    break

        aapo.screencap()
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
