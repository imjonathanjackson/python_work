from tkinter import Tk
from tkinter import messagebox
from random import randint
import tkinter.messagebox

low = 0
high = 100
rand = randint(low, high)
print(rand)

def check(guess):
    if guess < rand:
        tkinter.Label(tk, text=f"{guess} is too low.").pack()
    elif guess > rand:
        tkinter.Label(tk, text=f"{guess} is too high.").pack()
    else:
        tkinter.messagebox.showinfo(f"You WIN!", f"{guess} is correct.")

tk = tkinter.Tk()
tk.title("Guess Who?")

label = tkinter.Label(tk, text=f"Guess a number between {low} and {high}")
label.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Guess", command=lambda: check(int(entry.get())))
button.pack()

tk.mainloop()
