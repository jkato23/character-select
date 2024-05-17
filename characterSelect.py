characterInfo = {
    "Yun": ("", "I Youhou", "II Sourai Rengeki", "III Genei Jin"),
    "Gouki": ("", "I Messatsu Gou Hadou", "II Messatsu Gou Shouryuu", "III Messatsu Gou Rasen"),
    "Remy": ("", "I Hunnu no Supernova", "II Vierge ni Ansoku O", "III Shoushin no Nocturne"),
    "Ryu": ("", "I Shinkuu Hadou Ken", "II Shin Shouryuu Ken", "III Denjin Hadou Ken"),
    "Urien": ("", "I Tyrant Punish", "II Jupiter Thunder", "III Aegis Reflector"),
    "Q": ("", "I Tosshin Oyobi Chishi Renzoku Dageki (Kari)", "II Fukubu Oyobi Koutoubu e no Tsuuda (Kari)", "III Bakuhatsu o Tomonau Dageki ya Hokaku (Kari)"),
    "Oro": ("", "I Kishin Riki", "II Yagyou Dama", "III Tengu Ishi"),
    "Necro": ("", "I Chou Denji Storm", "II Slam Dance", "III Electric Snake"),
    "Chun-Li": ("", "I Kikou Shou", "II Houyoku Sen", "III Tensei Ranka"),
    "Dudley": ("", "I Rocket Upper", "II Rolling Thunder", "III Corkscrew Blow"),
    "Ibuki": ("", "I Kasumi Suzaku", "II Yoroi Dooshi", "III Yami Shigure"),
    "Makoto": ("", "I Seichuusen Godan-zuki", "II Abare Tosanami Kudaki", "III Tanden Renki: Seme no Kata"),
    "Elena": ("", "I Spinning Beat", "II Brave Dance", "III Healing"),
    "Sean": ("", "I Hadou Burst", "II Shouryuu Cannon", "III Hyper Tornado"),
    "Twelve": ("", "I X.N.D.L", "II X.F.L.A.T", "III X.C.O.P.Y"),
    "Hugo": ("", "I Gigas Breaker", "II Megaton Press", "III Hammer Mountain"),
    "Alex": ("", "I Hyper Bomb", "II Boomerang Raid", "III Stun Gun Headbutt"),
    "Yang": ("", "I Raishin Mahha Ken", "II Tenshin Senkyuutai", "III Sei'ei Enbu"),
    "Ken": ("", "I Shouryuu Reppa", "II Shinryuu Ken", "III Shippuujinrai Kyaku"),
    "Gill": ("", "I Meteor Strike", "II Seraphic Wing", "III Ressurection")
}

def chooseCharacter(characterInfo):
    global charSelect
    print(" ".join(str(key) for key in characterInfo.keys()),"\n")  
    charSelect = input("Which character do you choose? ")
    charSelect = charSelect.capitalize()
    if (charSelect in characterInfo.keys()):
        if (charSelect == "Gill"):
            print("\n" "Gill is not a selectable character. Please choose another character." "\n")
            chooseCharacter(characterInfo)
        else:
            print("\n" "Your character is " + charSelect + "." "\n")
    else:
        print("\n" "That is not a valid character selection. Please choose again." "\n")
        chooseCharacter(characterInfo)

def chooseSuper(charSelect):
    for value in characterInfo[charSelect][1:4]:
        print(value)
    try:
        superSelect = int(input("\n" "Which super art do you choose? Enter a number between 1 and 3: "))
        if (superSelect > 3 or superSelect < 1):
            print("\n" "That is not a valid super art selection. Please choose again." "\n")
            chooseSuper(charSelect)
        else:
            print("\n" + "Your character is " + charSelect + " and your super art is " + (characterInfo[charSelect][superSelect] + "."))
            if (charSelect == "Gouki"):
                if (superSelect == 1):
                    print("You also have access to the super arts Tenma Gou Zankuu, Shun Goku Satsu, and Kongou Kokuretsu Zan.")
                elif (superSelect == 3):
                    print("You also have access to the super arts Messatsu Gou Senpuu, Shun Goku Satsu, and Kongou Kokuretsu Zan.")
            if (charSelect == "Oro"):
                if (superSelect == 1):
                    print("You also have access to the super arts Kishin Kuuchuu Jigoku Guruma and Kishin Tsui.")
                if (superSelect == 2):
                    print("You also have access to the super art Yagyou Oodama.")
                if (superSelect == 3):
                    print("You also have access to the super art Tengu Midare Ishi.")
    except ValueError:
        print("\n" "You entered something that was not a number. Please choose again." "\n")
        chooseSuper(charSelect)

chooseCharacter(characterInfo)
chooseSuper(charSelect)
