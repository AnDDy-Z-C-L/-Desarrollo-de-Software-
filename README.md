![image](https://github.com/user-attachments/assets/9686a3b3-14ca-461d-ae70-b4f5d0c9b602)

# CARACTERISTICAS
# OBJETIVO PRINCIPAL DEL PROYECTO:

El objetivo principal de este proyecto es la creacion del juego SNAKE implementado: Mecánicas: Reglas del juego, crecimiento de la serpiente, colisiones, generación de comida, Interfaz Gráfica: Un diseño visual atractivo usando Turtle.

# DESCRIPCIÓN DEL PROYECTO: JUEGO SNAKE EN PYTHON CON TURTLE

El proyecto consiste en el desarrollo de un videojuego clásico del tipo Snake, implementado en el lenguaje de programación Python utilizando la biblioteca Turtle. El objetivo principal es crear un producto jugable, optimizado y visualmente atractivo, asegurando una experiencia de usuario fluida y entretenida.

El juego sigue la mecánica tradicional donde el jugador controla una serpiente que se mueve en un área delimitada, debe comer la comida para crecer y evitar colisionar con los bordes o su propio cuerpo.

# FUNCIONALIDADES PRINCIPALES

✅ MOVIMIENTO DE LA SERPIENTE

La serpiente se mueve automáticamente en la dirección establecida por el jugador.
Control mediante las teclas de dirección (arriba, abajo, izquierda, derecha).

✅ GENERACIÓN DE COMIDA

Se coloca comida en ubicaciones aleatorias dentro del área de juego.
Cuando la serpiente come la comida, su tamaño aumenta y la puntuación sube.

✅ DETECCIÓN DE COLISIONES

Si la serpiente choca contra los bordes de la pantalla, el juego termina.
Si la serpiente choca contra su propio cuerpo, también pierde.

✅ SISTEMA DE PUNTUACIÓN

Cada comida obtenida incrementa la puntuación.
Se muestra la puntuación en pantalla durante la partida.

✅ INTERFAZ GRÁFICA CON TURTLE

Dibujos de la serpiente y la comida usando Turtle.
Uso de colores y formas para mejorar la experiencia visual.

# FUNCIONES DE PROGRAMACIÓN UTILIZADAS

✅ get_player_name()

Utiliza tkinter para mostrar un cuadro de diálogo donde el jugador ingresa su nombre.
Si el jugador no ingresa un nombre, se le asigna "Jugador" por defecto.

✅ reset_food()

Genera coordenadas aleatorias dentro de los límites del juego y coloca la comida en una nueva posición.

✅ update_score()

Borra el marcador anterior y muestra el puntaje actualizado del jugador junto con el puntaje más alto.

✅ move()

Controla el movimiento de la serpiente en la dirección establecida.
Ajusta las coordenadas de la cabeza según la dirección actual.

✅ Funciones de control de movimiento

go_up() ↑ , go_down() ↓ , go_left() ← , go_right ➞ ()
Cambian la dirección de la serpiente asegurando que no se mueva en dirección opuesta.

✅ reset_game()

Reinicia el juego cuando el jugador pierde.
Actualiza el puntaje más alto si es necesario.
Limpia el cuerpo de la serpiente y la coloca en la posición inicial.
Pregunta al jugador si desea jugar de nuevo y maneja la respuesta.

✅ start_game()

Contiene el bucle principal del juego.
Maneja colisiones con los bordes y el propio cuerpo de la serpiente.
Detecta cuándo la serpiente come comida, añade segmentos al cuerpo y aumenta la velocidad.
Controla la actualización de la pantalla y la lógica de pausas con time.sleep(delay).


