import turtle
import time
import random
import tkinter as tk 
from tkinter import simpledialog, messagebox
#Definir función para pedir el nombre al jugador

def get_player_name():
    root= tk.Tk()
    root.withdraw()
    playername= simpledialog.askstring("Juagador", "¿Cual es tu nombre", parent=root)
    if not playername:
        playername= "Jugador"
    return playername
player_name = get_player_name()

#Configuración de la pantalla del Juego

win=turtle.Screen()
win.title("JUEGO DE LA SERPIENTE - Turtle")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)
turtle.mainloop()
# Coordenadas para colisión con las paredes (ajustadas para ampliar el área de colisión)
border_x = 600  # Aumentamos el límite horizontal
border_y = 600  # Aumentamos el límite vertical

# Snake (cabeza)
snake = turtle.Turtle()
snake.speed(0)
snake.shape("circle") 
snake.color("lime")  
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Comida
food = turtle.Turtle()
food.speed(0)
food.shape("square")  #
food.color("red")
food.penup()

# Inicializamos la comida en una posición aleatoria pero dentro del área de juego
def reset_food():
    x = random.randint(-border_x + 20, border_x - 20)
    y = random.randint(-border_y + 20, border_y - 20)
    food.goto(x, y)

reset_food()

# Cuerpo de la serpiente
body = []

# Marcador de puntaje
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)  # Ajustamos la posición para que no se sobreponga con la comida

# Función para actualizar el puntaje
def update_score():
    score_display.clear()
    score_display.write(f"{player_name} - Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Funciones de movimiento
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

def go_up():
    if snake.direction != "down":  # Evita que se mueva hacia abajo cuando está moviéndose hacia arriba
        snake.direction = "up"

def go_down():
    if snake.direction != "up":  # Evita que se mueva hacia arriba cuando está moviéndose hacia abajo
        snake.direction = "down"

def go_left():
    if snake.direction != "right":  # Evita que se mueva hacia la derecha cuando está moviéndose hacia la izquierda
        snake.direction = "left"

def go_right():
    if snake.direction != "left":  # Evita que se mueva hacia la izquierda cuando está moviéndose hacia la derecha
        snake.direction = "right"

# Controles del teclado

win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")
