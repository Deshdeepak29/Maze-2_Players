import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("sknkfkf")
wn.setup(600,600)

class pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
    
    def mup(self):
        self.goto(self.xcor(),self.ycor()+24)
    def mdown(self):
        self.goto(self.xcor(),self.ycor()-24)
    def mleft(self):
        self.goto(self.xcor()-24,self.ycor())
    def mright(self):
        self.goto(self.xcor()+24,self.ycor())

class player2(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("Red")
        self.penup()
        self.speed(0)

    def rup(self):
        self.goto(self.xcor(),self.ycor()+24)
    def rdown(self):
        self.goto(self.xcor(),self.ycor()-24)
    def rleft(self):
        self.goto(self.xcor()-24,self.ycor())
    def rright(self):
        self.goto(self.xcor()+24,self.ycor())

levels=[]
#We can create Pattern of maze here using "X", q and p are player 
level1 = [
    "X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X            q p               XXXXXXXXXXXXXXXXXXXXXX",
    "X  X  XXXXXXXXXX  XX   XX  XX  XXX               ",
    "X  X  X       XX  XX   XX  XX  XXX  XX  XX  XXXX",
    "X     XX  XX  XX  XX   XX  XX  XXX  XX  XX  XXXX",
    "X  X  X       XX  XX   XX  XX  XXX  XX  XX  XX",
    "X  X     XXXXXXX      XXXXXX            XX  XXXX",
    "XXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
   
]

levels.append(level1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x= -552 + (x*24)
            screen_y= 168 - (y*24)

            if character=="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
            if character=="p":
                pen.goto(screen_x,screen_y)
            if character=="q":
                pen.goto(screen_x,screen_y)
                    
pen = pen()
player=player()
player2=player2()


setup_maze(levels[0])
#Player1 Controls W A S D
turtle.listen()
turtle.onkey(player.mleft,"a")
turtle.onkey(player.mright,"d")
turtle.onkey(player.mup,"w")
turtle.onkey(player.mdown,"s")

#player2 settings
#Player 2 Control - Arrow keys
turtle.listen()
turtle.onkey(player2.rleft,"Left")
turtle.onkey(player2.rright,"Right")
turtle.onkey(player2.rup,"Up")
turtle.onkey(player2.rdown,"Down")

wn.tracer(0)

while True:
    wn.update()
