from langchain.schema import HumanMessage
from langchain_groq import ChatGroq
import speech_recognition as sr
import streamlit as st
import os
from gtts import gTTS

def bot(text):

    llm = ChatGroq(
        temperature=0.9,
        groq_api_key='YOUR GroqAPI KEY',
        model_name='llama-3.3-70b-versatile'
    )
    prompt = "मजेदार और छोटे हिंदी जवाब दो, जैसे दोस्त मजाक में बात करते हैं।"
    response = llm([HumanMessage(content=f"{prompt} {text}")])
    llm_Response = response.content
    return llm_Response

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that")
        return None

def talk(llm_Response):
    tts = gTTS(text=llm_Response, lang="hi",slow=False)
    wav_file = "test.mp3"
    tts.save(wav_file)
    return wav_file

def conversation():
    user_input = listen()
    if user_input:
        print(f"You: {user_input}")
        bot_response = bot(user_input)
        print(f"Bot:{bot_response}")
        wav_file = talk(bot_response)
    return wav_file

st.title("Chatbot Conversation App")
st.write("Press 'Start' to begin the conversation.")
start_button = st.button('Start Conversation')
stop_button = st.button('Stop Conversation')


if start_button:
    st.write("Conversation started... You can talk now!")
    audio_file = conversation()
    st.audio(audio_file, format="audio/mp3")
    
if stop_button:
    st.write("Stopping the app...")
    os._exit(0)