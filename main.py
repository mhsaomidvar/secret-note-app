from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import base64


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)



# window setup
secret_note_window = Tk()


def window_setup():
    secret_note_window.title("Secret Note")
    secret_note_window.minsize(width=400, height=650)
    secret_note_window.config(bg="pink")


window_setup()


# logo setup
logo = PhotoImage(file=r"put your logo icon path here").subsample(5,5)
logo_label = Label(secret_note_window,image=logo)
logo_label.config(background="pink")
logo_label.pack()

# icon setup
icon = PhotoImage(file = r"put your app icon path here")
secret_note_window.iconphoto(False, icon)

# title setup
title_label = Label(text="Enter note title:")
title_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
title_label.pack(pady=10, padx=10)
title_entry = Entry()
title_entry.focus()
title_entry.pack()


# note setup
note_label = Label(text="Enter your secret note:")
note_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
note_label.pack(pady=10, padx=10)
note_text = Text(height=15, width=20)
note_text.pack()


# master key setup
key_label = Label(text="Enter your master key:")
key_label.config(background="pink", foreground="white", font=["Arial", 11, "bold"])
key_label.pack(padx=10, pady=10)
key_entry = Entry()
key_entry.pack(pady=10, padx=10)



# file save and encrypt setup

def save_and_encrypt_notes():
    note_title = title_entry.get()
    secret_note = note_text.get("1.0", END)
    master_key = key_entry.get()

    if len(note_title) == 0 or len(secret_note) == 0 or len(master_key) == 0:
        messagebox.showerror(title="Error",message="Please enter all info.")
    else:
        note_encrypted = encode(master_key, secret_note)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{note_title}\n{note_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f"\n{note_title}\n{note_encrypted}")

        finally:
            title_entry.delete(0, END)
            key_entry.delete(0, END)
            note_text.delete("1.0", END)

def decrypt_note():
    secret_token = note_text.get("1.0", END)
    master_key = key_entry.get()

    if len(secret_token) == 0 or len(master_key) == 0:
        messagebox.showerror(title="Error", message="Please enter all info.")
    else:
        try:
            decrypted_token = decode(master_key, secret_token)
            note_text.delete("1.0", END)
            note_text.insert("1.0", decrypted_token)
        except:
            messagebox.showerror(title="Error", message="Wrong code.")


# save button setup
save_button = Button(text="Save & Encrypt", command=save_and_encrypt_notes)
save_button.pack(pady=5, padx=5)


# decrypt button
decrypt_button = Button(text="Decrypt", command=decrypt_note)
decrypt_button.pack(pady=5, padx=5)


secret_note_window.mainloop()
