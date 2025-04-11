class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

              
    def mueve_derecha(self, distancia):
        self._punto_a.x += distancia
        self._punto_b.x += distancia
     
    def mueve_izquierda(self, distancia):
        self._punto_a.x -= distancia
        self._punto_b.x -= distancia
        
    def mueve_arriba(self, distancia):
        self._punto_a.y += distancia
        self._punto_b.y += distancia
        
    def mueve_abajo(self,distancia):
        self._punto_a.y -= distancia
        self._punto_b.y -= distancia
        
        
    
    def __str__(self):
        return f"Línea de {self._punto_a} a {self._punto_b}"
    
    
punto1 = Punto(1,2)
punto2 = Punto(3,4)

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
