import turtle

boki = int(turtle.numinput('Pytanie', 'Podaj liczbę boków'))
t = turtle.Turtle()

for i in range(boki):
    t.forward(200)
    t.left(360 / boki)

turtle.mainloop()
