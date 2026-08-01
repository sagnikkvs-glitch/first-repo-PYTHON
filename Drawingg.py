import turtle
screen= turtle.Screen()
screen.bgcolor("black")
screen.title("Neon colors")
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

x=int(input("please enter the number of times yu want to repeate the funtion: " ))

petal_colors=["cyan","magenta","yellow","lime","deepskyblue","deeppink"]

for i in range(x):
    board.color(
            petal_colors[i % len(petal_colors)], petal_colors[(i + 2) % len(petal_colors)]
        )
    
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
        board.end_fill()
        board.right(10)
    
turtle.done()
    
    