from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
from PIL import Image


#---------------------------------------------------------------Login Function --------------------------------------
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

			cur.execute("select * from user_information where username=%s and password = %s",(user_name.get(),password.get()))
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

		

#---------------------------------------------------------------End Login Function ---------------------------------
def forget():
        
        def book():
                if auser_name.get() =="" or dob.get() =="":

                       messagebox.showerror("Error" , "All Fields Are Required" , parent = fwin) 
                else:
                        con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
                        cur = con.cursor()
                        print(auser_name.get())
                        cur.execute("select * from user_information where username='"+ auser_name.get()+"' and dob='"+dob.get()+"' ")
                        row = cur.fetchone()
                        print(f"ForgetPassword : {row[8]}")
                        messagebox.showinfo("HealthCare Forget" , f"ForgetPassword : {row[8]}", parent = fwin)
                        
                         
        def clear():
                auser_name.delete(0,END)
                dob.delete(0,END)
				 
                                 
                        
        		
        fwin = Tk()

	
# app title
        fwin.title("HEALTH MONITORING APP")

# fwindow size
        fwin.maxsize(width=700 ,  height=500)
        fwin.minsize(width=700 ,  height=500)
        
       
       


         

#heading label
        heading = Label(fwin , text = "FORGET PASSWORD" , font = 'Verdana 15 bold')
        heading.place(x=150 , y=100)

        #heading = Label(fwin , text = "Login" , font = 'Verdana 25 bold')
        #heading.place(x=180 , y=150)

        username = Label(fwin, text= "User Name :" , font='Verdana 10 bold')
        username.place(x=80,y=220)

        userpass = Label(fwin, text= "Date of Birth :" , font='Verdana 10 bold')
        userpass.place(x=80,y=260)

# Entry Box
        auser_name = StringVar()
        dob = StringVar()
	
        auser_name = Entry(fwin, width=40 , textvariable = auser_name)
        auser_name.focus()
        auser_name.place(x=200 , y=223)

        dob = Entry(fwin, width=40, textvariable = dob)
        dob.place(x=200 , y=260)


# button login and clear

        abtn_login = Button(fwin, text = "FORGET" ,font='Verdana 10 bold',command = book)
        abtn_login.place(x=200, y=293)


        abtn_login = Button(fwin, text = "CLEAR" ,font='Verdana 10 bold', command = clear)
        abtn_login.place(x=280, y=293)

        
                

		


                                
#---------------------------------------------------- DeshBoard Panel -----------------------------------------
def deshboard():
        

	def book():
		if docter_var.get() =="" or day.get() =="" or month.get() == "" or year.get() == "":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = des)

		else:
			con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
			cur = con.cursor()

			cur.execute("update user_information set docter ='" + docter_var.get() + "', day ='" +  day.get() + "', month = '" + month.get() + "', year = '" + year.get() + "' where username ='"+ user_name.get() +"'")
			con.commit()	
			con.close()
			messagebox.showinfo("Success" , "Booked Appointment " , parent = des)
	des = Tk()
	des.title("User Panel App")	
	des.maxsize(width=800 ,  height=500)
	des.minsize(width=800 ,  height=500)
	
	#image=PhotoImage(file="D:\\final\\pngtree.png")
	#l=Label(des,image=image)
	#l.pack(fill=BOTH,expand=True)
        
	

	#heading label
	heading = Label(des , text = f"User Name : {user_name.get()}" , font = 'Verdana 20 bold')
	heading.place(x=220 , y=50)
       

	f=Frame(des,height=1,width=800,bg="green")
	f.place(x=0,y=95)

	con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
	cur = con.cursor()

	cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
	row = cur.fetchall()

	a=Frame(des,height=1,width=400,bg="green")
	a.place(x=0,y=247)

	b=Frame(des,height=150,width=1,bg="green")
	b.place(x=400,y=97)
	
	for data in row: 
		first_name = Label(des, text= f"Name : {data[1]}" , font='Verdana 10 bold')
		first_name.place(x=20,y=100)

		last_name = Label(des, text= f"Guardian Name : {data[2]}" , font='Verdana 10 bold')
		last_name.place(x=20,y=130)

		age = Label(des, text= f"Age : {data[3]}" , font='Verdana 10 bold')
		age.place(x=20,y=160)

		gender = Label(des, text= f"Gender : {data[4]}" , font='Verdana 10 bold')
		gender.place(x=250,y=100)
                
		city = Label(des, text= f"Disease :{data[5]}", font='Verdana 10 bold')
		city.place(x=250,y=130)			 
		
		add = Label(des, text= f"DOB : {data[6]}" , font='Verdana 10 bold')
		add.place(x=250,y=160)
		
		add = Label(des, text= f"Medicine Take Time : " , font='Verdana 10 bold')
		add.place(x=470,y=150)
		add = Label(des, text= f" Morning : {data[14]}" , font='Verdana 10 bold')
		add.place(x=500,y=180)
		add = Label(des, text= f" AfterNoon : {data[15]}" , font='Verdana 10 bold' )
		add.place(x=500,y=210)
		add = Label(des, text= f" Night : {data[16]}" , font='Verdana 10 bold')
		add.place(x=500,y=240)
		add = Label(des, text= f"Meditiation : " , font='Verdana 10 bold')
		add.place(x=300,y=260)
		add = Label(des, text= f" : {data[17]}" , font='Verdana 10 bold')
		add.place(x=420,y=260)
		add = Label(des, text= f"Excersie : " , font='Verdana 10 bold')
		add.place(x=300,y=300)
		add = Label(des, text= f" : {data[18]}" , font='Verdana 10 bold')
		add.place(x=420,y=300)
		add = Label(des, text= f"Water Level : " , font='Verdana 10 bold')
		add.place(x=300,y=340)
		add = Label(des, text= f" Every 1 Hour Take Water: {data[19]}" , font='Verdana 10 bold')
		add.place(x=420,y=340)

		add = Label(des, text= f"Height : {data[12]} Cm" , font='Verdana 10 bold')
		add.place(x=250,y=190)
		add = Label(des, text= f"Weight : {data[13]} Kg" , font='Verdana 10 bold')
		add.place(x=20,y=190)

		add = Label(des, text= f"Blood Group : {data[11]}" , font='Verdana 10 bold')
		add.place(x=250,y=220)
		add = Label(des, text= f"Type Of Food : {data[10]}" , font='Verdana 10 bold')
		add.place(x=20,y=220)
		
                
               



		

	# button 
        
	Button1 = Checkbutton(des, text = "yes",variable = patient,onvalue = 1,offvalue = 0,height = 2,width = 10,command=patient)
	Button1.place(x=483, y=380)
	Button2 = Checkbutton(des, text = "no",variable = guardian,onvalue = 1,offvalue = 0,height = 2,width = 10,command=guardian)
	Button2.place(x=583, y=380)
	Checkbutton1 = IntVar()
	Checkbutton2 = IntVar()
        # Notification
	heading = Label(des , text = "Notification" , font = 'Verdana 20 bold')
	heading.place(x=470 , y=100)	

	#disease=x	

def patient():
         con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
         cur = con.cursor()
         cur.execute("update user_information set status = 'Yes' where username ='"+ user_name.get() +"'")
         con.commit()
         con.close()
         messagebox.showinfo("information", "patient takes tablet correctly")
         
          
def guardian():

        con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
        con1 = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
        cur = con.cursor()
        cur1= con1.cursor();
        cur1.execute("update user_information set status = 'No' where username ='"+ user_name.get() +"'")
        con1.commit()
        con1.close()
        cur.execute("select * from user_information where username ='"+ user_name.get() + "'")
        row = cur.fetchall()
        for data in row:
                disease=f"{data[5]}"
               
                print(disease)
                if(disease=="cancer"):
                       l.config(text='suggest doctor to curue disease')
                elif(disease=="Fever"):
                      messagebox.showinfo("information", "patient kindly takes dolo650 tablet correctly")
                elif(disease=="jaundice"):
                       messagebox.showinfo("information", "cholestyramine")
                elif(disease=="Diarrhea"):
                      messagebox.showinfo("information", "Metformin")
                elif(disease=="Headaches"):
                      messagebox.showinfo("information", "Antibiotics")
                elif(disease=="Mononucleosis"):
                      messagebox.showinfo("information", "Omeprazole.")
                elif(disease=="Mononucleosis"):
                      messagebox.showinfo("information", "Omeprazole.")
                else:
                      messagebox.showinfo("information", "patient cures.")
                     
 
 

       
#-----------------------------------------------------End Deshboard Panel -------------------------------------

 
                     
 
 
#----------------------------------------------------Glogin----------------------------------------------------

#----------------------------------------------------------- Signup Window --------------------------------------------------

def signup():
        
       
	# signup database connect
	
	def action():
               
		if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="":
			messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
		elif password.get() != very_pass.get():
			messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)
		else:
			try:
				con = pymysql.connect(host="localhost",user="root",password="",database="docterapp")
				cur = con.cursor()
				cur.execute("select * from user_information where username=%s",user_name.get())
				row = cur.fetchone()
				#print(var.get())
				if row!=None:
					messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
				else:
                                       
					cur.execute("insert into user_information(first_name,last_name,age,gender,disease,dob,username,password,stat,bp,he,we,med1,med2,med3,medc,exec,wat) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
						(
						first_name.get(),
						last_name.get(),
						age.get(),
						var.get(),
						city.get(),
						add.get(),
						user_name.get(),
						password.get(),
                                                stat1.get(),
                                                bp.get(),
                                                he.get(),
                                                we.get(),
                                                med.get(),
                                                med1.get(),
                                                med2.get(),
                                                mec.get(),
                                                exea.get(),
                                                wat.get()
						))
					con.commit()
					con.close()
					messagebox.showinfo("Success" , "Ragistration Successfull" , parent = winsignup)
					clear()
					switch()
				
			except Exception as es:
				messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)
				

	 
	# close signup function			
	def switch():
		winsignup.destroy()

	# clear data function
	def clear():
		first_name.delete(0,END)
		last_name.delete(0,END)
		age.delete(0,END)
		var.set("")
		city.delete(0,END)
		add.delete(0,END)
		user_name.delete(0,END)
		password.delete(0,END)
		very_pass.delete(0,END)
		stat1.delete(0,END)
		bp.delete(0,END)
		we.delete(0,END)
		he.delete(0,END)
		
	 
	# start Signup Window	

	winsignup = Tk()	
	winsignup.title("Docter Appointment App")
	winsignup.maxsize(width=700 ,  height=900)
	winsignup.minsize(width=700 ,  height=900)
	
	#image=PhotoImage(file="D:\\Final\\pngtree.png")
	#l1=Label(winsignup,image=image)
	#l1.pack(fill=BOTH,expand=True)
	scroll=Scrollbar(winsignup, orient=VERTICAL) 
             
        

	#heading label
	heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
	heading.place(x=80 , y=60)

	# form data label
	first_name = Label(winsignup, text= "Name :" , font='Verdana 10 bold')
	first_name.place(x=80,y=130)

	last_name = Label(winsignup, text= "Guardian Name :" , font='Verdana 10 bold')
	last_name.place(x=80,y=160)

	age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
	age.place(x=80,y=190)

	Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
	Gender.place(x=80,y=220)

	city = Label(winsignup, text= "Disease :" , font='Verdana 10 bold')
	city.place(x=80,y=260)

	add = Label(winsignup, text= "DOB :" , font='Verdana 10 bold')
	add.place(x=80,y=290)

	user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
	user_name.place(x=80,y=320)

	password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
	password.place(x=80,y=350)

	very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
	very_pass.place(x=80,y=380)
	stat = Label(winsignup, text= "Veg or Non Veg:" , font='Verdana 10 bold')
	stat.place(x=80,y=420)
	stat1 = Label(winsignup, text= "Blood Group:" , font='Verdana 10 bold')
	stat1.place(x=80,y=460)
	stat1 = Label(winsignup, text= "Height:" , font='Verdana 10 bold')
	stat1.place(x=80,y=500)
	stat1 = Label(winsignup, text= "Weight:" , font='Verdana 10 bold')
	stat1.place(x=320,y=500)
	stat1 = Label(winsignup, text= "Medicine:" , font='Verdana 10 bold')
	stat1.place(x=80,y=540)
	stat1 = Label(winsignup, text= "Meditation:" , font='Verdana 10 bold')
	stat1.place(x=80,y=580)
	stat1 = Label(winsignup, text= "Exercise:" , font='Verdana 10 bold')
	stat1.place(x=80,y=620)
	stat1 = Label(winsignup, text= "Water Level:" , font='Verdana 10 bold')
	stat1.place(x=80,y=660)
	 

	# Entry Box ------------------------------------------------------------------

	first_name = StringVar()
	last_name = StringVar()
	age = IntVar()
	var= StringVar()	
	city= StringVar()
	add = StringVar()
	user_name = StringVar()
	password = StringVar()
	very_pass = StringVar()
	stat1 = StringVar()
	bp = StringVar()
	he = StringVar()
	we = StringVar()
	med = StringVar()
	med1 = StringVar()
	med2 = StringVar()
	mec = StringVar()
	exea = StringVar()
	wat = StringVar()


	first_name = Entry(winsignup, width=40 , textvariable = first_name)
	first_name.place(x=250 , y=133)


	
	last_name = Entry(winsignup, width=40 , textvariable = last_name)
	last_name.place(x=250 , y=163)

	
	age = Entry(winsignup, width=40, textvariable=age)
	age.place(x=250 , y=193)

	r1=Radiobutton(winsignup,text="Male",value=0)
	r1.place(x=250 , y=220)

	r2=Radiobutton(winsignup,text="Female",value=1)
	r2.place(x=320 , y=220) 
	
	 


	city = Entry(winsignup, width=40,textvariable = city)
	city.place(x=250 , y=263)


	
	add = Entry(winsignup, width=40 , textvariable = add)
	add.place(x=250 , y=293)

	
	user_name = Entry(winsignup, width=40,textvariable = user_name)
	user_name.place(x=250 , y=323)

	
	password = Entry(winsignup, width=40,show="*" ,textvariable = password)
	password.place(x=250 , y=353)

	
	very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
	very_pass.place(x=250 , y=383)
	#stat1= Entry(winsignup, width = 27, textvariable = stat1) 
	#stat1.place(x=250 , y=420)
	 
	#stat1= Entry(winsignup, width=7 ,textvariable = stat1)
	#stat1.place(x=250 , y=420)
	stat1 = ttk.Combobox(winsignup, width=27, textvariable=stat1)
	stat1['values'] = ('Veg',' Non Veg' ,)
	stat1.current()
	stat1.place(x=250 , y=420)
        
        

		
	bp = ttk.Combobox(winsignup, width=27, textvariable=bp)
	bp['values'] = ('A+','A-','B+','B-','O+','O-')
	bp.current()
	bp.place(x=250 , y=460) 
	 

	he= Entry(winsignup, width=10 , textvariable = he)
	he.place(x=250 , y=500)

	we= Entry(winsignup, width=10 , textvariable = we)
	we.place(x=400 , y=500)
        
	med= Entry(winsignup, width=20 , textvariable = med)
	med.place(x=250 , y=540)
	med1= Entry(winsignup, width=20 , textvariable = med1)
	med1.place(x=380 , y=540)
	med2= Entry(winsignup, width=20 , textvariable = med2)
	med2.place(x=510 , y=540)
	mec= Entry(winsignup, width=40 , textvariable = mec)
	mec.place(x=250 , y=580)
	exea= Entry(winsignup, width=40 , textvariable = exea)
	exea.place(x=250 , y=620)
	wat= Entry(winsignup, width=40 , textvariable = wat)
	wat.place(x=250 , y=660)
        

	# button login and clear

	btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = action)
	btn_signup.place(x=200, y=720)


	btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
	btn_login.place(x=280, y=720)


	sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
	sign_up_btn.place(x=350 , y =20)
	


	winsignup.mainloop()
#---------------------------------------------------------------------------End Singup Window-----------------------------------	
#forget Password


 

 

#------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()

# app title
win.title("HEALTH MONITORING APP")

# window size
win.maxsize(width=700 ,  height=500)
win.minsize(width=700 ,  height=500)

image=PhotoImage(file="D:\\final\\digital.png")
l=Label(win,image=image)
l.pack(fill=BOTH,expand=True)

#heading label
heading = Label(win , text = "VIRTUAL HEALTH MONITORING SYSTEM" , font = 'Verdana 15 bold')
heading.place(x=150 , y=100)

heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
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

sign_up_btn = Button(win , text="Sign up" , command = signup )
sign_up_btn.place(x=300 , y =350)

#gurdianlogin
sign_up_btn = Button(win , text="Forget Password" , command = forget)
sign_up_btn.place(x=400 , y =350)


win.mainloop()

#-------------------------------------------------------------------------- End Login Window ---------------------------------------------------
