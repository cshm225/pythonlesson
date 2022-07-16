# pip install android-auto-play-opencv
from itertools import count
import android_auto_play_opencv as am
adbpath = "D:\\Program Files\\Nox\\bin\\"


def main():
    aapo = am.AapoManager(adbpath)

    def work_battle(touch_time):
        work_battlepath = "./images/workbattle/"
        imgs = [
            "workbattle1.PNG",
            "workbattle2.PNG",
            "workbattle3.PNG",
            "workbattle4.PNG",
        ]

        for imgpath in imgs:
            while True:
                aapo.screencap()
                if imgpath == imgs[0]:
                    result, x, y = aapo.chkImg2(work_battlepath+imgpath)
                    if result:
                        aapo.longTouchPos(x, y, touch_time)
                        break
                elif imgpath == imgs[3]:
                    if aapo.chkImg(work_battlepath+imgpath):
                        aapo.sleep(1)
                        aapo.touchPos(1615.5, 145)
                        break
                else:
                    if aapo.chkImg(work_battlepath+imgpath):
                        aapo.sleep(1)
                        aapo.screencap()
                        aapo.touchImg(work_battlepath+imgpath)
                        break
        aapo.sleep(1)
        aapo.touchPos(1615, 145)

    def hard():
        hardpath = "./images/hard/"
        imgs = [
            "hard1.PNG",
            "hard2.PNG",
            "hard3.PNG",
            "hard4.PNG",
            "hard5.PNG",
            "hard6.PNG",
            "hard7.PNG",
            "hard8.PNG",
            "hard9.PNG",
            "hard10.PNG",
            "hard11.PNG",
            "hard12.PNG",
            "hard13.PNG",
        ]
        aapo. screencap()
        aapo.touchImg("./images/work.PNG")
        aapo.sleep(1)
        while True:
            aapo.screencap()
            if aapo.chkImg(hardpath+"ninmu.PNG"):
                aapo.touchImg(hardpath+"ninmu.PNG")
                break
        while True:
            aapo.screencap()
            if aapo.chkImg(hardpath+"hardin.PNG"):
                break
            else:
                aapo.touchImg(hardpath+"checkhard.PNG")
        for imgpath in imgs:
            while True:
                aapo.screencap()
                if imgpath == imgs[0] or imgpath == imgs[3] or imgpath == imgs[10]:
                    if aapo.chkImg(hardpath+imgpath):
                        print("上下imgs[0]")
                        aapo.touchPos(1700, 440)
                        work_battle(3000)
                        aapo.sleep(1)
                        aapo.touchPos(1700, 700)
                        work_battle(3000)
                        while True:
                            aapo.screencap()
                            if aapo.chkImg(hardpath+"right.PNG"):
                                aapo.touchImg(hardpath+"right.PNG")
                                break
                        break
                if imgpath == imgs[1] or imgpath == imgs[11]:
                    if aapo.chkImg(hardpath+imgpath):
                        aapo.touchPos(1700, 540)
                        work_battle(3000)
                        aapo.sleep(1)
                        aapo.touchPos(1700, 700)
                        work_battle(3000)
                        while True:
                            aapo.screencap()
                            if aapo.chkImg(hardpath+"right.PNG"):
                                aapo.touchImg(hardpath+"right.PNG")
                                break
                        break
                if imgpath == imgs[2] or imgpath == imgs[5] or imgpath == imgs[7] or imgpath == imgs[9]:
                    if aapo.chkImg(hardpath+imgpath):
                        aapo.touchPos(1700, 700)
                        work_battle(3000)
                        aapo.sleep(1)
                        while True:
                            aapo.screencap()
                            if aapo.chkImg(hardpath+"right.PNG"):
                                aapo.touchImg(hardpath+"right.PNG")
                                break
                        break
                if imgpath == imgs[4] or imgpath == imgs[6] or imgpath == imgs[8]:
                    if aapo.chkImg(hardpath+imgpath):
                        aapo.touchPos(1700, 440)
                        work_battle(3000)
                        aapo.sleep(1)
                        aapo.touchPos(1700, 540)
                        work_battle(3000)
                        aapo.sleep(1)
                        aapo.touchPos(1700, 700)
                        work_battle(3000)
                        while True:
                            aapo.screencap()
                            if aapo.chkImg(hardpath+"right.PNG"):
                                aapo.touchImg(hardpath+"right.PNG")
                                break
                        break
                if imgpath == imgs[12]:
                    if aapo.chkImg(hardpath+imgpath):
                        aapo.touchPos(1700, 540)
                        work_battle(3000)
                        aapo.sleep(1)
                        break
                else:
                    break
        aapo.screencap()
        aapo.touchImg("./images/home.PNG")

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

    # cafe()
    # aapo.sleep(3)
    # event()
    # aapo.sleep(3)
    # battle()
    # aapo.sleep(3)
    # shop()
    # aapo.touchPos(1700,540)
    # aapo.touchPos(1700,440)
    # aapo.touchPos(1700,700)
    hard()


if __name__ == "__main__":
    main()
