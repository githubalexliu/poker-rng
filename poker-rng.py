import tkinter as tk

root = tk.Tk()
# root.overrideredirect(True) # removes title bar
root.title("Poker RNG")
root.geometry("150x100")

number_label = tk.Label(root, text="1", font=("Helvetica", 24))
number_label.pack(pady=20)

root.mainloop()