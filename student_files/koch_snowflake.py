import turtle

def koch_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, depth - 1)
        t.left(60)
        koch_snowflake(t, length, depth - 1)
        t.right(120)
        koch_snowflake(t, length, depth - 1)
        t.left(60)
        koch_snowflake(t, length, depth - 1)

t = turtle.Turtle()
t.speed(0)
t.color("blue")  # You can change this color
t.pensize(2)  # You can change line thickness
t.penup()
t.goto(-150, 150)
t.pendown()

koch_snowflake(t, 300, 3)
turtle.done()