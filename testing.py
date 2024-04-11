import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import cv2
import os
from PIL import Image, ImageTk
import numpy as np
import face_recognition
import time
from tkinter import Message ,Text
import tkinter.ttk as ttk
import tkinter.font as font
import csv
import json
import pandas as pd


#####Loading Data from txt file
def loading_data():
    file=open('data.txt','r',encoding='utf-8')  
    data=json.load(file)
    file.close()
    return data
##Saving Data to .txt file
def saving_data(data):
    file=open('data.txt','w',encoding='utf-8')
    json.dump(data,file,ensure_ascii=False)
    file.close()

##saving data in a variable
#data=dict()
data=loading_data()
print(data)

current_balance = 100000
transaction_history = []

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
canvas1 = tk.Canvas()
root.state('zoomed')
root.title("BIOMETRIC ATM SYSTEM")

root.rowconfigure(0,weight = 1)
root.columnconfigure(0,weight = 1)

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root,bg = "#C1C1FF")
frame4 = tk.Frame(root,bg = "#C1C1FF")
frame5 = tk.Frame(root,bg = "#C1C1FF")
frame6 = tk.Frame(root,bg = "#C1C1FF")
frame7 = tk.Frame(root,bg = "#C1C1FF")
frame8 = tk.Frame(root,bg = "#C1C1FF")
frame9 = tk.Frame(root,bg = "#C1C1FF")
for frame in (frame1,frame2,frame3,frame4,frame5,frame6,frame7,frame8,frame9):
    frame.grid(row=0,column=0,sticky='nsew')


#**************************************************************************FRAME 1**************************************************************************

frame_title = tk.Label(frame1,text = """WELCOME
TO
BIOMETRIC ATM SYSTEM""", bg = "#C1C1FF",fg = "#3C3CB3",font = ("TT Prosto Sans Trl Cnd Black",95))
frame_title.pack(fill = 'both', expand = True)


enter_button = tk.Button(frame1, text = "ENTER TO PROCEED",font = ("TT Prosto Sans Trl Cnd Black",20),command= lambda:show_frame(frame2))
enter_button.config(bg = '#2b07e0',fg = '#e4e3e8')
enter_button.place (x = 700,y = 750)

#**************************************************************************FRAME 2**************************************************************************

frame2_title=  tk.Label(frame2,text = 'SELECT TRANSACTION METHOD',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',55),height = 2000,width = 500)
frame2_title.pack(fill = 'both', expand = True)

frame2_btn1 = tk.Button(frame2,text="CARD",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8" ,command= lambda:show_frame(frame3))
frame2_btn1.place(x=570, y=650)

frame2_btn2 = tk.Button(frame2,text="CARDLESS",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame7))
frame2_btn2.place(x=970, y=650)

#**************************************************************************FRAME 3**************************************************************************


password_label = tk.Label(frame3,text = "ENTER PIN NUMBER",bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',55))
password_label.pack(pady=10)

my_password = tk.StringVar()

password_entry_box = tk.Entry(frame3,textvariable=my_password,width = 30,font = ('Arial 20'), borderwidth = 3,show = "*")
password_entry_box.focus_set()
password_entry_box.pack(ipady=7)

def handle_focus_in(_):
    password_entry_box.configure(fg='black',show='*')
password_entry_box.bind('<FocusIn>',handle_focus_in)

def check_password():
    if my_password.get() == txt4.get():
        my_password.set('')
        incorrect_password_label['text']=''
        password_label.forget()
        password_entry_box.destroy()        
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_0.destroy()
        button_clear.destroy()
        enter_button.destroy()

        name = tk.Label(frame3,text = 'WELCOME MR SANJAY A',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',40)).place(x = 100,y = 200)
        verify =  tk.Label(frame3,text = 'SELECT ANY ONE',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',50)).place(x = 600,y = 500)

        withdraw = tk.Button(frame3,text="CASH WITHDRAWAL",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        withdraw.place(x=110, y=370)

        deposit = tk.Button(frame3,text="CASH DEPOSIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame5))
        deposit.place(x=110, y=490)

        check_balance = tk.Button(frame3,text="CHECK BALANCE", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame6))
        check_balance.place(x=110, y=610)

        mini_statement = tk.Button(frame3,text="MINI STATEMENT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame7))
        mini_statement.place(x=110, y=730)

        change_pin = tk.Button(frame3,text="CHANGE PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        change_pin.place(x=1250, y=370)

        forgot_pin = tk.Button(frame3,text="FORGOT PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command= lambda:show_frame(frame4))
        forgot_pin.place(x=1250, y=490)

        green_pin = tk.Button(frame3,text="GREEN PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        green_pin.place(x=1250, y=610)

        exit_button = tk.Button(frame3,text="EXIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame1))
        exit_button.place(x=1250, y=730)

    elif my_password.get() == '2002':
        my_password.set('')
        incorrect_password_label['text']=''
        password_label.forget()
        password_entry_box.destroy()
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_0.destroy()
        button_clear.destroy()
        enter_button.destroy()

        name = tk.Label(frame3,text = 'WELCOME MR RAVULA PRAVEEN',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',40)).place(x = 100,y = 200)
        verify =  tk.Label(frame3,text = 'SELECT ANY ONE',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',50)).place(x = 600,y = 500)

        withdraw = tk.Button(frame3,text="CASH WITHDRAWAL",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        withdraw.place(x=110, y=370)

        deposit = tk.Button(frame3,text="CASH DEPOSIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame5))
        deposit.place(x=110, y=490)

        check_balance = tk.Button(frame3,text="CHECK BALANCE", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame6))
        check_balance.place(x=110, y=610)

        mini_statement = tk.Button(frame3,text="MINI STATEMENT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame7))
        mini_statement.place(x=110, y=730)

        change_pin = tk.Button(frame3,text="CHANGE PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        change_pin.place(x=1250, y=370)

        forgot_pin = tk.Button(frame3,text="FORGOT PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command= lambda:show_frame(frame4))
        forgot_pin.place(x=1250, y=490)

        green_pin = tk.Button(frame3,text="GREEN PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        green_pin.place(x=1250, y=610)

        exit_button = tk.Button(frame3,text="EXIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame1))
        exit_button.place(x=1250, y=730)

    elif my_password.get() == '3015':
        my_password.set('')
        incorrect_password_label['text']=''
        password_label.forget()
        password_entry_box.destroy()
        button_1.destroy()
        button_2.destroy()
        button_3.destroy()
        button_4.destroy()
        button_5.destroy()
        button_6.destroy()
        button_7.destroy()
        button_8.destroy()
        button_9.destroy()
        button_0.destroy()
        button_clear.destroy()
        enter_button.destroy()

        name = tk.Label(frame3,text = 'WELCOME MR VISHAL B',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',40)).place(x = 100,y = 200)
        verify =  tk.Label(frame3,text = 'SELECT ANY ONE',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',50)).place(x = 600,y = 500)

        withdraw = tk.Button(frame3,text="CASH WITHDRAWAL",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        withdraw.place(x=110, y=370)

        deposit = tk.Button(frame3,text="CASH DEPOSIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame5))
        deposit.place(x=110, y=490)

        check_balance = tk.Button(frame3,text="CHECK BALANCE", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame6))
        check_balance.place(x=110, y=610)

        mini_statement = tk.Button(frame3,text="MINI STATEMENT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame7))
        mini_statement.place(x=110, y=730)

        change_pin = tk.Button(frame3,text="CHANGE PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        change_pin.place(x=1250, y=370)

        forgot_pin = tk.Button(frame3,text="FORGOT PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command= lambda:show_frame(frame4))
        forgot_pin.place(x=1250, y=490)

        green_pin = tk.Button(frame3,text="GREEN PIN",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame4))
        green_pin.place(x=1250, y=610)

        exit_button = tk.Button(frame3,text="EXIT", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame1))
        exit_button.place(x=1250, y=730)

    else:
        incorrect_password_label['text']='Incorrect Password'

incorrect_password_label = tk.Label(frame3,text='',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',55),height = 2000,width = 500,anchor='n')
incorrect_password_label.pack(fill='both',expand=True)

def add_digit(digit):
    password_entry_box.insert(tk.END, digit)
    
# Function to clear the input field
def clear_my_password():
    password_entry_box.delete(0, tk.END)


button_1 = tk.Button(frame3, text="1",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8" ,command=lambda: add_digit("1"))
button_1.place (x = 600,y = 350)
button_2 = tk.Button(frame3, text="2",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("2"))
button_2.place (x = 680,y = 350)
button_3 = tk.Button(frame3, text="3", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command=lambda: add_digit("3"))
button_3.place (x = 760,y = 350)
button_4 = tk.Button(frame3, text="4",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("4"))
button_4.place (x = 600,y = 450)
button_5 = tk.Button(frame3, text="5",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("5"))
button_5.place (x = 680,y = 450)
button_6 = tk.Button(frame3, text="6", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command=lambda: add_digit("6"))
button_6.place (x = 760,y = 450)
button_7 = tk.Button(frame3, text="7", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command=lambda: add_digit("7"))
button_7.place (x = 600,y = 550)
button_8 = tk.Button(frame3, text="8",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("8"))
button_8.place (x = 680,y = 550)
button_9 = tk.Button(frame3, text="9",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("9"))
button_9.place (x = 760,y = 550)
button_0 = tk.Button(frame3, text="0",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command=lambda: add_digit("0"))
button_0.place (x = 600,y = 650)

button_clear = tk.Button(frame3, text="C", font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8",command=clear_my_password)
button_clear.place (x = 760,y = 650)

enter_button = tk.Button(frame3,text="ENTER",font = ("TT Prosto Sans Trl Cnd Black",40),bg = "#2b07e0",fg = "#e4e3e8",command=check_password,relief='raised')
enter_button.place (x = 900,y = 450)

#**************************************************************************FRAME 4**************************************************************************

amount_title = tk.Label(frame4,text = 'ENTER AMOUNT',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 650,y = 150)
amount = tk.Entry(frame4,width = 20,font = ('Arial' ,40), borderwidth = 3,)
amount.pack(padx = 200,pady = 300)

def withdraw():
    
    cash = int(amount.get())
    global current_balance
    current_balance -= cash
    print_withdraw = "YOU HAVE WITHDRAWN ₹{}".format(cash)
    new_amount = "YOUR BALANCE ₹{}".format(current_balance)

    print_amount =  tk.Label(frame4,text = print_withdraw,bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 450,y = 450)
    print_balance =  tk.Label(frame4,text = new_amount,bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 550,y = 550)
    
take_cash = tk.Button(frame4, text="ENTER",font = ("TT Prosto Sans Trl Cnd Black",40),bg = "#2b07e0",fg = "#e4e3e8", command= withdraw)
take_cash.place (x = 600,y = 650)

exit_btn = tk.Button(frame4, text="EXIT",font = ("TT Prosto Sans Trl Cnd Black",40),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame2))
exit_btn.place (x = 900,y = 650)

#**************************************************************************FRAME 5**************************************************************************

deposit_title = tk.Label(frame5,text = 'ENTER AMOUNT',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 650,y = 150)
deposit_amount = tk.Entry(frame5,width = 20,font = ('Arial' ,40), borderwidth = 3,)
deposit_amount.pack(padx = 200,pady = 300)

def deposit():    
    cash = int(deposit_amount.get())
    global current_balance
    current_balance += cash
    print_deposit = "YOU HAVE DEPOSITED ₹{}".format(cash)
    new_amount = "YOUR BALANCE ₹{}".format(current_balance)

    print_amount =  tk.Label(frame5,text = print_deposit,bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 450,y = 450)
    print_balance =  tk.Label(frame5,text = new_amount,bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 550,y = 550)
    
take_cash = tk.Button(frame5, text="ENTER",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= deposit)
take_cash.place (x = 600,y = 650)

exit_btn = tk.Button(frame5, text="EXIT",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame2))
exit_btn.place (x = 900,y = 650)

deposit_title = tk.Label(frame5,text = 'ENTER AMOUNT',bg = '#C1C1FF',fg = '#3C3CB3',font = ('TT Prosto Sans Trl Cnd Black',35)).place(x = 650,y = 150)  





def update_frame():
    take_cash = tk.Button(frame7, text="ENTER TO PROCEED",font = ("TT Prosto Sans Trl Cnd Black",30),bg = "#2b07e0",fg = "#e4e3e8", command= lambda:show_frame(frame3))
    take_cash.place (x = 600,y = 650)



#####Loading Data from txt file
def loading_data():
    file=open('data.txt','r',encoding='utf-8')
    data=json.load(file)
    file.close()
    return data
##Saving Data to .txt file
def saving_data(data):
    file=open('data.txt','w',encoding='utf-8')
    json.dump(data,file,ensure_ascii=False)
    file.close()

##saving data in a variable
#data=dict()
data=loading_data()
print(data)







#HEADINGS
login_label= tk.Label(frame7, text="Login Here" ,bg="gray"  ,fg="white"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
login_label.place(x=250, y=120)

reg_label= tk.Label(frame7, text="Register Here" ,bg="gray"  ,fg="white"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
reg_label.place(x=1000, y=120)

msg_label=tk.Label(frame7,text="Notification: ",bg='grey' ,fg='white',width=10,height=1,font=('times',15,'bold'))
msg_label.place(x=600,y=500)
message = tk.Label(frame7,text="",bg="Grey" ,fg="white", width=30, height=1, font=('times',15,'bold'))
message.place(x=750,y=500)


global txt
global txt2
#Login FIEDLS

lbl = tk.Label(frame7, text="Enter ID :",width=10,height=1  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl.place(x=250, y=210)

txt = tk.Entry(frame7,width=25  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt.place(x=450, y=210)

lbl2= tk.Label(frame7, text="Enter Password :",width=15  ,height=1  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl2.place(x=250, y=250)

txt2 = tk.Entry(frame7,width=25  ,bg="yellow" ,show='*',fg="red",font=('times', 15, ' bold '))
txt2.place(x=450, y=250)




#Register Fields

lbl3 = tk.Label(frame7, text="Enter ID :",width=10  ,height=1  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl3.place(x=1000, y=213)

txt3 = tk.Entry(frame7,width=25  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt3.place(x=1200, y=213)

lbl4= tk.Label(frame7, text="Enter Password",width=15  ,height=1  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl4.place(x=1000, y=250)

txt4 = tk.Entry(frame7,width=25  ,bg="yellow" ,show='*',fg="red",font=('times', 15, ' bold '))
txt4.place(x=1200, y=250)

lbl5= tk.Label(frame7, text="Enter Name",width=15  ,height=1  ,fg="red"  ,bg="yellow" ,font=('times', 15, ' bold ') ) 
lbl5.place(x=1000, y=275)

txt5 = tk.Entry(frame7,width=25  ,bg="yellow" ,fg="red",font=('times', 15, ' bold '))
txt5.place(x=1200, y=275)

#Main

def login_clear():
    txt.delete(0,'end')
    txt2.delete(0,'end')
    #res = ""
    #txt.configure(text= res)
    #txt2.configure(text=res)
def reg_clear():
    txt3.delete(0,'end')
    txt4.delete(0,'end')
    txt5.delete(0,'end')
    #res = ""
    #txt3.configure(text= res)
    #txt4.configure(text=res)



################## Login_Functions   ######################

#When Submit button is clicked We have to Track the Person from our data through web cam
    
def TrackImages(UserId):
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df=pd.read_csv("Details\Details.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX          
    run_count=0;run=True
    while run:
        
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print(Id, conf)
            if(conf < 50):
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                if (str(Id)==UserId):
                    message.configure(text="Face Recognized Successfully")
                    run=False
                    root.after(3000, update_frame)
                    
            else:
                Id='Unknown'                
                tt=str(Id)            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        run_count += 1    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q') or run_count==150):
            message.configure(text="Unable to Recognise Face")
            break
    
    cam.release()
    cv2.destroyAllWindows()
    


def login_submit():
    a=txt.get()
    b=txt2.get()
    if (a in data):
        if(data[a] == b):
            TrackImages(a)
        else:
            message.configure(text="Id and Password does not Match")
    else:
        message.configure(text="Entered Id does not Exists")

    login_clear()

################## Register_Functions   ######################


def TakeImages():        
    Id=(txt3.get())
    name=(txt4.get())
    per = (txt5.get())
    ret=0
    if (Id not in data):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +'.'+Id+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>100:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('Details\Details.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
        ret=1
    else:
        res = "User name Already Exists...Try another one!!!"
        message.configure(text= res)
    return ret

# Training Images

def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    #print(faces,np.array(Id))
    #res = "Image Trained"#+",".join(str(f) for f in Id)
    res="Registration Successful"
    message.configure(text= res)
    return True
    

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image path  s and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

pwd = txt4.get()
def reg_submit():
    Userid=txt3.get()

    if Userid.isdigit():
        if TakeImages()==1:
            if TrainImages():
                data[txt3.get()] = txt4.get()
                data[txt4.get()] = txt5.get()
                saving_data(data)
            else:
                pass
    
    else:
        message.configure(text="User Id Should contain number only!!!")
    reg_clear()
    print(data)





#Login Actions
submit = tk.Button(frame7, text="Submit",fg="red",command= login_submit, bg="yellow"  ,width=25  ,height=1 ,activebackground = "Red" ,font=('times', 10, ' bold '))
submit.place(x=250, y=300)

clearButton = tk.Button(frame7, text="Clear",fg="red", command=login_clear,bg="yellow"  ,width=25  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
clearButton.place(x=500, y=300)

#Register Actions
submit2 = tk.Button(frame7, text="Submit",fg="red", command=reg_submit, bg="yellow"  ,width=25  ,height=1 ,activebackground = "Red" ,font=('times', 10, ' bold '))
submit2.place(x=1000, y=300)

clearButton2 = tk.Button(frame7, text="Clear",command=reg_clear, fg="red"  ,bg="yellow"  ,width=25  ,height=1, activebackground = "Red" ,font=('times', 10, ' bold '))
clearButton2.place(x=1250, y=300)



show_frame(frame1)

root.mainloop()

















