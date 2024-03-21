import turtle

def main():
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    turtle.title("Casa da Lorena")
    screen.bgcolor("#011f4b")
    t = turtle.Turtle()
    t.shape("circle")
    t.speed(10)
    corpo(t)
    teto(t)
    cha(t)
    janela(t)
    lua(t)
    porta(t)
    chao(t)
   
   
    turtle.done()

def corpo(t):
    t.fillcolor("#ffcc5c")
    t.begin_fill()
    for _ in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

def teto(t):
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor("#740001")
    t.begin_fill()
    t.goto(200, 100)
    t.goto(100, 150)
    t.goto(0, 100)
    t.end_fill()

def porta(t):
    t.penup()
    t.goto(20, 1)
    t.pendown()
    t.fillcolor("#38220f")
    t.begin_fill()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.end_fill()


def cha(t):
    t.penup()
    t.goto(25, 100)
    t.pendown()
    t.fillcolor("#400000")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(70)
        t.left(90)   
    t.end_fill()

def janela(t):
    t.penup()
    t.home()
    t.goto(100, 25)
    t.pendown()
    t.fillcolor("#936C00")
    t.begin_fill()
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.forward(50)
    t.end_fill()

def lua(t):
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.fillcolor("#FFFFFF")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

def chao(t):
    t.penup()
    t.goto(250, 0) 
    t.pendown()
    t.fillcolor("#0f2702") 
    t.begin_fill()
    for _ in range(2):
        t.forward(600) 
        t.right(90)
        t.forward(600) 
        t.right(90)
    t.end_fill()








    
main()
