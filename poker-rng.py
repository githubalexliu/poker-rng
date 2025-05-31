import tkinter as tk
import random


def update_number():
    number = random.randint(1, 100)
    number_label.config(text=str(number))
    if number > 75:
        number_label.config(fg="red")
    elif number > 50:
        number_label.config(fg="pink")
    elif number > 25:
        number_label.config(fg="light green")
    else:
        number_label.config(fg="green")
    root.after(2000, update_number)


def start_move(event):
    root.x = event.x
    root.y = event.y


def do_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    new_x = root.winfo_x() + deltax
    new_y = root.winfo_y() + deltay
    root.geometry(f"+{new_x}+{new_y}")


root = tk.Tk()
root.overrideredirect(True) # removes title bar
root.title("Poker RNG")
root.geometry("70x60")
root.configure(bg="black")
root.attributes("-topmost", True)

number_label = tk.Label(root, text="", font=("Helvetica", 24), bg="black")
number_label.pack(pady=10)

update_number()

root.bind('<space>', lambda event: root.destroy())
root.bind('<Button-1>', start_move)
root.bind('<B1-Motion>', do_move)

root.mainloop()