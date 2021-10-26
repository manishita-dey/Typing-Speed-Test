import tkinter
import random
from tkinter import END, messagebox


MAX_TIME = 60

timer = None


def reset_timer():
    text.delete('1.0', END)
    window.after_cancel(timer)         #stops the timer
    canvas.itemconfig(timer_text, text="00")
    text.config(state='disabled')


def start_timer():
        text.config(state='normal')
        countdown(MAX_TIME)


def countdown(count):
    global timer
    count_sec = count


#Dynamic Typing
    if count_sec ==0:
        count_sec = "00"
    elif count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_sec}")
    if count>0:
        timer = window.after(1000, countdown, count-1)
    else:
        text.config(state = 'disabled')
        messagebox.showinfo('Your Typing Speed', f'Your typing speed is approximately {word_per_min()}wpm')


def word_per_min():
    word_string = text.get('1.0', END)
    word_list = word_string.split(' ')
    random_word_list = random_content.split(' ')
    no_of_words = len(word_list)

    final_list = random_word_list[:no_of_words]

    # checking how many words are typed correct:
    correct_count = 0
    for i in range(no_of_words):
        if word_list[i] == final_list[i]:
            correct_count+=1

    word_per_min = correct_count
    return word_per_min


window = tkinter.Tk()
window.title("Typing Speed Test")

window.config(padx=50, pady=50, bg = '#856ff8')
# Allow Window to be resizable
window.resizable(width = True, height = True)

#Heading Label
head_label = tkinter.Label(text = 'Typing Speed Test', font = ("Arial",24, 'bold'), padx = 50, pady = 50, bg = '#856ff8')
head_label.grid(row = 0,rowspan = 2, column = 1)

#Typing text label
with open('sampletext.txt') as file:
    contents = file.readlines()
    random_content = random.choice(contents)
text_label = tkinter.Label(text = random_content, font=('Arial',18,'normal'), wraplength = 900, justify = 'center', padx = 10, pady = 5, bg='#856ff8')
text_label.grid(row = 3, column = 0, columnspan = 3)

# User types here
text = tkinter.Text(height =5, width=80, font = ('Helvetica', 18, 'italic'),state = 'disabled')
text.focus()
text.insert(END, 'Start typing here.')
text.grid(row = 4, column = 1)

# canvas for timer
canvas = tkinter.Canvas(width = 70, height= 50, bg='#f7f5dd', highlightthickness= 0)
timer_text = canvas.create_text(35,30, text = "00", font =("Courier", 30, "bold"), fill = "black")
canvas.grid(column= 2, row = 0)

#Buttons
start_button = tkinter.Button(text = "Start", bg = "white", highlightthickness = 0, command = start_timer, padx = 10, pady = 10)
start_button.grid(column =0,columnspan = 2, row = 5)


reset_button = tkinter.Button(text = "Reset", bg = "white", highlightthickness=0, command = reset_timer, padx = 10, pady = 10)
reset_button.grid(column =2, row = 5)



window.mainloop()



# How to Operate:
# 1) To start typing press start. Then only you will be able to start typing and the timer of one minuite will start.
# 2) Keep typing till the timer stops. You will automatically be locked out of typing and will be shown your result.
# 3)You can reset your typing space and your timer by clicking reset. To start typing again click start.
# 4) You will be given random texts for typing test.