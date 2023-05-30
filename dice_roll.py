
import tkinter
import random

root = tkinter.Tk()  # Create the object.
root.geometry("850x550")  # Dimensions of the window that will appear. Width and Length.
root.title("Roll Dice")  # Title of the window.

label = tkinter.Label(root, text="", font=("times", 260))  # Configuration of the image of the dices.

def roll():
    dice = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]  # 1,2,3,4,5,6 dices.
    label.configure(text=f"{random.choice(dice)} {random.choice(dice)}")
    label.pack()

button = tkinter.Button(root, text="Let's Roll", width=40, height=5, font=10, bg="blue", bd=2, command=roll)  # Configuration of the button.
button.pack(padx=15, pady=15)  # Indicate the coordinates where will be located the button.

root.mainloop()  # Initiate the program.