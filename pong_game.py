import turtle

screen = turtle.Screen()
screen.title("Day 22 – Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle A (left)
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (right)
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6
ball.dy = 0.6

# Scoreboard
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"A: {score_a}  B: {score_b}", align="center", font=("Arial", 24, "normal"))


def update_score():
    pen.clear()
    pen.write(f"A: {score_a}  B: {score_b}", align="center", font=("Arial", 24, "normal"))


def paddle_a_up():
    if paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 20)

def paddle_a_down():
    if paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    if paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 20)

def paddle_b_down():
    if paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 20)


screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


def game_loop():
    global score_a, score_b

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top / Bottom wall bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right wall – A scores
    if ball.xcor() > 390:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Left wall – B scores
    elif ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle B collision
    if (340 < ball.xcor() < 360) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    # Paddle A collision
    if (-360 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    screen.update()
    screen.ontimer(game_loop, 5)


game_loop()
screen.mainloop()
