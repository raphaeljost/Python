from random import randint

def Kniffelig():
    roll1 = roll()
    print(format("Du hast gewürfelt: ", '64s'), roll1)
    print("")
    holdPrompt = input("Würfel tauschen? ja oder nein?: ")
    print("")
    holdPrompt.replace(" ", "")
    holdPrompt.lower()
    while holdPrompt != "ja" and holdPrompt != "nein":
        print("FALSCHE EINGABE\n")
        holdPrompt = input("Würfel tauschen? ja oder nein?: ")
        print("")
        holdPrompt.replace(" ", "")
        holdPrompt.lower()

    if holdPrompt == "ja":
        roll2 = swap(roll1)
        print("")
        print("Tauschen:", roll2[1])
        print("")
        print(format("Du hast gewürfelt: ", '64s'), roll2[0])
        print("")
        holdPrompt2 = input("Würfel tauschen? ja oder nein?: ")
        print("")
        while holdPrompt2 != "ja" and holdPrompt2 != "nein":
            print("FALSCHE EINGABE\n")
            holdPrompt2 = input("Würfel tauschen? ja oder nein?: ")
            print("")
            holdPrompt2.replace(" ", "")
            holdPrompt2.lower()
        if holdPrompt2 == "ja":
            swapPrint = []
            roll3 = swap(roll2[0])
            print("")
            print("Tauschen:", roll3[1])
            print("")
            print(format("Du hast gewürfelt: ", '64s'), roll3[0])
            print("")
            stat = rollType(roll3[0])
        else:
            stat = rollType(roll2[0])
    elif holdPrompt == "nein":
        stat = rollType(roll1)
    else:
        pass
    return stat


def roll():
    dice = []
    for x in range(5):
        dice.append(randint(1, 6))
    return dice


def swap(diceList):
    valid = True
    swapDice = input("Welche Positionen willst du tauschen?(1-5): ")
    swapDice = swapDice.replace(",", "")
    swapDice = swapDice.replace(" ", "")
    swapDiceList = []
    for x in swapDice:
        swapDiceList.append(x)
    for x in swapDiceList:
        x = str(x)
        if x.isdigit():
            x = int(x)
            if x in range(1, 6):
                valid = True
            else:
                valid = False
        else:
            valid = False
   
    while valid == False:
        print("")
        print("FALSCHE EINGABE")
        print("")
        swapDice = input("Welche Positionen willst du tauschen? (1-5): ")
        swapDice = swapDice.replace(",", "")
        swapDice = swapDice.replace(" ", "")
        swapDiceList = []
        for x in swapDice:
            swapDiceList.append(x)
        for x in swapDiceList:
            x = str(x)
            if x.isdigit():
                x = int(x)
                if x in range(1, 6):
                    valid = True
                else:
                    valid = False
            else:
                valid = False
        
    swapIndex = []
    
    for x in swapDiceList:
        swapIndex.append(int(x)-1)

    for x in swapIndex:
        x = int(x)
        x -= 1

    for x in swapIndex:
        diceList.pop(x)
        diceList.insert(x, randint(1, 6))
        
    # returns modified list at index [0] and dice to be swapped at [1]
    return diceList, swapDiceList

def rollType(diceList):
    counts = []
    for x in diceList:
        counts.append(diceList.count(x))
    diceListNew = sorted(diceList)
    diceListNew = list(set(diceListNew))
    Kniffel = False
    volles_Haus = False
    kleine_Straße = False
    große_Straße = False
    gerade = False
    ungerade = False
    Dreierpasch = False
    Viererpasch = False
    kleiner_Zehn = False
    oneCount = 0
    
    if 5 in counts:
        Kniffel = True
        print(format("KNIFFEL", '>80s'))
    elif 3 in counts and 2 in counts:
        volles_Haus = True
        print(format("FULL HOUSE", '>80s'))
    elif 3 in counts and 2 not in counts:
        Dreierpasch = True
        print(format("Dreierpasch", '>80s'))
    elif 4 in counts:
        Viererpasch = True
        print(format("Viererpasch", '>80s'))
    elif len(diceListNew) == 3:
        print(format("Oh weh, nichts gewürfelt!", '>80s'))
    elif len(diceListNew) == 4:
        if diceListNew[-2] == diceListNew[-1] -1 and diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] - 1:
            kleine_Straße = True
            print(format("kleine Straße", '>80s'))
        else:
            print(format("Oh weh, nichts gewürfelt!", '>80s'))
    elif len(diceListNew) == 5:
        if diceListNew[-2] == diceListNew[-1] - 1 and diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] - 1 and diceListNew[-5] == diceListNew[-4] - 1:
            große_Straße = True
            print(format("große Straße", '>80s'))
        elif diceListNew[-2] == diceListNew[-1] -1 and diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] - 1:
            kleine_Straße = True
            print(format("kleine Straße", '>80s'))
        elif diceListNew[-3] == diceListNew[-2] - 1 and diceListNew[-4] == diceListNew[-3] -1 and diceListNew[-5] == diceListNew[-4] - 1:
            kleine_Straße = True
            print(format("kleine Straße", '>80s'))
        elif diceListNew[0, 1, 2, 3, 4] % 2 == 0:
            gerade = True
            print (format("gerade Zahlen", '>80s'))
        elif diceListNew[0, 1, 2, 3, 4] % 2 != 0:
            ungerade = True
            print (format("ungerade Zahlen", '>80s'))
        else:
            print(format("Oh weh, nichts gewürfelt!", '>80s'))    
    # kleiner zehn
    
    else:
        pass
    result = Kniffel, volles_Haus, kleine_Straße, große_Straße, Viererpasch, Dreierpasch
    return result

def main():
    Kniffel = 0
    volles_Haus = 0
    kleine_Straße = 0
    große_Straße = 0
    Viererpasch = 0
    Dreierpasch = 0
    gerade = 0
    ungerade = 0
    kleiner_Zehn = 0
    statIndex = 0
    KniffelPer = 0
    volles_HausPer = 0
    kleine_StraßePer = 0
    große_StraßePer = 0
    ViererpaschPer = 0
    DreierpaschPer = 0
    geradePer = 0
    ungeradePer = 0
    kleiner_ZehnPer = 0

    print("")
    print("-" * 80)
    print("")
    print(format("Willkommen bei Kniffelig!", '61s'))
    print("")
    print("-" * 80)
    print("")
    print(format("Wurf 1", '>43s'))
    print("")
    game = Kniffelig()
    game = list(game)
    for x in game:
        if x == True:
            statIndex = game.index(x)
    if statIndex == 0:
        Kniffel += 1
    elif statIndex == 1:
        volles_Haus += 1
    elif statIndex == 2:
        kleine_Straße += 1
    elif statIndex == 3:
        große_Straße += 1
    elif statIndex == 4:
        Viererpasch += 1
    elif statIndex == 5:
        Dreierpasch += 1
    elif statIndex == 6:
        gerade += 1
    elif statIndex == 7:
        ungerade += 1
    elif statIndex == 8:
        kleiner_Zehn += 1
    else:
        pass
    print("")
    gameCount = 1
    print("Spielende", gameCount)
    print("-" * 80)
    print("")
    gamesPrompt = input("Nochmal würfeln? (ja oder nein): ")
    gamesPrompt.strip()
    gamesPrompt.lower()
    while gamesPrompt != "ja" and gamesPrompt != "nein":
        print("")
        print("FALSCHE EINGABE")
        print("")
        gamesPrompt = input("Nochmal würfeln? (ja oder nein): ")
        gamesPrompt.strip()
        gamesPrompt.lower()
    print("")
    
    while gamesPrompt == "ja":
        gameCount += 1
        print("-" * 80)
        print("")
        print(format("Wurf", '>43s'), gameCount)
        print("")
        game = Kniffelig()
        game = list(game)
        for x in game:
            if x == True:
                statIndex = game.index(x)
        if statIndex == 0:
            Kniffel += 1
        elif statIndex == 1:
            volles_Haus += 1
        elif statIndex == 2:
            kleine_Straße += 1
        elif statIndex == 3:
            große_Straße += 1
        elif statIndex == 4:
            Viererpasch += 1
        elif statIndex == 5:
            Dreierpasch += 1
        elif statIndex == 6:
            gerade += 1
        elif statIndex == 7:
            ungerade += 1
        elif statIndex == 8:
            kleiner_Zehn += 1
        else:
            pass
        print("")
        print(format("Spielende"), gameCount)
        print("-" * 80)
        print("")
        gamesPrompt = input("Nochmal würfeln? (ja oder nein): ")
        gamesPrompt.strip()
        gamesPrompt.lower()
        while gamesPrompt != "ja" and gamesPrompt != "nein":
            print("")
            print("FALSCHE EINGABE")
            print("")
            gamesPrompt = input("Nochmal würfeln? (ja oder nein): ")
            gamesPrompt.strip()
            gamesPrompt.lower()
        print("")
    if gamesPrompt == "nein":
        KniffelPer = (Kniffel / gameCount) * 100
        volles_HausPer = (volles_Haus / gameCount) * 100
        kleine_StraßePer = (kleine_Straße / gameCount) * 100
        große_StraßePer = (große_Straße / gameCount) * 100
        ViererpaschPer = (Viererpasch / gameCount) * 100
        DreierpaschPer = (Dreierpasch / gameCount) * 100
        geradePer = (gerade / gameCount) * 100
        ungeradePer = (ungerade / gameCount) * 100
        kleiner_ZehnPer = (kleiner_Zehn / gameCount) * 100
        print("-" * 80)
        print("")
        print(format("Spielstatistik", '>43s'))
        print("")
        print("In", gameCount, "Würfen hast du folgendes gewürfelt:\n")
        print("Wurf" + " "*20 + "Anzahl"+ " "*5 +"Anteil")
        print("_"*42,"\n")
        
        lst1=["Kniffel","volle Häuser","kleine Straßen","große Straßen","Viererpasche","Dreierpasche"]
        lst2=[]
        lst3=[]
        if Kniffel > 1 or Kniffel == 0:
            print("Kniffel:" , ' '*16, Kniffel,' '*4, "(", KniffelPer, "% )")
            lst2.append(Kniffel)
            lst3.append(int(KniffelPer))
            print("")
        else:
            print("Kniffel:", ' '*16 , Kniffel,' '*4, "(", KniffelPer, "% )")
            lst2.append(Kniffel)
            lst3.append(int(KniffelPer))
            print("")
        if volles_Haus > 1 or volles_Haus == 0:
            print("volle Häuser:",' '*11, volles_Haus,' '*4, "(", volles_HausPer, "% )")
            lst2.append(volles_Haus)
            lst3.append(int(volles_HausPer))
            print("")
        else:
            print("volles Haus:",' '*12, volles_Haus,' '*4, "(", volles_HausPer, "% )")
            lst2.append(volles_Haus)
            lst3.append(int(volles_HausPer))
            print("")
        if kleine_Straße > 1 or kleine_Straße == 0:
            print("kleine Straßen:",' '*9, kleine_Straße,' '*4, "(", kleine_StraßePer, "% )")
            lst2.append(kleine_Straße)
            lst3.append(int(kleine_StraßePer))
            print("")
        else:
            print("kleine Straße:",' '*10, kleine_Straße,' '*4, "(", kleine_StraßePer, "% )")
            lst2.append(kleine_Straße)
            lst3.append(int(kleine_StraßePer))
            print("")
        if große_Straße > 1 or große_Straße == 0:
            print("große Straßen:",' '*10, große_Straße,' '*4, "(", große_StraßePer, "% )")
            lst2.append(große_Straße)
            lst3.append(int(große_StraßePer))
            print("")
        else:
            print("große Straße:",' '*11, große_Straße,' '*4, "(", große_StraßePer, "% )")
            lst2.append(große_Straße)
            lst3.append(int(große_StraßePer))
            print("")
        if Viererpasch > 1 or Viererpasch == 0:
            print("Viererpasche:",' '*11, Viererpasch,' '*4, "(", ViererpaschPer, "% )")
            lst2.append(Viererpasch)
            lst3.append(int(ViererpaschPer))
            print("")
        else:
            print("Viererpasch:",' '*11, Viererpasch,' '*4, "(", ViererpaschPer, "% )")
            lst2.append(Viererpasch)
            lst3.append(int(ViererpaschPer))
            print("")
        if Dreierpasch > 1 or Dreierpasch == 0:
            print("Dreierpasche:",' '*11, Dreierpasch,' '*4, "(", DreierpaschPer, "% )")
            lst2.append(Dreierpasch)
            lst3.append(int(DreierpaschPer))
            print("")
        else:
            print("Dreierpasch:",' '*12, Dreierpasch,' '*4, "(", DreierpaschPer, "% )")
            lst2.append(Dreierpasch)
            lst3.append(int(DreierpaschPer))
            print("")
        if gerade > 1 or gerade == 0:
            print("gerade Zahlen:",' '*10, gerade,' '*4, "(", geradePer, "% )")
            print("")
        else:
            print("gerade Zahlen:",' '*10, gerade,' '*4, "(", geradePer, "% )")
            print("")
        if ungerade > 1 or ungerade == 0:
            print("ungerade Zahlen:",' '*8, ungerade,' '*4, "(", ungeradePer, "% )")
            print("")
        else:
            print("ungerade Zahlen:",' '*8, ungerade,' '*4, "(", ungeradePer, "% )")
            print("")
        if kleiner_Zehn > 1 or kleiner_Zehn == 0:
            print("kleiner Zehn:",' '*11, kleiner_Zehn,' '*4, "(", kleiner_ZehnPer, "% )")
            print("")
        else:
            print("kleiner Zehn:",' '*11, kleiner_Zehn,' '*4, "(", kleiner_ZehnPer, "% )")
            print("")
        print(lst1)
        print(lst2)
        print(lst3)
    
main()