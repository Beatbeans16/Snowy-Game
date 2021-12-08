## treeGame_Smithson.py
from itertools import count
from re import escape
import turtle as trtl
import random as r

import pygame
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('music.crdownload')
mixer.music.play()

#-----setup-----
tree_image = "tree.gif" # Store the file name of your shape

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(tree_image) # Make the screen aware of the new file
wn.bgpic("Snow.gif")

tree_1 = trtl.Turtle()
tree_2 = trtl.Turtle()
tree_3 = trtl.Turtle()
tree_4 = trtl.Turtle()
tree_5 = trtl.Turtle()
drawer_1 = trtl.Turtle()
drawer_2 = trtl.Turtle()
drawer_3 = trtl.Turtle()
drawer_4 = trtl.Turtle()
drawer_5 = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()

#tree penup function
tree_1.penup()
tree_2.penup()
tree_3.penup()
tree_4.penup()
tree_5.penup()
drawer_1.penup()
drawer_2.penup()
drawer_3.penup()
drawer_4.penup()
drawer_5.penup()
score_writer.penup()
counter.penup()

#tree hideturtle function
tree_1.hideturtle()
tree_2.hideturtle()
tree_3.hideturtle()
tree_4.hideturtle()
tree_5.hideturtle()
drawer_1.hideturtle()
drawer_2.hideturtle()
drawer_3.hideturtle()
drawer_4.hideturtle()
drawer_5.hideturtle()
score_writer.hideturtle()
counter.hideturtle()

#score function
score_writer.goto(200, -150)
counter.goto(-200, -150)
score = 0

font_setup = ('Arial', 20, 'normal')

#timer function
timer = 10
timer_up = False
counter_interval = 1000

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_trees_1(active_tree):
  treex = r.randint(-150, 150)
  treey = r.randint(-50, 150)
  active_tree.goto(treex,treey)
  active_tree.showturtle()
  active_tree.shape(tree_image)
  global letter_1
  letter_1 = r.choice(letters)
  letters.remove(letter_1)
  draw_letter_1(active_tree.xcor(), active_tree.ycor())
  wn.update()
  wn.onkeypress(drop_tree_1, letter_1)

#draw letter function
def draw_letter_1(x, y):
  drawer_1.color("white")
  drawer_1.goto(x - 18, y - 40)
  drawer_1.write(letter_1, font=("Arial", 55, "bold"))

#drop tree function
def drop_tree_1():
  if timer_up == False:
    tree_1.goto(tree_1.xcor(),-150)
    tree_1.hideturtle()
    drawer_1.clear()
    draw_trees_1(tree_1)
    draw_letter_1(tree_1.xcor(), tree_1.ycor())
    update_score()
  else:
    tree_1.hideturtle()
    drawer_1.clear()

#update score function
def update_score():
  score_writer.clear()
  global score
  score+= 1
  score_writer.write(score, font=font_setup)

#timer function
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#-----function calls-----
draw_trees_1(tree_1)

wn.listen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()