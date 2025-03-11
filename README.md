# Voice-Activated Chatbot

This project is a voice-activated chatbot that takes user input via speech, processes the input using a GPT-based model (Groq Llama), and then converts the model's output to speech using Google Text-to-Speech (gTTS). The user interface (UI) is developed using Streamlit for a seamless and interactive experience.

## Features
- Voice Input: The chatbot listens to voice commands using the speech_recognition library.
- AI Response: The chatbot uses the Groq Llama model to generate text-based responses to the user's queries.
- Voice Output: The chatbot responds with synthesized speech using Google Text-to-Speech (gTTS).
- Interactive UI: The Streamlit UI allows users to interact with the chatbot in a user-friendly manner.

## Technologies Used
- Python: The programming language used for the backend logic.
- SpeechRecognition: For recognizing speech and converting it into text.
- Groq Llama: GPT-based model used to generate responses.
- gTTS (Google Text-to-Speech): Converts the generated text into speech for output.
- Streamlit: A framework for creating interactive web applications and UIs.
## Installation
### Prerequisites
Ensure you have Python 3.x installed on your machine. You will also need to install the following Python libraries.

### Steps
1. Clone the repository:
```
git clone https://github.com/your-username/voice-activated-chatbot.git
cd voice-activated-chatbot
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Use the GroqAPI key to use Llama model.

4. Run the Streamlit UI:
```
streamlit run app.py
```
5. Follow the instructions on the Streamlit UI to interact with the chatbot.

### Usage
1. Open the application in your browser (Streamlit will provide a local server link).
2. Click on the start button to start recording your voice.
3. Speak your query.
4. The chatbot will process the query using Groq Llama and generate a response.
5. The response will be read out loud to you using Google Text-to-Speech.
### Example
1. User: "Aur sab kaesa hai mere bhai bot"
2. Chatbot (via Voice): "Sab badhiya hai bhai apna batao"
