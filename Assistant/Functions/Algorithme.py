
def Light(Action):
    if Action == "On":
        print("Allumer la lumière")
    elif Action == "Off":
        print("Éteindre la lumière")    
        
def Vent(Action):
    if Action == "On":
        print("Augmenter la température")
    elif Action == "Off":
        print("Diminuer la température")    

def Porte(Action):
    if Action == "On":
        print("Ouvre la porte")
    elif Action == "Off":
        print("Ferme la porte")    


def Temp_State(Action):
    print(" La température est: 23")

def Decider(Action, Target):
    if Target in Targets:
        Targets[Target](Action)

Targets = {
    "Light": Light,
    "Vent": Vent,
    "Temp_State": Temp_State,
    "Porte": Porte
}

def GuideNextStep(Dialog):
    Polarity = ""
    Target = ""
    Action = "question"

    if "allumer" in Dialog.lower() or "ouvre" in Dialog.lower() or "allume" in Dialog.lower():
        Polarity = "On"
    elif "ferme" in Dialog.lower() or "fermer" in Dialog.lower() or "éteint" in Dialog.lower() or "éteindre" in Dialog.lower():
        Polarity = "Off"
    if "lumière" in Dialog.lower():
        Target = "Light"
        Action = "action"
    if "porte" in Dialog.lower():
        Target="Porte"
        Action="action"    
    if "vent" in Dialog.lower():
        Target = "Vent"
        Action = "action"
    if "température" in Dialog.lower() and "dis-moi" in Dialog.lower():
            Target = "Temp_State"

    return Action,Polarity,Target