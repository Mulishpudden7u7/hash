class TablaHash:
    def __init__(self):
        self.tabla = {}

    def agregar(self, clave, valor):
        self.tabla[clave] = valor

    def buscar(self, clave):
        return self.tabla.get(clave, None)

# Ejemplo de uso
tabla = TablaHash()
tabla.agregar("Juan", 90)
tabla.agregar("María", 85)
tabla.agregar("Pedro", 95)

nombre_estudiante = "Juan"
print("La calificación de", nombre_estudiante, "es:", tabla.buscar(nombre_estudiante))
