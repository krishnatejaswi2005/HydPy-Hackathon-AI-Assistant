import openai
import speech_recognition as sr
import pyttsx3
import requests
import googlemaps
from dotenv import load_dotenv
import os
load_dotenv()


# API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# Initialize Text-to-Speech
def init_tts():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    return engine

tts_engine = init_tts()

# Function to Get User Location
def get_user_location():
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_MAPS_API_KEY}"
    response = requests.post(url)
    location = response.json().get("location")
    return location if location else None

# Function to Find Nearest Hospital
def find_nearest_hospital():
    location = get_user_location()
    if location:
        places_result = gmaps.places_nearby(
            location=(location['lat'], location['lng']),
            radius=5000,
            type='hospital'
        )
        if places_result.get('results'):
            hospital = places_result['results'][0]
            hospital_name = hospital['name']
            hospital_address = hospital['vicinity']
            
            distance_matrix = gmaps.distance_matrix(
                origins=(location['lat'], location['lng']),
                destinations=hospital_address,
                mode="driving"
            )
            if 'rows' in distance_matrix and distance_matrix['rows']:
                elements = distance_matrix['rows'][0]['elements']
                if elements and 'distance' in elements[0]:
                    distance_text = elements[0]['distance']['text']
                    return f"The nearest hospital is {hospital_name}, located at {hospital_address}. It is approximately {distance_text} away."
            
            return f"The nearest hospital is {hospital_name}, located at {hospital_address}."
    
    return "No nearby hospitals found."

# OpenAI API Call for Emergency Response
def get_emergency_response(user_text):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": (
                "You are an AI emergency assistant. If the user reports an emergency, provide immediate guidance. "
                "You are an AI emergency assistant. If the user reports an emergency, provide guidance. "
                "If the emergency is medical, crime-related, or fire-related, inform them accordingly. "
                "For medical emergencies, end the response with: 'Fetching the nearest hospital details...'"
                "For medical emergencies, include 'Fetching nearest hospital details...' at the end."
            )},
            {"role": "user", "content": user_text}
        ]
    )
    
    ai_response = response["choices"][0]["message"]["content"]

    # If ChatGPT determines it's a medical emergency, add hospital details
    if "Fetching nearest hospital details..." in ai_response:
        hospital_info = find_nearest_hospital()
        ai_response = ai_response.replace("Fetching nearest hospital details...", hospital_info)
    
    return ai_response

# Speech Recognition
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=7)
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand."
        except sr.RequestError:
            return "Speech recognition service unavailable."
        except Exception as e:
            return f"Error: {str(e)}"

# Text-to-Speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Main Program
def main():
    while True:
        user_input = recognize_speech()
        if user_input.lower() == "exit":
            speak("Exiting. Stay safe!")
            break

        emergency_response = get_emergency_response(user_input)
        print("AI Response:", emergency_response)
        speak(emergency_response)

if __name__ == "__main__":
    main()
