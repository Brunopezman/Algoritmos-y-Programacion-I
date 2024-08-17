"""
Escribir una clase TorreDeControl que modele el trabajo de una torre de control de
un aeropuerto con una pista de aterrizaje. Los aviones que están esperando para aterrizar tienen
prioridad sobre los que están esperando para despegar. La clase debe funcionar conforme al
siguiente ejemplo:
>>> torre = TorreDeControl()
>>> torre.nuevo_arribo('AR156')
>>> torre.nueva_partida('KLM1267')
>>> torre.nuevo_arribo('AR32')
>>> torre.ver_estado()
Vuelos esperando para aterrizar: AR156, AR32
Vuelos esperando para despegar: KLM1267
>>> torre.asignar_pista()
El vuelo AR156 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo AR32 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo KLM1267 despegó con éxito.
>>> torre.asignar_pista()
No hay vuelos en espera.

"""
class _Nodo:

    def __init__(self, dato) -> None:
        self.dato = dato
        self.prox = None

class TorreDeControl:

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None

    def nuevo_arribo(self, avion):
        nuevo = _Nodo(avion)
        if not self.ultimo:
            self.ultimo.prox = nuevo
        else:
            self.primero = nuevo 
            self.ultimo = nuevo 

    def nueva_partida(self, avion):
        if not self.primero:
            raise ValueError('No hay aviones para despegar') 
        
        despegue = self.primero.dato
        self.primero = self.primero.prox
        
        if not self.primero:
            self.ultimo = None

        return despegue

    def ver_estado(self):
        if not self.aviones:
            return 'No hay aviones para despegar o por aterrizar'
        
        por_aterrizar = ''
        por_despegar = ''

        return f'Vuelos esperando para aterrizar:'

    def asignar_pista(self):
        pass