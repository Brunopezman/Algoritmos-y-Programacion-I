"""
Crear las clases Materia y Carrera, que se comporten según el siguiente ejemplo:
nombre

>>> analisis2 = Materia("61.03", "Análisis 2", 8)
>>> fisica2 = Materia("62.01", "Física 2", 8)
>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
>>> c = Carrera([analisis2, fisica2, algo1])
>>> str(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
>>> c.aprobar("95.14", 7)
ValueError: La materia 75.14 no es parte del plan de estudios
>>> c.aprobar("75.40", 10)
>>> c.aprobar("62.01", 7)
>>> str(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)

"""

class Materia:

    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.aprobada = False
        self.nota = 0

    def __str__(self):
        return f"{self.codigo} {self.nombre} ({self.nota})"

    def aprobar_materia(self, nota):
        self.nota = nota
        self.aprobada = True


class Carrera:

    def __init__(self, materias) -> None:

        self.materias = {}

        for materia in materias:
            self.materias[materia.codigo] = materia

    def __str__(self):

        creditos_aprobados = 0
        suma_notas = 0
        materias_aprobadas = 0
        aprobadas = ""

        for materia in self.materias.values():
            if materia.aprobada:
                creditos_aprobados += materia.creditos
                suma_notas += materia.nota
                materias_aprobadas += 1
                aprobadas += str(materia) + "\n"

        if materias_aprobadas == 0:
            promedio = 'N/A'
        else:
            promedio = suma_notas / materias_aprobadas

        return f"Créditos: {creditos_aprobados} -- Promedio: {promedio} -- Materias aprobadas:\n{aprobadas}"

    def aprobar(self, codigo_materia, nota):
        if codigo_materia not in self.materias:
            raise ValueError(f"La materia {codigo_materia} no es parte del plan de estudios")

        self.materias[codigo_materia].aprobar_materia(nota)
