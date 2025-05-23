import random as rd
def random ():
    print("Guess the random number")
    print("\n")
    print("Enter a number between 1 to 100.\nIf you're close to the random number, you'll got fire 🔥\nYou have 5 tries.")
    rand= rd.randint(1,100)
    almost = "Not too near 🔥 not too far❄️"
    near = "🔥You are so near"
    far = "❄️ You are so far"
    for n in range(0,5,1):
        number: int = int(input("Enter the number: "))
        if ((number-rand) in [1,2,3,4,5]) or ((rand-number) in [1,2,3,4,5]):
            print(near)
        elif ((number-rand) > 10) or ((rand-number) >10):
            print(far)
        elif ((number-rand) in [6,7,8,9,10]) or ((rand-number) in [6,7,8,9,10]):
            print(almost)
        elif number == rand:
            print(f"You got it! The random number was {number} 🔥🔥🔥")
    else:
        print(f"You lose. The number was {rand}. Nice try.")
random()

