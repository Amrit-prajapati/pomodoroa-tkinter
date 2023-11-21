from tkinter import *
import math
reps = 0
window = Tk()
window.title("Pomodoro")
window.minsize(height = 280 , width = 450)
window.maxsize(height = 280 , width = 450)
window.config(padx = 50)
done = ""
timer = None
#  Commands 
def start_timer():
    global reps
    global count
    reps +=1
    if reps%2 ==0:
        cnt = math.floor(reps/2)
        doneShow.config(text = cnt)
        txt.config(text = "Break")
        canvas.itemconfig(timerTxt, fill = "red")
        count_down(5*60)          
    else:
        txt.config(text = "Work")
        canvas.itemconfig(timerTxt, fill = "green")
        count_down(25*60)
def count_down(count):
    global timer
    countmin = math.floor(count/60)
    countsec = math.floor(count%60)
    if countmin < 10:
        countmin = f"0{countmin}"
    if countsec < 10:
        countsec = f"0{countsec}"
    canvas.itemconfig(timerTxt , text = f"{countmin} : {countsec}")
    if count > 0:
        timer = window.after(1000 , count_down , count-1)
    else:
        start_timer()
def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timerTxt , text = "00 : 00")
    window.after_cancel(timer)
    doneShow.config(text ="")
#  User Interface
canvas = Canvas(height = 150 , width = 300)
timerTxt = canvas.create_text(150 , 70 , text = "00:00", font = ('Arial' , 25 , "bold")  ,fill = "red")
canvas.grid(row = 1, column = 1)
txt = Label(text  ="Work" ,font = ('Arial' , 35 , "bold") , fg= "black")
txt.grid(row = 0 , column = 1)
Startbutton = Button(text = "Start", command = start_timer)
Startbutton.grid(row = 2 , column = 0)
ResetButton= Button(text = "Reset" , command = reset_timer)
ResetButton.grid(row = 2, column= 2)
doneShow = Label(text = "", fg= "green", font = ('Arial' , 25 , "bold"))
doneShow.config(padx = 50)
doneShow.grid(row = 2, column=1)
window.mainloop()