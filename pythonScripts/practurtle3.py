import turtle

sam = turtle.Turtle()

def curve():
    sam.speed(100000000000)
    for i in range(200):
        sam.right(1)
        sam.forward(1)
    
def heart(a):
    sam.speed(1000000000)

    sam.fillcolor('red')

    sam.begin_fill()
    
    sam.left(a)
    sam.forward(113)

    curve()
    sam.left(120)
    curve()

    sam.forward(112)

    sam.end_fill()


def txt(a,b):
    sam.speed(10)

    sam.up()
    sam.setpos(a, b)
    sam.down()

    sam.color("lightgreen")

    sam.write("Hellow",font=("Verdana",16,"bold"))


a=140
heart(a)

sam.up()
sam.setpos(-200, -200)
sam.down()

a=280
heart(a)

sam.up()
sam.setpos(200, -200)
sam.down()

a=280
heart(a)

a=-45
b=95
txt(a,b)

a=-245
b=-105
txt(a,b)

a=155
b=-105
txt(a,b)

#sam.ht()

turtle.done()

