'''New Working Code'''
from tkinter import *
from tkinter import messagebox

# Login function
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Vivek' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms  # Import only when successful
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

# Window setup
window = Tk()
window.geometry('400x300')
window.title('Login System')
window.resizable(False, False)

# Login Frame
loginFrame = Frame(window, bg='white', padx=20, pady=20)
loginFrame.pack(expand=True)

# Username
usernameLabel = Label(loginFrame, text='Username:', font=('Times New Roman', 14), bg='white')
usernameLabel.grid(row=0, column=0, pady=10, padx=10, sticky=W)

usernameEntry = Entry(loginFrame, font=('Times New Roman', 14), bd=2)
usernameEntry.grid(row=0, column=1, pady=10, padx=10)

# Password
passwordLabel = Label(loginFrame, text='Password:', font=('Times New Roman', 14), bg='white')
passwordLabel.grid(row=1, column=0, pady=10, padx=10, sticky=W)

passwordEntry = Entry(loginFrame, font=('Times New Roman', 14), bd=2, show='*')
passwordEntry.grid(row=1, column=1, pady=10, padx=10)

# Login Button
loginButton = Button(
    loginFrame, text='Login', font=('Times New Roman', 12, 'bold'),
    fg='white', bg='cornflowerblue', width=15, command=login
)
loginButton.grid(row=2, column=1, pady=20)

# Run the window
window.mainloop()


''' Old Code:
1. Formatting Issue
2. Image Import Issue
3. Image Display Issue
'''
# from tkinter import *
# from tkinter import messagebox
# from PIL import Image, ImageTk

# def login():
#     if usernameEntry.get()=='' or passwordEntry.get()=='':  #if both fields are empty,this statement is true
#         messagebox.showerror('Error','Fields cannot be empty') #showing error box
#     elif usernameEntry.get()=='Vivek' and passwordEntry.get()=='1234': #for correct username and password
#         messagebox.showinfo('Success','Welcome')
#         window.destroy()
#         import sms
#     else:
#         messagebox.showerror('Error','Please enter correct credentials')

# bg_image = Image.open("img_assets/bg.jpg")
# logo_image = Image.open("img_assets/logo.jpg")
# password_image = Image.open("img_assets/password.png")
# user_image = Image.open("img_assets/user.png")

# window=Tk() #class

# window.geometry('1280x700+0+0') #height and width
# window.title('Login System of Student Managment System')

# window.resizable(False,False) #can't change window size

# backgroundImage=ImageTk.PhotoImage(bg_image)

# bgLabel=Label(window,image=backgroundImage)
# bgLabel.place(x=0,y=0) #Placing image in GUI

# loginFrame=Frame(window,bg='white')
# loginFrame.place(x=400,y=150) #for making frame for logo

# logoImage=ImageTk.PhotoImage(logo_image)

# logoLabel=Label(loginFrame,image=logoImage)
# logoLabel.grid(row=0,column=0,columnspan=2,pady=10)
# usernameImage=ImageTk.PhotoImage(user_image)
# usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
#                     ,font=('times new roman',20,'bold'),bg='white')
# usernameLabel.grid(row=1,column=0,pady=10,padx=20)

# usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='slate blue')
# usernameEntry.grid(row=1,column=1,pady=10,padx=20)  #Adding password box

# PasswordImage=ImageTk.PhotoImage(password_image)
# passwordLabel=Label(loginFrame,image=PasswordImage,text='Password',compound=LEFT
#                     ,font=('times new roman',20,'bold'),bg='white')
# passwordLabel.grid(row=2,column=0,pady=10,padx=20)

# passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='slate blue')
# passwordEntry.grid(row=2,column=1,pady=10,padx=20)  #Adding password box

# loginButton=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,
#                    fg='white',bg='cornflowerblue',activebackground='cornflowerblue'
#                    ,activeforeground='white',cursor='hand2',command=login)
# loginButton.grid(row=3,column=1,pady=10)



# window.mainloop()  #keep window on loop to let us see

