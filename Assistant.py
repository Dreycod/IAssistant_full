import asyncio
import paho.mqtt.client as mqtt
import Functions.Voice as Voice
import Functions.IA as IA
import Functions.Algorithme as Algorithme
import time 
# MQTT Configuration
mqtt_broker = "192.168.0.105"
mqtt_port = 1883
mqtt_user = "IAssistant/User"
mqtt_topicTemp = "IAssistant/Temperature"
mqtt_topicCO225 = "IAssistant/CO2/2.5"
mqtt_topicCO210 = "IAssistant/CO2/10"
mqtt_topicLumin = "IAssistant/Luminosité"
mqtt_Serrure = "IAssistant/State_Serrure"
mqtt_ventilateur = "IAssitant/Ventilo"

# Callback function for received messages
class MyMQTTClient(mqtt.Client):
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        
    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        if msg.topic == mqtt_user:
            Voice.speak_text("Bienvenu, " + payload)
        elif msg.topic == mqtt_Serrure:
            if payload == "on":
                Voice.speak_text("Porte ouverte, Bienvenu")
                time.sleep(3)
                publish_mqtt(mqtt_Serrure,"off")
            elif payload == "off":
                Voice.speak_text("Porte fermé")
        elif msg.topic == mqtt_ventilateur:
            if payload == "on":
                Voice.speak_text("Ventilateur allumé")
            elif payload == "off":
                Voice.speak_text("Ventilateur éteint")


# Configuration of the MQTT client
mqtt_client = MyMQTTClient()
mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.subscribe(mqtt_user)
mqtt_client.subscribe(mqtt_ventilateur)
mqtt_client.subscribe(mqtt_Serrure)


async def mqtt_loop():
    # Run the MQTT loop in the background
    mqtt_client.loop_start()
    while True:
        await asyncio.sleep(1)  # Allow asyncio to run other tasks concurrently


def publish_mqtt(topic, info):
    mqtt_client.publish(topic, info)


async def assistant_loop():
    """
    Main loop to handle the assistant's functionality.
    """
    while True:
        Voice.listen_for_keyword()  # Wait for "assistant"
        Voice.speak_text("Oui, dites-moi.")

        File = Voice.listen()  # Record user's question
        FirstDialog = Voice.transcribe_audio_to_text(File)  # Transcribe the question
        Decision, Polarity, Target = Algorithme.GuideNextStep(FirstDialog)
        print(FirstDialog)
        if Decision == "Stop":
            Voice.speak_text("Au revoir mon cher")
            break
        if Decision == "action":
            publish_mqtt(Target, Polarity)
        elif Decision == "question" and FirstDialog != "Null":
            print(f"Vous avez dit : {FirstDialog}")
            answer = IA.query_question(FirstDialog)
            Voice.speak_text(answer)
        elif Decision == "None":
            print("commande spéciale")
        else:
            Voice.speak_text("Je n'ai pas compris. Veuillez réessayer.")


async def main():
    # Run both MQTT loop and assistant loop concurrently
    await asyncio.gather(
        mqtt_loop(),
        assistant_loop()
    )


if __name__ == "__main__":
    # Run the asyncio event loop
    asyncio.run(main())
