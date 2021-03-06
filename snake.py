"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector
import random #Importa el modulo random de python para utilizar la funcion choice

#Codigo Modificado por: Ariel Campos Hernández
#Autor 1:Juan Pablo Elorriaga Gaitán
#Autor 2: Ariel Campos Hernández

food = vector(0, 0)    #Un vector
snake = [vector(10, 0)]    #Una serie de vectores
aim = vector(0, -10)
dir1 = vector(0, -5)
dir2 = vector(0, 5)
dir3 = vector(-5, 0)
dir4 = vector(5, 0) #Se definen 4 diferentes direcciones (arriba, abajo, izquierda y derecha)
rd = [dir1, dir2, dir3, dir4] #Se define una lista con las 4 posibles direcciones en las que se moverá la comida
rd1 = random.choice(rd) #Se utiliza la función choice del modulo random para que cada vez la comiuda se mueva en una dirección distinta

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    food.move(rd1) #Se aplica la misma funcion de movimiento a la comida

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    if not inside(food): #Si la comida sale del rango, entonces esta regresará a la posición (0, 0) y continuará moviendose desde ahi
        food.x=0
        food.y=0
    
    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, col1)

    square(food.x, food.y, 9, col2)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
col=['yellow','blue','purple','green','orange']   #Lista para seleccionar color
col1=random.choice(col)    #Selecciona un color al azar de la lista para serpiente
col2=random.choice(col)    #Selecciona un color al azar de la lista para comida
while col1==col2:    #Solucion para color repetido
        col1=random.choice(col)
        col2=random.choice(col)
hideturtle()
tracer(False)
listen()    #Escuchar los eventos del teclado

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
