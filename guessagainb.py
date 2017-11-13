import random
import turtle
import os
while True:
    computadora = random.randint(1, 9000)

threeB = "1"

pone = -1
option = int(raw_input("Would you like to face another player, (1), or the computer, (2)?"))




def winOne():
    print("You guessed the number, an you have won player one! You have received one disappoint doggo !!!")
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.addshape(os.path.expanduser("doggo.gif"))
    t.shape(os.path.expanduser("doggo.gif"))
    t.penup()
    t.stamp()
    wn.exitonclick()


def winTwo():
    print("You guessed the number, an you have won player two! You have received one moist catto!")
    wn = turtle.Screen()
    t = turtle.Turtle()
    wn.addshape(os.path.expanduser("4Bslg54.gif"))
    t.shape(os.path.expanduser("4Bslg54.gif"))
    t.penup()
    t.stamp()
    wn.exitonclick()


def player_game():
    global pone
    global threeB
    global choice
    choice = int(raw_input("Would you like the guessing game to be easy, (1), medium, (2), hard, (3)?"))
    if choice == 1:
        a = random.randint(1, 10)
        threeBTwo = "10"
        f = 10

    elif choice == 2:
        a = random.randint(1, 51)
        threeBTwo = "50"
        f = 50

    elif choice == 3:
        a = random.randint(1, 101)
        threeBTwo = "100"
        f = 100

    print("\n Im thinking of a number between " + threeB + " and " + threeBTwo + ". \n"
                                                                                 "\n You both have three chances. Can one of you guess it? \n")

    while pone != a or ptwo != a:

        # p1:
        pone = int(raw_input("Enter a number Player one!"))
        if pone <= f and pone >= 1:
            if pone > a:
                print("The number I have in mind is smaller...")
            elif pone < a:
                print("The number I have in mind is bigger...")
            else:
                winOne()
                break

        else:
            print("Invalid number! Restart the program and guess a number between One and Ten!")
            break

        # p2:

        ptwo = int(raw_input("Enter a number Player two!"))
        if ptwo <= f and ptwo >= 1:
            if ptwo > a:
                print("The number I have in mind is smaller...")
            elif ptwo < a:
                print("The number I have in mind is bigger...")
            else:
                winTwo()
                break

        else:
            print("Invalid number! Restart the program and guess a number between One and Ten!")


def robotic_morty():
    global computadora
    global pone
    a = random.randint(1, 9001)
    while computadora != a or pone != a:
        threeBTwo = "9001"
        f = 9000
        pone = int(raw_input("Enter a number Player one!"))
        if pone <= f and pone >= 1:
            if pone > a:
                print("The number I have in mind is smaller...")
            elif pone < a:
                print("The number I have in mind is bigger...")
            else:
                winOne()
                break

        else:
            print("Invalid number! Restart the program and guess a number between One and Ten!")
            break

if option == 1:
    player_game()

if option == 2:
    robotic_morty()

