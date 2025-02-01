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