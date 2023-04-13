import time
import random
class Boxer:

    def __init__(self, name, strengh, stamina, speed, toughness, recovery_rate):
        #parametros boxeador
        self.name = name
        self.strengh = strengh
        self.stamina = stamina
        self.speed = speed
        self.toughness = toughness

        self.vitality = (self.toughness * self.strengh) // 2
        self.maxvitality = (self.toughness * self.strengh) // 2

        self.recovery_rate = recovery_rate

        self.isclose = True

        self.times_knocked = 0
        self.in_combo = False
        self.is_knocked = False
        self.ko_punch = False


    def nozeronomax(self):
        #self.stamina = self.stamina
        self.stamina, self.vitality = max(0, self.stamina), max(0, self.vitality)
        self.vitality = self.maxvitality if self.vitality > 200 else self.vitality

    def punch(self):
        damage = (self.strengh //2 + self.speed //3) + random.randint(1,5)

        self.stamina -= random.randint(3,6)
        return damage

    def kopunch(self):
        self.ko_punch = True
        damage = (self.strengh//2  + self.speed // 2) + random.randint(3,6)

        self.stamina -= random.randint(5,10)
        return damage


    def block (self, other):
        if other.ko_punch:
            print(f"Punch thrown by: {other.name}\n")
            print (f"{self.name} Blocks the strike!\n")
            self.vitality-= other.kopunch() // 4
            self.stamina -= random.randint(1, 4)
        else:
            print(f"Punch thrown by: {other.name}\n")
            print (f"{self.name} Blocks the strike!\n")
            self.vitality-= other.punch() // 4
            self.stamina -= random.randint(1, 3)
        #print(f"{self.name}, has: {self.vitality}, vitality left\n")

    def avoid(self, other):
        other.ko_punch=False
        print(f"Punch thrown by: {other.name}\n")
        print (f"{self.name} avoided damage!\n")
        self.stamina -= random.randint(1,2)

    def counter(self, other):

        #self.punch()
        print(f"{self.name} counter attacks!\n")
        self.exchange(other)
        #other.takepunch(self)

    def takepunch(self, other):
        if other.ko_punch == True:
            self.vitality-= other.kopunch() - (self.toughness // 5)
            self.stamina -= random.randint(4,8)
            self.knocked(other)


        else:
            self.vitality-= other.punch() - (self.toughness // 4)
            self.stamina -= random.randint(3,5)
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
        if self.toughness < 20 and random.random() < 0.40:

            self.is_knocked = True
            self.times_knocked += 1
            print(f"{self.name} has been knocked!")
            #print("10, 9, 8")
            for i in range(10, 7, -1):
                time.sleep(0.5)
                print(i)
            print("...")
            time.sleep(1)


            if self.times_knocked <= 3 and random.random() < 0.8:

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
                if other.is_knocked == True:
                    return
                if other.vitality >0 and self.stamina >=30:
                    print("3!\n")
                    self.exchange(other)
                    if other.is_knocked == True:
                        return
                    #other.comboed = True
                    print(f"Combination from {self.name}!\n")


    def moveto(self, other):

        if  not self.isclose:

            print(f"{self.name} closes distance!")
            self.isclose = True
            other.isclose = True
            self.stamina -= 2
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
                if self.vitality <= ((other.vitality -25) // 2):
                    if random.random() < 0.7:
                        self.moveaway(other)
                        return "moveaway"


                c = random.randint(1,4)
                if c == 1 and not self.in_combo:

                    self.in_combo = True
                    self.combo(other)
                    self.in_combo = False
                    return "combo"
                else:
                    d = random.randint(1, 6)
                    if d == 1 and self.stamina > 20:

                        self.kopunch()
                        print(f"un golpe poderoso de parte de {self.name}\n")
                    else:
                        self.ko_punch = False
                        self.punch()

                    r = random.randint(1,3)
                    if r == 1:
                        other.avoid(self)
                        #return "avoid"
                        if other.speed > 10 and other.stamina > 25:
                            if random.random() < 0.5:
                                other.counter(self)
                                return "counter"
                    if r == 2:
                        other.block(self)
                        return "block"
                    if r == 3:
                        other.takepunch(self)
                        return ("takepunch")
            else:
                self.moveto(other)
                if random.choice([True, False]):
                    self.exchange(other)
        else:
            self.breath()
            return ("breath")

