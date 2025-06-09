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
    braineaten=False
    for zombie_chosen in sequence:
        if zombie_chosen==1:
            start1=time.time()
            print(EmotionalDamage)
            print(r'''                       
                                                                  .                                                                                                                   
                                                                  .*                                                                                                                  
                                                                  :*                 .    ::                                                                                          
                                                                :.+     :-*%%#*****#%%%*: * =++-.                                                                                     
                                                                :----%#===--=============%%*                                                                                          
                                                                 +%+=-:-================****%:                                                                                        
                                                            :.=%+=-:-==========++=======+*****%.                                                                                      
                                                            :%=-:===========*============+*****%-                                                                                     
                                                           :#=========*+=*%========****+==+*****%:                                                                                    
                                                          .%=========*%#+=======**###*****=+*****%                                                                                    
                                                          @==+================*@@=.  :+%@**+*****#=                                                                                   
                                                         .%******============%*        .:%%*******%.                                                                                  
                                                          :@%=-=#@*=========@=     .  .  -#%******%:                                                                                  
                                                         :%    . .+@========@.     .*: ..:=@******%:                                                                                  
                                                         *. .:+   .%*=======@:   .  .    :=@******%.                                                                                  
                                                         +-    . .:@+-==+@==*#. .  . . .:-%%***#**#:.                                                                                 
                                                          %=....::%*=#*==*+==*%:..   .:-=@%*******                                                                                    
                                                           +%%%%%#============+%@*=::=#@#******%:                                                                                     
                                                           =*====+**+*+++=======*************#%-                                                                                      
                                                            :%%%%=+*:=*+*-=*%%+%*=******=***%%%%%*:                                                                                   
                                                                 .*.:=*%%=-=*+***%+*******#%**#%##%#=                                                                                 
                                                                  =*+#%%#===+++*#%=+*****%-=**#***#%%#=                                                                               
                                                                =#%@#%@*##%%%*:*%#==***%==#=*##***#%%%%%=                                                                             
                                                                .*%*+==============**@#:%%%=*%*****%%%%%%%:                                                                           
                                                                  =#=+*#****+==*#%@@%%%%%%*-*#*#***%%%%%%%%=                                                                          
                                                                   :=##%##**+*%%-.*%%%%%%%%=*##****%%%%%%%%%*.                                                                        
                                                                                 .%%%%%+*%%*###***#%%%%%%%%%%%:                                                                       
                                                                                 :%%%%%*===*+%#****%%%%%%%%%%%%=                                                                      
                                                                                 =%%%*+#%%%*=%##***%%%%%%%%%%%%%=                                                                     
                                                                                 *#%%*+-:--+=%#**#%#%%%%%%%%%%%%%=                                                                    
                                                                                :%#%*********%****#*=#%%%%%%%%%%%%#.                                                                  
                                                                                *#*%+=::=+#%##****%*=+#%%%%%%%%%%%%#:                                                                 
                                                                                *#%*+****=::=*#***#%*=#%%%%%#%%%%%%%%#:                                                               
                                                                                =%%=:.:=****%%#****#%%%%%*##%%%%%%%%%%%%:                                                             
                                                                                *#%****=::::-%#*****%%%%%#*%%%%%%%%%%%:                                                               
                                                                                %*#*::=*****#%#****#%%%%%%%#%%%%%%%%%@-                                                               
                                                                               .%**#%*=-::-#*%***#%%%#%%%%%%%%%%%%%%%%=                                                               
                                                                               *##%%%%%#*%%%%******%%*#%%%%%%##%%%%%%%.                                                               
                                                                              :%****#%%%%*%%**%%%%%%%#*%%%%%%%%#%%%%%.                                                                
                                                                              :%***%%%%%%=-%#******#%%%%%%%%%#%%%#%%#                                                                 
                                                                               =#**#%%##%-:%##****#%%%%%%%%####%#%#%#                                                                 
                                                                             .*+=====**:   =++*#%%%%%%#%#%****#***#%*                                                                 
                                                                            .*======****  .*======+*#%#%%%%##*****#%*                                                                 
                                                                             *==#******=  ++=======*###%%: =%*****#%%.                                                                
                                                                            ***=********:.*=========*##%=  +##***%%#%-                                                                
                                                                            :#**#**#*******=======*==+***:.#***=-:+##=                                                                
                                                                             *==*****#***=+=====+==*++==***+=+*:                                                                      
                                                                              =*=+*#**#+.*==**==*===+**+=*====*#*+                                                                    
                                                                                =*==+.  =+=+##*==**=-+*: :+*#===**#.                                                                  
                                                                                        :*=+*##+=+=**-.     :#*==+**.                                                                 
                                                                                       .%****##%##*+.         =#+=###. =%##*                                                          
                                                                                      -@%#%###%#%*         .%#**%#**%%%%#**+*                                                         
                                                                                     %%%#%%%#%#%%:.:==-:    .********%##%#%=#:                                                        
                                                                                    -%%#%##%#%#%%@%####%%%: *#****###%#%%%%.                                                          
                                                                                   %%%%%@%%%#%#%#%%%*******###%%%%#**#%#*#%=                                                          
                                                                                   :%%%%#%%%%%@@@@#***********#%**%%*%%*#%%+                                                          
                                                                                   *%%%%#%#%%%%%*++***********%%%%%%%%%%%%%%:                                                         
                                                                                   -@%@%%%%%%%%%%#***********#%%%%%%%%%%%%%#                                                          
                                                                                     .:-=====%%#######%#%%%%%%%%%%%%%%%%%##.                                                          
                                                                                             :%%%%#%#%##%#%%%%*:                                                                      
                                                                                                 .....::..                                                                                                                                                                                                                      ''')
            print(Okay+Explodered)
            answer1=input("What zombie is this?" + Okay)
            answer1=answer1.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer1=="regular zombie":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end1=time.time()
                    break
                elif answer1=="zombie":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end1=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: This zombie is seen often."+Okay)
                    elif attempt==2:
                        print(Water+"Hint: This zombie appears most frequently."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'Regular Zombie', got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'Regular Zombie'!")
                    print(Explodered)
                answer1=input("What zombie is this?" + Okay)
                answer1=answer1.lower()
            time1=end1-start1
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time1} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==2:
            start2=time.time()
            print(Iceblue)
            print(r'''
                                                                                                            ..                                                                                          
                                                                                        +*#***#*.                                                                                     
                                                                                       +===*#%#*#.                                                                                    
                                                                                     .*===+===+**                                                                                     
                                                                                    :*==+=+=++***.                                                                                    
                                                                                   =+===++++=+**#.                                                                                    
                                                                                 .*===+++++=++***                                                                                     
                                                                                :*===++=++++=+***                                                                                     
                                                                               =*===+=+=++++=+**=                                                                                     
                                                                              +====++=+++=+=+***-                                                                                     
                                                                             *=====+=+=++=+=+***-                                                                                     
                                                                           .*=====+++=+++++=+***:                                                                                     
                                                                          :*=====+=++=+=++=+=**#:                                                                                     
                                                                         =*=====+=+++++=+=+=+**#.                                                                                     
                                                                  :*.   =+=====++++++++=++==+**#                                                                                      
                                                                 ..-*+##======+=++++++++=+++***#                                                                                      
                                                            :=***+===+%=======+++++++++=+==****#-.                                                                                    
                                                           :*#*+=====+#=====++=+=+++++++++=****%**##=:                                                                                
                                                           -*===*#*+===*#*====+=+=+=+=+++=+****%******#*.                                                                             
                                                            .*#*====*#*==+*#**++=+=+++++=+=****%*****%#%:                                                                             
                                                             -%=+*#*====*#*+=+**###*+++++*****#%**#%**#+                                                                              
                                                           .*#=-====+%#*===+*#*+===++++********%%**#*:                                                                                
                                                           -*======+*#**%%#*+==+*%#*+=+=+==+*%#*#%=                                                                                   
                                                          .%================+*##*+=+*%%**#%**##***%.                                                                                  
                                                          %*****+=============%%-+#*+==++#%#*******=                                                                                  
                                                          .%%@@@@%+==========@=    .=*%*=:+@*******%                                                                                  
                                                          =%.  . .*@========*%       .  . :#%******%                                                                                  
                                                         .%   *:. .=%=======%#  . . :%  ..-+@******%                                                                                  
                                                         :@   .   .-@====*===@.      ..  :-%%*******                                                                                  
                                                          %:   . .:%*=%+=*%==*%... .   .:-%%*****#%::.                                                                                
                                                           *%+-:-*@+==========+%%-::::-:#@******#*                                                                                    
                                                           :*+*+===============+**@@@@@#*******@:                                                                                     
                                                            =*=*%***#**#%%%%%%%#=+*******=#**%%%%=                                                                                    
                                                              ...=**.:=##*:=#%==%%=*********%#%%%%%*:                                                                                 
                                                                  .###*#%%**====+*#+******%*=**%***%%#=                                                                               
                                                                 -%@==%%+====*-:*%+=****#%#==*#****#%%%%=                                                                             
                                                                .#+=+*******#%@@@%==+**@-=##*#%****#%%%%%%:                                                                           
                                                                  :%*++===========**%@*=%%%=-#**#**#%%%%%%%+                                                                          
                                                                   #%*+=++***===#@*%%%%%%%%*=##****#%%%%%%%%#.                                                                        
                                                                       .::=+===.  :%%%%%%%%%=%##***#%%%%%%%%%%-                                                                       
                                                                                  =%%%%=--=**###***#%%%%%%%%%%%*                                                                      
                                                                                  #%%%%%%%#*+*##***#%%%%%%%%%%%%#                                                                     
                                                                                  %#%#---+*%#+##****#%%%%%%%%%%%%*                                                                    
                                                                                 :##%%%#*=--+*#***#%#%%%%%%%%%%%%%%.                                                                  
                                                                                :%*##::=***%%*#****#%=#%%%%%%%%%%%%%:                                                                 
                                                                                 %*%#**+-:-==**#**%*===#%%%%%%%%%%%%%+.                                                               
                                                                                .%#*:-+*****+*%*****#%#%%%%#*%%%%%%%%%%#-                                                             
                                                                                 %%%*=-::=+**#%******%%%%#*#%%%%%%%%%%%%-                                                             
                                                                                .%*%=+***+=::=%*****#%%%%%%##%%%%%%%%%@                                                               
                                                                                =%**#-.:-=+*%%%#***#%%%%%%%%%%%%%%%%%%@-                                                              
                                                                                +%*#%%%**=-**%#***##%%*%%%%%##%%%%%%%%@:                                                              
                                                                               -#***#%%%%%%%%%##***#%%*%%%%%%%#*#%%%%%:                                                               
                                                                               +#***%%%%%%:*%***####%%*#%%%%%%%%%%%%%#                                                                
                                                                               +%##%%%%%%%:###*****#%%%%%%%%%##%%%#%%*                                                                
                                                                               =*====*#::. :#%#***##%%%%%%%#***##%##%+                                                                
                                                                             .*+=====***-  .*====+*##%##%%#********#%=                                                                
                                                                             -*===+*****=  +=======**#%#%%%=*#*****#%+                                                                
                                                                             -*=+#******. :*========*###%-  *%****#%#%.                                                               
                                                                            =****#******#+-*=========+*#%- .*##%##*##%-                                                               
                                                                             -**#***#**#****=+=====*+=****:=*+*#:  :=-.                                                               
                                                                             .*==**#**#**:*=====++==***+**#+==+*.                                                                     
                                                                               :*=+****=.=+==*#==*===++*.-*====+***.                                                                  
                                                                                 ::...   *+=+##*==**+=**  .:-#*==+*#:                                                                 
                                                                                         *+=+*##*+-=*=        **===*#:    ..                                                          
                                                                                        *%****###%#=.          :#*#%%%:=%*++%:                                                        
                                                                                      :@@%%%%#%#%%:         .%#%##***#%%%%%#*#.                                                       
                                                                                     :%#%#%##%##%%=#%%%%#:    ********#%##%% :.                                                       
                                                                                    +@%####%#%#%%%@######%%=.%********##%#%%-                                                         
                                                                                   :%%%%@@@%%%%%%%%@***********%%%%%%#%@**%%:                                                         
                                                                                    *%%#%%%####%%%*+**********#%%**%#*%%*##%*                                                         
                                                                                   .%%%%%%%%%%%%#**************%%%%%%%%%%%%%%.                                                        
                                                                                    =%%%%%%%%%%%%%%%%######%%%%%%%%%%%%%%%%%*                                                         
                                                                                            ..%####%######%%#%%%%%==++=++-::                                                          
                                                                                              :*#%%#%%%%%%%%%%*:                                                                      
                                                                                                                                 ''')
            print(Okay+Explodered)
            answer2=input("What zombie is this?" + Okay)
            answer2=answer2.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer2=="conehead zombie":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end2=time.time()
                    break
                elif answer2=="roadcone zombie":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end2=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint:This zombie is much tougher than the regular zombie."+Okay)
                    elif attempt==2:
                        print(Water+"Hint:This zombie is the second most frequently appeared zombie in PvZ!"+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'conehead zombie', got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'conehead zombie'!")
                    print(Explodered)
                answer2=input("What zombie is this?" + Okay)
                answer2=answer2.lower()
            time2=end2-start2
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time2} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==3:
            start3=time.time()
            print(Explodered)
            print(r'''
                                                                                                                                                                                                        
                                                                      .:-=++**+==-:.                                                                                                  
                                                                   -*=:............::=+*#*=-:                                                                                         
                                                                  :*::.:................... .:=**=:                                                                                   
                                                                  *:::...:----:::..................:*+.                                                                               
                                                                 :+::....:::::=-::---::::::...........-*                                                                              
                                                                .*:::...::::::+:::::::::::::-------::..*:                                                                             
                                                                ==::....:::::==::::::::::::::::::..:::.*-                                                                             
                                                               :*:::....:::::*-::::::::::::::::::.::::.=:                                                                             
                                                               *-:::...:::::=*:::::::::::::::::::.::::.--                                                                             
                                                              :*:::....:::::*::::::::::::::::::::.::::.-=                                                                             
                                                              ==:::....::::++::::::::::::::::::::.::::.=:                                                                             
                                                              *-::....::::**-::::::::::::::::::::.:::..=:                                                                             
                                                             .*:::....::::+*:::::::::::::::::::::.:::..+:                                                                             
                                                             ==:::....::::**:-:::::::::::::=*::::.:::..+.                                                                             
                                                           -**-::....::::=*=:=::::::::::::::::::..:::..+                                                                              
                                                         :*+=*:::....:::=*=:=-::::::::::::::::::.::::.:=                                                                              
                                                       .*===+=:::....:::-*+-*:::::::::::=:::::::.::::.--                                                                              
                                                      =*:-=**-:::...::::=*=:*:::::::::::-:::::::.:::..=:                                                                              
                                                    .*-:-**:+::..::::::**+:-*+:::::::::::::::::::==:..+                                                                               
                                                   =*::=*:  ***=:..:::-===:**-:::::::::::::::::*=+*#::=                                                                               
                                                  *-:-**   -#******+=:-*****:----::::::::::::-*--++*:--                                                                               
                                                 *-:-*=     ##%@@@%*=+******=-::::::::::::--=*::=*=..:-                                                                               
                                                :*-::=*-   :%:.  . -@+========@::-=+******+*=:-+*==***:                                                                               
                                                  ++-:::++:#:  := . :@========@    .  %: :*::-******%:                                                                                
                                                    =*+-:::+*-. . . :%+===+*==@= .  .  .=+::=****#**@                                                                                 
                                                      .=*+-:::=**:.:=%=+#=+%+==@: .   :*::=*%*****#%=-:                                                                               
                                                         .=#*=-:::=#%+=+========%%=:=*::=+#%******%:                                                                                  
                                                             #***+=-::-=+****+===*#*::=+********#*                                                                                    
                                                             .%=+%#*#*+=-::::::-++::=+#***+****@%%+.                                                                                  
                                                               .::=*#::=*###*+=====*#*****+**%%#%%%%#-                                                                                
                                                                    *****%%#**=**#*%=*******%=**##**#%%+.                                                                             
                                                                  .#@*-#%*====*=:=%%=+****%%=-**#***#%%%%+.                                                                           
                                                                  +*=***###*##%%@@%+==**%*:*%**%#****%%%%%%=                                                                          
                                                                   .*#*============+*%@%-*%%*-*#*#***%%%%%%%#                                                                         
                                                                    :%*+=++***+==*%%#%%%%%%%%-*#*****%%%%%%%%%:                                                                       
                                                                        .:-=***+:   #%%%%%%%%=###****%%%%%%%%%%+                                                                      
                                                                                   :%%%%*--=***%#****%%%%%%%%%%%#.                                                                    
                                                                                   -%%%%%%%#**=%#****%%%%%%%%%%%%%.                                                                   
                                                                                   *#%%---=*%%=%##****#%%%%%%%%%%%%:                                                                  
                                                                                   ##%%%%*=:-=+%#**#%%%%%%%%%%%%%%%%-                                                                 
                                                                                  *#*%=:=***%%*%*****%+#%%%%%%%%%%%%%=                                                                
                                                                                  =##%**+-::==+*#**##===*%%%%%%%%%%%%%#.                                                              
                                                                                  *#%-:=*****++%#****#%##%%%%##%%%%%%%%%%=                                                            
                                                                                  +%%*+-::=+***%#*****#%%%%*#%%%%%%%%%%%%*.                                                           
                                                                                  **%+=***+=:::%#*****%%%%%%##%%%%%%%%%%-                                                             
                                                                                 .%**%+.:-==*%%%#****#%%%%%%%%%%%%%%%%%%#                                                             
                                                                                 :%#*%%%**+-=*%%***##%%#%%%%%%##%%%%%%%%*                                                             
                                                                                .%***#%%%%%%%%%%#****%%##%%%%%%%*#%%%%%*                                                              
                                                                                :%***#%%%%%++%***####%%#*%%%%%%%%%%%%%%.                                                              
                                                                                -%###%%%%%%+=%#******%%%%%%%%%%#%%%%%%%                                                               
                                                                                :#*===+#=:: .*%%****##%%%%%%#***#####%%                                                               
                                                                               =*=====+**+   =====+*#%###%%%*********#%                                                               
                                                                              .*====+*****  :*======+*##%%%%*=%******#%                                                               
                                                                              :*==#******:  *========*###%*. -%****#%#%:                                                              
                                                                             .***********#*:*==========*#%*  +##%####%%#                                                              
                                                                              .**#*#*#**#****==+====+*=+***=:#+**=. .==:                                                              
                                                                               *+=+*#**#**========*==***+=*#*===*:                                                                    
                                                                                .**=*#*#=::*==*#+=*+==++*-:*====+**#:                                                                 
                                                                                  :-:::   =*=+*%*==***=+*:  :-**==+*#=                                                                
                                                                                          -*=+*##*+=-**.       =#+==+#=    ..                                                         
                                                                                         :@#***##%#%=-          .***%%%=:#%*+#=                                                       
                                                                                       .*@%%%%##%#%+          *%%#%***#%%%%%#*#:                                                      
                                                                                       #%#%#%#%#%%@-*#%%%#=    -#******#%#%%%-::                                                      
                                                                                     :%%%###%##%#%%@%######%*.=#*******####%%+                                                        
                                                                                     %%%%@@@%%%%%%%%%%**********#%%%%%#%%#*#%=                                                        
                                                                                     -%%#%%%####%%@%************%%#*#%*%%###%%.                                                       
                                                                                     *%%%%%%%%%%%%*+************%%%%%%%%%%%%%%=                                                       
                                                                                     :%%%%@%%%%%%%%%%%###**###%%%%%%%%%%%%%%%%.                                                       
                                                                                          .....*%####%#####%%#%%%%%*+**++*=:-:                                                        
                                                                                                *%%%%#%%#%%%%%%%=                                                                     
                                                                                                                                                                                      
                                                                                                                                         ''')
            print(Okay+Explodered)
            answer3=input("What zombie is this?" + Okay)
            answer3=answer3.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer3=="buckethead zombie":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end3=time.time()
                    break
                elif answer3=="iron bucket zombie":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end3=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: This zombie is 5 times tougher than a regular zombie."+Okay)
                    elif attempt==2:
                        print(Water+"Hint: This zombie can be disarmed by a magnet shroom."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'buckethead zombie', got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'buckethead zombie'!")
                    print(Explodered)
                answer3=input("What zombie is this?" + Okay)
                answer3=answer3.lower()
            time3=end3-start3
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time3} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==4:
            start4=time.time()
            print(Wasted)
            print(r'''
                                                                                                                                                                                                        
                                                                                                ..                                                                                    
                                                                                              -#****#+.                                                                               
                                                                                             ====*#%#*#.                                                                              
                                                                                            +====++=+**                                                                               
                                                                           :===++***=+=-:..*===+=+=+***.                                                                              
                                                                        .*=:.............=*==+=+=+=+**#.                                                                              
                                                                        *-:.:::.........=+==+=+=++=+**#-.                                                                             
                                                                       -=::....::---:::*===+=++=++++***.:++.                                                                          
                                                                       *:::...:::::=-=*====++=+=+=++**=....+:                                                                         
                                                                      ==::....:::::==*====++++++++=***=:::.:*                                                                         
                                                                     :*:::....::::-*+=====++++++++=***-:::.:*                                                                         
                                                                     *-:::...:::::*=====++=+++++++=***::::.:*                                                                         
                                                                    :*:::....::::*======+=++++++++=**#::::..*                                                                         
                                                                    *=:::...:::-*=====++=+=+=+=++=+**#.:::..*                                                                         
                                                                    *:::....::=*=====+=++=++=+++=+***#.:::..*                                                                         
                                                                   :+:--+*#**%*=====++++++++=+=+=+****::::.:*                                                                         
                                                                   **+======**=====+=+=++==+++=+=+***%#*=:.:=                                                                         
                                                                  +*=*#*=====#*====+=+++++=+++++=****%****##+.                                                                        
                                                                =*+#*====*#*===*#*+=++===++++=+==****%******%%:                                                                       
                                                              -*==+=:=*#*===*##*==*##***+====+=++****%***#%***                                                                        
                                                            .*=:=**-::...-*#*====##*+==+**###########*#%#*##:                                                                         
                                                           =+:-=**-:::::.:::-#%#*===+##*+=+=+======*%#*##=:-                                                                          
                                                         .#=:=*+  %*:....--:+**:=##%*++=+#%#+==+*%#*#%**:.=:                                                                          
                                                        -+::=*.  =+****=-:::***+=--::-*%*+==+****%#*====#.+.                                                                          
                                                       ==::+*    =#**#%**+*#*****:::::::-=#%**%*=-*-:-*=:.=                                                                           
                                                      :*-.:*=    .@*:..:=@+======+*%*******+==--=+:-+*-:-=*.                                                                          
                                                       :*=:.:=*: %   :. ..%*=======@.    . @=..+-:-******%                                                                            
                                                         :*+=:::+#-. ..  .=%=======@= .      :*::=********                                                                            
                                                            :**=:::=**:. :%*-#==%*==@: . . :*=:-+%*****#%+=.                                                                          
                                                               :#*=-:::=#%*=++=======%%:::*-:=+#%******%.                                                                             
                                                                  .##*+=-::=+*#**+====*%#-:-+*#******%=                                                                               
                                                                   ++=*###*==-:::::-=**-:=+****+****@%*:                                                                              
                                                                    .---***:=*##**+==--=*******+**%#%%%%#+.                                                                           
                                                                         :****%%#**+**#*%=******##=**%***%%*:                                                                         
                                                                        =%%-+%%====+=:-%%=+****%#==*##***#%%%*:                                                                       
                                                                       .%++**###**##%@@%+=+**%+-#%*##****#%%%%%#                                                                      
                                                                         :%*=+==========+*%@#-%%%+-##*#**#%%%%%%%:                                                                    
                                                                          ##*++++*++==*%%*%%%%%%%#-##****%%%%%%%%%+                                                                   
                                                                              .::===-:   #%%%%%%%%=%##***%%%%%%%%%%#.                                                                 
                                                                                        :%%%%*---**###***%%%%%%%%%%%%-                                                                
                                                                                        -%%%%%%%%#*+##***#%%%%%%%%%%%%=                                                               
                                                                                        *#%%=-:-+*#+##****#%%%%%%%%%%%%=                                                              
                                                                                        ##%%%#**==++#***#%*%%%%%%%%%%%%%*                                                             
                                                                                       %**%-::+**%%##****##=#%%%%%%%%%%%%*.                                                           
                                                                                       =#%#***+-:::+*#**%#+==#%%%%%#%%%%%%%+.                                                         
                                                                                       =#%-.:=*****%%*****#%%%%%#*#%%%%%%%%%%#:                                                       
                                                                                       *#%***=:::==*%*****#%%%%#*#%%%%%%%%%%*:                                                        
                                                                                       %*#*:=****+=*%#****#%%%%%%##%%%%%%%%%+                                                         
                                                                                      .%**#%=:.::=%*#***#%%%#%%%%%%%%%%%%%%%*                                                         
                                                                                      =%%%%%%%**##%%*****#%%*%%%%%#*%%%%%%%@-                                                         
                                                                                     .%****%%%%%*%%#%%%##%%%*%%%%%%%%##%%%%:                                                          
                                                                                     :%***%%%%%%-=%*******%%#%%%%%%%#%%%%%%                                                           
                                                                                      +###%%%%%%:+%#*****%%%%%%%%%####%##%%                                                           
                                                                                     **=====**.   =**#%%%%%%#%%%*****#**#%#                                                           
                                                                                    *+=====****  :*======*##%#%%#%#******#%                                                           
                                                                                    *==#*****#-  *=======**##%%*..#*****##%.                                                          
                                                                                   ***=********.:*======+==##%%. :#%***#%%%*                                                          
                                                                                   :#**#**#*******=======*==***+ +****=-:#%*                                                          
                                                                                    *==********+=+====+===*++=*#**==*=                                                                
                                                                                     -*=+*#*##=:*==**==*===***-*+===+*#*.                                                             
                                                                                       -*===.  ++=+%#+=+*+=-** .=*#*==+*#:                                                            
                                                                                               -*=+*##+===*=:      =#+==*#:                                                           
                                                                                              :@****###%#*-         .#*=*%#: =%**#                                                    
                                                                                             +@%%%##%#%%:         +%%#%#**#%%%%#*+#                                                   
                                                                                           .%%##%%#%##%#:=+**+:    :%******##%#%%-+:                                                  
                                                                                          :*%%%###%#%#%%%#####%%#.:%*****#####%#%-                                                    
                                                                                          %%%%@@@%%%%%%%%@#*********#%%%%###%#*#%=                                                    
                                                                                          -%%#%%%#%#%%%%#+**********%%#*#%*%%##%%#                                                    
                                                                                          *%%%%%%%%%%%#*+***********%%%%%%%%%%%%%%:                                                   
                                                                                          :%%%@%%%%%%%%%%%%###*##%%%%%%%%%%%%%%%%#                                                    
                                                                                                   .############%##%%%%*=+===+-::.                                                    
                                                                                                    .*#%%%%%%%%%%%#*=                                                                 
                                                                                                                                         ''')
            print(Okay+Explodered)
            answer4=input("What zombie is this?" + Okay)
            answer4=answer4.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer4=="mixed zombie":
                    print(Iceblue+"Conehead Prince: No zombie knows that this wierd mixed zombie is made by my Photoshop mistake."+Okay)
                    end4=time.time()
                    break
                elif answer4=="conehead buckethead zombie" or answer4=="buckhead conehead zombie":
                    print(EmotionalDamage+"Buckhead Prince: It looks like Zom4 forgets to hide the layer for the cone when he is making a buckethead zombie! HAHAHAHA!"+Okay)
                    print(Iceblue+"Conehead Prince:(Punches Buckhead Prince)Now no zombie knows that this wierd mixed zombie is made by me."+Okay)
                    end4=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: Wait, is this a conehead or a buckethead?"+Okay)
                    elif attempt==2:
                        print(Water+"Hint: The answer for the last hinting question should be 'both'."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is...how can I describe that? a 'Mixed Zombie'! got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'Mixed Zombie'!")
                    print(Explodered)
                answer4=input("What zombie is this?" + Okay)
                answer4=answer4.lower()
            time4=end4-start4
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time4} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==5:
            start5=time.time()
            print(Victory)
            print(r'''
                                                                                                                                                                                                            
                                                                                                       -                                                                                  
                                                                                                    *@##.                                                                                 
                                                                                                +@#**#***                                                                                 
                                                              :#@@@@@@@@@@#=:.            :%@%*++**#**#*@                                                                                 
                                                        #@*++**************+*+*+++++*+++++*+***##*#*#*#*%.                                                                                
                                          #@%      :@#+***#*#***#*##*#*#*#*#*#*#*#*#*#*##*#*##*#*#**#**#*%                                                                                
                                      -%+***#:   @*+***#**#*#*#*#**#*#*#*#**#*#*#*#*#***#**#*:.*#*#* ##**@                                                                                
                                      #++*@@@%:%+***#*#*#*#*#*#*#*#*#*#******#*#*+:.  .***#..=****.# **#*#=                                                                               
                                      =%+++****@**#*#*#*#*#******#*#**-.  ..**#*#*#*:**###***=:. :*#*#**#*@                                                                               
                                      %*#*#**#*#*#*#*#*#*-**:**=+**#*=+.**:.****#*=*.*#***#**:=+=:=**.*#*#*+                                                                              
                                      %*#*#*#*#*#*#*#*#** :*.=+=:***#.+ **-.**#*+.      +#*##*****#*#*#*#*#@                                                                              
                                      @#*#*#*#****#*#**##:***=#*** #*#*#*#*#*#*#*#*#*#*#**#**#*#*#**#*#**#**@+-==*@=                                                                      
                                      .@#*#%@#%@##*#*#**=* *#***##**#**#*#**#*#*#*#*#*#*#*#*#*#*#*#*#**#*#*@--#****#*:                                                                    
                                        @*%=+***@++*#*#*#**#*#*#**#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*##***@--======+++                                                                    
                                         :**++**#@+**#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*%=--=======**-                                                                    
                                           @++***@@+**#*#*#*#**#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#**#**+**%----=======**:                                                                    
                                            *++***+@***#*#*#*#*#*#*#**#*#*#*#*#*#*#*#**#*#**#*.**##* *@----========*%.                                                                    
                                            *=++***.%+**#*#*#*#***#**#***#**#**#** .:.****#*  .:*#**##=---=========*%.                                                                    
                                             @+=+**%-***#**#*##*=*.:--+#**#**#***:.=* .-***#***:***%.   .*=========*@                                                                     
                                              @++**#:@***#***#= #: *+***#-.:***#*# *#*.* *#*##*#*-*    .:.::::=*%%#%@                                                                     
                                              .*++**@ @**#*#*#**== =: *##*#*#*#**-+*=**#*#*#*#*#%--*. .:.:.:.:.:.::-@                                                                     
                                               %+****-=*#*#*#*#*.*:# *: :*#*#*#*##*#*#***#*#*#*%:%===*.::.:.:.:.:.:-@                                                                     
                                                %+=**@ @**#**#***#**#*#*#*#*#*#**#*#*#*#*#**#*@   %===%:.:::.:::.:.-@+                                                                    
                                                :*+***%:%#*#*#*#*##*#*#*#**#*#*#*#*#**#*#*#**@:-   ==---%.:.:.:.:::-@##                                                                   
                                                 #+****-%#*#*#*#**#*#*#**#**#**#***#**==**%=*::::*-::#---*::.:.:.::-@%@:                                                                  
                                                  @*+**@ @#*#*#*#*#*+******+*-*===*+**=**%@%++%:::::-%-%-==*-:::-@%*#@                                                                    
                                                   *++******#*=*#*=*=****=****#-**-***%%@##*++####*+**###***+*###*+*@.                                                                    
                                                   %*+++++@****==***=--=******#@==------%*#@@@%%%%***###%*+**%@@%===-                                                                     
                                                  *+*#*#**##*#**==*#*#*#*#***%#+--------@======%+====+#+***+%=---#%@**@+                                                                  
                                                  =****#*#**#*#***#**#*#%%@@@@=--=%*------%=--====%-====+%+===*%=-==#*+***%#                                                              
                                                   @*#*#*#*#*#*#*#@*.          @=-----%*-----%*--====%======*@****%%**+****@@                                                             
                                                    @**##@%#**@-             :@-=++%*----+@=-----*@======%%==-====*%@***%#**-                                                             
                                                     @*%++**@               %::::--==+*@-----*%---====+%@%*++*#@@@*%+*@+*%#                                                               
                                                       =++***+             *:::::::=---==+%%-----*@+==========++***@**%%+#                                                                
                                                        %++**%.            + :::::=-::::-=-==+%%--===*@#========@***%@++=-*                                                               
                                                         %+***@           @:::*::=-=+::::::----==+%%=====+@*+%**%#++=%+@+--%                                                              
                                                          %++**@         *::::-=:==-*:...::::::--+-==+*@====*%*@==---=%%=-=-%                                                             
                                                          *++**%:       +::::-==%:+%=%::::::  .:::=*-=--#:#:..::%=:--===---=-%                                                            
                                                           @=+**@     :*:-*-%-  ....:%=:=-:::::::::......%:....:@---=---=-=-=%+*                                                          
                                                           .*=***+         *+  .@....:*=%:%=-::::::-..........::@=-=-=-=-=--==+=                                                          
                                                            %++**%        %+:........:@-=-=%@#---%............::@-=---=---=----===  -   .@                                                
                                                             @=+**@       *-%:......:=+-+@==@@=-=+@.........::*@=-=%-=-=-=-=*=::-=-%*%#*@+                                                
                                                             :*+***%      =::=@::::-%#=-+=----=--=**@:.:::::#@%%:=%==---=-=-=*%%#++*#%**%:                                                
                                                              *++***+     =::::=+++#-=-=--==-=-=---+%++**%#++*+%@++=-=-=---=-===++++@.                                                    
                                                               %=+**%     %:..:::%**=++#%@%%%%%*+==-=++++++++++*++*::--%-===-------=-=*%                                                  
                                                                @+=**@    .=:::-%:%%=+...=#%%::#%@==+%-++++++++%+@:::=*@--@-=-=-=-=--:--==*@@-                                            
                                                                -+=***+    *=::==@---%...:#%@#*%@@@%@%@=+++++++%-:::-+@@:@@@%=-=-::---=------=-*=                                         
                                                                 %+++*%.  =:*:---%-=-===#%%%%%@==*%***#-++++++@#*::-=@@@@@@@@@%--=--=--=-==-+@.                                           
                                                                  @=+**% =+  *:::=+--+@.:@%%%====#..=*#-=++++%+%:::-@@@@@@@@@@@@#-=--+===@+                                               
                                                                  .*=+**-    .::::=#%=%%%%%%*****+*:#=%-#+++*::%::-@@@@@@@@@@@@@@@-=-=%                                                   
                                                                   *++**#     *=:::-%=-=-=-=-=-=-=-----%++#@@-%%::-%@@@@@@@@@@@@@@@=@%                                                    
                                                                    @*+**@     %%:::-*=*-=++++++=+==-=+@@@@@@++@*::=@@@@@@@@@@@@@@@@%                                                     
                                                                     %==**#      %:::-+=@*====--====@+@@@@@@@++%%%::-#%@@@@@@@@@@@@@@*                                                    
                                                                    :@==-+=:.@@@%=:::=%=%=---@-=--=-=@@@@@@-::*=%--@@@@@@@@@@@@@@@@@@@%                                                   
                                                                    @----=+%==-=+%:::*  %+ .=%*%%**+@@@@@@@:::%-=+-@@@@@@@@@@@@@@@@@@@@*                                                  
                                                                   *%==-=-@:.=#=+%#%%%**:       -@@@@@@@@#++#@:=@%-@@@@@@@@@@@@@@@@@@@@@-                                                 
                                                                  =-=-=-=@=-*@=-=+%@@@@@@@%*=:::@@@@@@@@%++==#:*%@-@@@@@@@@@@@@@@@@@@@@@@                                                 
                                                                  .=-=@%=-==#%+==*%@@@@@@@@@@@@@@@@@@@@%::=#==+%@#-%@@@@@@@@@@@@@@@@@@@@@@                                                
                                                                   =@=-==+*%%%@+++%@@@@@@@@@@@@@@@@@@@@:::::.+%++++%@@@@@@@@@@@@@@@@@@@@@@@                                               
                                                                    @-=*+-=-=+@%+@@@@@@@@@@@@@@@@@@@@@==%.::::::::%=@@@@@@@@@@@@@@@@@@@@@@@@:                                             
                                                                     :@%%=%@#+**: @@@@@@@@@@@@@@@@@@@@=====%-::.::*@@@@@@@@@@@@@@@@@@@@@@@@@@@                                            
                                                                         .:**++*#:@@@@@@%@@@@@@@@@@@@@%*======*#::+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                          
                                                                           #+**+*@             .=#%%=  *:%=======+@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                                           
                                                                            @=++**@                     %.::%*=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@.                                             
                                                                             %+=+**                      =::.:-@@@@@@@@@@@@@@@@@@@@@@@@@@@%@                                              
                                                                              @@%:                         %%:@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%                                              
                                                                                                              = #@@@@@@@@@@@@@@@@@@%@@@@%%%%                                              
                                                                                                                @@@@@@@@@@@@@@@@@@@%#@@%%%%#                                              
                                                                                                               =@@@@@@@@@@@@@@@@@##%#%%#%%%#                                              
                                                                                                               *@@@@@@@@@@@@@@###%####%##%%%                                              
                                                                                                                +-=-=+*%%%%%  =%%#**#%#%#%%@                                              
                                                                                                               *--=-=-=+*%#@  +******#***##@                                              
                                                                                                              +-=-=-=---+@#@  **%+%******#%%:                                             
                                                                                                             =@-=--=-==-=*#:  * =+#*****#%#%@                                             
                                                                                                            .@@-==-=--===-=+**%=-++%****%*%##%                                            
                                                                                                              -===-*=+-+%-=*=*+%.+++++#   @#:                                             
                                                                                                             .=-=+@--*=-+++*%*%  %=-=+@                                                   
                                                                                                             =-=+@*=-=*+=*-##  ===-==+#*%                                                 
                                                                                                            ==-=+*+%--++***+*   *===+==++#                                                
                                                                                                             #%%%**+%==*.#@         %-==++@                                               
                                                                                                          :  .%#++@+: *+%%           *-==++:                                              
                                                                                                       :%***% @*+++*                  *=-++@     #%:                                      
                                                                                                       = :%##%#%%+# .==                =@**@*.*%****%                                     
                                                                                                         +**%#%###%##%             %**%*****%%%%%%@#*+                                    
                                                                                                       .%*##%%%%#%#%#@ =%%##%=      :*******####%#% :@                                    
                                                                                                        %*#%#%####%@+==++****%%%=. %******#%@%%%##%:                                      
                                                                                                      :*###%@**@@+==+*#%============#+:+@%****##%##%=                                     
                                                                                                      +#%%%=*+*+===*#*============+****=:%#:-*%*#%#@                                      
                                                                                                       @==========**============+*+*+*+*##*%%*%@@%%##                                     
                                                                                                       %***#%%****@@#+=========+*****+******#%%@%%%@+                                     
                                                                                                        =*%%%%%%##@*++=+***#%%%#%%+*+*+*+**+********                                      
                                                                                                                  =****+**+*+*+**+****@%****-.                                            
                                                                                                                   =@%#**********%%:                  
                                                                                                                   ''')
            print(Okay+Explodered)
            answer5=input("What zombie is this?" + Okay)
            answer5=answer5.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer5=="zom4":
                    print(Iceblue+"Conehead Prince: Why are you adding me as a zombie to guess?! I DONT EAT BRAINS!!"+Okay)
                    end5=time.time()
                    break
                elif answer5=="conehead prince":
                    print(EmotionalDamage+"Buckhead Prince: I personally kinda like this one. It makes Zom4 looks silly! HAHAHAHA!"+Okay)
                    end5=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: This zombie is not a normal conehead zombie."+Okay)
                    elif attempt==2:
                        print(Water+"Hint: This zombie is one of the zombies talking to you in this game."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is...I wish not to tell you this one, it is me(Zom4)."+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is me(Zom4).!")
                    print(Explodered)
                answer5=input("What zombie is this?" + Okay)
                answer5=answer5.lower()
            time5=end5-start5
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time5} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==6:
            start6=time.time()
            print(Plantgreen)
            print(r'''                                                                                                                                                                                                             
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                  
                                                                                           *.........:-             .........::::    .......    ..:.. #:::*::::::::::::::::::::::#::::::                                                          
                                                                                           :*..........:::.         ...:    .::- :  .............:#....:::%:::*#-::-=##::::::::::::#:::::::.                                                      
                                                                                            :#........ .  . .:::   #..-::...+-:......:=*=:::::..::... ::::%:::%::::::.::::-*:::::::::#::::::                                                      
                                                                                            ::@...        . .......:%%.:*:.................... #:%... #:::@:::::#:::::::::::::-:::::::#:::::                                                      
                                                                                             .:#..       .........:+.........................   + %...*:::%:::::::*::::::::::::*::::::::::::                                                      
                                                                                              ::-. ... ........::-..........................    ....#..:::@+-:::::::::::::::::::::::::::::::                                                      
                                                                                              ::#............:=.......................=:...#.. ......+#%@:%    .::::::::::::::::::::::::::::                                                      
                                                                                               ::#.:.......:%...............=:..       .#....:-:#......:....     .-:::-@%:::::::::::::::::::                                                      
                                                                                                := .#....:+..........=.....%  .. . . .  .-......:.=.....::#..     ::::::::::=:::::::::::::::                                                      
                                                                                                 :+ .#.::...........:.....:   ....:.......=.........:#..:..##.:     ::::::::::::::#:::::::::                                                      
                                                                                                  :+ ..+.  ...*....:.....+.   .*..:..@..:.............#.:..:...:      :::::::::::::::=::::::                                                      
                                                                                                  :* .:.    ..:...#.    ..::   ..::%:....:..*.:...............  -      :::::::::::*::::#::::                                                      
                                                                                                   :#...... ......:     ...    .:.....:..%.@-...............   .:-      ::-*::::::=:::::::::                                                      
                                                                                                    :*....:............=...    ..%....:...@....#.*. .......   ...:#     +::::::::::::::::-::                                                      
                                                                                                    %:...:*............:...   .. =......=@=.......:. .  .=... ...--#     #::::::::::::::::*#                                                      
                                                                                                    %:..:...@:..........:..%     =...-.@..%+...-..%.  .  .-......:-*%    #:=:::::-#:::::::*:                                                      
                                                                                                   .#.%+.....#@:....%.....:=%    #...@@@@@@@%#....=.......=......::=--   *:::::::#:::::*::::                                                      
                                                                                                  ..+..#.....:..@@..#..=...:     #..@#.:. %.#@@*:.:........:......::+  *  ::::::::::::::::::                                                      
                                                                                                  .==........@@@@@@@@:-.-.:.+   .@.##.======%.*..:.........@.......::#    ::::::#:::::::::::                                                      
                                                                                                  ..=.#:....@*#.:@..:  ....:.*  ...#-========= @+.-.......:::......:::.   +::::=::::::::::::                                                      
                                                                                                 .=.=#.+.:.@..:==+:%===  ..*:.  @.# ===.  .=== .*.:...*....:*......::::   *-::+:::::::::::::                                                      
                                                                                                .+..=.....:@:#.#%=  -===    .:#@.   #===%%====..+=..:.=.....#=+....::::#   :::::::::::::::::                                                      
                                                                                                 :....:...:@.:==@@   ===#    .%+     %==::::-.+.:=.:%*:.....=:.....:::::   :::::::*::+::::::                                                      
                                                                                                @:....##...++.@=========       .%%      -:    -:::==:%.......::...:-::::%  ::::::#::::::::::                                                      
                                                                                                @:.%.+::..==.:=:*=::::%                       #==::=*...:....*:....:::::.  ::::::::%=:::*:::                                                      
                                                                                                %:@.#:..*..#.#.:%-=                           =:::::....:....%::..:::::::#=:::::%::#::::::::                                                      
                                                                                                -#+-=...#..@.*::.*                  :+  =       #:.:....:....:::..#:::::::=::::-::::::::::::                                                      
                                                                                               #..+.=...:#..:::::.            =*    : ::-         .#...%:.....::::=:::::::+::::::::::::::#::                                                      
                                                                                               #..=.%....:-.@:.:::       =-   :@+:::::::.         .#..*:......@:::+:=::::::::::::.:.:::::%::                                                      
                                                                                               :..:.:....::::@::%          := :::::::::::        #...*:.. .  .-:::*::::=:::#:::::::::..::#::                                                      
                                                                                              #...:.:.%..#==#:             *::.::.:.:::-      :  .%:#:. .    .:%:::::=::::+%:::::::::::::#::                                                      
                                                                                              * ..:.=%....:#                =:::::#.   :        %.@@:.- .  ....:*::#::::#::#:::::::::::::*::                                                      
                                                                                                  **:-.....::-    .           #      %        .:@@@@:..:.......::%%:-:::::::#:::::::::::::::                                                      
                                                                                                 +%::* . *=.:.::%@.                        .=@@@@@#:...#......:::=::::=:::#:::::::::::::-:::                                                      
                                                                                              :.:.%*:-- ..%......##::::%%:               .%@@@@@..::......:...@:::::::::::+:::::::::::::::::                                                      
                                                                                               ...=.::=:....+:...+.:::%:::#@@@@@@@*      .%:@@...::.-....#@%::::::#::::=:#::::=:::::::::::::                                                      
                                                                                               ...:.=:%.:::--:...:...#:%::::+@@@@@@      #.#.:..%=*::+#:+:::::::::+::::%:::::::#:::::::::::#                                                      
                                                                                               ..::.#:%..:%.@.:..:%....::=:::*@@:..-    %..*:..#..:.:=@.:.:::-::::::::::::::::=:%::::::::*::                                                      
                                                                                              @-.::.#:-....:::::::::::-:#::::# .....#  ....:..-:..@:::...#%::::=:::::::::::::::::%::#:::::.:                                                      
                                                                                              @:..:.++.:....:=:::::::::::#.     -....=....:* .%.=::::@..@::::=#:::::::::::::=:::::#:::::::.:                                                      
                                                                                              @.:.-.%.+... .=:::#:::::::        #...%....*.:..@*:: .:@..*:::*:::::::::::-:::::::+-::::::::::                                                      
                                                                                              =..::.%.:  ..#:::%::::::*          ..%....*..:#+.::: :::..*:::::::::#:::::::::::::::=::#::::::                                                      
                                                                                              *...:...=...=*%::::::::%           =+..........+.#:  :::#.-::::%::::::::::=:::::#::::+:-@@=:::                                                      
                                                                                              :...-::.%..::::*+:-:::+    :-      =.....%....:*.:: ::::::+::::::::@:::%::::::::::::::::::::::                                                      
                                                                                              .:.:#::=+..#::#::#::::    :#      ......+::...:.::.:::::::#:::::::#::::=:=:::%:::%::::::::::::                                                      
                                                                                              ::=..:::..%%::::+:==.    ::     =.....--%*:.-#::::::::::::::::::=#:::#:+:-::::#::+:=::::=:::::                                                      
                                                                                             ::.:.:.:*=::=::#::-:      :.    @.......::*::-::::::::::::::::::@=#%::::-:::::::%:=:::::::%::::                                                      
                                                                                             %.::. =::::::=:.#-:#     :%    *......= .:%.:+::::::::::::::::::::::::::-::::::::=%::::::::-::=                                                      
                                                                                             . .::.=-::::-::: .      ::    ....... :@::::.%:%......#:::::::::::::::::-::+::-::#:::::::::::                                                        
                                                                     ..######%.             *..:=:#::=::::::@.==    .:#  +......# :%:.:%@%............*::::::::::::::%:::::::::::::::::::#                                                        
                                                                      .*#######%-           :.::-:::::=::::..........#  @.....        :@................:::::::::::::::::-:::::::::::::::-                                                        
                                                      =======*    --  .*%@@@@@@%%@@         .=::::=@: *:::%..........  *......         %.#:::::#.%.........*::::::-:%::-:+#:::::::::::#:::                                                        
                                                      ========+%:   %*==========++=======#  .           ::#:::::*.=.# :.....%         *#::::::::....#.......%::::::=:=#::=::::::#:::=::::::                                                       
                                                      ======+#      @+=+*#  %====================%       .@*::: .... .....-          :*:::::::-........:.....#==::=:+:-:::::::#:=#:::::::::                                                       
                                                      =+#@=    .   :+*:     %  *+#  *==========#            #*===++@.....#          ::*:::::::+.........#.....%::+:::=::::::-::::::::::::::                                                       
                                                        +..      %        -%   =    #*=======*                #*==*......         .:::::::::::...........*....#:#::::#:::::::::::::::::::::                                                       
                                                         %@.. ##@..      :  : :  +-.@@@@@@*.-                  :*+%...@          ::::::::-:::#..........+::...**-::-::::::::::::::=:::::::=                                                       
                                                               ##@..  *...   %..  +@%@@#%@:..                    **..=         :::::::::::=:: ..........::::.%*%:::::::::::::::::::::##:::                                                        
                                                                 .  ##@...........@=-@####@@%+...               .*.::=:      ::::::::::::::::  ........%::::=*+::::::*:::=:::::=:::::*                                                            
                                                                     :###@% %###=     ######%@@.......=*      ..-.....---=*%%%%#*=---:::::::%     .....::::@%#=::::: ::#-:  .   ..:                                                               
                                                                                                                                                                                             ''')
            print(Okay+Explodered)
            answer6=input("What zombie is this?" + Okay)
            answer6=answer6.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer6=="not zombie":
                    print(Iceblue+"Conehead Prince: Wait, why is the ALMIGHTY AYu a 74 HERE?! I need to 'ask the noob nicely' about this thing."+Okay)
                    end6=time.time()
                    break
                elif answer6=="ayu a 74":
                    print(EmotionalDamage+"Buckhead Prince: ALMIGHTY AYU A 74! I AM SORRY TO SAY THAT YOU ARE A ZOMBIE! COULD YOU PLEASE FORGET ME?"+Okay)
                    print("Narrator: Now you have a reason to beat this zombie author as hard as you can.")
                    end6=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: Is this a zombie?"+Okay)
                    elif attempt==2:
                        print(Water+"Hint: Is this REALLY a zombie?"+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'AYu a 74'!(I believe that the noob will be beaten badly soon as he offends the almighty AYu a 74), got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'AYu a 74'!")
                    print(Explodered)
                answer6=input("What zombie is this?" + Okay)
                answer6=answer6.lower()
            time6=end6-start6
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time6} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        elif zombie_chosen==7:
            start7=time.time()
            print(EmotionalDamage)
            print(r'''                                                                                                                                                                                       
                                                                                        .                                                                                               
                                                                                      -#%                                                                                               
                                                                                   :#%###=                                                                                              
                                                 ::---=:.                     .:+#########                                                                                              
                                          :*###*+++++++++*#####==--:--====####**#########%                                                                                              
                         :+##=        =##*++*#################***++++++++**###############:                                                                                             
                      :##****%-   :##*++##################################################+                                                                                             
                     :%+*#%###*=##++#######################################################                                                                                             
                      +##+=++**##*########################################################%:                                                                                            
                      =#*###################################################################                                                                                            
                     .#####################################################################%:                                                                                           
                     .#######################################################################                                                                                           
                      .#########%###########################################################%                                                                                           
                        +##*=##*##+###########################################################                                                                                          
                          .#*+#**%*+#########################################################%:                                                                                         
                           :%++#*#%++##########################################################                                                                                         
                            +#=*#*%#++#########################################################*                                                                                        
                             #*+#*#%#+*########################################################%*                                                                                       
                             :%+*#*#%#+#########################################################%+                                                                                      
                              =#+#**%#*+#########################################################%+                                                                                     
                               #*#+*#%%+##########################################################%+                                                                                    
                               .%#++*%#############################################################%#                                                                                   
                                -%+=*#%#############################################################%#                                                                                  
                                 *#==###%############################################################%#                                                                                 
                                 .#+=################################################################%%#                                                                                
                                  :#=+##%%###########################################################%#.                                                                                
                                   +###%%%%######################################################%#%%#                                                                                  
                                   -#++****#############################%%#####################%#%*.                                                                                    
                                  :#*###################################%%######################-  :                                                                                    
                                  =#########################%%%%%%##%##@%#########%@@@@@@@@@%#:   =: :-.                                                                                
                                   *#################%%#*+=--:::::-=+#%%@##%@%*=----==-===-=-=-=+@*.=                                                                                   
                                    *#######%%##%%*:                  ::*%=--:::--==-==-=-=====-+#+##                                                                                   
                                     :###+###%#:                     *#=-:::--=======-==-=-====-+++++#=                                                                                 
                                        =#+##%+                  :+#=--::--=-=-=---==+=====--=--=+++++=%:                                                                               
                                         **+##%:                 #=-::-====-======#--=-=-=-==-====++++++#=                                                                              
                                         .#+*##%.               #==-====+======*#=--=-====+++++==-=++++++#:                                                                             
                                          -#=*##*              *=-=--==-=-=*#*===-==-==+*####*++++==++++++%                                                                             
                                           #*=*#%=            :#====--=-====-=-=-=-==+@@=:   -#@@++=++++++#=                                                                            
                                           .#+=*#%.           %++++++===-=-====-====@#          -@%++++++++@                                                                            
                                            -#=+*##            #%@%%@@@+=-=-=-==-==@=            :#@+++++++%:                                                                           
                                             #*=**%=          =#       *@=-===-=-=*%             .:@*++++++%-                                                                           
                                             .#+=**%:        .#   :=    +@-=-==-=-##       =%    .:@#++++++%:                                                                           
                                              =#=+*##        -#         :@======-=+@             ::@*++**++@                                                                            
                                               **=+*%*       .%        :*#--*-=@#-=##           ::@%++++*###=:                                                                          
                                               .%+=**%=       :#-.  .::##==#========#@-.     .::*@#++++++#=                                                                             
                                                -%#+*#%         #%%@@%*==-==-=-=-=-=-=#@@=:::+@@*++*+++*%                                                                               
                                                 +###*##        #=======+==============+++***+++++*+++%#.                                                                               
                                                  #*##*%=        *+**#==+= -*===-+#####==+++++++=+*+*@####=                                                                             
                                                  :@+*##%:            .=- .=###:.=*#*+###=+++++++*+##*#######:                                                                          
                                                   =%=####              *####%%*======++%=+++++++##:***#***####=                                                                        
                                                    *#=#*#=           +%@--#%*----=+:.=#@-=++++*@#+:+*##***######=                                                                      
                                                     #*+#*%:         :#==+**########@%@%+==+++%+:+##+##*****#######:                                                                    
                                                     :%=###%:          =##+======-====-===+#@#.*%%%-=#**#***######%%+                                                                   
                                                      -#=####           %===+**+***===*%%%=##%%#%%#:=#******######%%%#                                                                  
                                                      .#**#*#*           .:==+########=. =####%%##%==###****#######%%%#-                                                                
                                                     =#===+**####*#                     *######=+###+###****#######%%%%%+                                                               
                                                     #==-=-=#+---=#+                   ######%#=-::#-###****########%%%%%#                                                              
                                                    :#***++#-:=+=-=**+##*=:         :=#*####%*##%%%*-*##****##########%#%%#.                                                            
                                                    *=-=--=#+++*+-=++#*****#####+=-:#**######-:..:=+*+##***#################.                                                           
                                                    *=-=+##*==***===+#****##****##*##*#####%#%#*=--:*+#****##############%##%:                                                          
                                                     ***=-=-=+*#*##+#################*#####*..-=*+#%#*#*****#+=##############%=                                                         
                                                      *=-=*#===++#%*######################%**+=:.:-==*****##==-=######%#########.                                                       
                                                       =*+#==-=##*##+#####################=:==***+===*#*****##########*#########%#=                                                     
                                                           -=##+#**%*####################%#=:. :=++**##******##%###*###############=                                                    
                                                              %++#**%:                   =*+**+-:. .:=%******##%####*###########%=                                                      
                                                              :%=*#*##                    := :-=***+*###****##%#################%%                                                      
                                                               **=#**#*                    .+-:. .:**##****###%##############%#%%@                                                      
                                                                #++*##:                      =#*+####%******##%+#######*####%%#%%+                                                      
                                                                 .::                          =%%#########*###%+#%#####%#####%%#=                                                       
                                                                                                . .##*******##%##%%%#########%%%.                                                       
                                                                                                  :###******##%##%%%%#########%#.                                                       
                                                                                                   =###***####%##%###***########                                                        
                                                                                                   :=-===+#######%##+**+*#***###                                                        
                                                                                                   *===-==-=+####%%##=#*+**+*###                                                        
                                                                                                  =+=-======+####%#. .#**+*+###%:                                                       
                                                                                                  *====-======###%:  =##****####*                                                       
                                                                                                  =============++**  +*+*#=+:+###.                                                      
                                                                                                  +=========*=====*=+*==+#                                                              
                                                                                                 ====+=-=*====+***#*=--=+*=.                                                            
                                                                                                :+==+##==++=-=-=* .*====-=++#:                                                          
                                                                                                -+==+##+=-=+*==*=    .=#====+#=                                                         
                                                                                                :*-==*##+==:+*.        .#*====#=                                                        
                                                                                               :@#+++*#####=-            =#=+#%#= -##++#:                                               
                                                                                              *@%#########*           +%####*+*#%%%##*+=#.                                              
                                                                                            :@###########@. ::--:      -#*++*+*+######%=*=                                              
                                                                                            -%###########@@#######%#. :##***###########                                                 
                                                                                          +@####@%#########@%%##########%%#%#**+**#####*                                                
                                                                                           %@@@%#%@@@@@@@%%@*+*+*+*+*+++*##*##%#%%#*###:                                                
                                                                                           %#############*+=++*+*+*+*+**####*##########%.                                               
                                                                                           %%%%%%#%%%%%%#*++*++*+*+*+*++#######%%%##%##*.                                               
                                                                                           =%%%%%%%%@%%###%%##########%%%%%%%%%%%%%%%%%*                                                
                                                                                                     .#################%%%%#=====-==:::                                                 
                                                                                                      :###############%#+:                                                              
                                                                                                                                                                                        
                                                                                                                                                         ''')
            print(Water)
            answer7=input("What zombie is this?" + Okay)
            answer7=answer7.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer7=="flag zombie":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end7=time.time()
                    break
                elif answer7=="a large wave of zombies are coming":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end7=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: This zombie appears when a large wave starts."+Okay)
                    elif attempt==2:
                        print(Water+"Hint: This zombie hints the arrival of a large group of zombies."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'Flag Zombie', got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'Flag Zombie'!")
                    print(Explodered)
                answer7=input("What zombie is this?" + Okay)
                answer7=answer7.lower()
            time7=end7-start7
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time7} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        else:
            start8=time.time()
            print(Okay)
            print(r'''
                                                                                                                                                                                                             
                                                          -                                                                                                                                
                                                           =:                                                                                                                              
                                                           +                           -                                                                                                   
                                                          +        .:=*#%%%%%###**:   =. --:                                                                                               
                                                        = =. .=##+=----=======-=-===*@=.=                                                                                                  
                                                         -:##=--:::--===-=--==-==-==*#+##                                                                                                  
                                                       :##=-::::-====-=-=-=-=-=-==-=+++++#=                                                                                                
                                                   :-#*==:::--===-=-=-==+===-===-==-=++++++%:                                                                                              
                                                   -#=-::-=-==-=-====*=-=-=-==-==--===++++++#+                                                                                             
                                                  -#=--=====--=+===#+:--=-====+++++==-=++++++#=                                                                                            
                                                 :#=-==-=-==+#####===-==-==++***+++++===++++++#.                                                                                           
                                                 %=-=--=-=----=-==-==-=-=*@@@#=*%@@@*++=++++++#*                                                                                           
                                                **+++++========-===-===+@*.        :#@*++++++++#.                                                                                          
                                                :%+#%@@@*==-=-==-=-=-=#@.           .=@#+++++++#+                                                                                          
                                                 %#:   .:#@==-=-=-==-=@.             :=@+++++++*#                                                                                          
                                                #:        :@==-==-=-=##        @*    ::@#++++++##                                                                                          
                                                %    =.    ##-=-==-=-*@              ::@#++++++#+                                                                                          
                                               .%         :##--=-=@===@=            ::+@++++#*+%:                                                                                          
                                                ++       :=%==#*-=##-==%+         .::#@++++++*#=                                                                                           
                                                 -%#=:::+%#=-==-=-===-==#@*::::::::#@#++++++*#:                                                                                            
                                                  *=*#*+===-=-=-==-=-=-==+*%@@@@@@#*++**+++#+                                                                                              
                                                  :#-=+###%########***++===+++++++++=**++*@#*:                                                                                             
                                                    *###*=++.:=*=*-:=#%#=*#==+++++++=**+%######=.                                                                                          
                                                          +. :=#%#=:-+==++=#*=++++++++*%++*#######:                                                                                        
                                                          -***##%#=---===*###=++++++*%=:+*******###*=.                                                                                     
                                                        =#@#-=##=-====+=.-#%=-=++++##++*=::::::::::::=+++=.                                                                                
                                                        +#====+++++++**#%@%#=-=++#%:-+:.:....        ..:::==          :==-.                                                                
                                                          =#*======-=-====-=++#@%--#*=:.::............:.:::+         =-.:.:==                                                              
                                                          :%+===+++***===+#%%*-=#####+-:.::..:.::::.::--====.:::::.  :++==-::=:                                                            
                                                            .:==+###%#####+:-:--######=::.::::.:.:.:.-==:-===:.....::-=+++*=::=                                                            
                                                                       :===+=---*#==*=::::::.:.::::::===:-==++--=-.....:=+====:                                                            
                                                                     :+-:::-+#####+=+::::..:.:.:....::--===+#%*==:.  ...-=:                                                                
                                                                       :++=:-#@%#%@%#=..:::::::::---------:=*#==:.......-++.                                                               
                                                                  .::-==:.:%*      .**=:------:-:--:--:----++=-::--: ..:=++-                                                               
                                                               .#*:. #=..:%-         -#=++****+*++++====-=+=-:..=--=-::=+=+=                                                               
                                                              :#=    *-..=#     +=    ###*#*****##=####+==-::-====-:-====++:                                                               
                                                              *-:    #=-:-%:          ##**#***##*=-=*==-:...========-======                                                                
                                                        .:.   *=    =-====*%.        +#-++##***###+=#-.....  .:::-:::=====.                                                                
                                                       =.:::-==+-==::=======#*:. .:+@=.=++#******##%=...      ..:+=====+*:                                                                 
                                                       -:=*+*+===-=========+=-====::...+::#******###:       .:-++=====+=                                                                   
                                                        :+*###*==============+++:....:==.=#******###     .:=++===+==++#                                                                    
                                                         .=*###++===========+*+==-.....  +##****###*..:=++====++++++#%@-                                                                   
                                                               -++*+=====+***++===-.... .#****####%*=++=======+++*###%@:                                                                   
                                                               =+==++++***+++++=====+++=*#******##%+=====++++++###%%%%-                                                                    
                                                                    -==--*+*++++=++++++##*#########===++++*#######%%#*                                                                     
                                                                        :#*****+++++++*%#********#%#++##%##########%%=                                                                     
                                                                         =#########**=+%##******###%##%%%###########%=                                                                     
                                                                        -*==-=-=**:    .##############%##**+*########:                                                                     
                                                                       ++=-=-=-=++*-   ===-====+######%%**#**+***+*##.                                                                     
                                                                      :*=-===+**++*=  .*==-=====+*####@%#==#***+*+###:                                                                     
                                                                      .*==+*+++++*+   +====-=-=-=*#####:  -##+*+*####*                                                                     
                                                                     :*++=+#++++++*+:.*==-========+####.  =###***####%.                                                                    
                                                                      =#*+#**+#+**+++*+====-======-=++*= .*+++*-=:-###:                                                                    
                                                                      .*==+*#++#*+*#*=+=======-==*===-+*=*+==+#                                                                            
                                                                       :#===+*#+*#*+.===-++-=*=====+**##+=-===*=:                                                                          
                                                                         :*=+****:. -===+##===*=-===+= -*======++#=                                                                        
                                                                           ..       =+-=+##+=-=+*+-+*:   ..+#==-=+#+                                                                       
                                                                                    =+===###+==:=*=         :#+====*+                                                                      
                                                                                   -@*+++*#####*+:            *#==###*  =%#+#+                                                             
                                                                                  *@%#########%.           *#+=+%#**#%%###++=++                                                            
                                                                                =@%###%######%=             ##+***+*+#######%##:                                                           
                                                                                =############@%%%####%%#:  .*#*+*##########%-                                                              
                                                                              *@##############%@#######%%#==######+*+**######=                                                             
                                                                              #%%%@@%@@%%%%####%%*+**+*+*+*++*####%%#%#%**##*                                                              
                                                                              :%####%########@#*=+*+*+*+*+*+*###*+##**#%*####=                                                             
                                                                              *%########%%%%#*==+*+*+*+*+*+**##############%##                                                             
                                                                              -%@%%%%%%%%%%%%##******+*+*****##%%%%%%%%%%%%%%=                                                             
                                                                                :=+*##*###%##############%#%%%%%%%%@%@%@@%%%#.                                                             
                                                                                          *#################%%#=.                                                                          
                                                                                           .-=**#########*=:.                                                                              
                                                                                                                                                          ''')
            print(Okay+Explodered)
            answer8=input("What zombie is this?" + Okay)
            answer8=answer8.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer8=="ducky tube zombie":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end8=time.time()
                    break
                elif answer8=="pool zombie":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end8=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+"Hint: This zombie can go into water."+Okay)
                    elif attempt==2:
                        print(Water+"Hint: This zombie is the only regular zombie that can go into water."+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is 'Ducky Tube Zombie', got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'Ducky Tube Zombie'!")
                    print(Explodered)
                answer8=input("What zombie is this?" + Okay)
                answer8=answer8.lower()
            time8=end8-start8
            steps=eatyourbrains-fails
            print(Wasted)
            print(f"The zombies are {steps} steps away from you!")
            print(Water)
            print(f"You have thought for {time8} seconds.")
            print(Okay)
            print(f"You tried {attempt} times.\n")
            attempt=0
        if not braineaten:
            if zombie_chosen==sequence[7]:
                brainstorm=time1+time2+time3+time4+time5+time6+time7+time8
                yes=input(Victory+"Congratulations! You survived to the end! Do you want to see your results? "+Okay)
                os.system('clear')
                #os.system('cls')
            else:
                ready=input("Are you ready for the next question? ")
        else:
            print(Explodered+"Brainzzz! Deliciouzzz!"+Okay)
            print("You lose.")
            break
    print(f"You tried {totalattempt} times to keep the zombies away from your brains, the zombies move {fails} steps towards you, and you used {brainstorm} seconds to think & write your answers.\n")
    if not braineaten:
        print("You successfully keep your brains safe!")
    else:
        print("Unfortunately, your brains are eaten by the zombies...")
     
def revenge():
    print(Wasted+"Conehead Prince: Now you can revenge towards the author! How to revenge is listed below!\n")   
    print("1 attempt = 1 slap\n1 fail = 1 punch\nevery 30 seconds used = 1 kick\nyou lose the game = 10 slaps + 15 punches + 5 kicks\n additional revenge can be added if you think he is kinda offending something") 
    print(EmotionalDamage+"Buckethead Prince: Oh NOOOO! This is the WORST PART of this game! Give me MERCY! Almighty Players!")  
    slapdamage=20
    punchdamage=50 
    kickdamage=100
    slap=int(input(Explodered+"How many slaps you want to apply? "+Okay))
    punch=int(input(Explodered+"How many punches you want to apply? "+Okay))
    kick=int(input(Explodered+"How many kicks you want to apply? "+Okay))
    totaldamage=slapdamage*slap+punchdamage*punch+kickdamage*kick
    if totaldamage<457:
        print(EmotionalDamage+"Buckethead Prince: Thank you for your mercy! I will not forget you forever!")
    elif totaldamage<913:
        print(EmotionalDamage+"Buckethead Prince: I think I deserves that...")
    elif totaldamage<1370:
        print(Wasted+"Conehead Prince: You beat him quite hard... He does not want to see anyone or any zombie now.")
    else:
        print(Wasted+"Conehead Prince: I think you beat him TOO HARD... He already fainted...")
    
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
        revenge()
guesszombie()
    