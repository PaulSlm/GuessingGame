import random

nb = random.randint(0,100)
k = 0

#print(nb) this was just used during the first phase of the testing

print("Let's play a game, you have to guess what number i have in my head, it's gonna be between 0 and 10")

guess = int(input("What's your first guess ?: "))

ok = False

#this is the first check to see if the guess is right 
if guess == nb:
    ok = True
    k += 1

#this loop checks wether of not the guess is right and allows the user to make a second guess indicating wether he is over or under the right number
while not ok:
    if guess < nb:
        guess = int(input("Try higher: "))
        k += 1
    elif guess > nb:
        guess = int(input("Try lower: "))
        k += 1
    else:
        ok = True
        k += 1

if ok == True:
    print("Well done, you guessed in",k,"tries")

#this variable is used to make it so the command prompt doesn't close after displaying "Bravo"
j = input("Press any key to exit")