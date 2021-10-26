import turtle

wn = turtle.Screen()

wn.title("Praveen")
wn.bgcolor("black")
wn.setup(width=800, height=600)  # height 600, the top y coordinate +300 and the bottom -300
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of the animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# paddle_a.shapesize(stretch_wid=5)
paddle_a.penup()  # turtle usually draw a line as they move , and we use penup as we dont need lines
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of the animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()  # turtle usually draw a line as they move , and we use penup as we dont need lines
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of the animation
ball.shape("circle")
ball.color("white")
ball.penup()  # turtle usually draw a line as they move , and we use penup as we dont need lines
ball.goto(0, 0)
ball.dx = 0.2  # Every time the ball moves , it moves by 2 pixel
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()  # we dont wanna see the turtle
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
