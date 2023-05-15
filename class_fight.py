import time
from guardarpeleadb import *
class Fight:
    def __init__(self, boxer1, boxer2):
        self.boxer1 = boxer1
        self.boxer2 = boxer2
        self.roundnum = 1
        self.winner = None

    def end(self):
        print("¡Fin del combate!\n")
        time.sleep(2)
        if self.boxer1.vitality > self.boxer2.vitality:
            print(f"{self.boxer1.name} gana!\n")
            self.winner = self.boxer1

        elif self.boxer1.vitality < self.boxer2.vitality:
            print(f"{self.boxer2.name} gana\n")
            self.winner = self.boxer2
        else:
            print("Empate!\n")
        time.sleep(2)
        guardar_pelea(self.boxer1, self.boxer2, self.winner.name, self.roundnum)
        self.estadisticas(self.boxer1)
        self.estadisticas(self.boxer2)


    def intercambio(self):
        self.boxer2.exchange(self.boxer1)
        self.boxer1.nozeronomax()
        print(f"*****************************{self.boxer1.name}, has: {self.boxer1.vitality}, vitality left and {self.boxer1.stamina} stamina left\n")
        time.sleep(2)
        self.boxer1.exchange(self.boxer2)
        self.boxer2.nozeronomax()
        print(f"*****************************{self.boxer2.name}, has: {self.boxer2.vitality}, vitality left and {self.boxer2.stamina} stamina left\n")
        time.sleep(2)

    def rounds(self):
        print (f"Round {self.roundnum}!\n")
        time.sleep(1)
        print ("Fight!\n")
        time.sleep(1)
        start_time = time.time()
        while self.boxer1.vitality > 0 and self.boxer2.vitality > 0:
            self.intercambio()
            elapsed_time = time.time() - start_time
            if elapsed_time >= 30:
                self.roundnum += 1
                print(f"¡Fin del round {self.roundnum-1}!\n")
                self.boxer1.recovery()
                self.boxer2.recovery()
                time.sleep(3)
                break

    def fight(self):
        print(f"{self.boxer1.name} vs {self.boxer2.name} - Fight!\n")
        time.sleep(1)
        while self.roundnum <= 12 and (self.boxer1.vitality > 0 and self.boxer2.vitality > 0):
            self.rounds()

        self.end()


    def estadisticas (self, boxer):

        print(f"las estadisticas de {boxer.name} son:\n")
        print(f"puñetazos recibidos por {boxer.name} {boxer.punchestaken}")
        print(f"puñetazos lanzados por {boxer.name} {boxer.punchesthrown}")
        print(f"golpes fuertes lanzados por {boxer.name} {boxer.kopunchesthrown}")
        print(f"puñetazos acertados por {boxer.name} {boxer.cleanpunches}")
        print(f"puñetazos fuertes acertados por {boxer.name} {boxer.cleankopunches}")
        print(f"puñetazos bloqueados por {boxer.name} {boxer.punchesblocked}")
        print(f"puñetazos esquivados por {boxer.name} {boxer.punchesavoided}")
        print(f"contragolpes por {boxer.name} {boxer.punchescountered}")
        print(f"combinaciones por {boxer.name} {boxer.numbercombos}")





