import random
from Personaje import Personaje
from Razas.Sayajin import Sayajin
from Razas.Namekiano import Namekiano

print("Estos son los personajes disponibles:")
# PERSONAJES
goku = Sayajin("Goku", 150, 100, 80, 150, "sayajin")
piccolo = Namekiano("Piccolo", 200, 90, 60, 120, "namekiano")
krillin=Personaje("Krillin",200,80,65, 90,"humano")
vegeta=Sayajin("Vegeta",180,90,70,100, "sayajin")
frieza=Personaje("Frieza",200,100,85,150, "monstruo")

equipo1 = []
equipo2 = []

equipo1.append(goku)
equipo1.append(piccolo)
equipo1.append(krillin)

equipo2.append(vegeta)
equipo2.append(frieza) 

print("Equipo 1:")
for personaje in equipo1:
    print(f"{personaje.nombre}")

print("Equipo 2:")

for personaje in equipo2:
    print(f"{personaje.nombre}")

nuevo= input("¿Deseas añadir más personajes a los equipos? (s/n): ")

if nuevo == "s" or nuevo == "si":
    otro = True
else:
    otro = False

print("Vamos a crear un personaje")
def crear():
    nombre = input("Introduce el nombre del personaje: ")
    
    vida = input("Cuánta vida tiene de 0 a 200 (default: 100): ")
    if vida == "":
        vida = 100
    else:
        vida = int(vida)
        
    ataque = input("Indica su poder de ataque (default: 50): ")
    if ataque == "":
        ataque = 50
    else:
        ataque = int(ataque)
    
    ki = input("¿Cuál es su nivel de ki de 0 a 100 (default: 80): ")
    if ki == "":
        ki = 80
    else:
        ki = int(ki)
    
    defensa = input("Cuántos puntos tiene de defensa de 0 a 200 (default: 60): ")
    if defensa == "":
        defensa = 60
    else:
        defensa = int(defensa)

    while True:
        raza = input("Elige una raza (humano, sayajin o namekiano): ").lower()
        if raza == "humano":
            personaje = Personaje(nombre, vida, ataque, ki, defensa, raza)
            break
        elif raza == "sayajin":
            personaje = Sayajin(nombre, vida, ataque, ki, defensa, raza)
            break
        elif raza == "namekiano":
            personaje = Namekiano(nombre, vida, ataque, ki, defensa, raza)
            break
        else:
            print("Raza no válida. Por favor, elige una raza válida.")
    
    print("Has creado este personaje:")
    print(f"Nombre: {personaje.nombre}")
    print(f"Vida: {personaje.vida}")
    print(f"Ataque: {personaje.ataque}")
    print(f"Ki: {personaje.ki}")
    print(f"Defensa: {personaje.defensa}")
    print(f"Raza: {personaje.raza}")
    
    if len(equipo1) <= len(equipo2):
        equipo1.append(personaje)
        print(f"Añadido {personaje.nombre} al equipo 1")
    else:
        equipo2.append(personaje)
        print(f"Añadido {personaje.nombre} al equipo 2")

    continuar = input("¿Deseas crear otro personaje para el otro equipo? (si/no): ").lower()
    return continuar in ["si", "sí"]

while otro:
    otro = crear()
        
print("Empecemos el combate")
print("Se enfrentará el Equipo 1, formado por:")

for personaje in equipo1:
    print(f"{personaje.nombre}")

print("Contra el Equipo 2, formado por:")

for personaje in equipo2:
    print(f"{personaje.nombre}")

# LÓGICA DE COMBATE

def combate():
    while len(equipo1) > 0 and len(equipo2) > 0:
        atacante1 = random.choice(equipo1)
        defensor2 = random.choice(equipo2)
        atacante1.atacar(defensor2)
        
        print(f"{atacante1.nombre} ha atacado a {defensor2.nombre} y ahora le quedan {defensor2.vida} pts de vida")
        
        if defensor2.vida <= 0:
            print(f"{defensor2.nombre} ha sido derrotado")
            equipo2.remove(defensor2)
        else:
            if isinstance(atacante1, Namekiano)and random.random() < 0.5:
                atacante1.curar()
            if isinstance(atacante1, Sayajin) and random.random() < 0.5:
                atacante1.transformar()
        
        if len(equipo2) == 0:
            break
        
        atacante2 = random.choice(equipo2)
        defensor1 = random.choice(equipo1)
        atacante2.atacar(defensor1)
        
        print(f"{atacante2.nombre} ha atacado a {defensor1.nombre} y ahora le quedan {defensor1.vida} pts de vida")
        
        if defensor1.vida <= 0:
            print(f"{defensor1.nombre} ha sido derrotado")
            equipo1.remove(defensor1)
        else:
            if isinstance(atacante2, Namekiano)and random.random() < 0.5:
                atacante2.curar()
            if isinstance(atacante2, Sayajin) and random.random() < 0.5:
                atacante2.transformar()
            
    if len(equipo1) > 0:
        print("Gana el equipo 1")
    else:
        print("Gana el equipo 2")

combate()
