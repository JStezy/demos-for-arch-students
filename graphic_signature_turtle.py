from turtle import Turtle, Screen
import string
d = dict(enumerate(string.ascii_lowercase, 1))

t = Turtle()
s = Screen()
s.setup(500,500)
t.hideturtle()
t.speed('fastest')

questions = ["What is your first name?","What is your last name?","How old are you? (enter a number)",
  "What is your favorite color? (primary/secondary colors only)","Second favorite color?"]

answers = []

for q in questions:
  answers.append(input(q).lower())

lengths = []
for let in answers[0]:
  lengths.append((ord(let)-96)*10)

angles = []
for let in answers[1]:
  angles.append((ord(let)-96)*10)

sides = 100*int(answers[2])

s.bgcolor(answers[3])

t.color(answers[4])

for x in range(sides):
  t.fd(lengths[x%len(lengths)])
  t.circle(angles[x%len(angles)]/3)
  t.home()
  t.left(angles[x%len(angles)])
