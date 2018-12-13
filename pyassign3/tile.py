#!/usr/bin/env python3

"""tile.py: tile the wall of the size m*n by bricks of size a*b.

__author__ = "Xiaxinyi"
__pkuid__  = "1700017788"
__email__  = "1700017788@pku.edu.cn"
"""

import turtle


def gen_ins(m, a, b, r, c, ins, sol):
    """
    generate the instructor
    :param m: the length of the wall
    :param a: the length of the brick
    :param b: the width of the brick
    :param r: the row position
    :param c: the column position
    :param ins:the instructor of the brick
    :param sol:one solution
    :return:renewed instructor
    """
    brick = ()
    for j in range(r, r + b):
        for k in range(c, c + a):
            piece = j * m + k
            ins[piece] = 1
            brick = brick + (piece,)
    sol.append(brick)


def judging(m, n, a, b, r, c, ins):
    """
    judge whether it can be tiled
    :param m: length of the wall
    :param n: width of the wall
    :param a: length of the brick
    :param b: width of the brick
    :param r: row position
    :param c: column position
    :param ins: instructor
    :return: True of False it can be tiled
    """
    if (c + a) > m or (r + b) > n:
        return False
    for j in range(r, r + b):
        for k in range(c, c + a):
            if ins[j * m + k] == 1:
                return False
    return True


def tile(m, n, a, b, r, c, all=[], ins=[], sol=[]):
    """
    tile the wall
    :param m: length of the wall
    :param n: width of the wall
    :param a: length of the brick
    :param b: width of the wall
    :param r: row position
    :param c: colomn position
    :param all: all the solution
    :param ins: instructor
    :param sol: one solution
    :return: all the solution
    """
    if ins==[]:
        ins = [0] * (m * n)
    if c == m:
        r += 1
        c = 0
    if (0 not in ins) and (sol not in all):
        all.append(sol[:])
    if ((r * m) + c) < (m * n) and ins[r * m + c] == 1:
        tile(m, n, a, b, r, c + 1, all, ins, sol)
    else:
        if judging(m, n, a, b, r, c, ins):
            inst= ins[:]
            solu = sol[:]
            gen_ins(m, a, b, r, c, inst, solu)
            tile(m, n, a, b, r, c + 1, all, inst, solu)
        if judging(m, n, b, a, r, c, ins):
            inst = ins[:]
            solu = sol[:]
            gen_ins(m, b, a, r, c, inst, solu)
            tile(m, n, a, b, r, c + 1, all, inst, solu)


def print_solution(m, n, solution):
    """
    visualize the solution
    :param m: length of the wall
    :param n: width of the wall
    :param solution: one solution
    :return: visualization of one solution
    """
    t = turtle.Turtle()
    t.color('black')
    t.speed(0)
    t.pensize(5)
    for brickplace in solution:
        leftup = brickplace[0]
        rightdown = brickplace[-1]
        lux = int(leftup // m)
        luy = int(leftup % m)
        rdx = int(rightdown // m) + 1
        rdy = int(rightdown % m) + 1
        t.up()
        t.goto((lux * 50)-200, (luy * 50)-200)
        t.down()
        t.goto((lux * 50)-200, (rdy * 50)-200)
        t.goto((rdx * 50)-200, (rdy * 50)-200)
        t.goto((rdx * 50)-200, (luy * 50)-200)
        t.goto((lux * 50)-200, (luy * 50)-200)


def visual(m,n,solution):
    """
    visualize the background and one solution
    :param m: length of the wall
    :param n: width of the wall
    :param solution: one solution
    :return: the outcome
    """
    wn=turtle.Screen()
    bob=turtle.Turtle()
    bob.color('yellow')
    bob.speed(0)
    bob.pensize(10)
    for j in range(m):
        for i in range(n):
            bob.up()
            bob.goto(i*50-200,j*50-200)
            bob.down()
            bob.goto((i+1)*50-200,j*50-200)
            bob.goto((i+1)*50-200,(j+1)*50-200)
            bob.goto(i*50-200,(j+1)*50-200)
            bob.goto(i*50-200,j*50-200)
    print_solution(m, n, solution)
    wn.exitonclick()



def main():
    """
    main module
    """
    m = int(input("input the length of the wall:"))
    n = int(input("input the width of the wall:"))
    a = int(input("input the length of the brick:"))
    b = int(input("input the width of the brick:"))
    all = []
    ins=[]
    sol=[]
    tile(m, n, a, b, 0, 0, all, ins, sol)
    print('Solutions are' )
    for s in all:
        print(s)
    print('There are ' + str(len(all)) + ' kinds of solution. ')
    if all != []:
        order = int(input('Input number of 0-'+str(len(all)-1)))
        visual(m, n, all[order])


if __name__ == '__main__':
    main()
