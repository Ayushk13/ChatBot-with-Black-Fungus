from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import pyttsx3

data_list = ['Hello',
             'How can I help you',
             'What are the Symptoms of Black Fungus',
             'Shortness of breath',
             'What are the side effects of Black Fungus on our body',
             'Blood Vomiting,Pain & Redness on eyes and nose',
             'Who is more suspectial patient to this  Black Fungus diseases',
             'Patients with diabetes,cancer patients',
             'What are the nutritional food to recover from Black Fungus',
             'Eat protient Diet & Fruits',
             'Are these infections life threatening',
             'These illnesses are extremely dangerous & the death rate ranges from 25% to 90%',
             ]

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

trainer.train(data_list)

def botReply():
    question = questionField.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END, 'You: ' + question + '\n\n')
    textarea.insert(END, 'Bot: ' + str(answer) + '\n\n')
    pyttsx3.speak(answer)
    questionField.delete(0, END)


root = Tk()

root.geometry('500x570+100+30')
root.title('ChatBot with Black Fungus')
root.config(bg='black')

logoPic = PhotoImage(file='pic.png')

logoPicLabel = Label(root, image=logoPic, bg='black')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('verdana', 20, 'bold'), height=10, yscrollcommand=scrollbar.set
                , wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdana', 10, 'bold'))
questionField.pack(pady=15, fill=X)

askPic = PhotoImage(file='ask.png')

askButton = Button(root, image=askPic, command=botReply)
askButton.pack()

def click(event):
    askButton.invoke()

root.bind('<Return>', click)

root.mainloop()
