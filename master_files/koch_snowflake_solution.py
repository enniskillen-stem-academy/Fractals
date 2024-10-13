import turtle

# Function to draw the Koch snowflake fractal
def koch_snowflake(t, length, depth):
    if depth == 0:
        t.forward(length)  # Draw a straight line if depth is 0
    else:
        length /= 3.0  # Divide the length by 3 for each iteration
        koch_snowflake(t, length, depth - 1)  # Draw the first segment
        t.left(60)  # Turn left to create the 'peak' of the snowflake
        koch_snowflake(t, length, depth - 1)  # Draw the second segment
        t.right(120)  # Turn right to create the 'valley'
        koch_snowflake(t, length, depth - 1)  # Draw the third segment
        t.left(60)  # Turn left to complete the peak
        koch_snowflake(t, length, depth - 1)  # Draw the final segment

# Function to draw the complete snowflake with three sides
def draw_full_snowflake(t, length, depth):
    for _ in range(3):
        koch_snowflake(t, length, depth)  # Draw one side of the snowflake
        t.right(120)  # Turn right to position for the next side

t = turtle.Turtle()
t.speed(0)  # Set the speed to maximum
t.penup()
t.goto(-150, 150)  # Move the turtle to the starting position
t.pendown()

draw_full_snowflake(t, 300, 4)  # Draw the complete snowflake with depth 4
turtle.done()  # Finish the drawing and keep the window open