import time
import random
from class_boxer import *


class Fight:
    def __init__(self, boxer1, boxer2):

        print(f"{boxer1.name} vs {boxer2.name} - Fight!\n")
        time.sleep(1)
        start_time = time.time()
        n = 0
        while True and n < 12:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 30:
                n += 1

                print(f"¡Fin del round {n}!\n")
                boxer1.recovery()
                boxer2.recovery()
                time.sleep(5)
                start_time = time.time()

            if boxer1.vitality <= 0 or boxer2.vitality <= 0:
                break

            boxer2.exchange(boxer1)
            boxer1.nozeronomax()
            print(f"*****************************{boxer1.name}, has: {boxer1.vitality}, vitality left and {boxer1.stamina} stamina left\n")

            time.sleep(1.5)

            boxer1.exchange(boxer2)
            boxer2.nozeronomax()
            print(f"*****************************{boxer2.name}, has: {boxer2.vitality}, vitality left and {boxer2.stamina} stamina left\n")

            time.sleep(1.5)

        print("¡Fin del combate!\n")
        if boxer1.vitality > boxer2.vitality:
            print(f"{boxer1.name} gana!\n")
        elif boxer1.vitality < boxer2.vitality:
            print(f"{boxer2.name} gana\n")
        else:
            print("Empate!\n")

    def estadisticas (self, other):
            print(f"las estadisticas de {self.name} son:\n")
            print (f"puñetazos recibidos por {self.name} {self.punchestaken}")
            print (f"puñetazos lanzados por {self.name} {self.punchesthrown}")
            print(f"golpes fuertes lanzados por {self.name} {self.kopunchesthrown}")
            print(f"puñetazos acertados por {self.name} {self.cleanpunches}")
            print(f"puñetazos fuertes acertados por {self.name} {self.cleankopunches}")
            print (f"puñetazos bloqueados por {self.name} {self.punchesblocked}")
            print (f"puñetazos esquivados por {self.name} {self.punchesavoided}")
            print (f"contragolpes por {self.name} {self.punchescountered}")
            print (f"combinaciones por {self.name} {self.numbercombos}")
            print(f"las estadisticas de {other.name} son:\n")
            print (f"puñetazos recibidos por {other.name} {other.punchestaken}")
            print (f"puñetazos lanzados por {other.name} {other.punchesthrown}")
            print(f"golpes fuertes lanzados por {other.name} {other.kopunchesthrown}")
            print(f"puñetazos acertados por {other.name} {other.cleanpunches}")
            print(f"puñetazos fuertes acertados por {other.name} {other.cleankopunches}")
            print (f"puñetazos bloqueados por {other.name} {other.punchesblocked}")
            print (f"puñetazos esquivados por {other.name} {other.punchesavoided}")
            print (f"contragolpes por {other.name} {other.punchescountered}")
            print (f"combinaciones por {other.name} {other.numbercombos}")






def main():
    boxer1 = Boxer("Seba", 20, 200, 19, 19, 3)
    boxer2 = Boxer("El Diablo", 20, 200, 19, 19, 3)
    fight1 = Fight(boxer1, boxer2)
    #fight1()
    fight1.estadisticas()


main()