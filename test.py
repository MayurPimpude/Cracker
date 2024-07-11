import streamlit as st
import speech_recognition as sr
import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate, LLMChain

# Load environment variables
load_dotenv()

# Configure Google generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to recognize speech from microphone
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Speak something...")
        audio_data = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Sorry, could not understand audio."
        except sr.RequestError as e:
            return "Error: Could not request results from Google Speech Recognition service;"

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.0-pro", temperature=0.5)

# Define the input prompt template
input_prompt = """
You are an interview helper that helps candidates with answering interviewers' questions in a crisp and short form that helps the interviewee clear the interview.
Here is the question: {question}
"""

prompt = PromptTemplate(template=input_prompt, input_variables=["question"])

# Create an LLM chain
chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit application title
st.title("Cracker")

# Button to record audio
if st.button("Press to Record"):
    # Recognize speech from microphone
    result = recognize_speech_from_mic()
    # result = "what is sql"
    # Display recognized text
    st.write(f"You said: {result}")
    
    # Generate response from LLM
    if result and not result.startswith("Sorry") and not result.startswith("Error"):
        response = chain({"question": result})
        st.write(response['text'])
    else:
        st.write(result)
