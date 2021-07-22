from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

ecolor = 'white'
lcolor = '#994422'


class LoginPasswordManager:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('350x500')
        self.window.title(' L O G I N ')
        self.window.resizable(0, 0)
        self.success = None
        
        #Making gradient frame
        j=0
        r=10
        for i in range(100):
            c=str(222222+r)
            Frame(self.window,width=10,height=500,bg="#"+c).place(x=j,y=0)   
            j=j+10                                                  
            r=r+1

        Frame(self.window, width=250, height=400, bg='white').place(x=50, y=50)

        self.user_name_label=Label(self.window,text='Username',bg='white')
        self.l=('Consolas',13)
        self.user_name_label.config(font=self.l)
        self.user_name_label.place(x=80,y=200)

        #entry for username entry
        self.user_name_entry=Entry(self.window,width=20,border=0)
        self.l=('Consolas',13)
        self.user_name_entry.config(font=self.l)
        self.user_name_entry.place(x=80,y=230)

        #entry for password entry
        self.password_entry=Entry(self.window,width=20,border=0,show='*')
        self.password_entry.config(font=self.l)
        self.password_entry.place(x=80,y=310)


        self.password_label=Label(self.window,text='Password',bg='white')
        self.password_label.config(font=self.l)
        self.password_label.place(x=80,y=280)


        ###lineframe on entry
        Frame(self.window, width=180, height=2, bg='#141414').place(x=80, y=332)
        Frame(self.window, width=180, height=2, bg='#141414').place(x=80, y=252)
        
        self.imagea=Image.open("login/log.png")
        self.imageb= ImageTk.PhotoImage(self.imagea) 

        self.image_label = Label(image=self.imageb, border=0, justify=CENTER)
        self.image_label.place(x=115, y=50)

        #Login Button
        self.login_button = Button(self.window,text='L O G I N',
                    width=20,
                    height=2,
                    fg=ecolor,
                    border=0,
                    bg=lcolor,
                    activeforeground=lcolor,
                    activebackground=ecolor,
                    command=self.login_check)
                    
        self.login_button.bind("<Enter>", self.on_entera) 
        self.login_button.bind("<Leave>", self.on_leavea)
        self.window.bind("<Return>", self.login_check)

        self.login_button.place(x=100,y=375)
        self.window.mainloop()


    
    
    #Login check authentication
    def login_check(self, event):
        if self.user_name_entry.get() == "admin" and self.password_entry.get() == "admin123":
            messagebox.showinfo(title="LOGIN SUCCESSFULL", message="         WELCOME TO PASSWORD MANAGER       ")
            self.window.destroy()
            self.success = True
        else:
            messagebox.showerror(title="LOGIN FAILED", message="        PLEASE TRY AGAIN        ")
            self.user_name_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.user_name_entry.focus()
            self.success = False
            



    #Button_with hover effect
    def on_entera(self,e):
        self.login_button['background'] = "#ffcc66" 
        self.login_button['foreground'] = "#000d33"  

    def on_leavea(self,e):
        self.login_button['background'] = lcolor
        self.login_button['foreground']= ecolor
