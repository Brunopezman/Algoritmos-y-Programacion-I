"""
Escribir una función que recibe una expresión matemática (en forma de cadena)
y devuelve True si los paréntesis ('()'), corchetes ('[]') y llaves ('{}') están correctamente
balanceados, False en caso contrario.
"""
class _Nodo:
    def __init__(self, dato, prox) -> None:
        self.dato = dato
        self.prox = prox

class Pila:

    def __init__(self) -> None:
        self.tope = None

    def apilar(self, dato):
        nuevo = _Nodo(dato, self.tope)
        self.tope = nuevo

    def ver_tope(self):
        if not self.tope:
            raise IndexError('La pila esta vacia')
        return self.tope.dato
    
    def desapilar(self):
        if not self.tope:
            raise IndexError('La pila esta vacia')
        
        dato = self.tope.dato
        self.tope = self.tope.prox

        return dato
    
    def esta_vacia(self):
        return self.tope is None
        

def validar(ec):
    pila = Pila()

    for c in ec:
        if c in '{([':
            pila.apilar(c)
        elif c in '})]':
            if pila.esta_vacia():
                return False
            comp = pila.desapilar()
            if (c == ')' and comp != '(') or (c == '}' and comp != '{') or (c == ']' and comp != '['):
                return False
    
    return pila.esta_vacia()

validar('(x+y)/2') #True
validar('[8*4(x+y)]+{2/5}') #True
validar('(x+y]/2') #False
validar('1+)2(+3') #False