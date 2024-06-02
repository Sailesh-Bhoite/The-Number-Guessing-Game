from tkinter import *
from tkinter import ttk
import random


def display(sentence: str):
    li: list = sentence.split()
    size: int = len(li)
    if size == 3:
        win.after(299, lambda: label.configure(foreground="green"))
        win.after(500, lambda: label_text.set("You "))
        win.after(1000, lambda: label_text.set("You Got "))
        win.after(1500, lambda: label_text.set("You Got It"))
        win.after(2000, lambda: label_text.set("You Got It!"))
        win.after(2200, lambda: label_text.set("You Got It!!"))
        win.after(2400, lambda: label_text.set("You Got It!!!"))
        win.after(3000, lambda: label_text.set("Congratulations!!!"))
    elif size == 5:
        win.after(299, lambda: label.configure(foreground="dark green"))
        win.after(300, lambda: label_text.set("Result"))
        win.after(500, lambda: label_text.set("Result will"))
        win.after(700, lambda: label_text.set("Result will be"))
        win.after(900, lambda: label_text.set("Result will be seen"))
        win.after(1100, lambda: label_text.set("Result will be seen here"))
        win.after(1300, lambda: label_text.set("Result will be seen here!"))
        win.after(1500, lambda: label_text.set("Result will be seen here!!"))
        win.after(1700, lambda: label_text.set("Result will be seen here!!!"))
    elif size == 4 and li[-1] == "low!":
        win.after(299, lambda: label.configure(foreground="blue"))
        win.after(300, lambda: label_text.set("Your "))
        win.after(400, lambda: label_text.set("Your number"))
        win.after(500, lambda: label_text.set("Your number is"))
        win.after(600, lambda: label_text.set("Your number is low"))
        win.after(700, lambda: label_text.set("Your number is low!"))
    elif size == 4 and li[-1] == "high!":
        win.after(100, lambda: label.configure(foreground="red"))
        win.after(300, lambda: label_text.set("Your"))
        win.after(400, lambda: label_text.set("Your number"))
        win.after(500, lambda: label_text.set("Your number is"))
        win.after(600, lambda: label_text.set("Your number is high"))
        win.after(700, lambda: label_text.set("Your number is high!"))
    elif size == 2:
        win.after(299, lambda: label.configure(foreground="brown"))
        win.after(300, lambda: label_text.set("Enter"))
        win.after(500, lambda: label_text.set("Enter numbers"))
        win.after(700, lambda: label_text.set("Enter numbers only"))
    elif size == 6:
        win.after(299, lambda: label.configure(foreground="brown"))
        win.after(300, lambda: label_text.set("Enter"))
        win.after(500, lambda: label_text.set("Enter number"))
        win.after(700, lambda: label_text.set("Enter number between"))
        win.after(1200, lambda: label_text.set("Enter number between 0"))
        win.after(1300, lambda: label_text.set("Enter number between 0 to"))
        win.after(1400, lambda: label_text.set("Enter number between 0 to 100"))
    else:
        win.after(200, lambda: label_text.set("Kuchh"))
        win.after(500, lambda: label_text.set("Kuchh Alag"))
        win.after(1100, lambda: label_text.set("Kuchh Alag Maal"))
        win.after(1500, lambda: label_text.set("Kuchh Alag Maal Maarela"))
        win.after(1900, lambda: label_text.set("Kuchh Alag Maal Maarela Hain"))
        win.after(2300, lambda: label_text.set("Kuchh Alag Maal Maarela Hain Kya"))


def check():
    try:
        s = int(textbox.get())
    except ValueError:
        print("Message: Enter a number")
        display("Enter number")
        win.configure(bg="purple")
    else:
        if s > 100 or s < 0:
            print("Message: Enter number between 0 to 100\nYou Entered:", s, "\n")
            display("Enter number between 0 to 100")
            win.configure(bg="violet")
        else:
            if x == s:
                print("Got it!!!\nThe number was", x)
                display("You Got It!!!")
                win.configure(bg="green")
            elif s > x:
                display("Your number is high!")
                print("Too high!\nYou Entered:", s, "\n")
                win.configure(bg="red")
            else:
                display("Your number is low!")
                print("Too low!\nYou Entered:", s, "\n")
                win.configure(bg="blue")


win = Tk()
win.geometry("850x550+200+50")  # Size of the window.
win.iconbitmap("number_guess_logo.ico")  # Icon of the Window.
win.title("The Number Guessing Game")  # The Title of the Window.
win.resizable(False, False)  # Window can't be expanded or shrink.
win.configure(bg="black")  # Initial background is black.
x = random.randint(0, 100)  # Specifying random number limit from 0 to 100.

style = ttk.Style()
style.configure("label.TLabel", font=("Algerian", 50), background="yellow")
label = ttk.Label(win, text="guess the number!", style="label.TLabel")
label.pack(pady=40)

textbox = ttk.Entry(font=("Times New Roman", 50), width=3)
textbox.pack()

style.configure("Submit_button.TButton", font=("Algerian", 50), foreground="olive", background="Yellow")
submit = ttk.Button(text="Submit", style="Submit_button.TButton", command=check)
submit.pack(pady=40)

remark = ttk.Frame()
remark.configure(width=50, height=50, border=80, borderwidth=10, relief="raised", padding=(5, 5, 5, 5))
remark.pack()

label_text = StringVar()
display("Result will be seen here")
label = ttk.Label(remark, textvariable=label_text, font=("consolas", 30))
label.grid(column=0, row=0, padx=10, pady=10)

win.mainloop()
