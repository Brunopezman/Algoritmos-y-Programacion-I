# Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos instantes de tiempo (números enteros expresados en segundos), con la condición desde < hasta.
# Implementar el método duracion que devuelve la duración en segundos del intervalo.
# Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo resultante de la intersección entre ambos, o lanzar una excepción si la intersección es nula
# Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo intervalo resultante de la unión entre ambos.

class Intervalo:
    """Representacion de un intervalo entre dos instantes de tiempo expresados en segundos"""
    def __init__(self, desde, hasta) -> None:
        "Constructor de un Intervalo. Desde y Hasta son numeros enteros con Desde < Hasta"
        if desde < hasta:
            self.desde = desde
            self.hasta = hasta
        else:
            raise ValueError("El valor 'desde' debe ser menor que 'hasta'")
    
    def duracion(self):
        return self.hasta - self.desde
    
    def interseccion(self,otro_intervalo):

        if not self.hasta <= otro_intervalo.hasta or self.hasta <= otro_intervalo.desde :
            raise ValueError("No hay intersección entre los intervalos.")
        else:
            interseccion_desde = max(self.desde, otro_intervalo.desde)
            interseccion_hasta = min(self.hasta, otro_intervalo.hasta)
            return Intervalo(interseccion_desde, interseccion_hasta)

    def union(self, otro_intervalo):
        if self.hasta < otro_intervalo.desde or self.desde > otro_intervalo.hasta:
            raise ValueError("Los intervalos no son adyacentes ni intersectan")
        else:
            union_desde = min(self.desde, otro_intervalo.desde)
            union_hasta = max(self.hasta, otro_intervalo.hasta)
            return Intervalo(union_desde, union_hasta)
        
intervalo1 = Intervalo(10,30)
intervalo2 = Intervalo(25,40)

try:
    interseccion = intervalo1.interseccion(intervalo2)
    print("Interseccion:", interseccion.desde, "-", interseccion.hasta)
except ValueError as e:
    print('Error:', e)

try:
    union = intervalo1.union(intervalo2)
    print("Union:", union.desde, "-", union.hasta)
except ValueError as e:
    print("Error:", e)