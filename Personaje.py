class Personaje:
    def __init__(self, nombre, vida, ataque, ki, defensa, raza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.ki = ki
        self.defensa = defensa
        self.raza = raza

    def atacar(self, defensor):
        daño = max(0, self.ataque - defensor.defensa * 0.1)
        defensor.vida = max(0, defensor.vida - daño)
        return defensor.vida
