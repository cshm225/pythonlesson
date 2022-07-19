import tkinter as tk
index = 0


def change_img():
    global index
    canvas.delete("PIC")
    canvas.create_image(400, 300, image=photos[index % len(photos)], tag="PIC")
    index+=1
    root.after(5000,change_img)

root = tk.Tk()
root.title("でじたるふぉとふれーむ")
canvas = tk.Canvas(width=800, height=600)
canvas.pack()
photos = [tk.PhotoImage(file=f'cat0{i}.png')for i in range(4)]
change_img()
root.mainloop()
