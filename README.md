# unab_pa_tp_3
Franco Alburquerque - Programacion Avanzada COM3.
# Ejercicio 2

# Crear la clase Punto con dos atributos x e y (ambos numéricos),
# con el correspondiente constructor que recibe ambos valores.

# Definir los siguientes métodos:

# - eje_x(): indica si el punto está sobre el eje X (es decir, si y == 0).
# - eje_y(): indica si el punto está sobre el eje Y (es decir, si x == 0).
# - impresion(): devuelve una representación en string del punto (x, y).
# - opuesto(): devuelve un nuevo punto con los valores de x e y cambiados de signo.
# - (Opcional) Cualquier otro método que se considere importante.


# Ejercicio 3

# Definir una clase Linea con dos atributos: _punto_a y _punto_b.
# Son dos puntos por los que pasa la línea en un espacio de dos dimensiones.

# La clase debe incluir los siguientes métodos:

# - __init__(punto_a: Punto, punto_b: Punto):
#   Constructor que recibe como parámetros dos objetos de la clase Punto,
#   que se usan para inicializar los atributos.

# - mueve_derecha(distancia: float):
#   Desplaza la línea a la derecha la distancia indicada.

# - mueve_izquierda(distancia: float):
#   Desplaza la línea a la izquierda la distancia indicada.

# - mueve_arriba(distancia: float):
#   Desplaza la línea hacia arriba la distancia indicada.

# - mueve_abajo(distancia: float):
#   Desplaza la línea hacia abajo la distancia indicada




# Ejercicio 4

# Desarrollar una clase Cancion con los siguientes atributos:

# - titulo: una variable String que guarda el título de la canción.
# - autor: una variable String que guarda el autor de la canción.

# Métodos:

# - __init__(titulo: str, autor: str):
#   Constructor que recibe como parámetros el título y el autor de la canción (en ese orden).

# - get_titulo():
#   Devuelve el título de la canción.

# - get_autor():
#   Devuelve el autor de la canción.

# - set_titulo(nuevo_titulo: str):
#   Establece un nuevo título para la canción.

# - set_autor(nuevo_autor: str):
#   Establece un nuevo autor para la canción.


# Ejercicio 5

# Crear una clase Libro que modele la información que se mantiene en una biblioteca sobre cada libro.

# Atributos:
# - título: str
# - autor: Persona (usar la clase Persona)
# - ISBN: str
# - páginas: int
# - edición: str
# - editorial: str
# - lugar: str (ciudad y país en un solo string o como prefieras dividirlo)
# - fecha_edicion: str (representada como texto)

# Métodos:
# - Getters y setters para cada atributo.
# - leer_informacion(): método que solicita al usuario ingresar todos los datos del libro.
# - mostrar_informacion(): método que muestra todos los datos del libro de forma ordenada.
