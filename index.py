import tkinter as tk
import tkinter.messagebox

import webbrowser

window = tk.Tk()


def on_button_click():
    tk.messagebox.Message(master=None, message="I love you so much!").show()


greeting = tk.Label(
    text="To My Lovely Wife...", fg="white", bg="black", width=50, height=10
)


button2 = tk.Button(
    text="Click me!", width=50, height=5, bg="blue", fg="Black", command=on_button_click
)
greeting.pack()
button2.pack()


window.mainloop()

