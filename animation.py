
def turtle_maze():
    """ 
    An animation that creates a maze and then has a turtle escape it!
    """
    
    import turtle
    wn = turtle.Screen()

    maze = turtle.Turtle()

    distance = 10
    for line in range(30):
        maze.forward(distance)
        maze.right(90)
        distance = distance + 20

    escapee = turtle.Turtle()
    escapee.shape('turtle')
    escapee.color('green')
    escapee.penup()
    escapee.forward(-10)
    escapee.right(-90)
    distance = 20
    for turt in range(27):
        escapee.forward(distance)
        escapee.right(90)
        distance = distance + 20
    wn.exitonclick()
