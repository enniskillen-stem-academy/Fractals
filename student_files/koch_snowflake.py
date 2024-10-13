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
t.speed(1)  # Change the speed: 0 is fastest, 1-10 are slower
t.penup()
t.goto(-150, 150)  # You can adjust the starting position of the drawing by changing these coordinates
t.pendown()

koch_snowflake(t, 300, 3)  # Try changing the value of 'depth' to see how it affects the complexity of the pattern
turtle.done()