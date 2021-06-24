import turtle
import json
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import choice, shuffle, randint
from cryptography.fernet import Fernet
from login.login import LoginPasswordManager


# ---------------------------- CONSTANTS ------------------------------------ # 
ecolor = 'white'
lcolor = '#994422'
l = ('Consolas', 13)


# ---------------------------- SEARCH DETAILS ------------------------------------ #
def search_info():
    req_website = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
        with open("key.json", mode="r") as key_file:
            key_data = json.load(key_file)
        req_email = data[req_website]["email"]
        req_encryp_password = data[req_website]["Encrypted Password"].encode("utf-8")
        req_key = key_data[req_website]["key"].encode("utf-8")
      
        fernet = Fernet(req_key)
        decrypted_password = fernet.decrypt(req_encryp_password).decode()

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.") 
    except KeyError:
        messagebox.showerror(title="Error", message=f"No Details for {req_website} exists.")
    else:
        website_entry.delete(0, END)         
        messagebox.showinfo(title=req_website, message=f"Email: {req_email} \nDecrypted Password: {decrypted_password}") 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password) 

# ---------------------------- SAVE DETAILS ------------------------------- #
def save_info():
    website = website_entry.get().title()
    email = email_username_entry.get()
    password = password_entry.get()
    
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encPassword = fernet.encrypt(password.encode())
    
    new_data = {
        website: {
            "email": email,
            "Encrypted Password": encPassword.decode()
        }
    }
    new_key = {
        website: {
            "key": key.decode()
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0: 
        messagebox.showerror(title="Oops", message="PLease don't leave any fields empty!!!")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading old Data
                data = json.load(data_file)
            with open("key.json", mode="r") as key_file:
                #Reading old Key
                key_data = json.load(key_file)
        except FileNotFoundError: 
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
            with open("key.json", mode="w") as key_file:
                json.dump(new_key, key_file, indent=4)
                
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

            messagebox.showinfo(title="Success", message="Details saved successfully!!!")
        else:
            #Updating old Data with new Data in data file
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                #Saving updated Data in data file
                json.dump(data, data_file, indent=4)


            #Updating old Data with new Data in key file
            key_data.update(new_key)

            with open("key.json", mode="w") as key_file:
                #Saving updated Data in key file
                json.dump(key_data, key_file, indent=4)

            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
            
            messagebox.showinfo(title="Success", message="Details saved successfully!!!")
            


# ---------------------------- EDIT DETAILS ------------------------------- #
def edit_info():
    screen = turtle.Screen()
    screen.bye()
    edit_website = screen.textinput(title="Edit Details", prompt="Enter the Website").title()
    try:
        with open("data.json", mode="r") as data_file:
            edit_data = json.load(data_file)
        with open("key.json", mode="r") as key_file:
            key_edit_data = json.load(key_file)
        edit_email = edit_data[edit_website]["email"]
        edit_password_enc = edit_data[edit_website]["Encrypted Password"].encode("utf-8")
        edit_key = key_edit_data[edit_website]["key"].encode("utf-8")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found to Edit.") 
    except KeyError:
        messagebox.showerror(title="Error", message=f"No Details for {edit_website} exists to Edit.")
    else:
        website_entry.delete(0, END)
        email_username_entry.delete(0, END)
        password_entry.delete(0, END)

        fernet = Fernet(edit_key)
        edit_password_dec = fernet.decrypt(edit_password_enc).decode()

        website_entry.insert(0, edit_website)
        email_username_entry.insert(0, edit_email)
        password_entry.insert(0, edit_password_dec) 

    
# ---------------------------- DELETE DETAILS ------------------------------- #
def delete_info():
    screen = turtle.Screen()
    screen.bye()
    delete_website = screen.textinput(title="Delete Details", prompt="Enter the Website").title()
    try:
        with open("data.json", mode="r") as data_file:
            delete_data = json.load(data_file)
        with open("key.json", mode="r") as key_file:
            key_delete_data = json.load(key_file)

        del delete_data[delete_website]
        del key_delete_data[delete_website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found to Delete.")
    except KeyError:
        messagebox.showerror(title="Error", message=f"No Details for {delete_website} exists to Delete.")
    else:
        with open("data.json", mode="w") as data_file:
            #Saving updated Data in data file after deletion
            json.dump(delete_data, data_file, indent=4)
        
        with open("key.json", mode="w") as key_file:
            #Saving updated Data in key file after deletion
            json.dump(key_delete_data, key_file, indent=4)
    
        messagebox.showinfo(title="Success", message=f"Details for {delete_website} deleted successfully!!!")
        


# ---------------------------- UI SETUP ------------------------------- #
login_window = LoginPasswordManager()

if login_window.success:
    window = Tk()
    window.geometry('600x600')
    window.title("P A S S W O R D       M A N A G E R")

    #Making gradient frame
    j=0
    r=10
    for i in range(100):
        c=str(222222+r)
        Frame(window,width=10,height=600,bg="#"+c).place(x=j,y=0)   
        j=j+10                                                  
        r=r+1

    Frame(window, width=500, height=500, bg='white').place(x=50, y=50)

    #Password Manager Logo
    imagea=Image.open("logo.png")
    imageb= ImageTk.PhotoImage(imagea) 
    image_label = Label(image=imageb, border=0, justify=CENTER)
    image_label.place(x=200, y=65)



    #Labels
    website_label=Label(window, text="Website:", bg="white", font=l)
    website_label.place(x=133, y=290)

    email_username_label = Label(window, text="Email/Username:", bg='white', font=l)
    email_username_label.place(x=70, y=340)

    password_label = Label(window, text="Password:", bg="white", font=l)
    password_label.place(x=123, y=390)



    #lineframe on entry
    Frame(window, width=180, height=2, bg='#141414').place(x=225, y=312)
    Frame(window, width=280, height=2, bg='#141414').place(x=225, y=362)
    Frame(window, width=180, height=2, bg='#141414').place(x=225, y=412)



    #Entries
    website_entry = Entry(window, width=20, border=0, font=l)
    website_entry.place(x=225, y=290)
    website_entry.focus()

    email_username_entry = Entry(window, width=31, border=0, font=l)
    email_username_entry.place(x=225, y=340)

    password_entry = Entry(window, width=20, border=0, font=l)
    password_entry.place(x=225, y=390)



    #Buttons
    #Search Button
    search_button = Button(window,text='S E A R C H',
                        width=13,
                        height=1,
                        fg=ecolor,
                        border=0,
                        bg=lcolor,
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=search_info)               
    search_button.place(x=425, y=290)

    #Generate Password Button
    generate_password_btn = Button(window,text="GENERATE   PASSWORD",
                        width=18,
                        height=1,
                        fg=ecolor,
                        border=0,
                        bg="#17423a",
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=generate_password)       
    generate_password_btn.place(x=412, y=390)

    #Add Button
    add_btn = Button(window,text="A D D",
                        width=20,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg="#064018",
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=save_info)       
    add_btn.place(x=220, y=460)

    #Edit Button
    edit_btn = Button(window,text="E D I T",
                        width=18,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg="#5e0761",
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=edit_info)       
    edit_btn.place(x=140, y=510)

    #Delete Button
    delete_btn = Button(window,text="D E L E T E",
                        width=18,
                        height=2,
                        fg=ecolor,
                        border=0,
                        bg="#700926",
                        activeforeground=lcolor,
                        activebackground=ecolor,
                        command=delete_info)       
    delete_btn.place(x=315, y=510)



    window.mainloop() 