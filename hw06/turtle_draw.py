# Turtle list program: prepared by Nachiket Dani
import turtle
import math


def main():
    # Create variables for star: side length & angle
    # Create variable for "n" dimension polygon that appears as a circle
    star_length = 500
    star_angle = 36
    """360 dimension polygon:"""
    polygon_to_circle = 360
    draw_circle(star_length, star_angle, polygon_to_circle)


# Function for drawing circle
def draw_circle(star_length, star_angle, polygon_to_circle):
    CIRCLE_ANGLE = 360
    """Polygon of side = arc_length
    Central angle for each side of polygon = arc_angle"""
    arc_length = 0
    arc_angle = CIRCLE_ANGLE/(polygon_to_circle)
    """Radius calculated based on cosine of bisected star angle"""
    radius = (star_length/2)/(math.cos(math.radians(star_angle/2)))
    """Calculate arc length from radius & arc angle (360/polygon_to_circle)"""
    arc_length = radius * (math.radians(arc_angle))

    # Variables set turtle co-ordinate for top of the circle if origin = (0,0)
    circletop_x = 0
    circletop_y = radius

    """Begin circle draw"""
    turtle.penup()
    turtle.setposition(circletop_x, circletop_y)
    turtle.pencolor('blue')
    turtle.fillcolor('cyan')
    turtle.pendown()
    turtle.begin_fill()
    for i in range(polygon_to_circle):
        turtle.forward(arc_length)
        turtle.right(arc_angle)
    turtle.end_fill()
    turtle.penup()
    draw_star(star_length, star_angle, radius)


def draw_star(star_length, star_angle, radius):
    STAR_SIDES = 5
    LINE_ANGLE = 180

    # Variables to set turtle co-ordinate for top apex of star
    star_top_x = 0
    star_top_y = radius

    turn_angle = LINE_ANGLE - star_angle

    """Begin star draw"""
    turtle.setposition(star_top_x, star_top_y)
    turtle.pencolor('red')
    turtle.fillcolor('yellow')
    turtle.pendown()
    turtle.right(turn_angle/2)
    turtle.begin_fill()
    for i in range(STAR_SIDES):
        turtle.forward(star_length)
        turtle.right(turn_angle)
    turtle.end_fill()
    turtle.penup()

    turtle.hideturtle()
    turtle.exitonclick()


main()
