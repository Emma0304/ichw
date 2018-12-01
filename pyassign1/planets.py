#!/usr/bin/env python3

"""planets.py: movements of planets in solar system.

__author__ = "Xiaxinyi"
__pkuid__  = "1700017788"
__email__  = "1700017788@pku.edu.cn"
"""


import turtle
import math


def genturtle():
    """
    generate the planets in the original position
    :return: original planets
    """
    for k in sequences.items():
        planets.append(k)
    for i in range(0,8):
        planets[i]=turtle.Turtle()
        planets[i].penup()
        planets[i].color(planetcolor(str(i+1)))
        planets[i].shape("circle")
        planets[i].shapesize(radius[i], radius[i], 2)
        planets[i].fd(20*(i+1))
        planets[i].pendown()


def planetcolor(starsequence):
   """
   generate the color of planets
   :param starsequence: the sequence of planets in the list of planets
   :return:
   """
   colors = {'1': 'gold',
             '2': 'tan',
             '3': 'blue',
             '4': 'orange',
             '5': 'gray',
             '6': 'red',
             '7': 'paleturquoise',
             '8': 'deepskyblue',
             }
   starcolor=colors[starsequence]
   return starcolor


def planetmove():
    """
    make the planets move
    :return: the moving planets
    """
    theta=0
    genturtle()
    while True:
        for n in range(0,8):
            planets[n].goto(20*(n+1)*math.cos(theta/(n+1)),10*math.sqrt(4*(n+1)**2-3)*math.sin(theta/(n+1)))
            theta=theta+0.01


def sun():
    """
    generate sun
    :return: turtle of sun
    """
    sun = turtle.Turtle()
    sun.penup()
    sun.goto(10, 0)
    sun.pendown()
    sun.color('#FF0000')
    sun.shape('circle')
    sun.shapesize(0.3, 0.3)
    return


def start():
    """
    start overall movement
    :return: overall movement
    """
    wn=turtle.Screen()
    wn.bgcolor("#191970")
    wn.title("Solar System")
    sun()
    planetmove()


def main():
	"""main model
	"""
	# the sequence of solar system
	sequences = {'mercury': 1,
                 'venus': 2,
                 'earth': 3,
                 'mars': 4,
                 'jupiter': 5,
                 'saturn': 6,
                 'uranus': 7,
                 'neptune': 8,
                 }
								 
								 
	# the list of planets
	planets=[]
	# the radius of planets
	radius = [0.2, 0.4, 0.4, 0.3, 0.6, 0.6, 0.2, 0.1]
    start()


if __name__ == '__main__':
    main()
