import turtle

t = turtle.Turtle()

t.shape('turtle')

def draw_rectangle():
    """Draw rectangle."""
    for i in range(4):
        t.forward(100)
        t.left(90)

def goto(x, y):
    """Move turtle to x, y position."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_circle():
    """Draw a circle."""
    t.circle(60)
    
def goto_home():
    """Move turtle to home position."""
    t.penup()
    t.home()
    t.pendown()

draw_rectangle()
goto(22, 22)
draw_rectangle()
goto(44, 44)
draw_rectangle()
goto_home()
goto(-44, -44)
draw_circle()
goto(-66, -66)
draw_circle()
goto(-88, -88)
draw_circle()
goto_home()
