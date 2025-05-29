import tkinter as tk
import random


def update_number():
    number = random.randint(1, 100)
    number_label.config(text=str(number))
    root.after(2000, update_number)


root = tk.Tk()
# root.overrideredirect(True) # removes title bar
root.title("Poker RNG")
root.geometry("150x100")
root.configure(bg="black")

number_label = tk.Label(root, text="", font=("Helvetica", 24), fg="white", bg="black")
number_label.pack(pady=20)

update_number()

root.mainloop()