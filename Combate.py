import random
from Personaje import Personaje
from Razas.Sayajin import Sayajin
from Razas.Namekiano import Namekiano

import time

def mostrar_mensaje_pausado(mensaje, pausa=0.02):
    for letra in mensaje:
        print(letra, end='', flush=True)
        time.sleep(pausa)
    print()  # Para añadir un salto de línea después de imprimir el mensaje


mostrar_mensaje_pausado("Estos son los personajes disponibles:")
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

mostrar_mensaje_pausado("Equipo 1:")
for personaje in equipo1:
    mostrar_mensaje_pausado(f"{personaje.nombre}")

mostrar_mensaje_pausado("Equipo 2:")

for personaje in equipo2:
    mostrar_mensaje_pausado(f"{personaje.nombre}")

nuevo= input("¿Deseas añadir más personajes a los equipos? (s/n): ")

if nuevo == "s" or nuevo == "si":
    otro = True
else:
    otro = False

def crear():
    mostrar_mensaje_pausado("Vamos a crear un personaje")
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
            mostrar_mensaje_pausado("Raza no válida. Por favor, elige una raza válida.")
    
    mostrar_mensaje_pausado("Has creado este personaje:")
    mostrar_mensaje_pausado(f"Nombre: {personaje.nombre}")
    mostrar_mensaje_pausado(f"Vida: {personaje.vida}")
    mostrar_mensaje_pausado(f"Ataque: {personaje.ataque}")
    mostrar_mensaje_pausado(f"Ki: {personaje.ki}")
    mostrar_mensaje_pausado(f"Defensa: {personaje.defensa}")
    mostrar_mensaje_pausado(f"Raza: {personaje.raza}")
    
    if len(equipo1) <= len(equipo2):
        equipo1.append(personaje)
        mostrar_mensaje_pausado(f"Añadido {personaje.nombre} al equipo 1")
    else:
        equipo2.append(personaje)
        mostrar_mensaje_pausado(f"Añadido {personaje.nombre} al equipo 2")

    continuar = input("¿Deseas crear otro personaje para el otro equipo? (si/no): ").lower()
    return continuar in ["si", "sí"]

while otro:
    otro = crear()
        
mostrar_mensaje_pausado("Empecemos el combate")
mostrar_mensaje_pausado("Se enfrentará el Equipo 1, formado por:")

for personaje in equipo1:
    mostrar_mensaje_pausado(f"{personaje.nombre}")

mostrar_mensaje_pausado("Contra el Equipo 2, formado por:")

for personaje in equipo2:
    mostrar_mensaje_pausado(f"{personaje.nombre}")

# LÓGICA DE COMBATE

def combate():
    while len(equipo1) > 0 and len(equipo2) > 0:
        atacante1 = random.choice(equipo1)
        defensor2 = random.choice(equipo2)
        atacante1.atacar(defensor2)
        
        mostrar_mensaje_pausado(f"{atacante1.nombre} ha atacado a {defensor2.nombre} y ahora le quedan {defensor2.vida} pts de vida")
        
        if defensor2.vida <= 0:
            mostrar_mensaje_pausado(f"{defensor2.nombre} ha sido derrotado")
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
        
        mostrar_mensaje_pausado(f"{atacante2.nombre} ha atacado a {defensor1.nombre} y ahora le quedan {defensor1.vida} pts de vida")
        
        if defensor1.vida <= 0:
            mostrar_mensaje_pausado(f"{defensor1.nombre} ha sido derrotado")
            equipo1.remove(defensor1)
        else:
            if isinstance(atacante2, Namekiano)and random.random() < 0.5:
                atacante2.curar()
            if isinstance(atacante2, Sayajin) and random.random() < 0.5:
                atacante2.transformar()
            
    if len(equipo1) > 0:
        mostrar_mensaje_pausado("Gana el equipo 1")
    else:
        mostrar_mensaje_pausado("Gana el equipo 2")

combate()
