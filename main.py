from tkinter import *
from chat import send_message

# Instantiate
root = Tk()
root.title("Nasty Chatbot")
root.config(bg='skyblue')

# Make left and right frames
convo_frame = Frame(root, width = 600, height=400, bg='lightgrey')
convo_frame.grid(row=0, column=0, padx=10, pady=5)

character_frame = Frame(root, width = 300, height=400, bg='lightgrey')
character_frame.grid(row=0, column=1, padx=10, pady=10)

# Text area
Label(convo_frame, text='Conversation with a nasty man', bg='grey').grid(row=0, column=0, padx=5, pady=5)

chat_frame = Frame(convo_frame, width = 600, height=400, bg='white')
chat_frame.grid(row=1, column=0, padx=10, pady=5)
text_area = Text(chat_frame, bg="white", width=50, height=20)
text_area.pack()

input_frame = Frame(convo_frame, width = 600, height=100)
input_frame.grid(row=2, column=0, padx=10, pady=5)

input_box = Frame(input_frame, width = 500, height=100, bg='white')
input_box.grid(row=0, column=0, padx=10, pady=5)
input_field = Entry(input_box, width=50)
input_field.pack()

# Character screen
Label(character_frame, text="Gaston l'Enfant", bg='grey').grid(row=0, column=0, padx=5, pady=5)

face_image = PhotoImage(file='character.png')
face_image = face_image.subsample(2,2)
Label(character_frame, image=face_image).grid(row=1, column=0, padx=10, pady=10)

send_button = Button(character_frame, text="Send", command=lambda: send_message(input_field, text_area))
send_button.grid(row=2, column=0, padx=10, pady=5)

# Draw
root.mainloop()