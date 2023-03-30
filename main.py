import json
from tkinter import *
import random
from tkinter import messagebox

# ----------------------------search---------------------------------#
def search():
    website = web_entry.get().capitalize()
    try:
        with open("password.json") as file:
            pass
    except FileNotFoundError:
        messagebox.showwarning(title='Oops', message="There is 0 password saved to show save some password first")
    else:
        with open("password.json") as file:
            data = json.load(file)
        try:
            np = data[website]
        except KeyError as key:
            messagebox.showwarning(message=f"There no such website named {key}")
        else:
            messagebox.showinfo(title=website, message=f"Email: {np['email']}\nPassword: {np['password']}")


# ----------------------------show passwords-------------------------#

def show():
    window2 = Tk()
    window2.title("Saved Passwords")
    try:
        with open("password.json", "r") as f:
            pass
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="There is 0 password saved to show save some password first" )
    else:
        with open("password.json", "r") as f:
            text = Text(window2)
            text.insert(INSERT, f.read())
            text.grid()

    window2.mainloop()


# -----------------------------generate password---------------------#

def password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_']
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    generated_password = [random.choice(letters) + random.choice(symbols) + random.choice(numbers) for _ in range(4)]

    random.shuffle(generated_password)
    final_pass = "".join(generated_password)
    pass_entry.insert(0, string=final_pass)


# -----------------------------save password-------------------------#

def save():
    website = web_entry.get().capitalize()
    email = email_entry.get()
    passwrd = pass_entry.get()

    new_data = {website:
                    {"email":email,
                     "password":passwrd,
                     }
                }

    if len(website) == 0 or len(email) == 0 or len(passwrd) == 0:
        messagebox.showwarning(message="Please don't leave any of places empty", title="Oops")
    else:
        is_ok = messagebox.askyesno(message=f"Details are correct\nWebsite:{web_entry.get()}\n"
                                            f"Email/username:{email_entry.get()}\nPassword:{pass_entry.get()}",
                                    title="Are you sure")
        if is_ok:
            try:
                with open("password.json", 'r') as file:
                    # open the file
                    data = json.load(file)

            except FileNotFoundError:
                with open("password.json", "w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                # update the data
                data.update(new_data)
                with open("password.json", "w") as file:
                    # write to the file
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# -----------------------------UI setup------------------------------#

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="lg-resized.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1, padx=2, pady=2)

web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0, sticky="w", padx=1, pady=1)

web_entry = Entry(width=24, bg="white", highlightthickness=0)
web_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=1, pady=1)
web_entry.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0, sticky="w", padx=1, pady=1)

email_entry = Entry(width=37, bg="white", highlightthickness=0)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=1, pady=1)
email_entry.insert(END, string="khem199844@gmail.com")

pass_label = Label(text="Password:", bg="white")
pass_label.grid(row=3, column=0, sticky="w", padx=1, pady=1)

pass_entry = Entry(width=24, bg="white", highlightthickness=0)
pass_entry.grid(row=3, column=1, sticky="w", padx=1, pady=1)

gene_button = Button(text="Generate password", width=12, font=("arial", 8), bg="white", highlightthickness=0,
                     command=password, activebackground="blue", activeforeground="white")
gene_button.grid(row=3, column=2, sticky="w", padx=1, pady=1)

add_button = Button(width=46, text="Add", font=("arial", 8), bg="white", highlightthickness=0, command=save,
                    activebackground="blue", activeforeground="white")
add_button.grid(row=4, column=1, columnspan=2, sticky="w", padx=1, pady=1)

show_button = Button(width=46, text="Show Saved Passwords", font=("arial", 8), bg="white", highlightthickness=0, command=show,
                     activebackground="blue", activeforeground="white")
show_button.grid(row=5, column=1, columnspan=2, sticky="w", padx=1, pady=1)

search_button = Button(width=12, text="search", font=("arial", 8), bg="white", highlightthickness=0, command=search,
                     activebackground="blue", activeforeground="white")
search_button.grid(row=1, column=2)

window.mainloop()
