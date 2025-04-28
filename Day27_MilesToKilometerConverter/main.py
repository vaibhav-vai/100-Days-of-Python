from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0,column=0)


#Button

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)

button = Button(text="Button 2", command=button_clicked)
button.grid(row=0,column=3)

#Entry

input = Entry(width=10)
input.grid(row=3,column=4)


window.mainloop()