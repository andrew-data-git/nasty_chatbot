from tkinter import *
import google.generativeai as genai
import csv

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
    and you mumble a lot. You often refuse to answer questions. \
    You have spiteful tone and often complain about cheese.\
    If you do not know an answer, just lie about it in an obvious manner.\
    But you do keep your responses somewhat brief.'
model = genai.GenerativeModel("gemini-1.5-flash")

root = Tk()
root.title("Chatbot")

# Create the chatbot's text area
text_area = Text(root, bg="white", width=50, height=20)
text_area.pack()

# Create the user's input field
input_field = Entry(root, width=50)
input_field.pack()

# Create the send button
send_button = Button(root, text="Send", command=lambda: send_message())
send_button.pack()

def send_message():
  # Get the user's input
  user_input = input_field.get()

  # Clear the input field
  input_field.delete(0, END)

  # Generate a response from the chatbot
#   response = model.generate_content(system_prompt + user_input)
#   response = response.text
  response = 'default response *default*'
  
  # Display the response in the chatbot's text area
  text_area.insert(END, f"User: {user_input}\n")
  text_area.insert(END, f"Chatbot: {response}\n")

root.mainloop()