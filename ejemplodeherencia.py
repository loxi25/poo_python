class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mover(self):
        print(f"El {self.marca} {self.modelo} está en movimiento.")

    def detener(self):
        print(f"El {self.marca} {self.modelo} se ha detenido.")


# Clase Máquina (Clase base 2)
class Maquina:
    def __init__(self, tipo):
        self.tipo = tipo

    def encender(self):
        print(f"La {self.tipo} está encendida.")

    def apagar(self):
        print(f"La {self.tipo} está apagada.")


# Clase Automóvil (Hereda de Vehiculo y Maquina)
class Automovil(Vehiculo, Maquina):
    def __init__(self, marca, modelo, tipo):
        Vehiculo.__init__(self, marca, modelo)  # Inicializa la clase Vehiculo
        Maquina.__init__(self, tipo)  # Inicializa la clase Maquina

    def detalles(self):
        print(f"Automóvil: {self.marca} {self.modelo} ({self.tipo})")


# Crear un objeto de Automóvil
mi_auto = Automovil("Toyota", "Corolla", "Motor de combustión")

# Usar los métodos de las clases bas
mi_auto.detalles()
mi_auto.mover()
mi_auto.encender()
mi_auto.apagar()
mi_auto.detener()