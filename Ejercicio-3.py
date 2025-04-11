class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        # muestra el punto como texto (x, y)
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, punto_a, punto_b):
        # guarda los dos puntos que forman la línea
        self._punto_a = punto_a
        self._punto_b = punto_b

              
    def mueve_derecha(self, distancia):
        # mueve la línea a la derecha sumando a x
        self._punto_a.x += distancia
        self._punto_b.x += distancia
     
    def mueve_izquierda(self, distancia):
        # mueve la línea a la izquierda restando a x
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        # mueve la línea hacia arriba sumando a y
        self._punto_a.y += distancia
        self._punto_b.y += distancia
        
    def mueve_abajo(self,distancia):
        # mueve la línea hacia abajo restando a y
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
        
        
    
    def __str__(self):
        # muestra la línea como texto con sus dos puntos
        return f"Línea de {self._punto_a} a {self._punto_b}"
    
# se crean dos puntos y una línea entre ellos
punto1 = Punto(1,2)
punto2 = Punto(3,4)

# se mueve la línea en diferentes direcciones
linea = Linea(punto1,punto2)
print(linea)

linea.mueve_derecha(3)
print(linea)

linea.mueve_izquierda(1)
print(linea)

linea.mueve_arriba(2)
print(linea)

linea.mueve_abajo(3)
print(linea)
