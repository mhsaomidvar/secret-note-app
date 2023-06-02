from tkinter import *
from tkinter.ttk import *


# window setup
secret_note_window = Tk()


def window_setup():
    secret_note_window.title("Secret Note")
    secret_note_window.minsize(width=400, height=650)
    secret_note_window.config(bg="pink")


window_setup()


# logo setup
logo = PhotoImage(file=r"D:\extraegitimler\udemy\python 100 gumluk kamp\secretnoteApp\6202718.png").subsample(5,5)
logo_label = Label(secret_note_window,image=logo)
logo_label.config(background="pink")
logo_label.pack()

# icon setup
icon = PhotoImage(file = r"D:\extraegitimler\udemy\python 100 gumluk kamp\secretnoteApp\3bfb0791a9fdddf7266c3a31a54ac5b9.png")
secret_note_window.iconphoto(False, icon)

# title setup
title_label = Label(text="Enter note title:")
title_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
title_label.pack(pady=10, padx=10)
title_entry = Entry()
title_entry.focus()
title_entry.pack()
note_title = title_entry.get()

# note setup
note_label = Label(text="Enter your secret note:")
note_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
note_label.pack(pady=10, padx=10)
note_text = Text(height=15, width=20)
note_text.pack()
secret_note = note_text.get("1.0", END)

# master key setup
key_label = Label(text="Enter your master key:")
key_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
key_label.pack(padx=10, pady=10)
key_entry = Entry()
key_entry.pack(pady=10, padx=10)
master_key = key_entry.get()

# save button setup
save_button = Button(text="Save & Encrypt")
save_button.pack(pady=5, padx=5)

# decrypt button
decrypt_button = Button(text="Decrypt")
decrypt_button.pack(pady=5, padx=5)

secret_note_window.mainloop()