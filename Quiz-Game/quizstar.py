import tkinter
from tkinter import *
import random
#List Of Questions

questions = [
    "How many Keywords are there in C Programming language ?",
    "Which of the following functions takes A console Input in Python ?",
    "Which of the following is the capital of India ?",
    "Which of The Following is must to Execute a Python Code ?",
    "The Taj Mahal is located in  ?",
    "The append Method adds value to the list at the ?",
    "In which year '@' sign was first chosen for its use in e-mail address"
    "Which of the following is not a costal city of india ?",
    "Which of The following is executed in browser(client side) ?",
    "Which of the following keyword is used to create a function in Python ?",
    "To Declare a Global variable in python we use the keyword ?",
    "Who was the 1st President of India",
    "Which one of the followings is a programming language"
    
]

#Options For The Questions Respectively

answers_choice = [
    ["23","32","33","43",],
    ["get()","input()","gets()","scan()",],
    ["Mumbai","Delhi","Chennai","Lucknow",],
    ["TURBO C","Py Interpreter","Notepad","IDE",],
    ["Patna","Delhi","Benaras","Agra",],
    ["custom location","end","center","beginning",],
    ["1976","1980","1977","1972"],
    ["Bengluru","Kochin","Mumbai","vishakhapatnam",],
    ["perl","css","python","java",],
    ["function","void","fun","def",],
    ["all","var","let","global",],
    ["Jawaharlal Nehru","Rajendra Prasad","Indira Gandhi","Sarvepalli Radhakrishnan"],
    ["HTTP","HTML","HPML","FTP"]
]

#(Correct Answer-1) Respectively
answers = [1,1,1,1,3,1,3,0,1,3,3,1,2] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#031222",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Inter",46,"bold"),
        background = "#031222",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Are Excellent !!")
        labelresulttext.config(background="#031222")
        labelresulttext.config(foreground="#2ED573")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better !!")
        labelresulttext.config(background="#031222")
        labelresulttext.config(foreground="#E2E531")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Should Work Hard !!")
        labelresulttext.config(background="#031222")
        labelresulttext.config(foreground="#EE7F89")

#Function Calculator To Calculate Score
def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("poppins", 44, "bold"),
        justify = "center",
        width = 500,
        wraplength = 1440,
        background = "#031222",
        foreground = "#ffffff"
    )
    lblQuestion.pack(pady=(250,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("inter", 20),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#031222",
        foreground = "#ffffff",
        activebackground = "#E2E531",
    )
    r1.pack(pady=20)
    r1.place(x = 420, y = 450)
    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("inter", 20),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#031222",
        foreground = "#ffffff",
        activebackground = "#E2E531",
    )
    r2.pack(pady=20)
    r2.place(x = 420, y = 530)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("inter", 20),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#031222",
        foreground = "#ffffff",
        activebackground = "#E2E531",
    )
    r3.pack(pady=20)
    r3.place(x = 420, y = 610)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("inter", 20),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#031222",
        foreground = "#ffffff",
        activebackground = "#E2E531",
    )
    r4.pack(pady=20)
    r4.place(x = 420, y = 690)


def startIspressed():
    
    
    btnStart.destroy()
    label1.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Test of knowledge")
root.geometry("1920x1080")
root.config(background="#031222")
root.resizable(0,0) 
bg = PhotoImage(file = "tok.png" )

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)



img2 = PhotoImage(file="Button.png")

btnStart = Button(
    root,
    image = img2,
    relief ="sunken",
    borderwidth = 0,
    background = "#031222",
    activebackground = "#031222",
    command = startIspressed, 
)
btnStart.pack(pady=(600,0))
btnStart.place(x = 90, y = 590)

root.mainloop()
