import tkinter as tk
ani=0
x=0
def animation():
    global x, ani
    x=x+10
    if x==480:
        x=0
    canvas.delete("BG")
    canvas.create_image(x-240,150,image=img_bg,tag="BG")
    canvas.create_image(x+240,150,image=img_bg,tag="BG")
    ani=(ani+1)%4
    canvas.create_image(240,200,image=img_dog[ani],tag="BG")
    root.after(200,animation)

root=tk.Tk()
root.title("scroll")
canvas=tk.Canvas(width=480,height=300)
canvas.pack()
img_bg=tk.PhotoImage(file="park.png")
img_dog=[
    tk.PhotoImage(file="dog0.png"),
    tk.PhotoImage(file="dog1.png"),
    tk.PhotoImage(file="dog2.png"),
    tk.PhotoImage(file="dog3.png")
]
animation()
root.mainloop()