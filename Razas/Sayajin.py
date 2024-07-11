from Personaje import Personaje

class Sayajin(Personaje):
    def __init__(self, nombre, vida, ataque, ki, defensa, raza="sayajin"):
        super().__init__(nombre, vida, ataque, ki, defensa, raza)

    def transformar(self):
        print(f"{self.nombre} se ha transformado en supersayajin!")
        self.ataque *= 1.5
        self.ki *= 1.2
        self.defensa *= 1.2
