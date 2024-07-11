from Personaje import Personaje

class Namekiano(Personaje):
    def __init__(self, nombre, vida, ataque, ki, defensa, raza="namekiano"):
        super().__init__(nombre, vida, ataque, ki, defensa, raza)

    def curar(self):
        curacion = self.vida * 0.1
        self.vida += curacion
        print(f"{self.nombre} se ha curado y ahora tiene {self.vida:.2f} puntos de vida")
