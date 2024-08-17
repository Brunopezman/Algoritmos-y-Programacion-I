"""
Escribir una funcion reemplazar que tome una Pila, un valor nuevo y un valor viejo y
reemplace en la Pila todas las ocurrencias de valor viejo por valor nuevo. Considerar que la
Pila tiene las primitivas apilar(dato), desapilar() y esta vacia().
"""
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
        return self.tope.dato
    
    def desapilar(self):
        """
        Desapila y devuelve el valor que esta en el tope
        Pre: la pila no esta vacia
        """
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
    '''Representa a una cola, con operaciones de encolar y 
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self.frente = None
        self.ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.frente = nodo
        else:
            self.ultimo.prox = nodo
        self.ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self.frente.dato
        self.frente = self.frente.prox
        if self.frente is None:
            self.ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self.frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self.frente is None

    def __str__(self):
        '''Devuelve la representación en cadena de la cola, indicando su frente
           y su fondo'''
        res = "frente <| "
        act = self.frente
        while act:
            res += str(act.dato)
            if act.prox:
                res += " <- "
            act = act.prox
        return res + " <| fondo"

class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None
        self.len = 0

    def __str__(self) -> str:
        
        if not self.prim:
            return 'Lista vacía'

        elementos = []
        act = self.prim

        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'

    def append(self, dato):
        
        if self.prim is None:
            self.prim = _Nodo(dato,None)
        else:

            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato,None)
            
        self.len += 1

    def invertir(self):

        pila = Pila()

        if not self.prim:
            return

        act = self.prim

        while act:
            pila.apilar(act.dato)
            act = act.prox

        act = self.prim

        while act:
            dato = pila.desapilar()
            act.dato = dato
            act = act.prox
        
    def suma_acum(self):

        nueva = ListaEnlazada()

        if not self.prim:
            return nueva
        
        nueva.prim = _Nodo(self.prim.dato)
        
        act = self.prim.prox
        nueva_act = nueva.prim

        while act:
            nueva_act.prox = _Nodo(nueva_act.dato + act.dato)
            act = act.prox
            nueva_act = nueva_act.prox

    # Ej parcialito
    def elementos_impares(self):
        nueva = ListaEnlazada()

        if not self.prim:
            return []
        act = self.prim
        n_act = nueva.prim 
        posicion = 0

        while act:
            if not posicion % 2 == 0: 
                if not n_act:
                    nueva.prim = _Nodo(act.dato)
                    n_act = nueva.prim
                else:
                    n_act.prox = _Nodo(act.dato)
                    n_act = n_act.prox

            act = act.prox
            posicion += 1

        return nueva

    def nplicar(self, elemento, n):

        if not self.prim:
            return 
        
        act = self.prim

        while act:
            if act.dato == elemento:
                for _ in range(n - 1):
                    nuevo_nodo = _Nodo(elemento)
                    nuevo_nodo.prox = act.prox
                    act.prox = nuevo_nodo
                    act = nuevo_nodo 
            
            act = act.prox

    def unir_medio(self, otra):
        if not self.prim or not otra.prim:
            return
        act = self.prim
        otra_act = otra.prim

        while act:
            act = act.prox
        while otra_act:
            nodo = _Nodo(otra_act.dato, None)
            act = nodo
            act = act.prox
            otra_act = otra_act.prox


def reemplazar(p, nuevo, viejo):

    pila_auxiliar = Pila()

    while not p.esta_vacia():
        elemento = p.desapilar()

        if elemento == viejo:
            elemento = nuevo
            
        pila_auxiliar.apilar(elemento)

    while not pila_auxiliar.esta_vacia():
        p.apilar(pila_auxiliar.desapilar())


"""
Escribir un metodo que invierta una ListaEnlazada utilizando una Pila como estructura
auxiliar y considerando que lista solo tiene una referencia al primer nodo.
"""
#Hecho en la ListaEnlazada

"""
Escribir una funcion que reciba una pila de numeros y elimine de la misma los elementos
consecutivos que estan repetidos. Se pueden usar estructuras auxiliares. La funcion no devuelve
nada, simplemente modifica los elementos de la pila que recibe por parametro.
Por ejemplo: remover duplicados consecutivos(Pila([2, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 7])) Genera: Pila([2, 8, 3, 2, 3, 1, 7])
"""

def eliminar_duplicados_consecutivos(p):
    
    if p.esta_vacia():
        return
    aux  = Pila()
    aux.apilar(p.desapilar())
    while not p.esta_vacia():
        if aux.ver_tope() == p.ver_tope():
            p.desapilar()
        else:
            aux.apilar(p.desapilar())
    while not aux.esta_vacia():
        p.apilar(aux.desapilar())
        
"""
Para una lista simplemente enlazada de numeros (que solo mantiene una referencia al
primer nodo) implementar la primitiva suma acumulativa() que devuelva una nueva lista (del
mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos
de la lista origina hasta el nodo i.
"""

#Hecho en la ListaEnlazada

"""
Escribir una funcion reducir que reciba por parametro una cola y una funcion f de dos
parametros, y aplique sucesivamente la funcion f a los dos primeros elementos de la cola (luego
de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funcion reducir
debe devolver el unico elemento restante en la cola.
"""

def reducir(cola, f):

    while not cola.esta_vacia():
        dato = cola.desencolar()
        if cola.esta_vacia():
            return dato
        dato2 = cola.desencolar()
        cola.encolar(f(dato,dato2))

"""
Escribir una funcion que reciba una cola y la cantidad de elementos en la misma, y
devuelva True si los elementos forman un palindromo o False si no.
Por ejemplo:
es palindromo([n, e, u, q, u, e,n], 7) - > True.
"""

def es_palindromo(cola, k):
    aux = Pila()

    for _ in range(k//2):
        aux.apilar(cola.desencolar())

    if k % 2 != 0 :
        cola.desencolar()
    for _ in range(k//2):
        if aux.desapilar() != cola.desencolar():
            return False
    return True

"""
Escribir una funcion recursiva que reciba una cadena y devuelva True si es un palındromo
(se lee igual hacia adelante que hacia atras) o False si no lo es.

"""

def es_palindromo(cadena):

    if len(cadena) < 2:
        return True
    if cadena[0] != cadena[-1]:
        return False
    
    return es_palindromo(cadena[1:-1])
    
"""
Escribir una funcion recursiva que reciba una lista y un parametro n, y devuelva otra
lista con los elementos de la lista replicados esa cantidad n de veces. Por ejemplo, replicar ([1,
3, 3, 7], 2) debe devolver ([1, 1, 3, 3, 3, 3, 7, 7]) .

"""

def replicar(lista, n):

    if len(lista) == 0:
        return []
    return lista[0] * n + replicar(lista[1:], n)

"""
Escribir una funcion recursiva en Python que cuente la cantidad de apariciones de un
elemento en una lista recibidos por parametro
"""

def contar_apariciones(lista, elemento):

    if len(lista) == 0:
        return 0
    
    if lista[0] == elemento:
        return 1 + contar_apariciones(lista[1:], elemento)
    return contar_apariciones(lista[1:], elemento)

lista = [1,2,3,4,4,4,4,5,6,6,7,7]

"""
Esta en el discrod
"""

def es_orden_valido(movimientos):

    lugares = [Pila(), Pila(), Pila()]

    for hora, estado, invitado, estacionamiento in movimientos: #Asumo que arranca desde el 0
        if estado == 'ENTRA':
            lugares[estacionamiento].apilar(invitado)
        if estado == 'SALE':
            lugares[estacionamiento].desapilar()
            if lugares[estacionamiento].desapilar() != invitado:
                return False
    return True

"""
Escribir una función recursiva que recibe una cadena s y un caracter c, y devuelve la cantidad de apariciones de c en s.
"""

def contar_apariciones(s,c):

    if len(s) == 0:
        return 0
    if c == s[0]:
        return 1 + contar_apariciones(s[1:], c)
    return contar_apariciones(s[1:], c)

"""
Realizar una función recursiva que elimine los números pares de una lista de Python que contiene únicamente números.
"""

def eliminar_pares(l):

    if len(l) == 0:
        return []
    n, *cola = l 

    if n % 2 == 0:
       eliminar_pares(cola)
    return n + eliminar_pares(cola)

