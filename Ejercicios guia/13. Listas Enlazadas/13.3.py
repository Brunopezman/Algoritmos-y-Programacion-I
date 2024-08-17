"""
Implementar el método remover_todos(elemento) de ListaEnlazada, que recibe un elemento y remueve de la lista todas las apariciones del mismo, devolviendo la cantidad
de elementos removidos. La lista debe ser recorrida una sola vez.
"""

class _Nodo:

    def __init__(self, dato, prox) -> None:
        self.dato = dato
        self.prox = None

class ListaEnlazada:

    def __init__(self) -> None:
        self.prim = None
        self.len = 0

    def __str__(self) -> str:
        if not self.prim:
            return 'Lista vacia'

        act = self.prim
        elementos = []

        while act:
            elementos.append(str(act.dato))
            act = act.prox

        return '[' + ', '.join(elementos) + ']'

    def append(self, dato):

        if not self.prim:
            self.prim = _Nodo(dato, None)
        else:
            act = self.prim

            while act.prox:
                act = act.prox
            act.prox = _Nodo(dato, None)

        self.len += 1

    def remover_todos(self, elemento):

        if not self.prim:
            return 0

        cantidad_removida = 0

        while self.prim.dato == elemento:
            self.prim = self.prim.prox
            cantidad_removida += 1

        act = self.prim

        while act.prox:
            if act.prox.dato == elemento:
                act.prox = act.prox.prox
                cantidad_removida += 1
            else:
                act = act.prox

        return cantidad_removida
    
    def downsample(self,k):

        if not self.prim or not k > 1:
            return
        
        act = self.prim
        ant = None
        i = 0

        while act:

            if i % k != 0:
                act = act.prox
                ant.prox = act
            else:
                ant = act
                act = act.prox

            i +=1
    
    def rotar_n_posiciones(self, n):
        if not self.prim or not self.prim.prox:
            return

        n = n % self.len  

        if n == 0:
            return 
  
        act = self.prim
        for _ in range(n - 1):
            act = act.prox # Me paro en la ultima posicion que quiero rotar
   
        nuevo_prim = act.prox # actualizo el puntero a la posicion siguiente
        act.prox = None # anulo la conexion entre la posicion actual y la siguiente
        act = nuevo_prim # El siguiente ahora es mi actual
        while act.prox:
            act = act.prox
        act.prox = self.prim
        self.prim = nuevo_prim 



# Ejemplo de uso:
mi_lista = ListaEnlazada()
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
mi_lista.append(4)
mi_lista.append(5)
mi_lista.append(6)
mi_lista.append(7)
mi_lista.append(8)
mi_lista.rotar_n_posiciones(2)

print(mi_lista)