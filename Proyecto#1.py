#Daniel Carranza Gutierrez 2-0859-0940
class Cliente():
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    def mostrar_cliente(self):
        print("Nombre: {}\nApellido: {}\nDNI: {}".format(self.nombre, self.apellido, self.dni))