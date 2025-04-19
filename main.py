from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.config(padx=100, pady=200)
window.title("Are you satisfied with your salary?")

def IKnewIt():
    messagebox.showinfo("Notice", "We know. :)")

def IDontThinkso():
    messagebox.showerror("Error", "I don't think so. ;)")

def cursor_on_no(event):
    mouse_x = event.x_root
    mouse_y = event.y_root

    btn_x = button_no.winfo_rootx()
    btn_y = button_no.winfo_rooty()
    btn_width = button_no.winfo_width()
    btn_height = button_no.winfo_height()
    
    margin = 30
    
    inside_x = (btn_x - margin) < mouse_x < (btn_x + btn_width + margin)
    inside_y = (btn_y - margin) < mouse_y < (btn_y + btn_height + margin)

    if inside_x and inside_y:
        positions = [(row, col) for row in range(1,5) for col in range(0,4) if (row, col) != (button_no_row[0], button_no_row[1])]
        positions.remove((2,0))
        random.shuffle(positions)

        for new_row, new_col in positions:
            button_no.grid_forget()
            button_no.grid(row=new_row, column=new_col)
            button_no_row[0], button_no_row[1] = new_row, new_col
            break


label = Label(window, text="Are you happy and satisfied with your salary?")
label.grid(row=0, column=1)

button_yes = Button(text="Yes!", command=IKnewIt)
button_yes.grid(row=2, column=0)

button_no_row = [2,2]
button_no = Button(text="No.", command=IDontThinkso)
button_no.grid(row=button_no_row[0], column=button_no_row[1])
button_no.bind("<Motion>", cursor_on_no)


window.mainloop()


