import random
import time
import logging

logging.basicConfig(
    filename = "output.txt",
    filemode = "w",  
    level = logging.INFO,
    format = "%(message)s",
    encoding = "utf-8",
)

def doppelt_print (mess: str):
    print(mess)  
    logging.info(mess)
u = [1,-1]
spieler_hp = 100
hunger = 100
ziel = [random.randint(8, 9) * 10 * random.choice(u), random.randint(5, 10) * 10 * random.choice(u)]
invetar  = ["Proviant"]
schaden = 30
punkte = 0
x = 0
gold = 40
y = 0
angst_punkte = 0
doppelt_print("Du stehst in einer endlosen Leere. Um dich gibt es keine Baume, keine Menschen... ")
time.sleep(3)
doppelt_print("Nur das beängstigendes Nichts...")
doppelt_print("Dann siehst du plötzlich eine schwebennde Lichtkugel")
name = input("Wie heißt du?, fragt die Lichtkugel.  ")
doppelt_print(f"Hallo, {name}. Du bist bestimmt ein bischen überrascht, aber ich freue mich das jemand außer mir auf diesem Ort ist. ")
doppelt_print("Du bist in einem Albtraum. Du musst wach werden. Dafür musst du den Ausgang finden. Dabei werde ich dir helfen, aber ich kenne deinen Traum ja nicht. Und noch etwas, probiere nicht so viele Angst_punkte zu haben, denn wenn du viele davon hast zerreist dich die Angst in Stüke.")
doppelt_print("Diese Welt ist aber klein [-100, 100] und deswegen probiere es nicht mehr als 100/-100 raus zu gehen. ")
def item_hinzufugen(invetar, item):
    doppelt_print(invetar)
    invetar.append(item)

def item_entfernen(invetar, item):
    doppelt_print(invetar)
    if item in invetar:
        invetar.remove(item)

def schatztruhe(spieler_hp, gold, invetar, angst_punkte):
    wahl = input ("Du findest einen schwarz gekleideten Zauberer. Versuchst du dein Glück? (Ja/Nein?) ")
    if wahl == "Ja" or wahl =="ja":
        inhalte = ["gold", "schwert", "falle", "heilzauber", "heilzauber", "Mut", "Dieb", "falle"]
        inhalt = random.choice(inhalte)
        if inhalt =="gold":
            doppelt_print("Du findest einen Schatz!!!")
            gold += random.randint(5, 25)
        elif inhalt == "schwert":
            doppelt_print("Du fidest ein Schwert!")
            item_hinzufugen(invetar,"schwert")
        elif inhalt == "falle":
            doppelt_print("Es war eine Falle!")
            spieler_hp -= random.randint(2, 20)
            angst_punkte += 1
        elif inhalt == "heilzauber":
            doppelt_print("Der Zauberer hat dich geheilt!!!")
            if spieler_hp <= 100:
                spieler_hp += 40
                if spieler_hp > 100:
                    spieler_hp = 100
        elif inhalt == "Mut":
            doppelt_print("Du füllst plötzlich Hoffnung. Du bekommst wieder Mut.")
            angst_punkte -= 2
            if angst_punkte < 0:
                angst_punkte = 0
        elif inhalt == "Dieb":
            geklaut = random.randint(5,10)
            gold -= geklaut
            if gold <= 0:
                geklaut = gold

            doppelt_print(f"Es war ein Schummler!!! Er hat {geklaut} Gold geklaut!!!!")
            
            if gold <= 0:
                gold = 0


    else:
        pass
    return spieler_hp , gold, invetar, angst_punkte
        
def handler(gold, invetar):
    doppelt_print("Du triffst einen Händler.")
    print(f"Dein Gold: {gold}")
    print("1. Heiltrank kaufen - 10 Gold")
    print("2. Proviant kaufen - 15 Gold")
    print("3. Trank des Mutes - 20 Gold")
    print("4. Nichts kaufen")
    antwort = int(input("1 oder 2 oder 3 ??? "))
    if antwort == 1 and gold >= 10:
        item_hinzufugen(invetar, "Heiltrank")
        gold -= 10
    elif antwort == 2 and gold >= 15:
        item_hinzufugen(invetar, "Proviant")
        gold -= 15
    elif antwort == 3 and gold >= 20:
        item_hinzufugen(invetar, "Trank des Mutes")

        gold -= 20
    else:
        pass
    return (gold, invetar)

def heiltrank(spieler_hp, invetar):

    if "Heiltrank" in invetar:
        invetar.remove("Heiltrank")
        spieler_hp += 50
    if spieler_hp > 100:
        spieler_hp -= spieler_hp - 100
    return(spieler_hp, invetar)

def proviant():
    global invetar
    global hunger
    if "Proviant" in invetar:
        invetar.remove("Proviant")
        hunger += 50
    if hunger > 100:
        hunger -= hunger - 100

def Mut():
    global invetar
    global angst_punkte
    if "Trank des Mutes" in invetar:
        invetar.remove("Trank des Mutes")
        angst_punkte -= 2
    if angst_punkte < 0:
        angst_punkte = 0
    return(invetar, angst_punkte)

def generiere_monster():
    monster_liste = [
        ["Der Zombie", 70, 100, 5], #Name, Minimum HP, Maximum Hp, Angriffsstärke
        ["Der  Wolf", 20, 30, 32],
        ["Der Geist", 50, 65, 15],
        ["Der Schatten", 60, 90 , 10],
        ["DIE ANGST", 50, 70, 17]
    ]
    
    pass
    monster = random.choice(monster_liste)# monster ist eine liste
    name = monster[0]
    hp_min = monster[1]
    hp_max = monster[2]
    starke = monster[3]
    monster_hp = random.randint(hp_min, hp_max)
    return name, monster_hp, starke

#Monsterkampf-Funktion
def monster_kampf(invetar, punkte, gold, schaden, angst_punkte, monster_name, monster_hp, monster_starke):
    doppelt_print(f"{monster_name} hat dich bemerkt.")
    logging.info(f"{monster_name} greift an.")
    global spieler_hp
    print(f"Deine HP: {spieler_hp} | {monster_name} HP: {monster_hp}")
    if "schwert" in invetar:
        aktion2 = input("Willst du ein Schwert benutzen? (Ja/Nein) ")
        if aktion2 =="Ja" or aktion2 == "ja":
            if "schwert" in invetar:
                item_entfernen(invetar,"schwert")
                schaden += 10
    
    while spieler_hp > 0 and monster_hp > 0:
        print(schaden)
        print(f"Deine HP: {spieler_hp} | {monster_name} HP: {monster_hp}")
        aktion = input("Angreifen oder Heilen(1/2) ")
        if aktion == "angreifen" or aktion == "Angreifen" or aktion == "1":

            angriff = random.randint(0, schaden)
            monster_hp -= angriff
            if angriff <= 0:
                print("Du hast verfehlt.")
            else:
                print(f"Du hast {angriff} Schaden gemacht.")
        elif aktion == "heilen" or aktion == "Heilen" or aktion == "2":
            spieler_hp, invetar = heiltrank(spieler_hp, invetar)
              
        #Warten eine Sekunde
        time.sleep(2)

        schaden2 = random.randint(0, monster_starke)
        spieler_hp -= schaden2
        print(f"{monster_name} greift an. Du hast {schaden2} HP verloren.")
        
        pass
    if spieler_hp > 0:
        gewinne = ["Gold", "Leben"]
        gewinn = random.choice(gewinne)
        if gewinn == "Gold":
            gold += random.randint(20, 40)
        elif gewinn == "Leben":
            spieler_hp += 30
        print(f"{monster_name} wurde besiegt und gab dir etwas {gewinn}!")
        if schaden == 40:
            doppelt_print("Leider geht dein Schwert kaputt.")
            schaden -= 10
            item_entfernen(invetar,"schwert")
        
        punkte += 1
        
        angst_punkte += 1
    else:
        spieler_hp = 0

    return spieler_hp, gold, punkte, invetar, schaden, angst_punkte
#============
#Spielstart
#============
def goblins(invetar):
    if invetar == []:
        doppelt_print("Die Goblins konnten nichts klauen.")
    else:
        doppelt_print("Oh nein, die Goblins klauen dir was!")
        invetar.remove(random.choice(invetar))
    return invetar

def Eine_kalte_Umarmung(angst_punkte):
    doppelt_print("Du spürst, wie die Angst nach dir greift. Du siehst schrecklige Dinge. Du hast Angst.")
    angst_punkte += 1
    return angst_punkte

def zufalls_event(invetar, spieler_hp, gold, punkte, schaden, angst_punkte):
    zufallsevents = ["kampf","schatz","handler","goblins","angst"]
    event = random.choice(zufallsevents) # Wähle zufallige elemente
    if event == "kampf":
        #Monsterkampf
        monster_name, monster_hp, monster_starke = generiere_monster()
        spieler_hp, gold, punkte, invetar, schaden, angst_punkte = monster_kampf(invetar, punkte, gold, schaden, angst_punkte, monster_name, monster_hp, monster_starke)
    elif event == "schatz":
        spieler_hp, gold, invetar, angst_punkte = schatztruhe(spieler_hp, gold, invetar, angst_punkte)
    elif event == "handler":
        gold,invetar = handler(gold, invetar)
    elif event == "goblins":
        invetar = goblins(invetar)
    elif event == "angst":
        angst_punkte = Eine_kalte_Umarmung(angst_punkte)
        
    return spieler_hp, gold, punkte, invetar, schaden, angst_punkte
def restart(x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte,spiel):
        entscheidung = input("Willst du den Bericht von deinem Abendteuer sehen? (Ja/Nein) ")
        if entscheidung == "Ja" or entscheidung == "ja":
            print("\n\n")
            with open("output.txt", "r", encoding = "utf-8") as file:
                for line in file:
                    
                    print(line.strip())
        else:
            pass
        weiter_spielen = input("Willst du weiter speilen? (Ja/Nein) ")
        if weiter_spielen == "Ja" or weiter_spielen == "ja":
            punkte = 0
            x = 0
            y = 0
            spieler_hp = 100
            hunger = 100
            angst_punkte = 0
            invetar = ["Proviant"]
            gold = 40
            with open("output.txt", "r+", encoding="utf-8") as file:
                file.truncate(0) 
        elif weiter_spielen == "Nein" or weiter_spielen == "nein":
            print("Bis dann...")
            spiel = False
        return(x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel)

spiel =True
#Haupt - Schleife
while spiel:
    while spieler_hp >= 0:
        doppelt_print(f"HP: {spieler_hp} | Gold: {gold} | Besiegte Monster: {punkte} | Standort: ({x},{y}) | Ziel: {ziel} | Hunger:{hunger} | Angst_punkte: {angst_punkte}")
        doppelt_print(f"Deine Sachen: {invetar}")
        if "Proviant" in invetar:
            wahl2 = input("Willst du was essen?(Ja/Nein) ")
            if wahl2  == "ja" or wahl2 == "Ja":
                proviant()
        else:
            pass
        if "Trank des Mutes" in invetar:
            wahl3 = input("Willst ein Trank des Mutes trinken? (Ja/Nein) ")
            if wahl3 == "ja" or wahl3 == "Ja":
                Mut()
        if x >100 :
            print("Die Welt endet hier")
            x-=10
            continue
        if x <-100 :
            print("Die Welt endet hier")
            x+=10
            continue
        if y >100 :
            print("Die Welt endet hier")
            y-=10
            continue
        if y <-100 :
            print("Die Welt endet hier")
            x+=10
            continue

        wahl1 = input("Gehst du nach links(l), rechts(r), geradeaus(g) oder hinter(h)? ")
        if wahl1 == "links" or wahl1 == "l":
            x-=10
            #Monsterkampf
            spieler_hp, gold, punkte, invetar, schaden, angst_punkte = zufalls_event(invetar, spieler_hp, gold, punkte, schaden, angst_punkte)
        elif wahl1 == "rechts" or wahl1 == "r":
            x+=10
            #Monsterkampf
            spieler_hp, gold, punkte, invetar, schaden, angst_punkte = zufalls_event(invetar, spieler_hp, gold, punkte,schaden, angst_punkte)
        elif wahl1 == "geradeaus" or wahl1 == "g":
            y+=10
            spieler_hp, gold, punkte, invetar, schaden, angst_punkte = zufalls_event(invetar, spieler_hp, gold, punkte, schaden, angst_punkte)
        elif wahl1 == "hinter" or wahl1 == "h": 
            y-=10
            spieler_hp, gold, punkte, invetar, schaden, angst_punkte = zufalls_event(invetar, spieler_hp, gold, punkte, schaden, angst_punkte)
        else:
            doppelt_print("Du bleibst stehen und nichts passiert. ")
        hunger -= 10
        if hunger < 0:
            hunger  += 10
        if hunger == 0:
            spieler_hp -= 20

        if x == ziel[0] and y == ziel[1]:
            doppelt_print("Lichtkugel: Oh nein, da wartet der Schattenkönig am Ausgang. Du musst ihn mit Mut besiegen.")
            monster_kampf(invetar, punkte, gold, schaden, angst_punkte,"Der Schattenkönig", spieler_hp, 27)
            if spieler_hp > 0:
                punkte += 1
            break
        
        if angst_punkte == 7:
            break

        if spieler_hp <= 0:
            break
        pass
    doppelt_print(f"HP: {spieler_hp} | Gold: {gold} | Besiegte Monster: {punkte} | Standort: ({x},{y}) | Ziel: {ziel} | Hunger:{hunger} | Angst_punkte: {angst_punkte}")
    doppelt_print(f"Deine Sachen: {invetar}")
    if spieler_hp <= 0:
        doppelt_print("Lichtkugel: Du kannst nicht in einem Traum sterben. Du wirst einfach wieder for deinem Computer aufwachen und dich Fragen was hier los ist. Aber keine Sorge, dies heißt nicht 'Leb wohl', sondern 'Wir sehen uns wieder'. Denn wir Albträume sind unsterblich und wir alle sind nur für einen Zweck da... ")
        time.sleep(10)
        print("Wir sind da um euch dran zu erinnern wovor ihr Angst habt, aber auch um die Angst zu überwiden. Bis dann...")
        time.sleep(1)
        
        x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel = restart(x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel)

    elif x == ziel[0] and y == ziel[1]:
        print(spieler_hp)
        doppelt_print(f"Leuchtkugel: Sehr gut gemacht. Du hast deine Angst besiegt! Aber jetzt müssen wir Abschied nehmen. Wir sehen uns wieder...")
        
        x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel = restart(x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel)


    if angst_punkte == 7:
        doppelt_print("Jetzt bist du einer von uns!!! Du bestehst nur aus Angst. Und du wirst waren bis man dich besiegt. Und jetzt lasse ich dich mit deiner Angst allein. Viel Spaß...")
       
        x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel = restart(x, y, spieler_hp, hunger, angst_punkte, invetar, gold, punkte, spiel)









