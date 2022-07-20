from tabnanny import check
import tkinter as tk
import random

from matplotlib import image

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0
mouse_c = 0
index = 0
player = 0


def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y


def mouse_press(e):
    global mouse_c
    mouse_c = 1


neko = []
check=[]

for i in range(10):
    neko.append([0,0,0,0,0,0,0,0])
    check.append([0,0,0,0,0,0,0,0])


def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60,
                                 image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x]=neko[y][x]


    for y in range(1,9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    neko[y-1][x]=7
                    neko[y][x]=7
                    neko[y+1][x]=7
                    return True
    for y in range(10):
        for x in range(1,7):
            if check[y][x] > 0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                    neko[y][x-1]=7
                    neko[y][x]=7
                    neko[y][x+1]=7
                    return True

    for y in range(1,9):
        for x in range(1,7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    neko[y-1][x-1]=7
                    neko[y][x]=7
                    neko[y+1][x+1]=7
                    return True
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    neko[y+1][x-1]=7
                    neko[y][x]=7
                    neko[y-1][x+1]=7
                    return True
    return False




def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x] = 0


def draw_txt(txt, x, y, siz, col, tg):
    fnt = ("Times New Roman", siz, "bold")
    cvs.create_text(x+2, y+2, text=txt, fill="black", font=fnt, tag=tg)
    cvs.create_text(x, y, text=txt, fill=col, font=fnt, tag=tg)




def game_main():
    global cursor_x,cursor_y,mouse_c,index,player
    if index == 0: # タイトルロゴ


        for i in range(10):
            neko[i]=([0,0,0,0,0,0,0,0])
        draw_txt("ねこねこ", 312, 240, 100, "violet", "TITLE")
        cvs.create_rectangle(168, 384, 456, 456, fill="skyblue", width=0, tag="TITLE")
        index=1
    if 660 <= mouse_x and mouse_x <840 and 100 <= mouse_y <160 and mouse_c ==1:
        mouse_c = 0
        check_neko()
    elif index == 1:
        # タイトル画面 スタート待ち
        cvs.delete("OVER")
        if mouse_c==1:
            index=2


    if 24 <= mouse_x and mouse_x< 24+72*8 and 24 <= mouse_y and mouse_y< 24+72*10 and player==0 and index==2:
        cvs.delete("TITLE")
        cursor_x=int((mouse_x-24)/72)
        cursor_y=int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c=0
            player=1
            neko[cursor_y][cursor_x]=1
            draw_neko()
            if check_neko():
                draw_neko()
                draw_txt("1Win", 312, 348, 60, "red", "OVER")

                index=0

    if 24 <= mouse_x and mouse_x< 24+72*8 and 24 <= mouse_y and mouse_y< 24+72*10 and player==1 and index==2:
        cvs.delete("TITLE")
        cursor_x=int((mouse_x-24)/72)
        cursor_y=int((mouse_y-24)/72)
        if mouse_c == 1:
            mouse_c=0
            player=0
            neko[cursor_y][cursor_x]=2
            draw_neko()
            if check_neko():
                draw_neko()
                draw_txt("2Win", 312, 348, 60, "red", "OVER")
                index=0

    cvs.delete("CURSOR")
    cvs.delete("NEKO")
    draw_neko()

    cvs.create_image(cursor_x*72+60,cursor_y*72+60,image=cursor,tag="CURSOR")
    root.after(100, game_main)


root = tk.Tk()
root.title("deleeeeeeeeeeeeeeeeeeeete")
root.resizable(False, False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
cvs = tk.Canvas(root, width=912, height=768)
cvs.pack()

bg = tk.PhotoImage(file="neko_bg.png")
cursor= tk.PhotoImage(file="neko_cursor.png")

img_neko = [
    None,
    tk.PhotoImage(file="neko1.png"),
    tk.PhotoImage(file="neko2.png"),
    tk.PhotoImage(file="neko3.png"),
    tk.PhotoImage(file="neko4.png"),
    tk.PhotoImage(file="neko5.png"),
    tk.PhotoImage(file="neko6.png"),
    tk.PhotoImage(file="neko_niku.png"),

]

cvs.create_image(456, 384, image=bg)
cvs.create_rectangle(660,100,840,160,fill="white")
cvs.create_text(750,130,text="テスト",fill="red",font=("Times New Roman", 30) )
game_main()
root.mainloop()
