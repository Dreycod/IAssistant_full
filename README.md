# Assistant IA MQTT

## 📌 Description
Ce projet est un assistant vocal intelligent utilisant **MQTT** pour communiquer avec des appareils domotiques. Il permet de contrôler des équipements comme une serrure et un ventilateur via la reconnaissance vocale et l'intelligence artificielle.

## 🚀 Fonctionnalités
- 🎙️ **Reconnaissance vocale** (détection du mot-clé "assistant")
- 🗣️ **Synthèse vocale** (réponse en audio)
- 🤖 **Interaction avec une IA** (réponses aux questions avec Ollama)
- 🌐 **Communication MQTT** (contrôle de périphériques connectés)
- 🏠 **Gestion des appareils domotiques** (serrure, ventilateur)

## 🏗️ Structure du projet
```
📂 AssistantIA
 ├── 📂 Functions
 │   ├── Algorithme.py    # Analyse des commandes vocales
 │   ├── IA.py            # Communication avec Ollama AI
 │   ├── Voice.py         # Gestion de la reconnaissance et synthèse vocale
 ├── Assistant.py         # Programme principal (boucle d'assistant)
 ├── requirements.txt     # Liste des dépendances
 ├── README.md            # Documentation du projet
```

## ⚙️ Installation et Utilisation

### 1️⃣ Pré-requis
- **Python 3.x**
- **Ollama** (installé et fonctionnel)
- **Un serveur MQTT** (ex: Mosquitto)

### 2️⃣ Installation des dépendances
```bash
pip install -r requirements.txt
```

### 3️⃣ Lancer l'assistant
```bash
python Assistant.py
```

## 🛠️ Technologies utilisées
- **Python**
- **SpeechRecognition** (Google Speech API)
- **Pyttsx3** (Synthèse vocale)
- **gTTS** (Google Text-to-Speech)
- **MQTT** (paho-mqtt)
- **Ollama AI** (modèle Mistral)

## 📌 Remarques
- Assurez-vous que le broker MQTT est configuré et en cours d'exécution.
- Vous pouvez personnaliser les commandes vocales dans `Algorithme.py`.

## 📧 Contact
Si vous avez des questions ou suggestions, n'hésitez pas à me contacter !
