# Emergency AI Assistant

## 📌 Overview

The **Emergency AI Assistant** is a voice-enabled AI system designed to provide immediate assistance during emergencies. It can detect whether the emergency is **medical, crime-related, or fire-related** and respond accordingly. Additionally, for medical emergencies, it fetches and provides the nearest hospital details using **Google Maps API**.

## 🚀 Features

- **Speech Recognition**: Listens to user input using `speech_recognition`.
- **AI-powered Responses**: Uses OpenAI's GPT model for emergency assistance.
- **Text-to-Speech**: Converts AI responses into speech using `pyttsx3`.
- **Location-based Hospital Search**: Finds the nearest hospital using Google Maps API.
- **Hands-free Interaction**: Operates through voice commands.

## 🛠️ Technologies & Libraries Used

- **Python**
- **OpenAI API (GPT-4-Turbo)** for AI responses
- **Google Maps API** for location services
- **SpeechRecognition** for voice input
- **Pyttsx3** for text-to-speech conversion
- **Requests** for API calls

## 📂 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/emergency-ai-assistant.git
cd emergency-ai-assistant
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add:

```ini
OPENAI_API_KEY=your_openai_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

### 5️⃣ Run the Program

```bash
python main.py
```

## 🎤 How It Works

1. The AI listens to user speech.
2. It identifies the type of emergency.
3. If it's a medical emergency, it fetches nearby hospitals.
4. The AI responds with appropriate guidance via voice.

## 📌 Example Usage

- **User**: "There’s a fire in my building!"
- **AI**: "This is a fire emergency. Please evacuate immediately and call the fire department."

- **User**: "Someone needs medical attention."
- **AI**: "This is a medical emergency. Fetching the nearest hospital details…" _(Provides hospital info)_

## 🤝 Contributing

Feel free to contribute! Open a pull request for improvements or bug fixes.
