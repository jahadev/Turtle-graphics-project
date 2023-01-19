from turtle import Turtle, Screen
import random

colors = [
    "CornflowerBlue", "light coral", "powder blue", "medium aquamarine",
    "DarkOrchid", "IndianRed", "LightSeaGreen", "SeaGreen", "wheat",
    "SlateGray"
]
angles = [0, 90, 180, 270]

color_palette = [(233, 239, 246), (246, 239, 242), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

tim = Turtle()
tim.shape("classic")
screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.colormode(255)


def draw_shapes():
    tim.speed("slow")
    tim.pensize(2)
    for num_sides in range(3, 11):
        tim.color(random.choice(colors))
        angle = 360 / num_sides
        for _ in range(num_sides):
            tim.forward(100)
            tim.right(angle)


def random_walk():
    tim.speed("fastest")
    tim.pensize(15)
    for _ in range(300):
        tim.color(random.choice(colors))
        tim.forward(30)
        tim.setheading(random.choice(angles))


def draw_spirograph():
  tim.speed("fastest")
  tim.pensize(1)
  for angle in range(0, 361, 5):
    tim.color(random.choice(colors))
    tim.seth(angle)
    tim.circle(100)

    
def dot_painting():
  tim.speed("fastest")
  tim.hideturtle()
  tim.penup()
  for y in range(-250, 200, 50):
    tim.setposition(-250, y)
    for x in range(10):
      tim.pendown()
      tim.dot(20, random.choice(color_palette))
      tim.penup()
      tim.fd(50)


draw_shapes()
screen.reset()
random_walk()
screen.reset()
draw_spirograph()
screen.reset()
dot_painting()
