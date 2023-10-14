import math
import turtle

boki = int(turtle.numinput('Pytanie', 'Podaj liczbę boków'))

obwod = 1600
kat = 360 / boki
dlugosc_boku = obwod / boki

t = turtle.Turtle()
t.penup()
t.goto(-dlugosc_boku/2, -obwod/(2*math.pi))
t.pendown()

t.color('blue', 'yellow')
t.width(5)
t.begin_fill()
for i in range(boki):
    t.forward(dlugosc_boku)
    t.left(kat)
t.end_fill()

turtle.mainloop()
