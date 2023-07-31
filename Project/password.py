from tkinter import * 
import random
from tkinter.ttk import *
import pyperclip
 
r = Tk()
r.geometry("650x250")
r.title('Password')

label=Label(r, text="Welcome to Naitik's Password Machine", font=("Courier 22 bold"), background="yellow")
label.pack(pady=20)

style = Style()
 
style.configure('TButton', font =
               ('calibri', 15, 'bold'),
                    borderwidth = '2')

style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])

def check():
    c = Tk()
    c.geometry("650x250")
    c['background']='yellow'
    label=Label(c, text="Enter your password\n", font=("Courier 22 bold"), background="yellow")
    label.pack()

    entry= Entry(c, width= 40)
    entry.focus_set()
    entry.pack()

    def getScore():
        password = entry.get()
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789!@#$%^&*()"
        containsMap = {'lower':False, 'upper':False, 'digits':False}

        for i in password:
            if i in lower:
                containsMap["lower"] = True
            elif i in upper:
                containsMap["upper"] = True
            elif i in digits:
                containsMap["digits"] = True
            else:
                return "Incorrect character detected!"
            
        score = list(containsMap.values()).count(True)
            
        if score==1:
            return "Your Password Strength is Low"
        elif score==2:
            return "Your Password Strength is Medium"
        else:
            return "Your Password Strength is Strong"
        
    def packPasswordScore():
        score = getScore()
        label2.config(text=score, background="yellow")
        label2.pack()

    cb = Button(c, text= "Submit",width= 20, command= packPasswordScore)
    cb.pack(pady=20)

    label2=Label(c,font=("Courier 22 bold"),background="yellow")
    label2.pack()
    

def generatebox():
    root = Tk()
    var = IntVar()
    root['background']='yellow'
    combo = Combobox(root)
    def low(combo:Combobox, var):
        entry.delete(0, END)
 
        # Get the length of password
        length = int(combo.get())
 
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
        password = ""
 
        # if strength selected is low
        if var.get() == 1:
            for i in range(0, length):
                password = password + random.choice(lower)
            return password
 
        # if strength selected is medium
        elif var.get() == 0:
            for i in range(0, length):
                password = password + random.choice(upper)
            return password
 
        # if strength selected is strong
        elif var.get() == 3:
            for i in range(0, length):
                password = password + random.choice(digits)
            return password
        else:
            print("Please choose an option")

    def generate(combo, var):
        
        password1 = low(combo, var)
        entry.insert(10, password1)

    def copy1():
        random_password = entry.get()
        pyperclip.copy(random_password)

    
    
    # root.geometry("650x250")
    root.title("Password Generator")

    Random_password = Label(root, text="Password",background="yellow")
    Random_password.grid(row=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)
 
    # create label for length of password
    c_label = Label(root, text="Length",background="yellow")
    c_label.grid(row=1)
        
    # create Buttons Copy which will copy
    # password to clipboard and Generate
    # which will generate the password
    copy_button = Button(root, text="Copy", command=copy1)
    copy_button.grid(row=0, column=2)
    generate_button = Button(root, text="Generate", command=lambda: generate(combo, var))
    generate_button.grid(row=0, column=3)
        
        # Radio Buttons for deciding the
        # strength of password
        # Default strength is Medium
    radio_low = Radiobutton(root, text="Low", variable=var, value=1)
    radio_low.grid(row=1, column=2, sticky='E')
    radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
    radio_middle.grid(row=1, column=3, sticky='E')
    radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
    radio_strong.grid(row=1, column=4, sticky='E')
    
        
        # Combo Box for length of your password
    combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                        17, 18, 19, 20, 21, 22, 23, 24, 25,
                        26, 27, 28, 29, 30, 31, 32, "Length")
    combo.current(0)
    combo.bind('<<ComboboxSelected>>')
    combo.grid(column=1, row=1)
    root.mainloop()

r['background']='yellow'
checkbutton = Button(r, text='Check', width=50, command=check).place(x=75, y=80)
# checkbutton.grid(row = 2, column = 2, pady = 10, padx = 100)
# checkbutton.pack()
generatebutton = Button(r, text='Generate', width=50, command=generatebox).place(x=75, y=130)
# generatebutton.grid(row = 3, column = 2, pady = 10, padx = 100)
# generatebutton.pack()
r.mainloop()
