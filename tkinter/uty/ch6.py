import tkinter as tk

from matplotlib import image
def mouse_click(e):
    px=e.x
    py=e.y
    print("座標({},{})".format(px,py))
    mx=int(px/48)
    my=int(py/48)

    if 0 <= mx and mx<=6 and 0 <= my and my <=4:
        n=map_data[my][mx]
        print("マップチップは"+CHIP_NAME[n])

root = tk.Tk()
root.title("まpp")
canvas = tk.Canvas(width=336, height=240)
canvas.pack()
canvas.bind("<Button>",mouse_click)
CHIP_NAME=["草","花","森","海"]
img = [
    tk.PhotoImage(file="chip0.png"),
    tk.PhotoImage(file="chip1.png"),
    tk.PhotoImage(file="chip2.png"),
    tk.PhotoImage(file="chip3.png"),
]
map_data = [
    [0, 1, 0, 2, 2, 2, 2],
    [3, 0, 0, 0, 2, 2, 2],
    [3, 0, 0, 1, 0, 0, 0],
    [3, 3, 0, 0, 0, 0, 1],
    [3, 3, 3, 3, 0, 0, 0],
]
for y in range(5):
    for x in range(7):
        n = map_data[y][x]
        canvas.create_image(x*48+24, y*48+24, image=img[n])
root.mainloop()