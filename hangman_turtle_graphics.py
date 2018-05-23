import random as r
import string
import turtle

# displays game status after each guess
def display_info(word, lives, guesses):
  print('\n')
  for x in range(len(word)):
    print(word[x]),
  print('\n')
  print('guessed letters: ' + str(guesses))
  print('')

# turtle function to draw gallows
def draw_gallows(tom):
  tom.pendown()
  tom.goto(-100,0)
  tom.goto(100,0)
  tom.goto(-50,0)
  tom.goto(-50,150)
  tom.goto(50,150)
  tom.goto(50,100)

# turtle function with logic to draw stick figure based on how many incorrect guesses the cpu has
def draw_body(tom, lives):
  if lives == 5:
    tom.circle(-15)
  elif lives == 4:
    tom.penup()
    tom.goto(tom.xcor(),tom.ycor() - 30)
    tom.pendown()
    tom.goto(tom.xcor(),tom.ycor() - 40)
  elif lives == 3:
    tom.penup()
    tom.goto(tom.xcor(), tom.ycor() + 40)
    tom.pendown()
    tom.goto(tom.xcor() + 15, tom.ycor() - 15)
  elif lives == 2:
    tom.penup()
    tom.goto(tom.xcor() - 15, tom.ycor() + 15)
    tom.pendown()
    tom.goto(tom.xcor() - 15, tom.ycor() - 15)
  elif lives == 1:
    tom.penup()
    tom.goto(tom.xcor() + 15, tom.ycor() - 25)
    tom.pendown()
    tom.goto(tom.xcor() - 15, tom.ycor() - 15)
  elif lives == 0:
    tom.penup()
    tom.goto(tom.xcor() + 15, tom.ycor() + 15)
    tom.pendown()
    tom.goto(tom.xcor() + 15, tom.ycor() -15)

# Guessing function which generates a totally random guess, with logic to avoid repeat guesses
# and input prompts to place correct guesses in their appropriate positions
def guess():
  global letters
  global lives
  global word
  global guesses
  global t
  # generate a guess
  guess = d[r.randint(1,26)]
  while(guess in guesses):
    guess = d[r.randint(1,26)]
  guesses.append(guess)
  correct = cleansed_input("Is \"" + guess + "\" in your word? (y/n)", ["y","n"], str)
  if correct == "y":
    done = False
    while(not done):
      pos = cleansed_input("Where does it go?", map(str, list(range(1,len(word)))), int) - 1
      word[pos] = guess
      letters = letters - 1
      done = cleansed_input("Any more places? (y/n)", ["y","n"], str)
      if done == "y":
        done = False
      else:
        done = True
  else:
    print("wrong guess.")
    lives = lives - 1
    draw_body(t, lives)

# function for cleansing user input
def cleansed_input(prompt, valid, type):
  response = None
  while not response:
    response = input(prompt)
    if response in valid:
      try:
        response = type(response)
        return response
      except ValueError as error:
        print(error)
    # get here only if there is a type error or invalid response
    print("invalid response\n")
    response = None

# set up the turtle graphics
t = turtle.Turtle()
t.hideturtle()
t.speed(7)
draw_gallows(t)

# letters of alphabet
d = dict(enumerate(string.ascii_lowercase, 1))

# gather information on the word from user, setup
letters = cleansed_input("How many letters are in your word?", map(str, list(range(1,50))), int)
word = []
for x in range(letters):
  word.append("_ ")
guesses = []
lives = 6

# gameplay- display info and guess until user or cpu wins
while(letters > 0 and lives > 0):
  display_info(word, lives, guesses)
  guess()

# deal with the aftermath
if letters == 0:
  print("I win! Good game.")
else:
  print("Ah man. I lost.")
