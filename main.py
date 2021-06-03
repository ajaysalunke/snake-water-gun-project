import random

def gameWin(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False 
        elif you == 'g':
            return True 
    elif comp == 'w':
        if you == 'g':
            return False 
        elif you == 's':
            return True 
    elif comp == 'g':
        if you == 's':
            return False 
        elif you == 'w':
            return True 
        

print("Comp's turn: Choose Snake(s) Water(s) or Gun(g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
if randNo == 2:
    comp = 'w'
if randNo == 3:
    comp = 'g'

you = input("Your's turn: Choose Snake(s) Water(s) or Gun(g)?")
a = gameWin(comp,you)

print(f"Comp choose {comp}")
print(f"You choose {you}")

if a == None:
    print("Game Tied")
elif a == True:
    print("You Won")
elif a == False:
    print("You Lose")
