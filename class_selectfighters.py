from class_boxer import *
from class_fight import *
class SelectFighters:
    #def __init__(self):
    def select():

        print("To select a fighter enter 1\n to create a fighter enter 2\n")
        option = str(input())

        if option == "1":
            print("select your fighter!")

            print("Mike Tyson enter 1")
            print("Muhhamad Ali enter 2")
            print("Sugar Ray Leonard enter 3")
            print("Roberto Durán enter 4")
            print("Marvelous Marvin Hagler enter 5")
            print("Thomas Hearns enter 6")
            print("George Foreman enter 7")
            print("Joe Frazier enter 8")
            character = str(input())
            if character == "1":
                boxer1 = Boxer("Mike Tyson", 19, 16, 17, 17, 3)

            elif character == "2":
                boxer1 = Boxer("Muhammad Ali", 16, 20, 16, 19, 3)

            if character == "3":
                boxer1 = Boxer("Sugar Ray Leonard", 18, 17, 15, 20, 2.5)

            elif character == "4":
                boxer1 = Boxer("Roberto Duran", 20, 15, 18, 16, 2.8)

            elif character == "5":
                boxer1 = Boxer("Marvelous Marvin Hagler", 19, 16, 20, 18, 2.5)

            elif character == "6":
                boxer1 = Boxer("Thomas Hearns", 20, 18, 16, 17, 2.7)

            elif character == "7":
                boxer1 = Boxer("George Foreman", 20, 14, 20, 14, 3)

            elif character == "8":
                boxer1 = Boxer("Joe Frazier", 18, 16, 18, 15, 2.5)

        elif option == "2":

            # Create fighter
            name = input("Enter fighter name: ")
            strengh = int(input("Enter strengh (1-20): "))
            speed = int(input("Enter speed (1-20): "))
            toughness = int(input("Enter toughness (1-20): "))
            agility = int(input("Enter agility (1-20): "))
            recovery_rate = float(input("Enter recovery rate (1-3): "))
            boxer1 = Boxer(name, strengh, speed, toughness, agility, recovery_rate)

        print("select your opponent")
        print("Mike Tyson enter 1")
        print("Muhhamad Ali enter 2")
        print("Sugar Ray Leonard enter 3")
        print("Roberto Durán enter 4")
        print("Marvelous Marvin Hagler enter 5")
        print("Thomas Hearns enter 6")
        print("George Foreman enter 7")
        print("Joe Frazier enter 8")
        opponent = str(input())
        if opponent == "1":
            boxer2 = Boxer("Mike Tyson", 19, 16, 17, 17, 3)

        elif opponent == "2":
            boxer2 = Boxer("Muhammad Ali", 16, 20, 16, 19, 3)

        if opponent == "3":
            boxer2 = Boxer("Sugar Ray Leonard", 18, 17, 15, 20, 2.5)

        elif opponent == "4":
            boxer2 = Boxer("Roberto Duran", 20, 15, 18, 16, 2.8)

        elif opponent == "5":
            boxer2 = Boxer("Marvelous Marvin Hagler", 19, 16, 20, 18, 2.5)

        elif opponent == "6":
            boxer2 = Boxer("Thomas Hearns", 20, 18, 16, 17, 2.7)

        elif opponent == "7":
            boxer2 = Boxer("George Foreman", 20, 14, 20, 14, 3)

        elif opponent == "8":
            boxer2 = Boxer("Joe Frazier", 18, 16, 18, 15, 2.5)
        return boxer1, boxer2




def main():

    boxer1, boxer2 = SelectFighters.select()
    fight1 = Fight(boxer1, boxer2)
    fight1.estadisticas(boxer1)
    fight1.estadisticas(boxer2)

main()