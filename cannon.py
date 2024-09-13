from random import randrange
from turtle import *

from freegames import vector
#se importan las librerías necesarias

ball = vector(-200, -200 # posición de la bola
speed = vector(0, 0) # velocidad inicial, al ser tiro parabólico es 0
targets = []


def tap(x, y):
    # responde a un clic
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
# verifica si la coordenada está dentro de los límites
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    # dibuja la bola y los objetos
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    # mueve la bola y los objetivos
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.25 #Asi es mas rapido

    if inside(ball):
        speed.y -= 0.35 # cambio de velocidad para simular gravedad
        ball.move(speed)
    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    for target in targets:
        if not inside(target):  #en caso de que el objetivo salga de rango
            target.x = 200       #reposicionar en el borde derecho
            target.y = randrange(-150, 150)  # Nueva posición aleatoria

    if not inside(ball):  # si la bola sale de la pantalla la guarda en un punto en específico afuera
        ball.x = -200
        ball.y = -200

    draw()

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
