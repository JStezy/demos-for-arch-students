import turtle
from random import randrange as ran
screen = turtle.Screen()

width = 500
screen.setup(width,width)
screen.bgcolor("black")
border = 200
yourspeed = 30
caught = True
movecount = 0
changespeed = 5
score = 0

def changeborder(size):
  global border
  b.clear()
  b.home()
  b.color("green")
  b.write(score,font=("Arial",20,"normal"))
  b.color("red")
  b.penup()
  b.goto(-size//2, size//2)
  b.pendown()
  b.speed(10)
  for x in range(4):
    b.forward(size)
    b.right(90)
  b.speed(0)
  b.penup()
  border = size

def gameover():
  global score
  t.hideturtle()
  t.home()
  t.write("Game Over. Score: " + str(score), font=("Arial",15,"normal"))


b = turtle.Turtle()
b.hideturtle()
b.speed(0)
b.pensize(10)
b.color("red")
b.penup()

def moveguy():
  global border
  global yourspeed
  global caught
  global score
  yourspeed = yourspeed + 5
  if caught:
    changeborder(border + 10)
    score = score + 1
  else:
    changeborder(border - 60)
  g.goto(ran(-border//2,border//2),ran(-border//2,border//2))
  caught = False

g = turtle.Turtle()
g.penup()
g.speed(9)
g.shape("circle")
g.color("blue")

t = turtle.Turtle()
t.speed(yourspeed)
t.shape("turtle")
t.color("white")
t.penup()

moveguy()


# keyboard functions
def goleft():
  t.left(10)

def goright():
  t.right(10)

def move():
  global border
  global yourspeed
  global caught
  global movecount
  global changespeed
  if t.distance(g) < 15:
    caught = True
    movecount = 0
    changespeed = changespeed*.95
    moveguy()
  pos = t.pos()
  xbound = (pos[0] > -border//2) and (pos[0] < border//2)
  ybound = (pos[1] > -border//2) and (pos[1] < border//2)
  if (not (xbound and ybound)):
    gameover()
    return
  t.forward(1)
  movecount += 1
  if movecount >= yourspeed*changespeed:
    movecount = 0
    changespeed = changespeed*.92
    caught = False
    moveguy()
  screen.ontimer(move,1000//yourspeed)


screen.onkey(goleft, "Left")
screen.onkey(goright, "Right")
screen.listen()

print("Use the left and right arrow keys to get the food before the border collapses!")

move()
