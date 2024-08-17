
class _Nodo:
    def __init__(self, dato, prox = None) -> None:
        self.dato = dato
        self.prox = prox

class Pila:

    def __init__(self) -> None:
        self.tope = None

    def apilar(self, dato):
        nuevo = _Nodo(dato, self.tope)
        self.tope = nuevo

    def ver_tope(self):
        """
        Devuelve el valor que esta en el tope
        PRE: La pila no esta vacia
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        
        return self.tope.dato
    
    def desapilar(self):
        """
        Desapila y devuelve el valor que esta en el tope
        Pre: la pila no esta vacia
        """
        if self.esta_vacia():
            raise ValueError("pila vacía")
        
        dato = self.tope.dato
        self.tope = self.tope.prox

        return dato

    def esta_vacia(self):
        return self.tope is None
    
    def __str__(self):
        '''Devuelve la representación en cadena de la pila, indicando su tope
           y su fondo'''
        res = "tope <| "
        act = self.tope
        while act:
            res += str(act.dato)
            if act.prox:
                res += " <- "
            act = act.prox
        return res + " <| fondo"

    
class Cola:

    def __init__(self) -> None:
        # Invariante:
        # si la cola esta vacia => ambos son None
        # si la cola NO esta vacia => ambos NO son None
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        nuevo = _Nodo(dato, None)
        if self.frente is None:
            # cola vacia
            self.frente = nuevo    
        else:
            # cola no vacia
            self.ultimo.prox = nuevo
            self.ultimo = nuevo

    def ver_frente(self):
        """Devuelve el valor que esta al frente
        Pre: La cola no esta vacia
        """
        return self.frente.dato
    
    def esta_vacia(self):
        return self.frente is None

    def desencolar(self):
        """
        Desencola y devuelve el valor que esta al frente.
        Pre: la cola no esta vacia
        """
        dato = self.frente.dato
        self.frente = self.frente.dato
        if self.frente is None:
            # la cola quedo vacia luego de desencolar
            self.ultimo = None
            
        return dato
    

def clonar_pila(pila):

    nueva = Pila()
    temporal = Pila()

    while not pila.esta_vacia():
        e = pila.desapilar()
        temporal.apilar(e)

    while not temporal.esta_vacia():
        e = temporal.desapilar()
        nueva.apilar(e)
        pila.apilar(e)

    return nueva

def producto_numeros(pila):
    if pila.esta_vacia():
        return 1
    e = pila.desapilar()
    prod_resto = producto_numeros(pila)
    pila.apilar(e)
    return e * prod_resto



