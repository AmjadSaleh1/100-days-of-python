from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- Search Website ------------------------------- #
def search_website():
    try:
        with open("data.json", "r") as data_f:
            data = json.load(data_f)
    except FileNotFoundError as m_error:
        messagebox.showerror(f" data file not found : {m_error}")
    else:
        for word in data:
            if word in website_entry.get():
                messagebox.showinfo(title="information",
                                    message=f"website: {word}\nPassword:{data[word]["password"]}")
            else:
                messagebox.showerror(message=f"no details found for this website")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    username = Username_entry.get()
    password2 = Password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password2,
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password2) == 0:
        messagebox.showerror(title="Error", message="need to fill all the fields")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# website label and entry
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
#Email/Username label and entry
Username_label = Label(text="Email/Username:")
Username_label.grid(column=0, row=2)
Username_entry = Entry(width=35)
Username_entry.grid(column=1, row=2, columnspan=2)
Username_entry.insert(0, "amjad@email.com")
#Password label and entry
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)
Password_entry = Entry(width=21)
Password_entry.grid(column=1, row=3)
#Generte button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
search_button = Button(text="Search", width=14, command=search_website)
search_button.grid(row=1, column=2)
#Add button
Add_button = Button(text="Add", width=36, command=add)
Add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
