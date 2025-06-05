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
                if answer2=="":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end2=time.time()
                    break
                elif answer2=="":
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
                        print(Water+""+Okay)
                    elif attempt==2:
                        print(Water+""+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is , got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is !")
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
                if answer3=="":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end3=time.time()
                    break
                elif answer3=="":
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
                        print(Water+""+Okay)
                    elif attempt==2:
                        print(Water+""+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is , got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is !")
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
                    end4=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+""+Okay)
                    elif attempt==2:
                        print(Water+""+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is...how can I describe that? a 'mixed zombie'! got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is 'mixed zombie'!")
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
                        print(Water+""+Okay)
                    elif attempt==2:
                        print(Water+""+Okay)
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
            print(r'''''')
            print(Okay+Explodered)
            answer6=input("What zombie is this?" + Okay)
            answer6=answer6.lower()
            while True:
                attempt+=1
                totalattempt+=1
                if answer6=="":
                    print(Iceblue+"Conehead Prince: At least your brain is safe...for now."+Okay)
                    end6=time.time()
                    break
                elif answer6=="":
                    print(EmotionalDamage+"Buckhead Prince: This is TOO EASY for YOU! It will be harder soon! HAHAHAHA!"+Okay)
                    end6=time.time()
                    break
                else:
                    print(Wasted+"Wrong answer!!"+Explodered+"We Gonna Eat Your Brains!"+Okay)
                    fails+=1
                    if eatyourbrains==fails:
                        braineaten=True
                        break
                    if attempt==1:
                        print(Water+""+Okay)
                    elif attempt==2:
                        print(Water+""+Okay)
                    elif attempt==3:
                        print(Wasted+"Conehead Prince: You are stupid enough for me to give you the answers...it is , got it?"+Okay)
                    else:
                        print(Explodered+"Your brains is stupid! We love stupid brains!")
                        time.sleep(0.5)
                        print(Wasted+"Conehead Prince: Are you blind?! The answer is !")
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
    