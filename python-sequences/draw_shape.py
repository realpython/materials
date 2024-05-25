import turtle

from shape import ShapePoints

triangle = ShapePoints([(100, 100), (-200, 100), (-200, -200)])

# Draw the shape using turtle graphics
turtle.penup()
# Move to the first point
turtle.setposition(triangle[0])
turtle.pendown()
# Draw lines to the other points
for point in triangle[1:]:
    turtle.setposition(point)

turtle.done()
