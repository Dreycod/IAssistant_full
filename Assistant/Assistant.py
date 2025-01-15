import Functions.Voice as Voice
import Functions.IA as IA
import Functions.Algorithme as Algorithme
def main():
    """
    Main loop to handle the assistant's functionality.
    """
    while True:
        Voice.listen_for_keyword()  # Wait for "assistant"
        Voice.speak_text("Oui, dites-moi.")

        File = Voice.listen()  # Record user's question
        FirstDialog = Voice.transcribe_audio_to_text(File)  # Transcribe the question
        Decision,Polarity,Target = Algorithme.GuideNextStep(FirstDialog)
        print(FirstDialog)
        if Decision == "action":
            Algorithme.Decider(Polarity,Target)
        elif Decision == "question":
            print(f"Vous avez dit : {FirstDialog}")
            answer = IA.query_question(FirstDialog)
            Voice.speak_text(answer)
        else: 
            Voice.speak_text("Je n'ai pas compris. Veuillez réessayer.")

if __name__ == "__main__":
    main()
