from tkinter import *
from  tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
from numpy.ma.extras import row_stack

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    [password_list.append(choice(letters)) for _ in range(nr_letters)]
    [password_list.append(choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(choice(numbers)) for _  in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    # print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

#---------------------------- Save Data -------------------------------------------#

def get_detail():
    website = website_input.get()
    email = eu_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showerror("Empty field", message="Please fill all the fields")
    else:
        try:
            with open("data.json", 'r') as file:
               data = json.load(file)

        except FileNotFoundError:
              with open('data.json', 'w') as file:
                 json.dump(new_data, file, indent=4)

        else:
            with open('data.json', 'w') as file:
               data.update(new_data)
               json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            eu_input.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    try:
        website = website_input.get().lower()
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="No file", message=" No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]["email"]} \n password: {data[website]["password"]}" )
        else:
            messagebox.showerror(title="invalid website", message="Website not found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website_input = Entry(width=21, )
website_input.grid( row=1, column=1)

search_btn = Button(text='search', width=14, command=search)
search_btn.grid(row=1, column=2)

eu_text = Label(text="Email/Username:")
eu_text.grid( row=2, column=0)

eu_input = Entry(width=45)
eu_input.insert(0, "yahyagodiwa@gmail.com")
eu_input.grid( row=2, column=1, columnspan=3)

password_text = Label(text="Password:")
password_text.grid( row=3, column=0,)

password_input = Entry(width=21)
password_input.grid( row=3, column=1)

password_btn = Button(text="Generate password", command=generate)
password_btn.grid( row=3, column=2,)

add_btn = Button(text="Add", width=35, command=get_detail)
add_btn.grid( row=4, column=1, columnspan=2)





window.mainloop()