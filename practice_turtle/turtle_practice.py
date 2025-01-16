import turtle

def draw_turtle_shape():
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Turtle Shape Drawing")

    # Create a turtle object
    turtle_obj = turtle.Turtle()
    turtle_obj.shape("turtle")
    turtle_obj.speed(5)
    turtle_obj.color("green")

    # Draw the body (circle)
    turtle_obj.penup()
    turtle_obj.goto(0, -100)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(100)
    turtle_obj.color("green")
    turtle_obj.end_fill()

    # Draw the head
    turtle_obj.penup()
    turtle_obj.goto(0, 100)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(40)
    turtle_obj.color("green")
    turtle_obj.end_fill()

    # Draw the legs
    legs = [(-80, -60), (80, -60), (-80, -140), (80, -140)]
    for leg in legs:
        turtle_obj.penup()
        turtle_obj.goto(leg)
        turtle_obj.pendown()
        turtle_obj.begin_fill()
        turtle_obj.circle(30)
        turtle_obj.color("green")
        turtle_obj.end_fill()

    # Draw the tail
    turtle_obj.penup()
    turtle_obj.goto(0, -200)
    turtle_obj.pendown()
    turtle_obj.begin_fill()
    turtle_obj.circle(20)
    turtle_obj.color("green")
    turtle_obj.end_fill()

    # Finish
    turtle_obj.penup()
    turtle_obj.hideturtle()
    screen.mainloop()

# Call the function to draw the turtle shape
draw_turtle_shape()