#to do- make the game less wordy and ready instead make it more interactive
#to do- make health replenish even if dice rolled > health that can be restored (error faced while talkin to ishaan bhya)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#CHEAT CODE to defeat pirate= 1-1-4-1
#CHEAT CODE to defeat diciple= 1-3-4-1-4-3-4-1-4-4-3-4-1-4-3-4-2-4-1

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
toxicgas=("1. TOXIC GAS (Gives 30 damage to target when used, then 5 damage each subsequent round. Cost: 25 Magic)")
pointer=("2. THREE POINTER (Restores 3x <dice roll> Health. Cost: 10 Magic)")
somn=("3. SOMN (When used, enables you to dodge next attack directed at you. It can not be used consecutively Cost: 15 Magic)")
son=('4. SONG OF NATURE (Restores 15 Magic)')
powers=('What power would you like to use? (TOXIC GAS (1), 3 POINTER (2), SOMN (3), SONG OF NATURE (4) ):')
usetoxic=('--> Henry used TOXIC GAS and gave 30 damage')
usepointer=('--> Henry used 3 POINTER and restored')
farewell=('We didnt expect you to leave this early :(, Farewell warrior')
usesomn=('--> Henry used SOMN to dodge the next attack')
useson=('--> Henry used SONG OF NATURE and restored 15 magic')
toxicgas2=("1. TOXIC GAS (Gives 40 damage to target when used Cost: 25 Magic)")
pointer2=("2. THREE POINTER (Restores 3x <dice roll> Health. Cost: 10 Magic)")
somn2=("3. SOMN (When used, enables you to dodge next attack directed at you. It can only be used once Cost: 15 Magic)")
son2=('4. SONG OF NATURE (Restores 20 Magic)')
powers=('What power would you like to use? (TOXIC GAS (1), THREE POINTER (2), SOMN (3), SONG OF NATURE (4) ):')
usetoxic2=('--> Henry used TOXIC GAS and gave 40 damage')
usepointer2=('--> Henry used THREE POINTER and restored')
usesomn2=('--> Henry used SOMN to dodge the next attack')
useson2=('--> Henry used SONG OF NATURE and restored 20 magic')

tidalconflict =("Kraken used TIDAL CONFLICT and drained 20 magic")
poseidon=("Kraken used POSEIDON'S RAGE and gave 60 damage" ) 
whip=("Krake used WHIP and gave 20 damage")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#GAME,STATS = >>
#STORY= |>
#MOVES,PROMPTS= -->"""

import random as r


import time,os,sys

def typingprint(text):
        
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.0)
    
def typinginput(text):
        
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.0)
        value = input()  
        return value  

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
story1=("|> You begin your journey at the docks, where you are surrounded by a gang of pirates. You must defeat their chief to make it to the ship")
story2=("|> PHEWW! That was an intense fight.")
story3=("|> The pirate dropped a MAGICALy POTION on the ground")
story4=("|> This potion has a 50/50 chance of either giving you +30 hp or -5hp, choose wisely Warrior alot is at STAKE here!")
story5=("|> You refused to drink the potion. Hmm... smart choice, I wouldn't trust that pirate anyways.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

story6=("|> NICE WARRIOR, the job is done. The CHIEF has been defeated.")

story7=("|> The pirate's crew surrendered themselves and swore their loyalty to you as their new CAPTAIN.")

story8=("|> ALRIGHT, it's time to get the gears running! Get on the pirate's ship and start sailing.")

story9=("* You are in the waters now with no sign of land and a few more hours pass by *")

story10=("|> The weather seems to be perfect today!")

story11=(" Wha- What's that?" ) 

story12=("|> A CREW MEMBER - 'I guess its an island. What should we do Captain ?'")     

story13=("--> Enter (Yes) to stop at the Island and (no) to move ahead : ") #Dont be a pussiyo

story14=("|> You anchored your ship and set out to explore the island, the crew members stayed behind to protect the ship.")

story15=("|> You set foot in the island and can see a big banner in the distance.")
banner1=("                          |-------------------|                        ")
banner2=("                          |  KRAKEN FESTIVAL  |                        ")
banner3=("                          |-------------------|                        ")
banner4=("                          |                   |                        ")
banner5=("                          |                   |                        ")


story16=("|> WHAT AN AMAZING FESTIVAL! I have to check this OUT !!")
story17=("|> You enter the festival and see a huge map of the whole island")
story18=("Beneath the map you see information about the festival")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def map1():





                print('                                    KRAKEN ISLAND                                      ')
                print("---------------------------------------------------------------------------------------")
                print("                                          ,-.^._                      _                ")
                print("                                        .'      `-.                 ,'  ;              ")
                print("                           /`-.  ,----'            `-.       _ ,-.,'  /                ")
                print("                        _.'   `--'                    `-' '-'    ._ ;                  ")
                print("                        :                         o             ;    __,-.             ")
                print("       You are here <-------  o                 Narva           ;_,-',.__'--.          ")
                print("                        : Rothenburg                           ,--```    `--'          ")
                print("                        :                                      ;                       ")
                print("                        :                                      :                       ")
                print("                        ;                                      :                       ")
                print("                        (                    Jorvik            ;                       ")
                print("                        `-.                    o              ,'                       ")
                print("                          ;                                   :                        ")
                print("                         .'                             .-._,'                         ")
                print("                       .'                                 `.                           ")
                print("                    _.'                                .__;                            ")
                print("                    `._                   *           ;                                ")
                print("                       `.              KANDHAR       :     ,---------------------.     ")
                print("                         `.              ,..__,---._;      |    KRAKEN Island    |     ")
                print("                           `-.__         :                 | Capital: KANDHAR    |     ")
                print("                                `.--.____;                 | Population: 4000    |     ")
                print("                                                           | Area: 6475 sq.km.   |     ")
                print("                                                           `---------------------'     ")                      
                print("                                                                                       ")
                print("                                                                                       ")
                print("                                                                                       ")
                print("---------------------------------------------------------------------------------------")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def map2():





                print('                                    KRAKEN ISLAND                                      ')
                print("---------------------------------------------------------------------------------------")
                print("                                          ,-.^._                      _                ")
                print("                                        .'      `-.                 ,'  ;              ")
                print("                           /`-.  ,----'            `-.       _ ,-.,'  /                ")
                print("                        _.'   `--'                    `-' '-'    ._ ;                  ")
                print("                        :                         o             ;    __,-.             ")
                print("                       ,'     o                 Narva           ;_,-',.__'--.          ")
                print("                        : Rothenburg                           ,--```    `--'          ")
                print("                        :                                      ;                       ")
                print("                        :                                      :                       ")
                print("                        ;                                      :                       ")
                print("                        (                    Jorvik            ;                       ")
                print("                        `-.                    o              ,'                       ")
                print("                          ;                                   :                        ")
                print("                         .'                             .-._,'                         ")
                print("                       .'                                 `.                           ")
                print("                    _.'                                .__;                            ")
                print("                    `._                   *           ;                                ")
                print("                       `.              KANDHAR       :     ,---------------------.     ")
                print("                         `.              ,..__,---._;      |    KRAKEN Island    |     ")
                print("                           `-.__         :    ▲            | Capital: KANDHAR    |     ")
                print("                                `.--.____;    ▲            | Pop: 4000           |     ")
                print("                                              ▲            | Area: 2500 sq.mi.   |     ")
                print("                                         You are here      |      (6475 sq.km.)  |     ")
                print("                                                           `---------------------'     ")
                print("---------------------------------------------------------------------------------------")

def henry2():
    import random as r


    import time,os,sys
    def tp(text):  
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        
    def ti(text):
            
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.1)
        value = input()  
        return value 


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    os.system('clear')
    print("*"*100)
    print('')
    tp(story6)
    print('')
    print('')
    
    tp(story7)
    print('')
    print('')
    tp(story8)
    print('')
    print('')
    tp(story9)
    print('')
    print('')
    tp(story10)
    print('')
    print('')
    
    tp('|> WAIT!')
    for character in ('....'):
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.8)
    tp(story11) 
    print(" ")
    print(" ")
    tp(story12)
    print(" ")
    print(" ")
    print("-"*100)
    print(" ")
    
    

    a3=ti(story13)
    if a3=="yes":
        print('')
        print('')
        tp(story14)
        print('')
        print('')
        tp(story15)
        print('')
        print('')      
        time.sleep(1) 
        os.system('clear') 
        print(banner1)
        print(banner2)
        print(banner3)
        print(banner4)
        print(banner5)       
        print(' ')
        print('*'*100)
        print(' ')
        tp(story16)
        print('')
        print('')
        tp(story17)
        print('')
        print('')
        time.sleep(1)
        print('')
        print('')
        map1()
        print('')
        print('')
        tp("|> You look at the map and seeing it gives you some inexplicable, blurry flashbacks. \n|> You snap out of it and looking around, feel lost at the festival")
        print(" ")
        print(" ")
        print(" ")
        tp("|> You remember your quest, and decide to go find information on where to find the Kraken rather than enjoying a festival.")
        print(" ")
        print(" ")
        print(" ")
        tp("|> You decide to head to the nearest city, ROTHENBURG.")
        print(" ")
        print(" ")
        tp("|> As you are roaming the streets of the city, you get the weird feeling that you are being tailed...")
        print(" ")
        print(" ")
        tp("|> You look over your shoulder and sure enough, there is a mysterious cloaked man following you. You remember him from the festival.")
        print(" ")
        print(" ")
        tp("|> You turn into a narrow alleyway with the intention of confronting this stalker, but he catches you by surprise!")
        print(" ")
        print(" ")
        tp("|> He corners you and holds a knife to your neck. He introduces himself as BLUFFMASTER.")
        print(" ")
        print(" ")
        tp("|> BLUFFMASTER: 'Who are you and what are you here for?'")
        print(" ")
        print(" ")
        tp("|> HENRY: 'I am Henry from the fields of Eastwood, here on a quest to kill the Kraken'")
        print(" ")
        print(" ")
        tp("|> BLUFFMASTER: 'It really is you. You aren't ready to take on the Kraken yet, but I can help you'")
        print(" ")
        print(" ")
        tp("|> HENRY: 'Who are you and why should I trust you?'")
        print(" ")
        print(" ")
        tp("|> BLUFFMASTER: 'I was an ally of your parents during the revolution... I was there on the fateful night when the Kraken killed them...'")
        print(" ")
        print(" ")
        tp("** BLUFFMASTER shows you a picture of his younger self with your parents **")
        print(" ")
        print(" ")
        tp("|> BLUFFMASTER: 'You need to learn more, and become stronger to beat the Kraken. You must go to NARVA, and defeat my disciple to prove that you are capable of taking on the Kraken.'")
        print(" ")
        print(" ")
        
        tp('|> With that, just as mysteriously as he had appeared, BLUFFMASTER disappeared into the crowd.')
        print(" ")
        print(" ")
        tp("|> You find a carriage on the outskirts of ROTHENBURG, but have no money to pay for the ride to NARVA.")
        print(" ")
        print(" ")
        tp("|> The carriage owner, CIED, gives you an offer...")
        print(" ")
        print(" ")
        tp("|> CIED: 'Play my game and if you win, you get the ride for free. Roll the 2 dice I give you, and if the total is greater than 7, you win.'")
        print(" ")
        print(" ")
        tp("|> All out of options, you agree")
        print(" ")
        print(" ")
        tp("|> CIED: 'Very well... here we go'")
        print(" ")
        print(" ")
        d1=r.randint(3,6)
        d2=r.randint(4,6)
        tp(f'|> You roll the first dice... You got a {d1}')
        print(" ")
        tp(f'|> You roll the second dice and get a {d2}')
        print(" ")
        print(" ")
        tp("|> CIED: 'You have won! That was highly unlikely, you are a lucky one. Hop on, let's go to NARVA'")
        print(" ")
        print(" ")
        print("*"*100)
        print(" ")
        print(" ") 
        
#---------------------------------------------------------------------------------------NARVA---------------------------------------------------------------------------------------------------------
#correct the alignment when you uncomment the above code
        os.system('clear')      
        print("*"*100)
        print(" ")
        tp("|> You reach NARVA, a small city and see a temple. The disciple must be there!")
        print(" ")
        print(" ")
        tp("|> You enter the temple and are met with an eerie silence. Ahead of you stands a man clad in armour, poised for battle.")
        print(' ')
        print(" ")
        tp("|> DISCIPLE: 'I am the disciple of the legendary warrior now known as BLUFFMASTER... I have been expecting you'")
        print(" ")
        print(" ")
        tp("With that, the disciple charges towards you")
        print(" ")
        print(" ")
        
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
        
        e2hp2=140
        tp("|> The DISCIPLE has 140 health")
        print(' ')
        print(' ')
        print("*"*100)
        print(" ")
        print(" ")
        health=150
        magic=60
        while e2hp2>0:
            if health>0:
                a1=input(powers)
                print(" ")
                print("-"*100)
                print(" ")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
                if a1=='1':
                    if magic>=25:
                        magic-=25
                        e2hp2-=30
                        print(usetoxic)               
                        print(' ')
                        print(" ")
                        print(' ')
                        print("-"*100)
                        print(" ")
                        
                    else:
                        print(f">. {magic} magic left")
                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)
                        continue   
                    print(f'>> The Disciple has {e2hp2} health left')                                              
                elif a1=='2':
                    if magic>=10:
                        rh=r.randint(1,10)
                        print(f'{usepointer} {5*rh} health')
                        print(' ')
                        print(' ')
                        health+=5*rh
                        if health>=150:
                            health=150
                            print("HEALTH IS ALREADY FULL YOU CAN'T GET ANY STRONGER ;)")
                            print(f'>> Health is now {health} and {magic} magic left')
                            print(' ')
                            print("-"*100)
                            print(" ")
                        else:
                            tp(f'>> Health is now {health}')
                            print(' ')
                            magic-=10
                            print(f'>> Henry has {magic}magic left')           
                            print(' ')
                            print("-"*100)
                            print(" ")
                    else:
                        print(f">> {magic} magic left")
                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)
                        continue 
                    print(f'>> The Disciple has {e2hp2} health left')
                elif a1=='3':
                    if magic>=15:
                        print(usesomn)
                        print(" ")
                        magic-=15
                        print(f'>> Henry has {health} health and {magic} magic left')
                        print(" ")                 
                        print("-"*100)
                        print(" ")
                    else:
                        print(f">> {magic} magic left")
                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)
                        continue 
                    print(f'>> The Disciple has {e2hp2} health left')
                elif a1=='4':
                    print(useson)
                    print(" ")
                    magic+=15
                    if magic>=60:
                        magic=60
                        print(f'>> Henry has {health} health and {magic} magic left')
                        print(" ")
                        print("-"*100)
                        print(" ")
                    else:
                        print(f'>> Henry has {health} health and {magic} magic left')
                        print(" ")
                        print("-"*100)
                        print(" ")
                    print(f'>> The Disciple has {e2hp2} health left')
                else: 
                    print('|> Wrong input.')
                    print(" ")
                    continue
                
                if e2hp2<=0:
                    e2hp2=0
                    os.system('clear')
                    print("YOU HAVE DEFEATED THE DECIPAL")
                
                else:
                    if a1=='3':
                        for i in range(1):
                            print("--> The Disciple attacked but Henry Dodged !!")
                            print(' ')
                            print("-"*100)
                            print(" ")
                            a1=ti(powers)
                            print(" ")
                            print("-"*100)
                            print(" ")
                            if health>0:
                                if a1=='1':
                                    if magic>=25:
                                        magic-=25
                                        e2hp2-=30
                                        print(usetoxic)               
                                        print(' ')
                                        print(" ")
                                        print(' ')
                                        print("-"*100)
                                        print(" ")
                                        
                                    else:
                                        print (f">. {magic} magic left")
                                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                                        print(" ")
                                        print("*"*100)
                                        continue   
                                    print(f'>> The Disciple has {e2hp2} health left')                                              
                                elif a1=='2':
                                    if magic>=10:
                                        rh=r.randint(1,10)
                                        print(f'{usepointer} {5*rh} health')
                                        print(' ')
                                        print(' ')
                                        health+=5*rh
                                        if health>=150:
                                            health=150
                                            print("HEALTH IS ALREADY FULL YOU CAN'T GET ANY STRONGER ;)")
                                            print(f'>> Health is now {health} and {magic} magic left')
                                            print(' ')
                                            print("-"*100)
                                            print(" ")
                                        else:
                                            print(f'>> Health is now {health}')
                                            print(' ')
                                            magic-=10
                                            print(f'>> Henry has {magic}magic left')           
                                            print(' ')
                                            print("-"*100)
                                            print(" ")
                                    else:
                                        print(f">> {magic} magic left")
                                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                                        print(" ")
                                        print("*"*100)
                                        continue 
                                    print(f'>> The Disciple has {e2hp2} health left')
                                elif a1=='3':
                                    if magic>=15:
                                        print(usesomn)
                                        print(" ")
                                        magic-=15
                                        print(f'>> Henry has {health} health and {magic} magic left')
                                        print(" ")                 
                                        print("-"*100)
                                        print(" ")
                                    else:
                                        print(f">> {magic} magic left")
                                        print("(Not enough magic, use SONG OF NATURE to replenish)")
                                        print(" ")
                                        print("*"*100)
                                        continue 
                                    print(f'>> The Disciple has {e2hp2} health left')
                                elif a1=='4':
                                    print(useson)
                                    print(" ")
                                    magic+=15
                                    if magic>=60:
                                        magic=60
                                        print(f'>> Henry has {health} health and {magic} magic left')
                                        print(" ")
                                        print("-"*100)
                                        print(" ")
                                    else:
                                        print(f'>> Henry has {health} health and {magic} magic left')
                                        print(" ")
                                        print("-"*100)
                                        print(" ")
                                    print(f'>> The Disciple has {e2hp2} health left')
                                else: 
                                    print('|> Wrong input.')
                                    print(" ")
                                    continue
                                    
                                print("--> The Disciple attacked but Henry Dodged !!")
                                print(' ')
                                print("-"*100)
                                print(" ")
                            else:
                                print("|> GAME OVER (No Health Left)")
    
                    else:
                        da=r.randint(10,25)
                        health-=da
                        print(f'--> The Disciple attacked you and gave you {da} damage')
                        print(' ')
                        print(f">> Henry has {health} health left and {magic} magic left")
                        print(' ')
                        print("-"*100)
                        print(" ")
            else:
                print("|> GAME OVER (No Health Left)")
                print(" ")
                print("*"*100)
                print(" ")
                break

def henry3():
    story19=("|> The dust inside the old temple settles... You have done it! After the intense battle, you have emerged victorious")
    story20=("DISCIPLE : 'Impressive... I am KAYTARO, the first disciple of the legendary warrior now known as BLUFFMASTER.'")
    story21=("HENRY : 'Who is BLUFFMASTER and what relation does he heave with my parents?'")
    story22=("KAYTARO : 'I don't have the answer to that. All I know is that he was one of the most legendary warriors in the revolution, until he lost everyone he loved and retired from fighting. He trained me for years to complete his task and defeat the KRAKEN. But, I was unsuccessful...' ")
    story23=("|> KAYTARO shows a huge scar on his chest")
    story24=("KAYTARO : 'The road you have chosen to walk is a long and difficult one. The price to pay is huge, so be careful. The BLUFFMASTER believes you have what it takes to free the people of this land from the tyranny of the KRAKEN, but you will need a strong suit of armour to stand any chance.' ")
    story25=("|> KAYTARO gives you a magnificent, rustic suit of armour that gleams in the moonlight. Upon seeing the armour, you see flashes of war, but try to ignore them and stay focused on your quest")
    story26=("KAYTARO : 'You must rest here for the night. I shall see you in the morning'")
    story27=("|> You settle in and KAYTARO takes off into the night...")
    story28=("|> The next morning you wake up to a horror scene! KAYTARO is laying in front of you, taking his final breaths...")
    story29=("KAYTARO : 'I don't have time to explain... they know you're here... take this...'")
    story30=("|> KAYTARO hands you a mysterious, dark orb")
    story31=("KAYTARO : 'This will be useful to you... you'll know when the time is right... only you can save this island now...'")
    story32=("|> With those final words, KAYTARO passes away in your arms.")
    print(story19)
    print('')
    print(story20)
    print('')
    print(story21)
    print('')
    print(story22)
    print('')
    print(story23)
    print('')
    print(story24)
    print('')
    print(story25)
    print('')
    print(story26)
    print('')
    print(story27)
    print('')
    print('-'*100)
    print('')
    print(story28)
    print('')
    print(story29)
    print('')
    print(story30)
    print('')
    print(story31)
    print('')
    print(story32)
    print('-'*100)
    print('')
    print('')
    print('WOAH, I feel really different, the new armour makes me feel a lot stonger! ')
    print('')
    print("--> All of Henry's attributes have gained +10 effect")
    print('')
    print('-'*100)
    print('')
    print("|> With that Henry leaves the temple and sets out to Kandhar on his journey to defeat the KRAKEN.")
    print("")
    print("|> The journey is a long one! From the temple in Narva to the city of Jorvic to the dangerous city of KANDHAR ")
    print("")
    print("|> Henry reaches Jorvic where he notices that people are in distress due to the suffering caused by KRAKEN")
    print("")
    print("HENRY: I need to do something about this soon! It's not fair whats happening to this beautiful land")
    print("")
    print("|> HENRY looks towards the orb he got from kaytaro and notices that it has a slight glow.")
    print("")
    print("|> With this in mind Henry sets out with a strong determination to defeat the KRAKEN and end the suffering once and for all")
    print("")
    print("|> Henry reaches the dangerous city of KANDHAR")
    print("")
    print("|> Before you lies a once prosperous city that has now fallen to ruin. The KRAKEN has turned Kandhar to a ghost town, where the dilapidated buildings and whistling winds resonate the suffering of the people that once called this land home.")
    print("")
    print("|> Seeing the ruins makes the visions from your nightmares reappear, and the mysterious orb KAYTARO gave you starts to glow even brighter... ")
    print("")
    print("|> As you navigate your way through the fallen city, marching on towards the KRAKEN, you can't stop thinking about all the things that have led you to this point- there is no turning back now...")
    print("")
    print("|> As you approach the port, you suddenly hear a huge crashing of waves... and sure enough, there he is, your nemesis- THE MIGHTY KRAKEN")
    print("")
    print("KRAKEN : 'Took you long enough... HENRY of Eastwood! I have been waiting for you... You shall fall to same fate as your parents and their revolution! Prepare to die!'")
    print("")
    print("HENRY : 'My whole life, I have longed to avenge the death of my parents. I have watched, learned, and grown... and today, I shall have my revenge!'")
    print("")
    print("|> Time stands still as the legendary battle between you, the greatest warrior in the land, and the mighty, seemingly undefeatable KRAKEN starts...")
    print("")

def henry4():
    khp=500
    hhp=250
    hmagic=100

    import random as r
    import os


    while khp>0:
                if hhp>0:
                    a1=input(powers)
                    print(" ")
                    print("-"*100)
                    print(" ")
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
                    if a1=='1':
                        if hmagic>=25:
                            khp-=40
                            print(usetoxic2)               
                            print(' ')
                            print('>> Kraken has', khp ,'health left')
                            hmagic-=25
                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                            print(' ')
                            print("-"*100)
                            print(" ")
                        else:
                            print(">>", hmagic ,"magic left")
                            print("(Not enough magic, use SONG OF NATURE to replenish)")
                            print(" ")
                            print("*"*100)                                                 
                    elif a1=='2':
                        if hmagic>=10:
                            rh=r.randint(5,10)
                            print(usepointer2, 3*rh, 'health')
                            print(' ')
                            hhp+=3*rh
                            if hhp>=250:
                                hhp=250
                                print("HEALTH IS ALREADY FULL YOU CAN'T GET ANY STRONGER ;)")
                                print('>> Health is now', hhp ,'and' , hmagic , 'magic left')
                                print(' ')
                                print("-"*100)
                                print(" ")
                            else:
                                print('>> Health is now', hhp)
                                print(' ')
                                hmagic-=10
                                print('>> Henry has', hmagic, 'magic left')           
                                print(' ')
                                print("-"*100)
                                print(" ")
                        else:
                            print(">>", hmagic ,"magic left")
                            print("(Not enough magic, use SONG OF NATURE to replenish)")
                            print(" ")
                            print("*"*100)
                            break
                    elif a1=='3':
                        if hmagic>=15:
                            print(usesomn2)
                            print(" ")
                            hmagic-=15
                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                            print(" ")
                            print("-"*100)
                            print(" ")
                        else:
                            print(">>", hmagic ,"magic left")
                            print("(Not enough magic, use SONG OF NATURE to replenish)")
                            print(" ")
                            print("*"*100)
                            break
                    elif a1=='4':
                        print(useson2)
                        print(" ")
                        hmagic+=20
                        if hmagic>=100:
                            hmagic=100
                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                            print(" ")
                            print("-"*100)
                            print(" ")
                        else:
                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                            print(" ")
                            print("-"*100)
                            print(" ")
                    else: 
                        print('|> Wrong input.')
                        print(" ")
                        continue
    #___________________________________________________________________________________________________________________
                    if khp<=0:
                        khp=0
                        print("Kraken was DEFEATED !!")
                        
    #____________________________________________________________________________________________________________________________
                    else:
                        if a1=='3':
                            for i in range(1):
                                print("--> Kraken attacked but Henry Dodged !!")
                                print(' ')
                                print("-"*100)
                                print(" ")
                                a1=input(powers)
                                print(" ")
                                print("-"*100)
                                print(" ")
                                if hhp>0:
                                    if a1=='1':
                                            if hmagic>=25:
                                                khp-=40
                                                print(usetoxic2)
                                                print(' ')
                                                print('>> Kraken has', khp, 'health left')
                                                hmagic-=25
                                                print('>> Henry has', hhp , 'health and', hmagic, 'magic left)')
                                                print(' ')
                                                print("-"*100)
                                                print(" ")
                                            else:
                                                print(">>", hmagic ,"magic left")
                                                print("(Not enough magic, use SONG OF NATURE to replenish)")
                                                print(" ")
                                                print("*"*100)
                                                break
                                    elif a1=='2':
                                        if hmagic>=10:
                                            rh=r.randint(5,10)
                                            print(usepointer2, 3*rh, 'health')
                                            print(' ')
                                            health+=3*rh
                                            if health>=250:
                                                health=250
                                                print('>> Health is now', health)
                                                print(' ')
                                                print("-"*100)
                                                print(" ")
                                            else:
                                                print('>> Health is now', hhp)
                                                print(' ')
                                                hmagic-=10
                                                print('>> Henry has', hhp ,'health and', hmagic, 'magic left')           
                                                print(' ')
                                                print("-"*100)
                                                print(" ")
                                        else:
                                            print(">>", hmagic ,"magic left")
                                            print("(Not enough magic, use SONG OF NATURE to replenish)")
                                            print(" ")
                                            print("*"*100)
                                            break
                                    elif a1=='3':
                                        if hmagic>=15:
                                            print(usesomn2)
                                            print(" ")
                                            hmagic-=15
                                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                                            print(" ")
                                            print("-"*100)
                                            print(" ")
                                        else:
                                            print(">>", hmagic ,"magic left")
                                            print("(Not enough magic, use SONG OF NATURE to replenish)")
                                            print(" ")
                                            print("*"*100)
                                            break
                                    elif a1=='4':
                                        print(useson2)
                                        print(" ")
                                        hmagic+=20
                                        if hmagic>=100:
                                            hmagic=100
                                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                                            print(" ")
                                            print("-"*100)
                                            print(" ")
                                        else:
                                            print('>> Henry has', hhp, 'health and', hmagic, 'magic left')
                                            print(" ")
                                            print("-"*100)
                                            print(" ")                     
                                    print("--> The Pirate attacked but Henry Dodged !!")
                                    print(' ')
                                    print("-"*100)
                                    print(" ")
                                else:
                                    print("|> GAME OVER (No Health Left)")

                        else:
                            prob=r.randint(1,4)
                            if prob==1 or prob==2:
                                print(poseidon)
                                hhp-=60
                                print('>> Henry has', hhp, 'health')
                            if prob==3:
                                print(tidalconflict)
                                hmagic-=20
                                print('>> Henry has ', hmagic ,'magic left')
                            if prob==4:
                                print(whip)
                                hhp-=20
                                print('>> Henry has', hhp, 'health')
                                
                                
                                
                else:
                    print("|> GAME OVER (No Health Left)")
                    print(" ")
                    print("*"*100)
                    print(" ")
                    break
    print("|> You lay on the ground, dumbfounded by the strength of the KRAKEN, severely wounded and on the verge of death... As you lay there, slowly losing your consciousness, you finally see it - the visions you kept having... the scene of terror you witnessed as a young boy")
    print("")
    print("|> You now vividly remember seeing the KRAKEN conquering your hometown, destroying and killing everything in its path. You had trained all your life for revenge, but now you lay on the ground, defeated, resigned to your fate... BUT WAIT! ")
    print("")
    print("|> WHAT IS THAT? THE ORB KAYTARO GAVE YOU!")
    print("")
    print("|> You had seemingly forgotten about the orb, but now it glows with a blinding blue light!")
    print("")
    print("|> 'You will know when the time is right...' - IT ALL MAKES SENSE! THE SUFFERING OF THE PEOPLE YOU HAD WITNESSED HAD CHANNELED THE ENERGY OF THE UNIVERSE INTO THE ORB, AND THIS WAS THE MISSING PIECE OF THE PUZZLE! THIS WAS THE KRYPTONITE OF THE KRAKEN!")
    print("")
    print("|> With a sudden burst of light, the orb bursts open, energizing you, bringing you back from the brink of death and making you feel powerful like you have never felt before!")
    print("")
    fin=input('Press F to finish the KRAKEN! : ')
    if fin=='f' or "F":
        print("|> YOU CHANNEL THE ENERGY FROM THE ORB, AND FIRE IT WITH ALL YOUR MIGHT AT THE KRAKEN!")
        print("")
        print("|> WITH A HUGE CRASH, THE KRAKEN COLLAPSES UNDER THE FORCE FROM YOUR ENERGY BEAM!")
        print("")
        print("|> YOU HAVE DONE IT! YOU HAVE FINALLY DEFEATED THE MIGHTY KRAKEN AND FREED ALL OF THE LAND! YOU FINALLY HAVE YOUR REVENGE!")
        print("")
        print("|> KRAKEN : 'Ho- how? How is this possible? The ORB OF KALOS? I remember your parents had discovered this from the ancient Temple of Livramento in the land of the Aztecs, bu- but nobody ever knew how to use it... Not them, not their friend the BLUFFMASTER, not his son KAYTARO... How is this possible?...'")
        print("")
        print("HENRY : 'Good always triumphs over evil... I was the chosen one, and now your reign of terror finally comes to an end.'")
        print("")
        print("|> With that, you head to the shore to return to your hometown a victorius warrior, leaving the Kraken there to die...")
        print("")
        print("|> CONGRATULATIONS WARRIOR! YOU HAVE COMPLETED YOUR QUEST AND BROUGHT PROSPERITY TO THE WHOLE LAND! WITH THIS WE MUST PART WAYS. UNTIL NEXT TIME...")
    else: 
        print("|> You take too long to make your move, and the KRAKEN realises what you are about to do. With a mighty wave of the sea, he finishes you before you are able to take your chance.")
        print("")
        print("|> GAME OVER. PLEASE TRY AGAIN!")
        


def henry1():   
    e1hp1=80
    print(' ')
    print("*"*100)
    print(" ")
    typingprint('WELCOME! to your quest, noble beast Henry. Here are your attributes: ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print('>> Health: 150')
    print('>> Magic: 60')
    print(' ')
    print('_'*100)
    print(" ")
    typingprint('Your Special Powers are:' )
    print(' ')
    typingprint(toxicgas)
    print(' ')
    typingprint(pointer)
    print(' ')
    typingprint(somn)
    print(' ')
    typingprint(son)
    print(' ')
    print(' ')
    print('_'*100)
    print(" ")
    health=150
    magic=60
    n=typinginput('>> Are you ready to begin your quest? (Y/N):  ')
    print(" ")
    print("-"*100)
    print(" ")
    if n=='Y'or n=='y' :
        typingprint(story1)
        print(' ')
        typingprint('|> The pirate has 80 health')
        print(" ")
        print("-"*100)
        print(" ")
        while e1hp1>0:
            if health>0:
                a1=input(powers)
                print(" ")
                print("-"*100)
                print(" ")
 #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
                if a1=='1':
                    if magic>=25:
                        e1hp1-=30
                        typingprint(usetoxic)               
                        print(' ')
                        print('>> The Pirate has', e1hp1,'health left')
                        magic-=25
                        print('>> Henry has', health, 'health and', magic, 'magic left')
                        print(' ')
                        print("-"*100)
                        print(" ")
                    else:
                        print(">>", magic ,"magic left")
                        typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)                                                 
                elif a1=='2':
                    if magic>=10:
                        rh=r.randint(1,10)
                        print(usepointer, 3*rh, 'health')
                        print(' ')
                        health+=3*rh
                        if health>=150:
                            health=150
                            typingprint("HEALTH IS ALREADY FULL YOU CAN'T GET ANY STRONGER ;)")
                            print('>> Health is now', health ,'and' , magic , 'magic left')
                            print(' ')
                            print("-"*100)
                            print(" ")
                        else:
                            print('>> Health is now', health)
                            print(' ')
                            magic-=10
                            print('>> Henry has', magic, 'magic left')           
                            print(' ')
                            print("-"*100)
                            print(" ")
                    else:
                        print(">>", magic ,"magic left")
                        typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)
                        break
                elif a1=='3':
                    if magic>=15:
                        typingprint(usesomn)
                        print(" ")
                        magic-=15
                        print('>> Henry has', health, 'health and', magic, 'magic left')
                        print(" ")
                        print("-"*100)
                        print(" ")
                    else:
                        print(">>", magic ,"magic left")
                        typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                        print(" ")
                        print("*"*100)
                        break
                elif a1=='4':
                    typingprint(useson)
                    print(" ")
                    magic+=15
                    if magic>=60:
                        magic=60
                        print('>> Henry has', health, 'health and', magic, 'magic left')
                        print(" ")
                        print("-"*100)
                        print(" ")
                    else:
                        print('>> Henry has', health, 'health and', magic, 'magic left')
                        print(" ")
                        print("-"*100)
                        print(" ")
                else: 
                    print('|> Wrong input.')
                    print(" ")
                    continue
#______________________________________________________storyline2_________________________________________________
                if e1hp1<=0:
                    e1hp1=0
                    os.system('clear')
                    typingprint('You have defeated the pirate')
                    
                    print(" ")
                    print("*"*100)
                    print(" ")
                    print(story2)
                    print(" ")
                    print(">> Henry is on",health,"health and ",magic,"magic")
                    print(" ")
                    typingprint(story3)
                    print(" ")
                    typingprint(story4)
                    print(' ')
                    print('_'*100)
                    print(" ")
                    a2=typinginput("|> If you wish to drink it enter (drink) and if you dont want to enter (no) : ")
                    print(' ')
                    print('_'*100)
                    print(" ")
                    if a2=='drink'or a2=='Drink' :
                       i=r.randint(1,2)
                       if i==1:
                           health+=30
                           typingprint("|> You are a lucky one!")
                           print(" ")
                           print('>> Health increased to', health )
                           print(" ")
                           print(">> Henry now has", health ,"and", magic , "magic")
                           print(' ')
                           print('_'*100)
                           print(" ")
                           map1()
                           henry2()
                           henry3()
                           henry4()
                       else:
                           health-=5
                           typingprint("|> Bad choice; No worries it's just 5 hp right?")
                           print(" ")
                           print('>> Health decreased to', health )
                           print(" ")               
                           print(">> Henry now has", health ,"and", magic , "magic")
                           print(' ')
                           print('_'*100)
                           print(" ")
                           map1()
                           henry2()
                           henry3()
                           henry4()
                    elif a2=='no' or a2=='No':
                        print(' ')
                        print('_'*100)
                        print(" ")
                        typingprint(story5)
                        print(' ')
                        print('_'*100)
                        print(" ")
                        map1()
                        henry2()
                        henry3()
                        henry4()
                    else:
                        print('Please type the given set of words')
                        continue
#____________________________________________________________________________________________________________________________
                else:
                    if a1=='3':
                        for i in range(1):
                            typingprint("--> The Pirate attacked but Henry Dodged !!")
                            print(' ')
                            print("-"*100)
                            print(" ")
                            a1=typinginput(powers)
                            print(" ")
                            print("-"*100)
                            print(" ")
                            if health>0:
                                if a1=='1':
                                        if magic>=25:
                                            e1hp1-=30
                                            typingprint(usetoxic)
                                            print(' ')
                                            print('>> The Pirate has', e1hp1, 'health left')
                                            magic-=25
                                            print('>> Henry has', health, 'health and', magic, 'magic left)')
                                            print(' ')
                                            print("-"*100)
                                            print(" ")
                                        else:
                                            print(">>", magic ,"magic left")
                                            typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                                            print(" ")
                                            print("*"*100)
                                            break
                                elif a1=='2':
                                    if magic>=10:
                                        rh=r.randint(1,10)
                                        print(usepointer, 3*rh, 'health')
                                        print(' ')
                                        health+=3*rh
                                        if health>=150:
                                            health=150
                                            print('>> Health is now', health)
                                            print(' ')
                                            print("-"*100)
                                            print(" ")
                                        else:
                                            print('>> Health is now', health)
                                            print(' ')
                                            magic-=10
                                            print('>> Henry has', health ,'health and', magic, 'magic left')           
                                            print(' ')
                                            print("-"*100)
                                            print(" ")
                                    else:
                                        print(">>", magic ,"magic left")
                                        typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                                        print(" ")
                                        print("*"*100)
                                        break
                                elif a1=='3':
                                    if magic>=15:
                                        typingprint(usesomn)
                                        print(" ")
                                        magic-=15
                                        print('>> Henry has', health, 'health and', magic, 'magic left')
                                        print(" ")
                                        print("-"*100)
                                        print(" ")
                                    else:
                                        print(">>", magic ,"magic left")
                                        typingprint("(Not enough magic, use SONG OF NATURE to replenish)")
                                        print(" ")
                                        print("*"*100)
                                        break
                                elif a1=='4':
                                    typingprint(useson)
                                    print(" ")
                                    magic+=15
                                    if magic>=60:
                                        magic=60
                                        print('>> Henry has', health, 'health and', magic, 'magic left')
                                        print(" ")
                                        print("-"*100)
                                        print(" ")
                                    else:
                                        print('>> Henry has', health, 'health and', magic, 'magic left')
                                        print(" ")
                                        print("-"*100)
                                        print(" ")                     
                                typingprint("--> The Pirate attacked but Henry Dodged !!")
                                print(' ')
                                print("-"*100)
                                print(" ")
                            else:
                                typingprint("|> GAME OVER (No Health Left)")

                    else:
                        pa=r.randint(10,25)
                        health-=pa
                        print('--> The Pirate attacked you and gave you', pa, 'damage')
                        print(' ')
                        print('>> Henry has', health, 'health left')
                        print(' ')
                        print("-"*100)
                        print(" ")
            else:
                typingprint("|> GAME OVER (No Health Left)")
                print(" ")
                print("*"*100)
                print(" ")
                break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
 
    
    elif n=='N' or n=='n':
            typingprint(farewell)
            print(" ")
            print("*"*100)
            print(" ")
            
    else:
        print("Wrong input , please restart ")
        print(" ")
        print("*"*100)
        print(" ")
   
            
henry1()
