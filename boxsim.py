#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bruno
#
# Created:     09/04/2023
# Copyright:   (c) bruno 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time
import random
class Boxer:

    def __init__(self, name, strengh, speed, toughness, agility, recovery_rate):
        #parametros boxeador
        self.name = name

        self.strengh = strengh
        self.speed = speed
        self.agility = agility
        self.toughness = toughness

        self.recovery_rate = recovery_rate

        self.stamina = (recovery_rate * 60) + self.toughness
        self.maxstamina = (recovery_rate * 60) + self.toughness

        self.vitality = (self.toughness + self.strengh) * 5
        self.maxvitality = (self.toughness + self.strengh) * 5



        self.isclose = True

        self.times_knocked = 0
        self.in_combo = False
        self.is_knocked = False
        self.ko_punch = False

        self.punchesthrown = 0
        self.kopunchesthrown = 0
        self.cleanpunches = 0
        self.cleankopunches= 0
        self.punchesavoided = 0
        self.punchescountered = 0
        self.punchesblocked = 0
        self.punchestaken = 0
        self.numbercombos = 0

    def prob(self, value):
        if random.randint(1, 100) <= (value/20) * 100:
            return True
        else: return False

    def nozeronomax(self):
        #self.stamina = self.stamina
        self.stamina, self.vitality = max(0, self.stamina), max(0, self.vitality)
        self.vitality = self.maxvitality if self.vitality > self.maxvitality else self.vitality

    def punch(self):
        damage = (self.strengh //2 + self.speed //3) + random.randint(1,5)

        self.stamina -= random.randint(3,6)
        self.punchesthrown +=1
        return damage

    def kopunch(self):
        self.ko_punch = True
        damage = (self.strengh//2  + self.speed // 2) + random.randint(3,6)

        self.stamina -= random.randint(5,10)
        self.kopunchesthrown +=1
        return damage


    def block (self, other):
        if other.ko_punch:
            print(f"Punch thrown by: {other.name}\n")
            print (f"{self.name} Blocks the strike!\n")
            self.vitality-= other.kopunch() // 4
            self.stamina -= random.randint(1, 4)
            other.ko_punch=False
        else:
            print(f"Punch thrown by: {other.name}\n")
            print (f"{self.name} Blocks the strike!\n")
            self.vitality-= other.punch() // 4
            self.stamina -= random.randint(1, 3)
            other.ko_punch=False
        self.punchesblocked +=1

    def avoid(self, other):
        other.ko_punch=False
        print(f"Punch thrown by: {other.name}\n")
        print (f"{self.name} avoided damage!\n")
        self.stamina -= random.randint(1,2)
        self.punchesavoided += 1

    def counter(self, other):


        print(f"{self.name} counter attacks!\n")
        self.punchescountered += 1
        other.in_combo = False
        self.exchange(other)


    def takepunch(self, other):
        self.punchestaken += 1
        if other.ko_punch == True:
            self.vitality-= other.kopunch() - (self.toughness // 5)
            self.stamina -= random.randint(4,8)
            other.cleankopunches +=1
            self.knocked(other)


        else:
            self.vitality-= other.punch() - (self.toughness // 4)
            self.stamina -= random.randint(3,5)
            other.cleanpunches +=1
            print(f"punch thrown by: {other.name}\n")
            print("punch taken by:", self.name,"\n")

    def breath(self):
        self.stamina += (random.randint(5,7) * self.recovery_rate) + 10
        print(f"{self.name} took a breath\n")

    def recovery(self):
        if self.stamina < 50 and self.recovery_rate > 1:
            self.stamina = self.stamina * self.recovery_rate

        else:
            self.stamina += 45
        self.vitality += self.recovery_rate * 15

    def knocked(self, other):
        other.ko_punch == False
        if self.toughness < 20 and not self.prob(self.toughness//2):

            self.is_knocked = True
            self.times_knocked += 1
            print(f"{self.name} has been knocked!")

            for i in range(10, 7, -1):
                time.sleep(0.5)
                print(i)
            print("...")
            time.sleep(1)


            if self.times_knocked <= 3 and self.prob(self.toughness):

                print(f"{self.name} gets up!")
                self.is_knocked = False
                self.times_knocked += 1
            else:
                print (f"{self.name} cant get up!")
                self.vitality = 0
        else:
            print("el golpe lo hace ratroceder!")
            self.moveaway(other)

    def combo(self, other):

        if self.stamina >= 40:
            print(f"Looks like a combination from {self.name}!")
            print("1!\n")
            self.exchange(other)

            if other.is_knocked:
                return
            if other.vitality > 0 and self.stamina >= 35:
                print("2!\n")
                self.exchange(other)
                if other.is_knocked == True or not self.in_combo:
                    return
                if other.vitality >0 and self.stamina >=30:
                    print("3!\n")
                    self.exchange(other)
                    print(f"Combination from {self.name}!\n")

                    self.numbercombos +=1
                    if other.is_knocked == True or not self.in_combo:
                        return




    def moveto(self, other):

        if  not self.isclose:

            print(f"{self.name} closes distance!")
            self.isclose = True
            other.isclose = True
            self.stamina -= 2

            if random.choice([True, False]):
                self.exchange(other)

    def moveaway(self, other):
        print(f"{self.name} moves away!")
        self.isclose = False
        other.isclose = False
        self.stamina -= 2


    def exchange(self,other):
        if self.is_knocked or other.is_knocked:
            return
        if self.stamina > 0:
            if self.isclose:
                if self.vitality <= ((other.vitality - 20) // 2):
                    if random.random() < 0.7:
                        self.moveaway(other)
                        if other.prob(other.agility):
                            other.moveto(self)
                        return "moveaway"


                c = random.randint(1,4)
                if c == 1 and not self.in_combo:

                    self.in_combo = True
                    self.combo(other)
                    self.in_combo = False
                    return "combo"
                else:

                    if self.prob(self.strengh/3) and self.stamina > 25:

                        self.kopunch()
                        print(f"un golpe poderoso de parte de {self.name}\n")
                    else:
                        self.ko_punch = False
                        self.punch()


                    if random.choice([True, False]):
                        if other.stamina > 15 and other.prob(other.speed):
                            other.avoid(self)
                            if other.prob(other.agility) and other.stamina > 30:
                                #if random.random() < 0.5:
                                other.counter(self)
                                return "counter"
                        else:
                            if random.choice([True, False]):
                                other.block(self)
                                return "block"
                            else:
                                other.takepunch(self)
                                return "takepunch"
                    else:
                        if random.choice([True, False]):
                            other.block(self)
                            return "block"
                        else:
                            other.takepunch(self)
                            return "takepunch"

            else:
                self.moveto(other)

        else:
            self.breath()
            return ("breath")

    def estadisticas (self, other):
        print (f"las estadisticas de {self.name} son:\n")
        print (f"puñetazos recibidos por {self.name} {self.punchestaken}")
        print (f"puñetazos lanzados por {self.name} {self.punchesthrown}")
        print (f"golpes fuertes lanzados por {self.name} {self.kopunchesthrown}")
        print (f"puñetazos acertados por {self.name} {self.cleanpunches}")
        print (f"puñetazos fuertes acertados por {self.name} {self.cleankopunches}")
        print (f"puñetazos bloqueados por {self.name} {self.punchesblocked}")
        print (f"puñetazos esquivados por {self.name} {self.punchesavoided}")
        print (f"contragolpes por {self.name} {self.punchescountered}")
        print (f"combinaciones por {self.name} {self.numbercombos}")
        print (f"las estadisticas de {other.name} son:\n")
        print (f"puñetazos recibidos por {other.name} {other.punchestaken}")
        print (f"puñetazos lanzados por {other.name} {other.punchesthrown}")
        print (f"golpes fuertes lanzados por {other.name} {other.kopunchesthrown}")
        print (f"puñetazos acertados por {other.name} {other.cleanpunches}")
        print (f"puñetazos fuertes acertados por {other.name} {other.cleankopunches}")
        print (f"puñetazos bloqueados por {other.name} {other.punchesblocked}")
        print (f"puñetazos esquivados por {other.name} {other.punchesavoided}")
        print (f"contragolpes por {other.name} {other.punchescountered}")
        print (f"combinaciones por {other.name} {other.numbercombos}")


    def fight(self, other):
        print(f"{self.name} vs {other.name} - Fight!\n")
        time.sleep(1)
        start_time = time.time()
        n = 0
        while True and n < 12:
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time >= 30:
                n += 1

                print(f"¡Fin del round {n}!\n")
                self.recovery()
                other.recovery()
                time.sleep(5)
                start_time = time.time()

            if self.vitality <= 0 or other.vitality <= 0:
                break

            other.exchange(self)
            self.nozeronomax()
            print(f"*****************************{self.name}, has: {self.vitality}, vitality left and {self.stamina} stamina left\n")

            time.sleep(2)

            self.exchange(other)
            other.nozeronomax()
            print(f"*****************************{other.name}, has: {other.vitality}, vitality left and {other.stamina} stamina left\n")

            time.sleep(2)

        print("¡Fin del combate!\n")
        if self.vitality > other.vitality:
            print(f"{self.name} gana!\n")
        elif self.vitality < other.vitality:
            print(f"{other.name} gana\n")
        else:
            print("Empate!\n")

        time.sleep(3)
        self.estadisticas(other)


def main():
    boxer1 = Boxer(name= "Seba",strengh= 15, speed= 15, agility= 15, toughness= 15, recovery_rate= 3)
    boxer2 = Boxer("El Diablo", strengh= 14, speed= 14, agility= 14, toughness= 14, recovery_rate= 3)
    boxer1.fight(boxer2)



main()