from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image

def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)

def close():
	win.destroy()	


def login():
	if user_name.get()=="" or password.get()=="":
		messagebox.showerror("Error","Enter User Name And Password",parent=win)	
	else:
		try:
			con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
			cur = con.cursor()

			cur.execute("select * from user_information where last_name=%s and password = %s",(user_name.get(),password.get()))
			row = cur.fetchone()

			if row==None:
				messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

			else:
				messagebox.showinfo("Success" , "Successfully Login" , parent = win)
				close()
				deshboard()
			con.close()
		except Exception as es:
			messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = win)
#----------------------------------------------------------------------------------------------------------------------------------
def deshboard():

        
        des = Tk()
        des.title("User Panel App")	
        des.maxsize(width=800 ,  height=500)
        des.minsize(width=800 ,  height=500)
        des['bg']='#504A4B'
        
	

	#heading label
        heading = Label(des , text = f"Guardian Name : {user_name.get()}" , font = 'Verdana 20 bold', foreground='black')
        heading.place(x=220 , y=50)
       

        f=Frame(des,height=1,width=800,bg="green")
        f.place(x=0,y=95)

        con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
        cur = con.cursor()

        cur.execute("select * from user_information where last_name ='"+ user_name.get() + "'")
        row = cur.fetchall()
        for data in row:
                sta=f"{data[9]}"
                disease=f"{data[5]}"
                print(sta)
                print(disease)
                if(sta=="Yes"):
                        heading = Label(des , text = "patient takes tablet correctly" , font = 'Verdana 15 bold')
                        heading.place(x=150 , y=100)
                        print("Patient takes tablet correctly")
                else:
                       print("No")
                       if(disease=="cancer" or disease=="Cancer" or disease=="CANCER"):
                                heading = Label(des , text = "User Not Taken The Tablet" , font = 'Verdana 12 bold')
                                heading.place(x=270 , y=250)
                       elif(disease=="fever" or disease=="Fever" or disease=="FEVER"):
                                heading = Label(des , text =  "User Not Taken The Tablet", font = 'Verdana 12 bold')
                                heading.place(x=270 , y=250)
                       elif(disease=="Jaundice" or disease=="jaundice" or disease=="JAUNDICE"):
                                heading = Label(des , text =  "User Not Taken The Tablet" , font = 'Verdana 12 bold')
                                heading.place(x=270 , y=250)
                       elif(disease=="Diarrhea" or disease=="diarrhea" or disease=="DIARRHEA"):
                                heading = Label(des , text = "User Not Taken The Tablet", font = 'Verdana 12 bold')
                                heading.place(x=270 , y=250)
                       elif(disease=="Headaches" or disease=="headaches" or disease=="HEADACHES") :
                                heading = Label(des , text =  "User Not Taken The Tablet" , font = 'Verdana 12 bold')
                                heading.place(x=270 , y=250)
                       elif(disease=="Mononucleosis" or disease=="mononucleosis" or disease=="MONONUCLEOSIS"):
                                heading = Label(des , text =  "User Not Taken The Tablet", font = 'Verdana 12 bold')
                                heading.place(270 , y=250)
                       else:
                              #messagebox.showinfo("information", "Patient Cures.")
                               pass
        






        	 
#---------------------------------------------------------------------------------------------------------------------------------
win = Tk()

# app title
win.title("Guardian Login APP")

# window size
win.maxsize(width=700 ,  height=500)
win.minsize(width=700 ,  height=500)
image=PhotoImage(file="D:\\Final\\digital.png")
l=Label(win,image=image)
l.pack(fill=BOTH,expand=True)

#heading label
#heading = Label(win , text = "Guardian Login" , font = 'Verdana 15 bold')
#heading.place(x=150 , y=100)

heading = Label(win , text = "Guardian Login" , font = 'Verdana 25 bold')
heading.place(x=180 , y=150)

username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# Entry Box
user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)


# button login and clear

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login )
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

 


win['bg']='white'
win.mainloop()
