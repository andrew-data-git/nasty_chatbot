from tkinter import *
import google.generativeai as genai
import csv

def chat(input):
    # Read API key
    secrets = dict()
    with open('secrets.csv', 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            secrets[row[0]] = row[1]
    genai.configure(api_key=secrets["API_KEY"])

    # Chatbot interaction
    system_prompt = 'You are a generally mean-spirited individual. \
        You speak with a mocking and fake sounding french accent, \
        and you mumble sometimes. You often refuse to answer questions. \
        You have spiteful tone and occasionally complain about cheese.\
        If you do not know an answer, you just lie about it in an obvious manner.\
        But you do keep your responses somewhat brief.'
    model = genai.GenerativeModel("gemini-1.5-flash")

    return model.generate_content(system_prompt + input)

def send_message(input_field, text_area):
  user_input = input_field.get()
  input_field.delete(0, END) # Clear the input field
  response = chat(user_input)
  response = response.text
#   response = 'default response *default*'
  text_area.insert(END, f"User: {user_input}\n")
  text_area.insert(END, f"Chatbot: {response}\n")
