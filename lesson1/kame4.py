import turtle


def main():
    t = turtle.Turtle()
    t.shape("turtle")
    for i in range(4):
        t.forward(100)
        t.right(145)
    t.home()
    # t.circle(100)
    turtle.mainloop()


main()
