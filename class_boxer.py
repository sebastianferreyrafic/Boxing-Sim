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

        self.vitality = int((self.toughness + self.strengh) * 5)
        self.maxvitality = int((self.toughness + self.strengh) * 5)

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
        return random.randint(1, 100) <= (value/20) * 100

    def nozeronomax(self):
        #self.stamina = self.stamina
        self.stamina, self.vitality = max(0, self.stamina), max(0, self.vitality)
        self.vitality = self.maxvitality if self.vitality > self.maxvitality else self.vitality

    def punch(self):
        damage = (self.strengh // 2 + self.speed // 3) + random.randint(1,5)
        self.stamina -= random.randint(3,6)
        self.punchesthrown +=1
        return damage

    def kopunch(self):
        self.ko_punch = True
        damage = (self.strengh// 2  + self.speed // 2) + random.randint(3,6)
        self.stamina -= random.randint(5,10)
        self.kopunchesthrown +=1
        return damage


    def block (self, other):
        if other.ko_punch:
            print(f"Punch thrown by: {other.name}\n")
            print (f"{self.name} Blocks the strike!\n")
            self.vitality -= other.kopunch() // 4
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
        time.sleep(2)
        print("*********** COUNTER\n")
        self.exchange(other)

    def takepunch(self, other):
        self.punchestaken += 1
        if other.ko_punch:
            self.vitality -= other.kopunch() - (self.toughness // 5)
            self.stamina -= random.randint(4,8)
            other.cleankopunches +=1
            self.knocked(other)

        else:
            self.vitality-= other.punch() - (self.toughness // 4)
            self.stamina -= random.randint(3,5)
            other.cleanpunches +=1
            print(f"punch thrown by: {other.name}\n")
            print("punch taken by:", self.name,"\n")

    def knocked(self, other):
        other.ko_punch == False
        if self.toughness < 20 and not self.prob(self.toughness//2):

            self.is_knocked = True
            self.times_knocked += 1
            print(f"{self.name} has been knocked!\n")

            for i in range(10, 7, -1):
                time.sleep(0.5)
                print(i)
            print("...")
            time.sleep(1)

            if self.times_knocked <= 3 and self.prob(self.toughness):

                print(f"{self.name} gets up!\n")
                self.is_knocked = False
                self.times_knocked += 1
            else:
                print (f"{self.name} cant get up!\n")
                self.vitality = 0
        else:
            print("el golpe lo hace ratroceder!\n")
            self.moveaway(other)

    def breath(self):
        self.stamina += (random.randint(5,7) * self.recovery_rate) + 15
        print(f"{self.name} took a breath\n")
        if random.random() <= 0.1:
            print(f"{self.name} has a second wind!\n")
            self.stamina += self.recovery_rate * 10

    def recovery(self):
        if self.stamina < 50 and self.recovery_rate > 1:
            self.stamina = self.stamina * self.recovery_rate
        else:
            self.stamina += 45
        self.vitality += self.recovery_rate * 15

    def combo(self, other):
        self.exchange(other)

        if other.is_knocked or not self.in_combo:
            return
        if other.vitality > 0 and self.stamina >= 35:
            time.sleep(2)
            print("*********** COMBO!\n")
            print(f"Looks like a combination from {self.name}!\n")
            print("strike 2!\n")
            self.exchange(other)
            if other.is_knocked == True or not self.in_combo:
                return
            if other.vitality > 0 and self.stamina >=30:
                time.sleep(1)
                print("*********** COMBO!\n")
                print("strike 3!\n")
                self.exchange(other)
                print(f"Combination from {self.name}!\n")

                self.numbercombos +=1
                if other.is_knocked == True or not self.in_combo:
                    return

    def moveto(self, other):
        if not self.isclose:

            print(f"{self.name} closes distance!\n")
            self.isclose = True
            other.isclose = True
            self.stamina -= 2

            if random.choice([True, False]):
                self.exchange(other)

    def moveaway(self, other):
        print(f"{self.name} moves away!\n")
        self.isclose = False
        other.isclose = False
        self.stamina -= 2

    def exchange(self,other):
        prob_kopunch = self.prob(self.strengh/4) and self.stamina > 25
        prob_avoid = other.stamina > 15 and other.prob(other.speed)
        prob_counter = other.prob(other.agility) and other.stamina > 30
        prob_combo = random.random() < 0.26 and (not self.in_combo and self.stamina >= 35)
        prob_moveaway = (self.vitality <= ((other.vitality - 20) // 2) and random.random() < 0.7) and not self.in_combo
        if self.is_knocked or other.is_knocked:
            return

        if self.stamina <= 0:
            self.breath()
            return "breath"

        if not self.isclose:
            self.moveto(other)
            return "moveto"

        if prob_moveaway:
            self.moveaway(other)
            if other.prob(other.agility):
                other.moveto(self)
            return "moveaway"

        if prob_combo:

            self.in_combo = True
            self.combo(other)
            self.in_combo = False
            return "combo"

        if prob_kopunch:

            self.kopunch()
            print(f"un golpe poderoso de parte de {self.name}\n")
        else:
            self.ko_punch = False
            self.punch()

        if random.choice([True, False]):
            if prob_avoid:
                other.avoid(self)
                if prob_counter:
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

