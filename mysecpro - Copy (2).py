#Three-Level password authentication system

from tkinter import*
from PIL import ImageTk,Image
import ttkcalendar
import tkSimpleDialog
from tkinter import messagebox as msg 
import sqlite3 
from twilio.rest import Client
import time
import smtplib
import pyotp
import random as r
import time
import string
from random import *


class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

root =Tk()
root.title("Security Authentication system")
root.geometry("1366x768")
frame = Frame(width=1366,height=768)
frame.place(x=0,y=0)
#main page
def main(root,frame):
    
    img = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\securityservice123.jpg"))
    L1=Label(frame,image=img)
    L1.place(x=0,y=0)
    L1=Label(frame,text="Three-Level Password Authentication System",width = 90,height = 3,background = 'skyblue4',
             font = ("algerian",18,'bold'),borderwidth=10,relief="raised")
    L1.place(x=0,y=0)

    B1=Button(frame,text="REGISTER",width = 10,fg="black",bg = "skyblue4",bd=10,
              font = ("algerian",20,'bold'),command =lambda:register(root,frame))
    B1.place(x=360,y=220)

    B2=Button(frame,text="LOGIN",width = 10,fg="black",bg = "skyblue4",bd = 10,
              font = ("algerian",20,'bold'),command =lambda:login(root,frame))
    B2.place(x=120,y=220)
    frame.mainloop()
#register page
def register(root,frame):
    #Create Table for database
    conn = sqlite3.connect('projectdatabase.db')
    conn.execute('''create table if not exists security(First_name TEXT NOT NULL,Last_name TEXT NOT NULL,Username TEXT NOT NULL,Password TEXT NOT NULL,Email TEXT NOT NULL, Mobile int(10) NOT NULL,Gender TEXT NOT NULL,Dob TEXT NOT NULL,City TEXT NOT NULL);''')
    
    

    def getdate(frame):
        cd = CalendarDialog(frame)
        result = cd.result
        selected_date.set(result.strftime("%d-%m-%Y"))
    frame.destroy()
    frame = Frame(width=1366,height=768)
    frame.place(x=0,y=0)
    img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\guiimages\\pp.jpeg"))
    L2 = Label(frame,image=img1)
    L2.place(x=0,y=0)

    L2 = Label(frame,text = "REGISTRATION",width = 32,height= 1,bd = 3,background = 'grey86',
               font = ("algerian",20,'bold'),borderwidth=10, relief="ridge", highlightcolor="black")
    L2.place(x=690,y=30)
    
    def nextb(root,frame,E6):
        txt1 = E1.get()
        print(txt1)

        txt2 = E2.get()
        print(txt2)

        global txt3
        txt3 = E3.get()
        print(txt3)

        txt4 = E4.get()
        print(txt4)

        global txt5
        txt5 = E5.get()
        print(txt5)

        txt6 = E6.get()
        print(txt6)

        txt7 = var.get()
        print(txt7)

        txt8 = E8.get()
        print(txt8)

        txt9 = c.get()
        print(txt9)
        
        if txt1 == 'Enter First Name' or txt2 == 'Enter Last name' or txt3 == 'Enter Username' or txt4 == 'Enter Password' or txt5 == 'Enter Email Id' or txt6 == 'Enter Mobile No' or txt7 == '' or txt8 == 'dd-mm--yyyy' or txt9 == '' :
            print('all fields are required')
            msg.showwarning('Warning!','All the details are required!')
            #register(root,frame)
            return
        
        ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
        print(ans)
        if ans=="no":
            print('no pressed')
            register(root,frame)
                
        elif ans=='yes':
            print("yes proceed")
            msg.showinfo('successful','successfully registered.')
            after_nextb(root,frame,txt6)
                    
                #Insert table for database
            conn = sqlite3.connect('projectdatabase.db')
            conn.execute('''INSERT INTO security(First_name,Last_name,Username,Password,Email,Mobile,Gender,Dob,City)\
            VALUES('%s','%s','%s','%s','%s',%d,'%s','%s','%s')''' %(txt1,txt2,txt3,txt4,txt5,int(txt6),txt7,txt8,txt9))
            
                
            
            
                #fetch table
            cursor = conn.execute("select * from security")
                    
            for row in cursor:
                print('First_name = ',row[0])
                print('Last_name = ',row[1])
                print('Username = ',row[2])
                print('Password = ',row[3])
                print('Email = ',row[4])
                print('Mobile = ',row[5])
                print('gender = ',row[6])
                print('Dob = ',row[7])
                print('City = ',row[8])
                                
            conn.commit()
            conn.close()
        
        

    L1=Label(frame,text = "First Name",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge") 
    L1.place(x=690,y=100)

    L2=Label(frame,text = "Last Name",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L2.place(x=690,y=150)

    L3=Label(frame,text = "Username",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L3.place(x=690,y=200)

    L4=Label(frame,text = "Password",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L4.place(x=690,y=250)

    L5=Label(frame,text = "Email Id",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L5.place(x=690,y=300)

    L6=Label(frame,text = "Mobile No",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L6.place(x=690,y=350)

    L7=Label(frame,text = "Gender",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L7.place(x=690,y=400)
    
    L8=Label(frame,text = "Date Of Birth",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L8.place(x=690,y=450)

    L9=Label(frame,text = "City",bg = 'light yellow',width = 20,
             font =("times new roman",18,'bold'),borderwidth=4, relief="ridge")
    L9.place(x=690,y=500)
    #entry
    ########################################
    def oncli(event):
        E1.delete(0,END)
        E1.config(fg='black')
    
    E1=Entry(frame,bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E1.place(x=1040,y=100)
    E1.insert(END,'Enter First Name')
    E1.config(fg='grey')
    E1.bind('<Button-1>',oncli)
    ########################################

    def oncli(event):
        E2.delete(0,END)
        E2.config(fg='black')
        
    E2=Entry(frame,bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E2.place(x=1040,y=150)
    E2.insert(END,'Enter Last name')
    E2.config(fg='grey')
    E2.bind('<Button-1>',oncli)
    
    def oncli(event):
        E3.delete(0,END)
        E3.config(fg='black')
        

    def mat(event):
        txt3=E3.get()
        conn = sqlite3.connect('projectdatabase.db')
        cursor = conn.execute('SELECT Username from security')
            
        for i in cursor:
            if i[0]==txt3:
                print(i[0])
                print('Username already taken')
                ans = msg.showwarning('Try again','Username already taken.')
                break
                
        conn.close()
        
    E3=Entry(frame,bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E3.place(x=1040,y=200)
    E3.insert(END,'Enter Username')
    E3.config(fg='grey')
    E3.bind('<Button-1>',oncli)
    E3.bind('<Leave>',mat)
    
    def oncli(event):
        E4.delete(0,END)
        E4.config(fg='black')
    def onenter(event):
        E4.config(show='')
    def onleave(event):
        E4.config(show='*')
    
    E4=Entry(frame,show="*",bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E4.place(x=1040,y=250)
    E4.insert(END,'Enter Password')
    E4.config(fg='grey')
    photo0 = PhotoImage(file = r"C:\\Users\\HP\Desktop\\guiimages\\download1.png")
    B4=Button(frame,text="Show",image = photo0,width = 50,height=27,fg="black",bg = "grey",font = ("arial black",10,'bold'),
             borderwidth=4, relief="raised",command = lambda:onenter(event))
    B4.place(x=1230,y=250)
    E4.bind('<Button-1>',oncli)
    B4.bind('<Enter>',onenter)
    B4.bind('<Leave>',onleave)

    def oncli(event):
        E5.delete(0,END)
        E5.config(fg='black')
    E5=Entry(frame,bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E5.place(x=1040,y=300)
    E5.insert(END,'Enter Email Id')
    E5.config(fg='grey')
    E5.bind('<Button-1>',oncli)
    
    def oncli(event):
        E6.delete(0,END)
        E6.config(fg='black')
    E6=Entry(frame,bg = 'antique white',width = 20,font =("times new roman",17,'bold'),bd=4)
    E6.place(x=1040,y=350)
    E6.insert(END,'Enter Mobile No')
    E6.config(fg='grey')
    E6.bind('<Button-1>',oncli)

    

    var = StringVar()
    var.set(0)
    Radiobutton(frame,text = "Male",fg ='black',font = ('bold',14),variable = var,value='Male',
                borderwidth=4,width =7 ,relief="sunken").place(x=1040,y=400)
    Radiobutton(frame,text = "Female",fg ='black',font = ('bold',14),variable = var,value='Female',
                borderwidth=4,width =7, relief="sunken").place(x=1176,y=400)
    selected_date= StringVar()
    date=StringVar()

    def oncli(event):
        E8.delete(0,END)
        E8.config(fg='black')

    E8=Entry(frame,bg = 'antique white',textvariable=selected_date,width = 20,font =("times new roman",17,'bold'),bd=4)
    E8.place(x=1040,y=450)
    E8.insert(END,'dd-mm--yyyy')
    E8.config(fg='grey')
    E8.bind('<Button-1>',oncli)
    
    b1=Button(frame,text='--Select--',font = ('bold',13),command=lambda:getdate(frame),width=9,borderwidth=3, relief="sunken")
    b1.place(x=1195,y=450)
    list1 = {'Jaipur','Surat','Pune','Ahemdabad','Hyderabad','Banglore','Chennai','New Delhi','Mumbai','Kolkata'} #can be used[]/()
    c= StringVar()
    droplist=OptionMenu(frame,c,*list1)
    droplist.config(width =19,font = ('bold',15))
    c.set("--select your city--")
    droplist.place(x=1040,y=500)
    
    
    #next button
    B3=Button(frame,text="NEXT",width = 23,fg="black",bg = "lime green",bd=5,font = ("arial black",13,'bold'),
              command = lambda:nextb(root,frame,E6))
    B3.place(x=690,y=570)
    #B3.bind('<Button-1>',find)

    #reset button
    B44=Button(frame,text="RESET",width = 20,fg="black",bg = "lime green",bd=5,font = ("arial black",13,'bold'),
              command = lambda:reset(root,frame))
    B44.place(x=1040,y=570)
    
    #back button
    B4=Button(frame,text="BACK",width = 9,fg="black",bg = "grey86",font = ("arial black",15,'bold'),
              borderwidth=10, relief="raised",command = lambda:back(root,frame))
    B4.place(x=0,y=40)
    #login button
    B4=Button(frame,text="LOGIN",width = 9,fg="black",bg = "grey86",font = ("arial black",15,'bold'),borderwidth=10,
              relief="raised",command = lambda:login(root,frame))
    B4.place(x=0,y=120)
    root.mainloop()



    

def back(root,frame):    
    main(root,frame)
   




def login(root,frame):
    def levellogin1(root,frame):
        global txt3
        txt3=E3.get()
        txt4=E4.get()
        conn = sqlite3.connect('projectdatabase.db')
        cursor = conn.execute('SELECT Username,Password from security')
        for row in cursor:
            if row[0]==txt3 and row[1]==txt4:
                print('Login successful')
                ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
                print(ans)
                if ans=="yes":
                    print("yes proceed")
                    after_levellogin1(root,frame,txt3,txt4)
                else:
                    print("no proceed")
                    login(root,frame)
                conn.close()
                return   #you can use function too
        else:
            print('Invalid login details')
            msg.showwarning('login failed','invalid username or password')
            login(root,frame)
            conn.close()
    
    frame.destroy()
    frame = Frame(width=1366,height=768)
    frame.place(x=0,y=0)
    img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\23.jpg"))
    L91 = Label(frame,image = img2)
    L91.place(x=0,y=0)
    
    #label
    L10=Label(frame,text = "Username",bg = 'light yellow',width = 15,font =("times new roman",19,'bold'),
              borderwidth=6, relief="raised")
    L10.place(x=120,y=480)

    L11=Label(frame,text = "Password",bg = 'light yellow',width = 15,font =("times new roman",19,'bold'),
              borderwidth=6, relief="raised")
    L11.place(x=120,y=550)
    #entry
    E3 = Entry(frame,width = 19,font =("times new roman",18,'bold'),bd=5,relief="raised")
    E3.place(x=400,y=480)
    

    E4 = Entry(frame,show = "*",width = 19,font =("times new roman",18,'bold'),bd=5,relief="raised")
    E4.place(x=400,y=550)
    #login button
    B=Button(frame,text="CONTINUE",width = 10,fg="black",bg = "medium turquoise",font = ("arial black",12,'bold'),
             borderwidth=8, relief="raised",command = lambda:levellogin1(root,frame))
    B.place(x=700,y=510)
    #forgot password
    B=Button(frame,text="Forgot Password?",fg = "red",width = 16,bg = 'light yellow',font = ("arial black",12,'bold','underline'),
             relief="raised",command = lambda:forgot_password(root,frame))
    B.place(x=420,y=620)
    
    B=Button(frame,text="Change Password?",fg = "red",width = 16,bg = 'light yellow',font = ("arial black",12,'bold','underline'),
             relief="raised",command = lambda:change_password(root,frame))
    B.place(x=150,y=620)
    #back button
    B4=Button(frame,text="BACK",width = 9,fg="black",bg = "grey86",font = ("arial black",15,'bold'),
              borderwidth=10, relief="raised",command = lambda:back(root,frame))
    B4.place(x=0,y=40)
    #register button
    B4=Button(frame,text="REGISTER",width = 9,fg="black",bg = "grey86",font = ("arial black",15,'bold'),
              borderwidth=10, relief="raised",command = lambda:register(root,frame))
    B4.place(x=0,y=120)
        
        
        
    frame.mainloop()



def change_password(root,frame):
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img10 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\2345.jpg"))
    L81 = Label(frame,image = img10)
    L81.place(x=0,y=0)
    #table created
    conn = sqlite3.connect('projectdatabase.db')
    conn.execute('''create table if not exists match(Username TEXT NOT NULL,old_password TEXT NOT NULL,new_password TEXT NOT NULL,confirm_password TEXT NOT NULL);''')
    

    def reset_password(root,frame):
        global txt101
        global txt102
        global txt100
        txt100 = E49.get()
        print(txt100)
        
        txt101 = E50.get()
        print(txt101)

        txt102 = E51.get()
        print(txt102)

            
        txt103 = E52.get()
        print(txt103)
        
        if txt100=='' or txt101=='' or txt102=='' or txt103=='':
            print('all fields are required')
            msg.showwarning('title','Enter password!')
            #register(root,frame)
        else:
            ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
            print(ans)
            
            if ans=="no":
                print('no pressed')
                change_password(root,frame)
                    
            elif ans=='yes':
                print("yes proceed")
                msg.showinfo('title','Updated successfully.')
                login(root,frame)
                #Insert table for database
                conn = sqlite3.connect('projectdatabase.db')
                conn.execute('''INSERT INTO match VALUES(?,?,?,?)''' ,[txt100,txt101,txt102,txt103])
                conn.execute('''Update security set Password= "%s" where Password= "%s" AND Username="%s"'''%(txt102,txt101,txt100))

                cursor = conn.execute("select * from match")
                    
                for row in cursor:
                    print('Username = ',row[0])
                    print('old_password = ',row[1])
                    print('new_password = ',row[2])
                    print('confirm_password = ',row[3])
                        
                conn.commit()
                #conn.close()
        
    


    
    
    L89=Label(frame,text = "| Reset your P***w**d |",bg = 'lime green',width = 18,fg='black',
             font =("times new roman",22,'bold'),borderwidth=4,relief="raised")
    L89.place(x=525,y=330)

    L49=Label(frame,text = "Enter Username :",bg = 'light grey',width = 20,
             font =("times new roman",18,'bold'),borderwidth=5,relief="raised")
    L49.place(x=345,y=410)

    L50=Label(frame,text = "Enter old Password :",bg = 'light grey',width = 20,
             font =("times new roman",18,'bold'),borderwidth=5,relief="raised")
    L50.place(x=345,y=470)
    
    L51=Label(frame,text = "Create new Password :",bg = 'light grey',width = 20,
             font =("times new roman",18,'bold'),borderwidth=5,relief="raised")
    L51.place(x=345,y=530)
    L52=Label(frame,text = "Confirm Password* :",bg = 'light grey',width = 20,
             font =("times new roman",18,'bold'),borderwidth=5,relief="raised")
    L52.place(x=345,y=590)

    #entry

    E49 = Entry(frame,show = "*",width = 23,font =("times new roman",18,'bold'),bd=4,relief="raised")
    E49.place(x=670,y=410)
    
    def onenter(event):
        E50.config(show='')
    def onleave(event):
        E50.config(show='*')
    E50 = Entry(frame,show = "*",width = 18,font =("times new roman",18,'bold'),bd=4,relief="raised")
    E50.place(x=670,y=470)
    #######
    photo1 = PhotoImage(file = "C:\\Users\\HP\Desktop\\guiimages\\download1.png")
    B50=Button(frame,text="Show",image = photo1,width = 50,height=27,fg="black",bg = "grey",font = ("arial black",10,'bold'),
             borderwidth=4, relief="raised",command = lambda:onenter(event))
    #######
    B50.place(x=895,y=470)
    B50.bind('<Enter>',onenter)
    B50.bind('<Leave>',onleave)
    
    def onenter(event):
        E51.config(show='')
    def onleave(event):
        E51.config(show='*')
    photo2 = PhotoImage(file = "C:\\Users\\HP\Desktop\\guiimages\\download1.png")
    E51 = Entry(frame,show = "*",width = 18,font =("times new roman",18,'bold'),bd=4,relief="raised")
    E51.place(x=670,y=530)
    B51=Button(frame,text="Show",image = photo2,width = 50,height=27,fg="black",bg = "grey",font = ("arial black",10,'bold'),
             borderwidth=4, relief="raised",command = lambda:onenter(event))
    B51.place(x=895,y=530)
    B51.bind('<Enter>',onenter)
    B51.bind('<Leave>',onleave)

    def onenter(event):
        E52.config(show='')
    def onleave(event):
        E52.config(show='*')
    photo3 = PhotoImage(file = "C:\\Users\\HP\Desktop\\guiimages\\download1.png")
    E52 = Entry(frame,show = "*",width = 18,font =("times new roman",18,'bold'),bd=4,relief="raised")
    E52.place(x=670,y=590)
    B52=Button(frame,text="Show",image = photo3,width = 50,height=27,fg="black",bg = "grey",font = ("arial black",10,'bold'),
             borderwidth=4, relief="raised",command = lambda:onenter(event))
    B52.place(x=895,y=590)
    B52.bind('<Enter>',onenter)
    B52.bind('<Leave>',onleave)
    
    #button
    B53=Button(frame,text="SUBMIT",width = 12,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:reset_password(root,frame))
    B53.place(x= 700,y=640)
    B53=Button(frame,text="BACK",width = 12,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:login(root,frame))
    B53.place(x= 450,y=640)
        

    frame.mainloop()


    



########################################################################################################################################    
      
def forgot_password(root,frame):
    
    def send_password(E40,root,frame):
        
        txt40 = E40.get()
        print(txt40)
        conn = sqlite3.connect('projectdatabase.db')
        abc=conn.execute('''SELECT Password from security where Email = "%s"'''%(txt40))
        for i in abc:
            passw=i[0]
            
        if txt40=='':  
            print('cannot sent')
            msg.showwarning('warning','Enter Mail.')
            return
        elif txt40!='':
            sender = "salonidad6@gmail.com"
            characters = string.ascii_letters + string.punctuation  + string.digits
            pwd =  "".join(choice(characters) for x in range(randint(8,16)))
            message1="Here is your default password , Please login with this password to continue.\n\n"
            message2="\n\nTHANK YOU"
            ct=message1+str(pwd)+message2
            receiver="salonimaheshwari903@gmail.com"
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login("salonidad6@gmail.com", "$*Dad70@#123")
            mail.sendmail(sender,receiver,ct)
            print(pwd)
            print('mail sent successfully')
            mail.close()
            print('code is done')
            ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
            print(ans)
            if ans=="yes": 
                print("yes proceed")
                msg.showinfo('Success','Your default password has been sent on your entered Mail-Id.')
                #Insert table for database
                conn = sqlite3.connect('projectdatabase.db')
                conn.execute('''Update security set Password= "%s" where Password= "%s"'''%(ct,passw))
                #conn.commit()
                
            else:
                print("no proceed")
                forgot_password(root,frame)
            
        '''else:
            print('Invalid')
            msg.showwarning('failed','invalid Mail-Id.')
            forgot_password(root,frame) '''
        
############################################################################################################################################
    
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img6 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\12.jpg"))
    L31 = Label(frame,image = img6)
    L31.place(x=0,y=0)
    L81=Label(frame,text = "Forgot your Password?",bg = 'lightsalmon2',width = 20,fg='black',
             font =("times new roman",20,'bold'),borderwidth=4,relief="raised")
    L81.place(x=500,y=50)
    L82=Label(frame,text = "Check your mail inbox\n for new password",bg = 'azure3',width = 25,fg='black',
             font =("times new roman",18,'italic'),borderwidth=4,relief="raised")
    L82.place(x=500,y=130)
    
    #label
    L40=Label(frame,text = "Enter Email :",bg = 'light grey',width = 22,
             font =("times new roman",20,'bold'),borderwidth=5,relief="raised")
    L40.place(x=290,y=230)
    #entry
    E40 = Entry(frame,width = 22,font =("times new roman",22,'bold'),bd=4,relief="raised")
    E40.place(x=680,y=230)
    B55=Button(frame,text="SUBMIT",width = 12,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:send_password(E40,root,frame))
    B55.place(x= 710,y=350)
    B56=Button(frame,text="BACK",width = 12,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:login(root,frame))
    B56.place(x= 480,y=350)
    
    frame.mainloop()
    
    
def reset(root,frame):    
    register(root,frame)


def after_levellogin1(root,frame,txt3,txt4):
    def eml(e):
        sender = "salonidad6@gmail.com"
        global content
        #Your Login-OTP is here \n
        content= r.randint(1000,10000)
        message1="Here is your one-time passcode \n\n"
        message2 = """\n\nEnter the code in the web page where you requested it.\n\nNOTE: This one-time passcode expires in 90 seconds after it was requested."""
        ct=message1+str(content)+message2
        receiver = e
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login("salonidad6@gmail.com", "$*Dad70@#123")
        mail.sendmail(sender,receiver,ct)
        print(content)
        global t1
        t1=time.perf_counter()
        mail.close()

    def verify(root,frame):
        global content
        print('iam in this',end='')
        print(content)
        txt94 = E94.get()
        print(txt94)
        if txt94=='':
            print('code is required')
            msg.showinfo('warning','Enter the verification code.')
            return
        
        
        elif txt94==str(content):
            global t1
            print(t1)
            t2=time.perf_counter()
            if(t2-t1>=89):
                msg.showwarning('Title','Code Expires')
            else:

                print('code is done')
                ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
                print(ans)
                if ans=="yes": 
                    print("yes proceed")
                    msg.showinfo('Success','Verification successful.')
                    after_verify(root,frame)
                else:
                    print("no proceed")
                    after_levellogin1(root,frame,txt3,txt4) 
        else:
            print('Invalid')
            msg.showwarning('Verification failed','invalid verification code.')
            after_levellogin1(root,frame,txt3,txt4) 

        
    conn = sqlite3.connect('projectdatabase.db')
    cursor = conn.execute('SELECT Email from security where username = "%s" and Password = "%s"'%(txt3,txt4))  
    e=cursor.fetchall()[0][0]
    print(e)
    print(type(e))
        
                
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\abstract-data-security-background-with-key-vector-176206622211.jpg"))
    L92 = Label(frame,image = img3)
    L92.place(x=0,y=0)

    img12 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\simple1.png"))
    L102=Label(frame,image=img12)
    L102.place(x=250,y=70)

    B93 = Button(frame,text = "| LOGIN - OTP |",width = 15,height= 2,bd = 3,background = 'medium turquoise',
                font = ("arial black",15,'bold'),borderwidth=8, relief="raised",highlightcolor="black",command = lambda:eml(e))
    B93.place(x=30,y=70)
    #B93.bind('<Button-1>',pqr)

    L93 = Label(frame,text = "Kindly enter OTP received on your Gmail account\n below to login",width = 50,
                height= 2,bd = 3,background = 'azure3',font = ("arial",15,'bold'),borderwidth=3,
                relief="raised",highlightcolor="black")
    L93.place(x=30,y=170)
    
    L94=Label(frame,text = "Enter code",bg = 'azure3',width = 10,font =("times new roman",22,'bold'),
              borderwidth=6, relief="raised")
    L94.place(x=60,y=280)
    E94 = Entry(frame,width = 10,font =("times new roman",23,'bold'),bd=4,relief="raised")
    E94.place(x=300,y=280)
    #E94.bind('<Leave>',xyz)
    L95=Label(frame,text = "Expires in : ",bg = 'azure3',width = 13,font =("times new roman",15,'bold'),
              borderwidth=3, relief="raised")
    L95.place(x=60,y=350)
    
    B4=Button(frame,text="verify",width = 10,fg="black",bg = "medium turquoise",font = ("arial black",12,'bold'),
              borderwidth=5, relief="raised",
              command = lambda:verify(root,frame))
    B4.place(x=320,y=450)
    B4=Button(frame,text="Generate New OTP",width = 20,fg="black",bg = "medium turquoise",
              font = ("arial black",12,'bold'),borderwidth=5, relief="raised",
              command = lambda:eml(e))
    B4.place(x=270,y=525)
    frame.mainloop()



def after_verify(root,frame):

    def access(root,frame):
        global s
        txt19 = E19.get()
        print(txt19)

        if txt19=='':
            print('code is required')
            msg.showwarning('Warning!','Enter the verification code.')
            return
        elif txt19==s:
            print('successfully login')
            ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
            print(ans)
            if ans=="yes":
                    print("yes proceed")
                    msg.showinfo('Success','Login Successful.')
                    after_access(root,frame)
            else:
                print("no proceed")
                after_verify(root,frame)
            return  
        else:
            print('Invalid')
            msg.showwarning('login failed','Enter valid code.')
            after_verify(root,frame) 



            
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\hcpr-cyber-security1.jpg"))
    L95 = Label(frame,image = img4)
    L95.place(x=0,y=0)
    L96 = Label(frame,text = "| LOGIN |",width = 10,height= 2,bd = 3,background = 'lightskyblue3',
                font = ("arial black",15,'bold'),borderwidth=8, relief="raised",highlightcolor="black")
    L96.place(x=0,y=5)
    L96 = Label(frame,text = "CAPTCHA",width = 15,height= 2,bd = 3,background = 'lightskyblue3',
                font = ("arial black",15,'bold'),borderwidth=8, relief="raised",highlightcolor="black")
    L96.place(x=0,y=75)
    L11=Label(frame,text = "Click on GENERATE CAPTCHA \nand enter the text in a box \nfor successful login",bg = 'gray91',width = 29,font =("times new roman",16,'bold'),
              borderwidth=4, relief="groove",height=3)
    L11.place(x=20,y=160)
   
    B87=Button(frame,text="LOGIN  >>",width = 32,fg="black",bg = "indianred1",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:access(root,frame))
    B87.place(x=20,y=600)

    L19=Label(frame,text = "Text in the box:",bg = 'white',width = 12,font =("times new roman",16,'bold'),
              borderwidth=6, relief="groove")
    L19.place(x=20,y=500)
    
    E19 = Entry(frame,width = 12,font =("times new roman",22,'bold'),bd=5,relief="raised")
    E19.place(x=200,y=500)


        
    def cap():
        c.delete("all")

        h =[]
        for i in range(0,5):
            h.append(chr(r.randint(65,90)))
            #h1 = chr(r.randint(65,90))
        color = ["black","yellow","red","blue","green","purple4"]
        global s
        s=''

        fnt = ['Verdana','arial','papyrus',"Calibri",'algerian']
        t1 = c.create_text(50+r.randint(0,10),60+r.randint(0,10),text=h[0],font = fnt[r.randint(0,4)]+" 28 bold",fill=color[r.randint(0,5)])
        t2 = c.create_text(100+r.randint(0,10),60+r.randint(0,10),text=h[1],font = fnt[r.randint(0,4)]+" 28 bold",fill=color[r.randint(0,5)])
        t3 = c.create_text(150+r.randint(0,10),60+r.randint(0,10),text=h[2],font = fnt[r.randint(0,4)]+" 28 bold",fill=color[r.randint(0,5)])
        t4 = c.create_text(200+r.randint(0,10),60+r.randint(0,10),text=h[3],font = fnt[r.randint(0,4)]+" 28 bold",fill=color[r.randint(0,5)])
        t5 = c.create_text(250+r.randint(0,10),60+r.randint(0,10),text=h[4],font = fnt[r.randint(0,4)]+" 28 bold",fill=color[r.randint(0,5)])
        for i in h:
        
            s=s+i
        #print(s)
        for i in range(0,5):
            l= c.create_line(r.randint(5,295),r.randint(5,195),r.randint(5,295),r.randint(5,195)
                             ,fill = color[r.randint(0,5)],width = r.randint(1,3))

    #root = Tk()
    #root.geometry("300x250")

    c =Canvas(width = 370,height = 150,bg='lightskyblue3')

    #line1 = c.create_line(0,0,150,150,fill ='red',width =3)
    #line2 = c.create_line(50,75,225,75,fill ='blue',width =5)
    #line3 = c.create_line(50,50,50,275,fill ='green',width =2)


    b = Button(text = "GENERATE CAPTCHA",font ="Verdana 16 bold",width= 24,command = cap)
    b.place(x=20,y=405)
    c.place(x=20,y=250)
  
    
    frame.mainloop()


def otp(txt6):
        p=txt6
        print(p)
        totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
        account_sid = '###############################'
        auth_token = '################################'
        client = Client(account_sid, auth_token)
        
        message = client.messages \
                        .create(
                             body=("Mobile verification-OTP for three-level authentication: %s"%(totp.now())),
                             from_='+16174407715',
                             to= p   #'+918619637591'
                         )


        print('code has been sent.')
        print(message.body)
        global code
        code=totp.now()



def after_nextb(root,frame,txt6):
#################################################################################################################
    def Verify(root,frame):
        global code
        txt12 = E12.get()
        print(txt12)

        if txt12=='':
            print('code is required')
            msg.showwarning('Warning!','Enter the verification code.')
            return
        elif txt12==code:
            print('Login successful')
            ans = msg.askquestion('ask question','do you want to proceed?') #(title and msg)
            print(ans)
            if ans=="yes":
                    print("yes proceed")
                    msg.showinfo('Success','Successful.')
                    main(root,frame)
            else:
                print("no proceed")
                after_nextb(root,frame)
                #conn.close()
            return   
        else:
            print('Invalid')
            msg.showwarning('Verification failed','invalid verification code.')
            after_nextb(root,frame)
            #conn.close()
            
##################################################################################################################            
    
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\copy s.jpg"))
    L92 = Label(frame,image = img3)
    L92.place(x=0,y=0)

    img11 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\click12.png"))
    L101=Label(frame,image=img11)
    L101.place(x=10,y=65)
    
    L93 = Label(frame,text = "A text message with a verification code has \nbeen sent to your Mobile number\n\n Enter the code here:",width = 38,
                height= 4,bd = 3,background = 'azure3',font = ("arial",15,'bold'),borderwidth=3,
                relief="raised",highlightcolor="black")
    L93.place(x=100,y=150)
    #entry
    E12 = Entry(frame,width = 10,font =("times new roman",30,'bold'),bd=6,relief="raised")
    E12.place(x=220,y=320)

    L93 = Label(frame,text = "Didn't get a verification code?",width = 30,
                height= 1,bd = 3,background = 'azure3',font = ("arial",15,'bold'),borderwidth=3,
                relief="raised",highlightcolor="black")
    L93.place(x=160,y=400)
    #button
    B93=Button(frame,text="Send a new code",width = 15,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:otp(txt6))
    B93.place(x=100,y=500)

    B93=Button(frame,text="Verify",width = 12,fg="black",bg = "lime green",font = ("arial black",12,'bold'),
             borderwidth=5, relief="raised",command = lambda:Verify(root,frame))
    B93.place(x=410,y=500)

    L96 = Label(frame,text = "->> You cannot proceed further if your number didn't get verified.",width = 60,
                height= 1,bd = 3,background = 'azure3',font = ("arial black",16,'italic'),borderwidth=3,
                relief="raised",highlightcolor="black")
    L96.place(x=100,y=600)

    B95 = Button(frame,text = "| Verify your mobile number |",width = 32,height= 2,bd = 3,background = 'light slategrey',
                font = ("arial black",15,'bold'),borderwidth=5, relief="raised",highlightcolor="black",command = lambda:otp(txt6))
    B95.place(x=100,y=50)

    #you cannot proceed further if your number didnt get verified.
    #If your number is not verified, then you can not proceed.

    frame.mainloop()


    



#def Verify(root,frame):
 #   main(root,frame)


def after_access(root,frame):
    
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img6 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\P.jpg"))
    L85 = Label(frame,image = img6)
    L85.place(x=0,y=0)

    L84 = Label(frame,text = "| BANK TRANSACTION |",width = 95,height= 2,bd = 3,background = 'lightsteelblue1',fg = 'black',
                font = ("arial black",15,'bold'),borderwidth=4, relief="raised")
    L84.place(x=10,y=10)
    
    L96 = Label(frame,text = "now, You are authorized \nto access the \nBank Transaction",width = 28,
                height= 3,bd = 3,background = 'khaki1',fg = 'black',font = ("arial black",16,'italic','underline'),borderwidth=3,
                relief="raised")
    L96.place(x=920,y=200)
    
    B3=Button(frame,text="NEXT >>",width = 15,fg="black",bg = "lightsteelblue1",bd=5,font = ("arial black",15,'bold'),
              borderwidth= 4,command = lambda:access_next(root,frame))
    B3.place(x=1050,y=370)
    B3=Button(frame,text="LOGOUT",width = 10,fg="lightsteelblue1",bg = "black",bd=5,font = ("arial black",15,'bold'),
              borderwidth= 4,command = lambda:logout(root,frame))
    B3.place(x=1190,y=13)
    frame.mainloop()


def logout(root,frame):
    login(root,frame)  



def access_next(root,frame):
    frame.destroy()
    frame = Frame(width = 1366,height = 768)
    frame.place(x=0,y=0)
    img6 = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\Desktop\\guiimages\\m.jpg"))
    L85 = Label(frame,image = img6)
    L85.place(x=0,y=0)

    L84 = Label(frame,text = " THANK YOU ",width = 20,bd = 3,background = 'azure3',fg = 'midnightblue',
                font = ("arial black",38,'italic'),borderwidth=4, relief="raised")
    L84.place(x=330,y=610)
    B3=Button(frame,text="CLOSE",width = 14,fg="lightsteelblue1",bg = "black",bd=5,font = ("arial black",16,'bold'),
              borderwidth= 4,command = lambda:close(root,frame))
    B3.place(x=1090,y=620)

    frame.mainloop()



def close(root,frame):
    
    root.destroy()
    root.mainloop()
main(root,frame)   


