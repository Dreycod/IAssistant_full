import Functions.Voice as Voice

mqtt_topicTemp = "IAssistant/Temperature"
mqtt_topicCO225 = "IAssistant/CO2/2.5"
mqtt_topicCO210 = "IAssistant/CO2/10"
mqtt_topicLumin = "IAssistant/Luminosité"
mqtt_Serrure = "IAssistant/State_Serrure"
mqtt_user = "IAssistant/User"
mqtt_ventilateur = "IAssistant/Ventilo"
def GuideNextStep(Dialog):
    Polarity = ""
    Target = ""
    Action = "question"

    if "allumer" in Dialog.lower() or "ouvre" in Dialog.lower() or "allume" in Dialog.lower():
        Polarity = "on"
    elif "ferme" in Dialog.lower() or "fermer" in Dialog.lower() or "éteint" in Dialog.lower() or "éteindre" in Dialog.lower() or "éteins" in Dialog.lower() :
        Polarity = "off"
    if "porte" in Dialog.lower():
        Target=mqtt_Serrure
        Action="action"    
    if "vent" in Dialog.lower():
        Target = mqtt_ventilateur
        Action = "action"
    if ("stop" in Dialog.lower() or "stoppe" in Dialog.lower()) and ( "spécial" in Dialog.lower() or "spéciale" in Dialog.lower()) :
            Action = "Stop"
    if "température" in Dialog.lower() and "dis-moi" in Dialog.lower():
            Target = "Temp_State"
    return Action,Polarity,Target
