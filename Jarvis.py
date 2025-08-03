from tkinter import *
import pyttsx3
import speech_recognition as sr
from tkinter.messagebox import *
import random
import webbrowser
import datetime
import pyautogui
import wikipedia
import pywhatkit as pwk
from plyer import notification
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",200)
class Jarvis:
    def speak(self):
        while True:
            request=self.MyAudio().lower()
            if "hello" in request:
                engine.say("Hii ! How I Can Help You")
                engine.runAndWait()
                print(request)
            elif "play music" in request:
                engine.say("Playing Music...")
                engine.runAndWait()
                print(request)
                num=random.randint(1,5)
                if num==1:
                    webbrowser.open("https://www.youtube.com/watch?v=2WDbjU3eIKQ&list=RD2WDbjU3eIKQ&index=1&pp=8AUB")
                elif num==2:
                    webbrowser.open("https://www.youtube.com/watch?v=KsMXoG7WONI&list=RD2WDbjU3eIKQ&index=6&pp=8AUB")
                elif num==3:
                    webbrowser.open("https://www.youtube.com/watch?v=bK-nQ1Cicxc&list=RD2WDbjU3eIKQ&index=14&pp=8AUB")
                elif num==4:
                    webbrowser.open("https://www.youtube.com/watch?v=5KDpLJks_Ls&list=RD2WDbjU3eIKQ&index=15&pp=8AUB")
            elif "open youtube" in request:
                engine.say("Opening Youtube")
                engine.runAndWait()
                webbrowser.open("https://www.youtube.com/")
            elif "open whatsapp" in request:
                engine.say("Opening Whatsapp")
                engine.runAndWait()
                webbrowser.open("https://web.whatsapp.com/")
            elif "say time" in request:
                time=datetime.datetime.now().strftime("%H:%M")
                engine.say("Current Time Is :"+str(time))
                engine.runAndWait()
            elif "say date" in request:
                date=datetime.datetime.now().strftime("%d:%m")
                engine.say("Current Date Is :"+str(date))
                engine.runAndWait()
            elif "open google" in request:
                engine.say("Opening Google")
                engine.runAndWait()
                webbrowser.open("https://www.google.co.in/")
            elif "open chat" in request:
                engine.say("Opening Chat Gpt")
                engine.runAndWait()
                webbrowser.open("https://openai.com/chatgpt/overview/")
            elif "open wikipedia" in request:
                engine.say("Opening Wikipedia")
                engine.runAndWait()
                webbrowser.open("https://www.wikipedia.org/")
            elif "open facebook" in request:
                engine.say("Opening Facebook")
                engine.runAndWait()
                webbrowser.open("https://www.facebook.com/")
            elif "open" in request:
                query=request.replace("open","").lower()
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.sleep(2)
                pyautogui.press("enter")
            elif "search google" in request:
                request=request.replace("jarvis","")
                request=request.replace("search google","")
                webbrowser.open("https://www.google.co.in/search?q="+request)
            elif "wikipedia" in request:
                request=request.replace("jarvis","")
                request=request.replace("search wikipedia","")
                result=wikipedia.summary(request,sentences=2)
                engine.say(result)
                engine.runAndWait()
            elif "send whatsapp" in request:
                pwk.sendwhatmsg("+919507582209","Hello Boys",23,47,30)
            elif "new task" in request:
                task=request.replace("new task","")
                task=task.strip()
                print(task)
                if task!="":
                    engine.say("Adding Task :"+task)
                    with open("todo.txt","a") as file:
                        file.write(task+"\n")
            elif "all task" in request:
                with open("todo.txt","r") as file:
                    engine.say("Work We Have To Do Today Is :"+file.read())
                    engine.runAndWait()
            elif "work" in request:
                with open("todo.txt","r")as file:
                    tasks=file.read()
                notification.notify(
                    title="Today's Work",
                    message=tasks
                )
    def MyAudio(self):
        content=" "
        while content==" ":
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("\nSay Something")
                showinfo("Info","Click OK To Speak....")
                audio=r.listen(source)
            try:
                content=r.recognize_google(audio,language='en-in')
                print("\nYou Said.....")
                print("\nCommand = "+content)
            except Exception as e:
                print("Please Try Again...")
        return content
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x760+10+10")
        self.root.title("Jarvis Project")
        self.root.resizable(width=False,height=False)
        self.root.config(bg="sky blue")
        self.button=Button(self.root,text="Speak",font=("Calibri",30),command=self.speak)
        self.button.place(x=20,y=20,width=200,height=100)
 
if __name__=="__main__":
    root=Tk()
    obj=Jarvis(root)
    root.mainloop()
