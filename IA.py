
import json
import re 
import requests
import Functions.Voice as Voice
OLLAMA_API_URL = "http://localhost:11434/api/chat"  # Default API endpoint for Ollama

def query_question(prompt):
    """
    Send a prompt to the Ollama API and return the model's response.
    """
    payload = {
    "model": "mistral:latest",  # Replace with the model name you're using
    "messages": [{"role": "user", "content": 
                 "Réponds brièvement (max 10 mots) en français à cette question du client : " + prompt}             
                ]
    }
    
    response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
    # Check the response status
    if response.status_code == 200:
        full_response = ""  # String to accumulate the full response
        for line in response.iter_lines(decode_unicode=True):
            if line:  # Ignore empty lines
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        full_response += json_data["message"]["content"]
                except json.JSONDecodeError:
                    pass  # Skip any lines that cannot be parsed
        return full_response  # Return the entire response after processing all lines
    else:
        print(f"Error: {response.status_code}")
        print(response.text)