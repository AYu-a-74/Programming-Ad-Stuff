import os
import random
import time
Victory="\033[1;33m"
Wasted="\033[1;35m"
Okay="\033[0;30m"
Explodered="\033[1;31m"
Plantgreen="\033[1;32m"
Iceblue="\033[1;34m"
Water="\033[1;36m"
EmotionalDamage="\033[1;37;40m"
sequence=[1,2,3,4,5,6,7,8]
random.shuffle(sequence)
print(Okay)
def prologue():
    print(Victory+"Narrator=AYu a 74(The ultimate creator, color='Okay'), \nThe Conehead Prince=Zom4(The pro in the video,color='Wasted' or 'Iceblue'), \nThe Buckhead Prince=Noob_Zombie(The noob in the video, this game's creator, \ncolor='EmotionalDamage'), Other Zombies=Those zombies who want to eat your brains(color='Explodered')")
    print(Okay)
    time.sleep(3)
    print("Narrator: This ASCII Art game is made by a zombie(who is called 'The Buckhead Prince') who just became a programming pro after studying in Mr.Poon's class.\nHe had a hard time learning these concepts, but he mastered mose parsts of this course with this game provided as his final project.\n")
    time.sleep(2)
    print("Narrator: Unlike other ASCII Art guessing games, if you fail 10 guesses in total, Your brain will be eaten by a zombie.\nThe only way you can escape from that is to correctly guess all of the zombies provided in the game.\n")
    time.sleep(2)
    print(Iceblue+"Conehead Prince: After you win(or fail) the game, you can choose to revenge towards the author(the noob)!\nYou can hit him as hard as you can! If you feel angry towards the game, Make sure to revenge!\n")
    time.sleep(2)
    print(EmotionalDamage+"Buckhead Prince: Zom4! You traitor! Players! Dont revenge at me! I am innocent!\n")
    time.sleep(1)
    print(Okay+"Narrator: End of prologue now! Now, the game will start soon. Good Luck!\n")
    time.sleep(1)
def guess():
    fails=0
    attempt=0
    totalattempt=0
    eatyourbrains=10
    for zombie_chosen in sequence:
        if zombie_chosen==1:
            start1=time.time()
            print(EmotionalDamage)
            print(r'''''')
            print(Okay+Explodered)
            answer1=input("What zombie is this?" + Okay)
            answer1=answer1.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer1=="":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end1=time.time()
                    break
                elif answer1=="":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end1=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
        #elif zombie_chosen==2:
        #elif zombie_chosen==3:
        #elif zombie_chosen==4:
        #elif zombie_chosen==5:
        #elif zombie_chosen==6:
        #elif zombie_chosen==7:
        #else:
def guesszombie():
    os.system('clear')
    #os.system('cls')
    prologue()
    ready=input("Are u ready? Your answer determines how possible your brains will survive! ")
    ready=ready.lower()
    if ready=="no":
        print("The zombies will not wait if you are not ready!")
        time.sleep(1)
        guess()
guesszombie()
    