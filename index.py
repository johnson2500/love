import tkinter as tk
import tkinter.messagebox

import webbrowser

window = tk.Tk()


def on_button_click(): 
    tk.messagebox.Message(master=None, message="I love you so much!").show()
    print("Button clicked!")


greeting = tk.Label(text="Hello.")


button2 = tk.Button(
    text="Click me!", width=5, height=5, bg="blue", fg="Black", command=on_button_click
)
button2.pack()


greeting.pack()
window.mainloop()

