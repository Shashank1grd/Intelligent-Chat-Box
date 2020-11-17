from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

# 1
bot1 = ChatBot('MY BOT')

convo=[
    "Hi there!",
    "What is your name?",
    "My name is Bot. I am created by Ankit.",
    "How are you?",
    "I am fine. How are you doing?",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "Where do you live in?",
    "I live in India.",
    "What is your nationality?",
    "I am Indian.",
    "In which language you talk?",
    "I mostly talk in English."
]

trainer=ListTrainer(bot1)

trainer.train(convo)

#print("Talk to Bot")

#while True:
#    query=input()
 #   if query=='exit':
  #      break
   # answer=bot1.get_response(query)
   # print("Bot:",answer)

# 2
main = Tk()

main.geometry("500x650")
main.title("My ChatBot")

img = PhotoImage(file = "robo2.png")

img = img.zoom(2)
img = img.subsample(10)

photoL = Label(main, image = img)
photoL.pack(pady = 5)

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Your bot is listening, try to speak.")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()

        except Exception as e:
            print(e)
            print("not recognized")


# 3
def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot1.get_response(query)
    msgs.insert(END, "You: "+ query)
    msgs.insert(END, "Bot: "+ str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)

sc = Scrollbar(frame)
#listbox = Listbox(frame, yscrollcommand=sc.set)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn=Button(main, text="Ask from bot", font=("Verdana, 20"), command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>', enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target = repeatL)

t.start()

main.mainloop()