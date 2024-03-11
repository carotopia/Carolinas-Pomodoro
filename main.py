from tkinter import *
import pygame


import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer= None

reps= 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text=" Carolina's Pomodoro!")
    checks.config(text="")
    global reps
    reps =0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():

    global reps
    reps +=1

    work_sec = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Long Break!", fg=RED)

    if reps%2 ==0:
        count_down(short_break)
        title.config(text="Break!", fg=RED)
    else:
        count_down(work_sec)
        title.config(text="WORK!", fg=RED)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("ring.mp3")
    pygame.mixer.music.play()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min= math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec= f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        play_sound()
        start()
        mark= ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+="✓"
        checks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(" Carolina's Pomodoro!")
window.config(padx= 120, pady=70, bg=PINK)
canvas = Canvas(width=520, height=520, bg=PINK, highlightthickness=0)
imagen_tomate = PhotoImage(file="tomate.png")
canvas.create_image(256,256, image= imagen_tomate)


timer_text= canvas.create_text(256,270,text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=2,row=1)


title = Label(window, text="Carolina's Pomodoro!", fg=YELLOW, font=(FONT_NAME, 55, "bold"), bg=PINK, highlightthickness=0)
title.grid(column=2, row=0)

checks = Label(window, text="", fg=GREEN, font=(FONT_NAME, 55, "bold"), bg=PINK, highlightthickness=0)
checks.grid(column=2, row=4)

start_button = Button(text="Start", width=8, height=2, highlightbackground=PINK, command=start)
start_button.grid(column=1,row=3)

reset_button= Button(text="Reset", width=8, height=2, highlightbackground=PINK, command=reset_timer)
reset_button.grid(column=3,row=3)


window.mainloop()