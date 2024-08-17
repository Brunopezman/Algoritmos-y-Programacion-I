
# Composicion de objetos

class Rectangulo:

    def __init__(self, x, y, x2, y2) -> None:
        self.p1 = _Punto2D(x,y)
        self.p2 = _Punto2D(x2, y2)

    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)
    
class _Punto2D:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __sub__(self, otro):
        return _Punto2D(self.x - otro.x, self.y - otro.y)

    
##

#metodos: calificar(n), obtener_nota(n), esta_aprobado()
# Estoy usando una clase ejercicio que contiene como metodos a calificar(n), obtener_nota(n)
class Examen:

    def __init__(self, ejercicios) -> None:
        self.ejercicios = ejercicios
        
    def calificar(self, i, n):
        try:
            self.ejercicios[i].calificar(n)
        except IndexError:
            raise ValueError('No existe el ejercicio')
    
    def esta_aprobado(self):
        ejs_aprobados = 0
        notas = self.obtener_nota_ejs()

        for nota in notas:
            if nota >= 6:
                ejs_aprobados += 1
                
        return ejs_aprobados >= len(self.ejercicios) * 0.6
        
    def obtener_nota_ejs(self):
        nota = []

        for ej in self.ejercicios:
            try:
                nota.append(ej.obtener_nota())
            except:
                nota.append(0)

        return nota
    
    def obtener_nota(self):
        if not self.esta_aprobado():
            return 2
        notas_ejs = self.obtener_nota_ejs

        return sum(notas_ejs) / len(notas_ejs)