import turtle
from random import choice, randint

# functions of movements rackets
def move_upl():
    y = racket_l.ycor() + 10
    if y > 310:
        y = 310
    racket_l.sety(y)


def move_downl():
    y = racket_l.ycor() - 10
    if y < -310:
        y = -310
    racket_l.sety(y)

def move_upr():
    y = racket_r.ycor() + 10
    if y > 310:
        y = 310
    racket_r.sety(y)

def move_downr():
    y = racket_r.ycor() - 10
    if y < -310:
        y = -310
    racket_r.sety(y)


# coordinates for painting area
alu_p = (-480, 360)
ald_p = (-480, -360)
aru_p = (480, 360)
ard_p = (480, -360)


# Title
window = turtle.Screen()
window.title("Pong")
window.setup(width = 1280.0, height = 1024.0)
window.bgcolor('blue')



# painting area
border = turtle.Turtle()
border.speed(0)
border.color('black')
border.begin_fill()
border.goto(alu_p)
border.goto(ald_p)
border.goto(ard_p)
border.goto(aru_p)
border.goto(alu_p)
border.end_fill()

# painting net
border.goto(0, 360)
border.color('white')
border.setheading(270)

for i in range(29):
    if i%2 == 0:
        border.forward(24.8)
    else:
        border.up()
        border.forward(24.8)
        border.down()

border.hideturtle()


# painting racket_l
racket_l = turtle.Turtle()
racket_l.color('white')
racket_l.shape('square')
racket_l.shapesize(stretch_len = 1, stretch_wid = 5)
racket_l.penup()
racket_l.goto(-460,0)

# control racket_l
window.listen()
window.onkeypress(move_upl, "w")
window.onkeypress(move_downl, "s")

# printing racket_r
racket_r = turtle.Turtle()
racket_r.color('white')
racket_r.shape('square')
racket_r.shapesize(stretch_len = 1, stretch_wid = 5)
racket_r.penup()
racket_r.goto(460,0)


# Scores
FONT = ("Arial", 50)
score_l = 0
sl = turtle.Turtle(visible = False)
sl.color('white')
sl.penup()
sl.setposition(-70, 290)
sl.write(score_l, font = FONT)

score_r = 0
sr = turtle.Turtle(visible = False)
sr.color('white')
sr.penup()
sr.setposition(30, 290)
sr.write(score_r, font = FONT)



# control racket_r
window.onkeypress(move_upr, "i")
window.onkeypress(move_downr, "k")


# painting a ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)

# Moving ball
ball.dx = choice([4, 3, 2, -2, -3, -4])
ball.dy = choice([4, 3, 2, -2, -3, -4])
ball.penup()
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)

    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 350:
        ball.dy = -ball.dy

    if ball.ycor() <= -350:
        ball.dy = -ball.dy

    if ball.xcor() >= 470:
        score_l += 1
        sl.clear()
        sl.write(score_l, font = FONT)
        ball.goto(0, randint(-150,150))
        ball.dx = choice([2, 3, 4])
        ball.dy = choice([2, 3, 4])

    if ball.xcor() <= -470:
        score_r += 1
        sr.clear()
        sr.write(score_r, font = FONT)
        ball.goto(0, randint(-150,150))
        ball.dx = choice([-4, -3, -2])
        ball.dy = choice([-4, -3, -2])

    if ((score_r == 10) or (score_l == 10)):
        rest.write(rest, font = FONT)
        if window.onkeypress(" "):
            window.restart()

    #calculatings for if
    yb = ball.ycor()
    xb = ball.xcor()

    xl = racket_l.xcor()
    yl = racket_l.ycor()

    xr = racket_r.xcor()
    yr = racket_r.ycor()

    if ((xb >= xl - 15) and (xb <= xl + 15) and (yb >= yl - 50) and (yb <= yl + 50)):
        ball.dx = choice([2, 3, 4])
        ball.dy = choice([2, 3, 4])

    if  ((xb >= xr - 15) and (xb <= xr + 15) and (yb >= yr - 50) and (yb <= yr + 50)):
        ball.dx = choice([-2, -3, -4])
        ball.dy = choice([-2, -3, -4])

window.mainloop()
