from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':  #if both fields are empty,this statement is true
        messagebox.showerror('Error','Fields cannot be empty') #showing error box
    elif usernameEntry.get()=='Vivek' and passwordEntry.get()=='1234': #for correct username and password
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')


window=Tk() #class

window.geometry('1280x700+0+0') #height and width
window.title('Login System of Student Managment System')

window.resizable(False,False) #can't change window size

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0) #Placing image in GUI

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150) #for making frame for logo

logoImage=PhotoImage(file='logo.png')

logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='slate blue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)  #Adding password box

PasswordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=PasswordImage,text='Password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='slate blue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)  #Adding password box

loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,
                   fg='white',bg='cornflowerblue',activebackground='cornflowerblue'
                   ,activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



window.mainloop()  #keep window on loop to let us see
