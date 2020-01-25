from tkinter import*
from tkinter import messagebox
import sqlite3
win=Tk()
win.title("BANK")
username=StringVar()
password=StringVar()
accountno=StringVar()
username1=StringVar()
fathername=StringVar()
emailid=StringVar()
gender=StringVar()
contactno=StringVar()
initialamount=StringVar()
s1=StringVar()
s2=StringVar()
s3=StringVar()
initial=StringVar()
withdraw=StringVar()
balance=StringVar()
s7=StringVar()
a1=StringVar()
a2=StringVar()
initialamount=StringVar()
a5=StringVar()
balance=StringVar()
#a7=StringVar()
e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
e7=StringVar()
e8=StringVar()
e9=StringVar()
c1=StringVar()
c2=StringVar()
c3=StringVar()
c4=StringVar()
d1=StringVar()
d2=StringVar()
d3=StringVar()
d4=StringVar()
fadm=Frame(win)
fadm.grid(row=0)
def signup():
    ins= sqlite3.connect('admin.db')
    usernames=username.get()
    passwords=password.get()
    if(usernames==""):
        messagebox.showinfo('banking management','please enter the username')
    elif(passwords==""):
        messagebox.showinfo('banking management','please enter the password')
    else:
        ins.execute("CREATE TABLE IF NOT EXISTS LOGINAPP1(USERNAME CHAR(20) NOT NULL,PASSWORD CHAR(20) NOT NULL);")
        ins.execute("INSERT INTO LOGINAPP1(USERNAME,PASSWORD)VALUES(?,?)",(usernames,passwords,));
        print('SIGNUP PROCSS COMPLETE')
        messagebox.showinfo('SIGNUP COMPLETE', 'YOU R REGISTERED USER')
        fadm.grid_forget()
        fadd.grid(row=0)
        ins.commit()
   
        show=ins.execute('SELECT * FROM LOGINAPP1')
        for row in show:
            print(row[0]+" "+row[1])
            
def logincheck():
    usernames=username.get()
    passwords=password.get()
    ins= sqlite3.connect('admin.db')
    if(usernames==""):
        messagebox.showinfo('banking management','please enter the username')
    elif(passwords==""):
        messagebox.showinfo('banking management','please enter the password')
    else:
        show=ins.execute("SELECT * FROM LOGINAPP1 WHERE USERNAME=? AND PASSWORD=?",(usernames,passwords,))
    if show.fetchone() is None:
            messagebox.showinfo('signup process', 'please enter the right username and password')
    else:
            messagebox.showinfo('SIGNUP Process', 'you are administrator of project')
            fadm.grid_forget()
            fadd.grid(row=0)
    
def clear():

    username.set("")
    password.set("")
    print("you clicked on clear button")

def next():
        fadd.grid_forget()
        fada.grid(row=0)
        
def next1():
            fada.grid_forget()
            fadf.grid(row=0)
            
def next2():
                fada.grid_forget()
                fadw.grid(row=0)
                
def prev():
                    fadf.grid_forget()
                    fada.grid(row=0)
                    
def next3():
    fada.grid_forget()
    fade.grid(row=0)
    
    
def nextpage():
    fadd.grid_forget()
    faee.grid(row=0)

def nextpage1():
   fadd.grid_forget()
   facc.grid(row=0)
   
def addcomplaint1():
       facc.grid_forget()
       facc1.grid(row=0)
       
def addsuggesstion1():
       fass.grid_forget()
       fads.grid(row=0)

def prev1():
    fadw.grid_forget()
    fada.grid(row=0)

def prev2():
    fade.grid_forget()
    fada.grid(row=0)

def prev3():
    faee.grid_forget()
    fadd.grid(row=0)
    
def prev4():
     facc.grid_forget()
     fadd.grid(row=0)

def prev5():
    facc1.grid_forget()
    facc.grid(row=0)

def prev6():
    fads.grid_forget()
    fass.grid(row=0)

def exit():
    fadd.grid_forget()
    fath.grid(row=0)

def exit1():
    fada.grid_forget()
    fadd.grid(row=0)

def nextpage2():
    fadd.grid_forget()
    fass.grid(row=0)

def nextpage3():
    fass.grid_forget()
    fadd.grid(row=0)

def saves():
    ins= sqlite3.connect('admin.db')

    accountno1=accountno.get()
    usernames1=username1.get()
    fathername1=fathername.get()
    emailid1=emailid.get()
    gender1=gender.get()
    contactno1=contactno.get()
    initialamounts=initialamount.get()
    if(accountno1==""):
        messagebox.showinfo("banking management system","enter the account no")
    elif(usernames1==""):
        messagebox.showinfo("banking management system","enter the username")
    elif(fathername1==""):
        messagebox.showinfo("banking management system","enter the fathername")
    elif(emailid1==""):
        messagebox.showinfo("banking management system","enter the emailid")
    elif(gender1==""):
        messagebox.showinfo("banking management system","enter gender ")
    elif(contactno1==""):
        messagebox.showinfo("banking management system","enter the contactno")
    elif(initialamounts==""):
        messagebox.showinfo("banking management system","enter the initialamount")
    else:
        print(accountno1+" " +usernames1+" " +fathername1+" "+emailid1+" " +gender1+" " +contactno1+" "+initialamounts)
        ins.execute("CREATE TABLE IF NOT EXISTS  CLIENTAPP11(ACCOUNTNO CHAR(30) NOT NULL PRIMARY KEY,USERNAME1 CHAR(40) NOT NULL, FATHERNAME CHAR(40),EMAILID CHAR(57) NOT NULL,GENDER CHAR(57) NOT NULL,CONTACTNO CHAR(40) NOT NULL,INITIALAMOUNT CHAR(40) NOT NULL);")
        ins.execute("INSERT INTO CLIENTAPP11(ACCOUNTNO,USERNAME1,FATHERNAME,EMAILID,GENDER,CONTACTNO,INITIALAMOUNT)VALUES(?,?,?,?,?,?,?)",(accountno1,usernames1,fathername1,emailid1,gender1,contactno1,initialamounts,));
        print("client Information stored")
        messagebox.showinfo("client database","Record Inserted")
        ins.commit()

    show=ins.execute("SELECT * FROM CLIENTAPP11")
    for row in show:
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" " +row[5]+" " +row[6])
    
def updates():
    ins=sqlite3.connect('admin.db')
    
    accountno1=accountno.get()
    usernames1=username1.get()
    fathername1=fathername.get()
    emailid1=emailid.get()
    gender1=gender.get()
    contactno1=contactno.get()
    initialamounts=initialamount.get()
    print(accountno1+" " +usernames1+" " +fathername1+" "+emailid1+" " + gender1+" " +contactno1+ " " +initialamounts)

    ins.execute("UPDATE CLIENTAPP11 SET USERNAME1=?,FATHERNAME=?,EMAILID=? ,GENDER=?,CONTACTNO=?,INITIALAMOUNT=? where ACCOUNTNO=?",(usernames1,fathername1,emailid1,gender1,contactno1,initialamounts,accountno1,));
    print('Client Record Updated')
    messagebox.showinfo('CLIENT  DATABASE', 'Client RECORD UPDATED')
    ins.commit()
    show=ins.execute("SELECT * FROM CLIENTAPP11")
    for row in show:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])

def deletes():
    accountno1=accountno.get()
   
    ins= sqlite3.connect('admin.db')
    print("welcome in oops")
    ins.execute("delete from CLIENTAPP11 where ACCOUNTNO=?",(accountno1,))
    ins.commit()
    print("Record Deleted")
    messagebox.showinfo('Client DATABASE', 'Client RECORD DELETED')

def resets():
     accountno.set("")
     username1.set("")
     fathername.set("")
     emailid.set("")
     gender.set("")
     contactno.set("")
     initialamount.set("")
     
def showall():
    accountno1=accountno.get()
    ins=sqlite3.connect('admin.db')
    show=ins.execute("select * from clientapp11")
    
    for row in show:
       print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6])

       
    ins.commit()
    showframe = Toplevel(win)
    lb1=Label(showframe,text=row[0],bg="pink",font=('arial',20,'bold')).grid(row=0,column=1,stick='w')
    lb2=Label(showframe,text=row[1],font=('arial',20,'bold')).grid(row=0,column=2,stick='w')
    lb3=Label(showframe,text=row[2],font=('arial',20,'bold')).grid(row=0,column=3,stick='w')
    lb4=Label(showframe,text=row[3],font=('arial',20,'bold')).grid(row=0,column=4,stick='w')
    lb5=Label(showframe,text=row[4],font=('arial',20,'bold')).grid(row=0,column=5,stick='w')
    lb6=Label(showframe,text=row[5],font=('arial',20,'bold')).grid(row=0,column=6,stick='w')
    lb7=Label(showframe,text=row[6],font=('arial',20,'bold')).grid(row=0,column=6,stick='w')



def search():
    accountno1=accountno.get()
    messagebox.showinfo('banking management',accountno1);
    ins=sqlite3.connect('admin.db')
    messagebox.showinfo('Client database','Client Record Found')
    show=ins.execute("SELECT * FROM CLIENTAPP11 WHERE ACCOUNTNO=?",(accountno1,));
    for row in show:
        accountno.set(row[0])
        username1.set(row[1])
        fathername.set(row[2] )
        emailid.set(row[3])
        gender.set(row[4])
        contactno.set(row[5])
        initialamount.set(row[6])
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" " +row[6])

def balance1():
    ins=sqlite3.connect('admin.db')
    accountno1=s1.get()
    show=ins.execute("SELECT USERNAME1,INITIALAMOUNT FROM CLIENTAPP11 WHERE ACCOUNTNO =?",(accountno1,));
    for row in show:
        s2.set(row[0])
        initial.set(row[1])
        print(row[0]+" "+row[1])


def withdraw1():
    ins=sqlite3.connect('admin.db')
    accountno1=s1.get()
    withdraws=int(withdraw.get())
    show=ins.execute("SELECT USERNAME1,INITIALAMOUNT FROM CLIENTAPP11 where ACCOUNTNO=?",(accountno1,));
    for row in show:
        s2=row[0]
        initial=int(row[1])
       
    ins.execute("CREATE TABLE IF NOT EXISTS DEPOSIT11(ACCOUNTNO CHAR(20) NOT NULL PRIMARY KEY,USERNAME CHAR(30) NOT NULL,INITIAL1 INTEGER  NOT NULL);")
    if(initial<withdraws):
        messagebox.showinfo('Bank database','Insufficient Balance')
    else:
        totalbalance=initial-withdraws
    ins.execute("UPDATE DEPOSIT11 SET INITIAL1=? WHERE ACCOUNTNO=?",\
                (totalbalance,accountno1));
    messagebox.showinfo('Bank database','Balance Updated')
    balance.set(totalbalance)
    print(totalbalance)
    ins.execute("UPDATE CLIENTAPP11 SET INITIALAMOUNT=? WHERE ACCOUNTNO=?",\
                (totalbalance,accountno1));
    ins.commit()
    for row in show:
           print(row[0]+" "+row[1]+" "+row[2])


def resetbutton():
    s1.set("")
    s2.set("")
    initial.set("")
    withdraw.set("")
    balance.set("")

def balance2():
    accountno1=a1.get()
    ins=sqlite3.connect('admin.db')
    #accountno1=a1.get()
    show=ins.execute("SELECT USERNAME1,INITIALAMOUNT FROM CLIENTAPP11 where ACCOUNTNO=?",(accountno1,));
    for row in show:
        a2.set(row[0])
        initialamount.set(row[1])
        print(row[0]+" "+row[1])
    
def deposite1():
    ins=sqlite3.connect('admin.db')
    accountno1=a1.get()
    deposites=int(a5.get())
    show=ins.execute("SELECT USERNAME1,INITIALAMOUNT FROM CLIENTAPP11 where ACCOUNTNO=?",(accountno1,));
    for row in show:
        a2=row[0]
        initialamount=int(row[1])
       
    ins.execute("CREATE TABLE IF NOT EXISTS DEPOSIT11(ACCOUNTNO  CHAR(29) NOT NULL PRIMARY KEY,USERNAME CHAR(30) NOT NULL,\
    INITIAL1 INTEGER NOT NULL);")
    totalbalance=initialamount+deposites
    ins.execute("update deposit11 set initial1=? where accountno=?",\
                (totalbalance,accountno1));
    messagebox.showinfo('Bank database','Balance Updated')
    
    balance.set(totalbalance)
    print(totalbalance)
    ins.execute("update clientapp11 set initialamount=? where accountno=?",\
                (totalbalance,accountno1));
    ins.commit()

def resetdeposite():
    a1.set("")
    a2.set("")
    initialamount.set("")
    a5.set("")
    balance.set("")


def save2():
       ins=sqlite3.connect('admin.db')
       usernames=c1.get()
       emailids=c2.get()
       contactnos=c3.get()
       complaints=c4.get()
       if(usernames==""):
           messagebox.showinfo("banking management system","enter the username")
       elif(emailids==""):
           messagebox.showinfo("banking management system","enter the emailid")
       elif(contactnos==""):
           messagebox.showinfo("banking management system","enter the contactno")
       elif(complaints==""):
           messagebox.showinfo("banking management system","enter the complaint")
       else:
               print(usernames+" " +emailids+" " +contactnos+" "+complaints)
               ins.execute("CREATE TABLE IF NOT EXISTS  COMPLAINTAPP12(CUSER CHAR(30) NOT NULL PRIMARY KEY,CEMAIL CHAR(40) NOT NULL, CCONTACT CHAR(40) NOT NULL,CCOMPLAINTS CHAR(57) NOT NULL);")
               ins.execute("INSERT INTO COMPLAINTAPP12(CUSER,CEMAIL,CCONTACT,CCOMPLAINTS) VALUES (?,?,?,?)",(usernames,emailids,contactnos,complaints,));
               print("customer complaint stored")
               messagebox.showinfo("complaint database","Record Inserted")
               ins.commit()

       show=ins.execute("SELECT * FROM COMPLAINTAPP12")
       for row in show:
           print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])

def resetcomplaint():
    c1.set("")
    c2.set("")
    c3.set("")
    c4.set("")

def seecomplaint():
    
    ins=sqlite3.connect('admin.db')
    show=ins.execute("SELECT * FROM COMPLAINTAPP12")
    
    for row in show:
       print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])

       
    ins.commit()
    showframe1 = Toplevel(win)
    b1=Label(showframe1,text=row[0],bg="pink",font=('arial',20,'bold')).grid(row=0,column=1,stick='w')
    b2=Label(showframe1,text=row[1],font=('arial',20,'bold')).grid(row=0,column=2,stick='w')
    b3=Label(showframe1,text=row[2],font=('arial',20,'bold')).grid(row=0,column=3,stick='w')
    b4=Label(showframe1,text=row[3],font=('arial',20,'bold')).grid(row=0,column=4,stick='w')


def seesuggesstion():
    ins=sqlite3.connect('admin.db')
    show=ins.execute("SELECT * FROM SUGGESSTION")
    
    for row in show:
       print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])

       
    ins.commit()
    showframe2 = Toplevel(win)
    lbs1=Label(showframe2,text=row[0],bg="pink",font=('arial',20,'bold')).grid(row=0,column=1,stick='w')
    lbs2=Label(showframe2,text=row[1],font=('arial',20,'bold')).grid(row=0,column=2,stick='w')
    lbs3=Label(showframe2,text=row[2],font=('arial',20,'bold')).grid(row=0,column=3,stick='w')
    lbs4=Label(showframe2,text=row[3],font=('arial',20,'bold')).grid(row=0,column=4,stick='w')

def saves1():
    ins= sqlite3.connect('admin.db')
    employeeid1=e1.get()
    employeename1=e2.get()
    fathername1=e3.get()
    address1=e4.get()
    emailid1=e5.get()
    designation1=e6.get()
    salary1=e7.get()
    date1=e8.get()
    gender1=e9.get()
    if(employeeid1==""):
        messagebox.showinfo("banking management system","enter the employeeid")
    elif(employeename1==""):
        messagebox.showinfo("banking management system","enter the employeename")
    elif(fathername1==""):
        messagebox.showinfo("banking management system","enter the fathername")
    elif(address1==""):
        messagebox.showinfo("banking management system","enter address")
    elif(emailid1==""):
        messagebox.showinfo("banking management system","enter the emailid")
    elif(designation1==""):
        messagebox.showinfo("banking management system","enter designation")
    elif(salary1==""):
        messagebox.showinfo("banking management system","enter the salary")
    elif(date1==""):
        messagebox.showinfo("banking management system","enter date")
    elif(gender1==""):
        messagebox.showinfo("banking management system","enter gender")
    else:
        print(employeeid1+" " +employeename1+" " +fathername1+" "+address1+" " +emailid1+" " +designation1+" " +salary1+" " +date1+" " +gender1)
        ins.execute("CREATE TABLE  IF NOT EXISTS EMPLOYEEDATA5(EMPID CHAR(30) PRIMARY KEY NOT NULL,EMPNAME CHAR(30) NOT NULL,EMPFATHERNAME CHAR(30) NOT NULL,EMPADD CHAR(30) NOT NULL,EMPEMAIL CHAR(30) NOT NULL,EMPDESIG CHAR(30) NOT NULL,EMPSAL CHAR(30) NOT NULL,EMPDAT CHAR(30) NOT NULL,EMPGENDER CHAR(30) NOT NULL);")
        ins.execute("INSERT INTO EMPLOYEEDATA5(EMPID ,EMPNAME,EMPFATHERNAME ,EMPADD,EMPEMAIL ,EMPDESIG,EMPSAL,EMPDAT ,EMPGENDER)VALUES(?,?,?,?,?,?,?,?,?)",(employeeid1,employeename1,fathername1,address1,emailid1,designation1,salary1,date1,gender1,));
        print("employee Information stored")
        messagebox.showinfo("employee database","Record Inserted")
        ins.commit()
        show=ins.execute("SELECT * FROM EMPLOYEEDATA5")
        for row in show:
            print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" "+row[6]+" "+row[7]+" "+row[8])
                                                                                                                                                            
def updateemployee():
    ins=sqlite3.connect('admin.db')

    employeeid1=e1.get()
    employeename1=e2.get()
    fathername1=e3.get()
    address1=e4.get()
    emailid1=e5.get()
    designation1=e6.get()
    salary1=e7.get()
    date1=e8.get()
    gender1=e9.get()

    print(employeeid1+" " +employeename1+" " +fathername1+" "+address1+" " +emailid1+" " +designation1+" " +salary1+" " +date1+" " +gender1)
    ins.execute("UPDATE EMPLOYEEDATA5 SET EMPNAME=?,EMPFATHERNAME=? ,EMPADD=?,EMPEMAIL=? ,EMPDESIG=?,EMPSAL=?,EMPDAT=? ,EMPGENDER=? WHERE EMPID=?",(employeename1,fathername1,address1,emailid1,designation1,salary1,date1,gender1,employeeid1,));
    print('Client Record Updated')
    messagebox.showinfo('Client  DATABASE', 'Client RECORD UPDATED')
    ins.commit()
   
    show=ins.execute("SELECT * FROM EMPLOYEEDATA5")
    for row in show:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])

def deleteemployee():
    employeeid1=e1.get()
   
    ins= sqlite3.connect('admin.db')
    print("welcome in oops")
    ins.execute("DELETE FROM EMPLOYEEDATA5 where EMPID=?",(employeeid1,))
    ins.commit()
    print("Record Deleted")
    messagebox.showinfo('EMPLOYEE DATABASE', 'EMPLOYEE RECORD DELETED')



def searchemployee():
    employeeid1=e1.get()
    ins=sqlite3.connect('admin.db')
    messagebox.showinfo('Employee database','Employee Record Found')
    show=ins.execute("SELECT * FROM EMPLOYEEDATA5 WHERE EMPID=?",(employeeid1,));
    for row in show:
        ins= sqlite3.connect('admin.db')
        e1.set(row[0])
        e2.set(row[1])
        e3.set(row[2])
        e4.set(row[3])
        e5.set(row[4])
        e6.set(row[5])
        e7.set(row[6])
        e8.set(row[7])
        e9.set(row[8])
        print(row[0]+" "+row[1]+" "+row[2]+" "+row[3]+" "+row[4]+" "+row[5]+" " +row[6]+" " +row[7]+" "+row[8])

def resetemployee():
    e1.set("")
    e2.set("")
    e3.set("")
    e4.set("")
    e5.set("")
    e6.set("")
    e7.set("")
    e8.set("")
    e9.set("")
   
        
fadm=Frame(win)
fadm.grid(row=0)    
t1=Label(fadm,text="Bank Management system",bg='black',fg='white',font=('mangal',40,'bold'))
ls15=Label(fadm,text="",height=3).grid(row=1)
t2=Label(fadm,text="admin Pannel",font=('arial',30,'bold'),bg="steel blue")
label1=Label(fadm,text="Username",font=('arial',20,'bold'),height=2)
ls11=Label(fadm,text="",height=2).grid(row=4)
entry1=Entry(fadm,textvariable=username,bg="white",bd=5,font=('arial',25,'bold'),border='3',fg='black')
label2=Label(fadm,text="Password",font=('arial',20,'bold'),height=2)
entry2=Entry(fadm,textvariable=password,show="*",bg="white",bd=5,font=('arial',25,'bold'),border='3',fg='black')
button1=Button(fadm,text="Login",font=('arial',20,'bold'),padx=35,pady=2,bd=5,bg="cyan",border='4',command=logincheck)
button2=Button(fadm,text="Signup" ,font=('arial',20,'bold'),padx=35,pady=2,bd=5,bg="cyan",border='4',command=signup)
button3=Button(fadm,text="Clear",font=('arial',20,'bold'),padx=35,pady=2,bd=5,bg="cyan",border='4',command=clear)
t1.grid(row=0,column=2, columnspan=4)
t1.grid(row=3,column=2, columnspan=4)
label1.grid(row=5, column=2)
entry1.grid(row=5, column=3)
label2.grid(row=6,column=2)
entry2.grid(row=6, column=3)
button1.grid(row=10,column=3,sticky='w')
button2.grid(row=10, column=3,sticky='e')
ls12=Label(fadm,text="",height=1).grid(row=11)
button3.grid(row=13,column=3,sticky='w')
ls13=Label(fadm,text="",height=3).grid(row=14)

#>>>>>>>>>

fadd=Frame(win)
fadd.grid(row=0)
fadd.grid_forget()
wel1=Label(fadd,text=" WELCOME TO BANKING SYSTEM ",bg='black',fg='white',font=('arial',40,'bold'))
wel2=Label(fadd,text="",height=3)
"""l1=Label(fadd,text="",height=2)
l2=Label(fadd,text="",height=2)
l3=Label(fadd,text="",height=2)
l4=Label(fadd,text="",height=2)
l5=Label(fadd,text="",height=3)"""
button4=Button(fadd,text="Account management",fg='white',font=('mangal',40,'bold'),padx=7,pady=2,bd=7,bg="cyan",command=next)
button5=Button(fadd,text="Employee details",fg='white',font=('mangal',40,'bold'),padx=84,pady=2,bd=7,bg="cyan",command=nextpage)
button6=Button(fadd,text="Complaint",fg='white',font=('mangal',40,'bold'),padx=82,pady=2,bd=7,bg="cyan",command=nextpage1)
button7=Button(fadd,text="Suggestion",fg='white',font=('mangal',40,'bold'),padx=75,pady=2,bd=7,bg="cyan",command=nextpage2)
button8=Button(fadd,text="Exit",fg='white',font=('mangal',40,'bold'),padx=75,pady=2,bd=7,bg="cyan",command=exit)
wel1.grid(row=4, column=4,columnspan=5)
wel2.grid(row=5)
button4.grid(row=6, column=4,columnspan=5)
#l1.grid(row=7)
button5.grid(row=8, column=4,columnspan=5)
#l2.grid(row=9)
button6.grid(row=10, column=4, columnspan=5)
#l3.grid(row=11)
button7.grid(row=12, column=4, columnspan=5)
#l4.grid(row=13)
button8.grid(row=13, column=4, columnspan=5)
#l5.grid(row=15)


fada=Frame(win)
fada.grid(row=0)
fada.grid_forget()
label4=Label(fada,text=" ACCOUNT MANAGEMENT ",bg='black',fg='white',font=('arial',40,'bold')).grid(row=4, column=4,columnspan=5)
l=Label(fada,text="",height=3).grid(row=5)
acc1=Label(fada,text="",height=2)
acc2=Label(fada,text="",height=2)
acc3=Label(fada,text="",height=2)
acc4=Label(fada,text="",height=2)
acc5=Label(fada,text="",height=3)
button9=Button(fada,text="create account ",font=('arial',20,'bold'),padx=52,pady=2,bd=7,bg="cyan",command=next1)
button10=Button(fada,text="Withdraw Money",font=('arial',20,'bold'),padx=41,pady=2,bd=7,bg="cyan",command=next2)
button11=Button(fada,text="Deposit Money",font=('arial',20,'bold'),padx=44,pady=2,bd=7,bg="cyan",command=next3)
button12=Button(fada,text="See all accounts",font=('arial',20,'bold'),padx=65,pady=2,bd=7,bg="cyan",command=showall)
button13=Button(fada,text="Previous",font=('arial',20,'bold'),padx=100,pady=2,bd=7,bg="cyan",command=exit1)
button9.grid(row=6, column=4, columnspan=5)
acc1.grid(row=7)
button10.grid(row=8, column=4, columnspan=5)
acc2.grid(row=9)
button11.grid(row=10, column=4, columnspan=5)
acc3.grid(row=11)
button12.grid(row=13, column=4, columnspan=5)
acc4.grid(row=14)
button13.grid(row=15, column=4, columnspan=5)
acc5.grid(row=16)

#
fath=Frame(win)
labelth=Label(fath,text="thanks for visiting here").grid(row=0,column=0)

#
fadf=Frame(win)
fadf.grid(row=0)
fadf.grid_forget()
t3=Label(fadf,text="CUSTOMER ACCOUNT  ",bg='black',fg='white',font=('arial',40,'bold')).grid(row=3,column=2,columnspan=4,sticky='e')
label3=Label(fadf,text="Accountno",font=('arial',20,'bold'))
entry3=Entry(fadf,textvariable=accountno,justify="right",bd=5,font=('arial',20,'bold'),bg="steelblue",fg='white')
label4=Label(fadf,text="Username",font=('arial',20,'bold'))
entry4=Entry(fadf,textvariable=username1,justify="right",bg="steelblue",bd=5,font=('arial',25,'bold'),fg='white')
label5=Label(fadf,text="fathername",font=('arial',20,'bold'))
entry5=Entry(fadf,textvariable=fathername,justify="right",bg="steelblue",bd=5,font=('arial',25,'bold'),fg='white')
label6=Label(fadf,text="emailid",font=('arial',20,'bold'))
entry6=Entry(fadf,textvariable=emailid,bg="steelblue",justify="right",bd=5,font=('arial',25,'bold'),fg='white')
label7=Label(fadf,text="gender",font=('arial',20,'bold'))
entry7=Entry(fadf,textvariable=gender,bg="steelblue",justify="right",bd=5,font=('arial',25,'bold'),fg='white')
label8=Label(fadf,text="contactno",font=('arial',20,'bold'))
entry8=Entry(fadf,textvariable=contactno,bg="steelblue",justify="right",bd=5,font=('arial',25,'bold'),fg='white')
labelia=Label(fadf,text="InitialAmount",font=('arial',20,'bold'))
entryia=Entry(fadf,textvariable=initialamount,justify="right",bg="steelblue",bd=5,font=('arial',25,'bold'),fg='white')
l1=Label(fadf,text="",height=1)
l2=Label(fadf,text="",height=1)
l3=Label(fadf,text="",height=3)
l4=Label(fadf,text="",height=3)
l1.grid(row=17)
label3.grid(row=6,column=2)
entry3.grid(row=6,column=4)
label4.grid(row=7,column=2)
entry4.grid(row=7,column=4)
label5.grid(row=8,column=2)
entry5.grid(row=8,column=4)
label6.grid(row=9,column=2)
entry6.grid(row=9,column=4)
label7.grid(row=10,column=2)
entry7.grid(row=10,column=4)
label8.grid(row=11,column=2)
entry8.grid(row=11,column=4)
labelia.grid(row=12,column=2)
entryia.grid(row=12,column=4)
buttona=Button(fadf,text="save",font=('arial',20,'bold'),padx=84,pady=2,bd=5,bg="grey",command=saves)
buttona.grid(row=18, column=2,columnspan=3,sticky='w')
buttona=Button(fadf,text="reset",font=('arial',20,'bold'),padx=69,pady=2,bd=5,bg="grey",command=resets)
buttona.grid(row=18, column=3,columnspan=3,sticky='e')
l2.grid(row=19)
buttona=Button(fadf,text="update",font=('arial',20,'bold'),padx=74,pady=2,bd=5,bg="grey",command=updates)
buttona.grid(row=20, column=2,columnspan=3,sticky='w')
buttona=Button(fadf,text="delete",font=('arial',20,'bold'),padx=74,pady=2,bd=5,bg="grey",command=deletes)
buttona.grid(row=20, column=3,columnspan=3,sticky='e')
l3.grid(row=21)
buttona=Button(fadf,text="search",font=('arial',20,'bold'),padx=74,pady=2,bd=5,bg="grey",command=search)
buttona.grid(row=22, column=2,columnspan=3,sticky='w')
l1.grid(row=23)
button13=Button(fadf,text="go to previous",font=('arial',20,'bold'),padx=21,pady=2,bd=5,bg="grey",command=prev)
button13.grid(row=6, column=11,columnspan=3,sticky='e')

#

fadw=Frame(win)
fadw.grid(row=0)
fadw.grid_forget()
label9=Label(fadw,text="accountno",font=('arial',20,'bold'),justify='left')
entry9=Entry(fadw,textvariable=s1,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label10=Label(fadw,text="Username",justify='left',font=('arial',20,'bold'))
entry10=Entry(fadw,textvariable=s2,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label12=Label(fadw,text="initialamount",font=('arial',20,'bold'),justify='left')
entry12=Entry(fadw,textvariable=initial,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label13=Label(fadw,text="withdraw money",font=('arial',20,'bold'),justify='left')
entry13=Entry(fadw,textvariable=withdraw,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label14=Label(fadw,text="balance",font=('arial',20,'bold'),justify='left')
entry14=Entry(fadw,textvariable=balance,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label9.grid(row=6,column=2)
entry9.grid(row=6,column=3)
label10.grid(row=8,column=2)
entry10.grid(row=8,column=3)
label12.grid(row=9,column=2)
entry12.grid(row=9,column=3)
label13.grid(row=10,column=2)
entry13.grid(row=10,column=3)
label14.grid(row=11,column=2)
entry14.grid(row=11,column=3)
button15=Button(fadw,text="Resetbutton",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=resetbutton)
button15.grid(row=18, column=5,columnspan=3,sticky='e')
button16=Button(fadw,text="save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=withdraw1)
button16.grid(row=18, column=3,columnspan=3,sticky='w')
buttn1=Button(fadw,text="go to prev page ",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=prev1)
buttn1.grid(row=6, column=9,columnspan=2,sticky='e')
buttn1=Button(fadw,text="show detail",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=balance1)
buttn1.grid(row=7,column=3)
#>>>>>>>>>>

fade=Frame(win)
fade.grid(row=0)
fade.grid_forget()
label16=Label(fade,text="Accountno",font=('arial',20,'bold'),justify='left')
entry16=Entry(fade,textvariable=a1,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label17=Label(fade,text="username",justify='left',font=('arial',20,'bold'))
entry17=Entry(fade,textvariable=a2,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label19=Label(fade,text="current amount",font=('arial',20,'bold'),justify='left')
entry19=Entry(fade,textvariable=initialamount,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label20=Label(fade,text="deposit money",font=('arial',20,'bold'),justify='left')
entry20=Entry(fade,textvariable=a5,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label21=Label(fade,text="Balance",font=('arial',20,'bold'),justify='left')
entry21=Entry(fade,textvariable=balance,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
#label22=Label(fade,text="date",font=('arial',20,'bold'),justify='left')
#entry22=Entry(fade,textvariable=a7,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
dep=Label(fade,text="",height=1)
label16.grid(row=6,column=2)
entry16.grid(row=6,column=3)
label17.grid(row=8,column=2)
entry17.grid(row=8,column=3)
label19.grid(row=9,column=2)
entry19.grid(row=9,column=3)
label20.grid(row=10,column=2)
entry20.grid(row=10,column=3)
label21.grid(row=11,column=2)
entry21.grid(row=11,column=3)
#label22.grid(row=12,column=2)
#entry22.grid(row=12,column=3)
buttn2=Button(fade,text="go to previous page",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=prev2)
buttn2.grid(row=6, column=9,columnspan=2,sticky='e')
buttnd=Button(fade,text="showdetail",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=balance2)
buttnd.grid(row=7, column=3)
buttnd1=Button(fade,text="deposit",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=deposite1)
buttnd1.grid(row=18, column=3,columnspan=3,sticky='w')
dep.grid(row=19,columnspan=10)
buttnd2=Button(fade,text="Reset",font=('arial',20,'bold'),padx=30,pady=2,bd=4,bg="grey",command=resetdeposite)
buttnd2.grid(row=20, column=2,columnspan=5)


#fshow=Frame(win)
#fshow.grid_forget()
#fshow.grid(row=0)

#>>>>>>>>
faee=Frame(win)
faee.grid(row=0)
faee.grid_forget()
label00=Label(faee,text="  EMPLOYEE DETAILS  ",bg='black',fg='white',font=('arial',40,'bold'))
label01=Label(faee,text="")
label23=Label(faee,text="EmployeeId",font=('arial',20,'bold'),justify='left')
entry23=Entry(faee,textvariable=e1,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label24=Label(faee,text="employeename",font=('arial',20,'bold'),justify='left')
entry24=Entry(faee,textvariable=e2,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label25=Label(faee,text="fathername",font=('arial',20,'bold'),justify='left')
entry25=Entry(faee,textvariable=e3,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label26=Label(faee,text="address",font=('arial',20,'bold'),justify='left')
entry26=Entry(faee,textvariable=e4,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label27=Label(faee,text="emailid",font=('arial',20,'bold'),justify='left')
entry27=Entry(faee,textvariable=e5,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label28=Label(faee,text="designation",font=('arial',20,'bold'),justify='left')
entry28=Entry(faee,textvariable=e6,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label29=Label(faee,text="salary",font=('arial',20,'bold'),justify='left')
entry29=Entry(faee,textvariable=e7,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
labeld=Label(faee,text="date",font=('arial',20,'bold'),justify='left')
entryd=Entry(faee,textvariable=e8,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
labelg=Label(faee,text="gender",font=('arial',20,'bold'),justify='left')
entryg=Entry(faee,textvariable=e9,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
iep1=Label(faee,text="")
iep2=Label(faee,text="")
label00.grid(row=4,column=3,columnspan=5,sticky='e')
label01.grid(row=5,columnspan=10)
label23.grid(row=6,column=2)
entry23.grid(row=6,column=3)
label24.grid(row=7,column=2)
entry24.grid(row=7,column=3)
label25.grid(row=8,column=2)
entry25.grid(row=8,column=3)
label26.grid(row=9,column=2)
entry27.grid(row=9,column=3)
label28.grid(row=10,column=2)
entry28.grid(row=10,column=3)
label29.grid(row=11,column=2)
entry29.grid(row=11,column=3)
labeld.grid(row=12,column=2)
entryd.grid(row=12,column=3)
labelg.grid(row=13,column=2)
entryg.grid(row=13,column=3)
iep1.grid(row=14,columnspan=10)
iep2.grid(row=14,columnspan=10)
buttne=Button(faee,text="Save",font=('arial',20,'bold'),padx=84,pady=2,bd=7,bg="grey",command=saves1)
buttne.grid(row=16, column=2,columnspan=3)
buttne1=Button(faee,text="Update",font=('arial',20,'bold'),padx=69,pady=2,bd=7,bg="grey",command=updateemployee)
buttne1.grid(row=16, column=3,columnspan=3,sticky='e')
buttne2=Button(faee,text="delete",font=('arial',20,'bold'),padx=74,pady=2,bd=7,bg="grey",command=deleteemployee)
buttne2.grid(row=18, column=2,columnspan=3)
buttns=Button(faee,text="search",font=('arial',20,'bold'),padx=70,pady=2,bd=7,bg="grey",command=searchemployee)
buttns.grid(row=18, column=4,columnspan=3,sticky='e')
buttn3=Button(faee,text="Reset",font=('arial',20,'bold'),padx=16,pady=2,bd=7,bg="grey",command=resetemployee)
buttn3.grid(row=18, column=3,columnspan=3)
buttnr=Button(faee,text="go to previous",font=('arial',20,'bold'),padx=78,pady=2,bd=7,bg="grey",command=prev3)
buttnr.grid(row=6, column=11,columnspan=3,sticky='e')



facc=Frame(win)
facc.grid(row=0)
facc.grid_forget()
btn1=Button(facc,text="add complaint",bg='black',fg='white',font=('arial',40,'bold'),command=addcomplaint1)
btn1.grid(row=3,column=3,columnspan=5,sticky='e')
btn2=Button(facc,text="see all complaint",bg='black',fg='white',font=('arial',40,'bold'),command=seecomplaint)
btn2.grid(row=4,column=3,columnspan=5,sticky='e')
btn3=Button(facc,text="go to prev page",bg='black',fg='white',font=('arial',40,'bold'),command=prev4)
btn3.grid(row=5,column=4,columnspan=6,sticky='e')

facc1=Frame(win)
facc1.grid(row=0)
facc1.grid_forget()
sugg1=Label(facc1,text="ADD COMPLAINT",bg='black',fg='white',font=('arial',40,'bold'))
sugg2=Label(facc1,text="")
sugg3=Label(facc1,text="")
label30=Label(facc1,text="username",font=('arial',20,'bold'),justify='left')
entry30=Entry(facc1,textvariable=c1,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label31=Label(facc1,text="emailid",font=('arial',20,'bold'),justify='left')
entry31=Entry(facc1,textvariable=c2,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label32=Label(facc1,text="contactno",font=('arial',20,'bold'),justify='left')
entry32=Entry(facc1,textvariable=c3,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label33=Label(facc1,text="complaint",font=('arial',20,'bold'),justify='left')
entry33=Entry(facc1,textvariable=c4,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
sugg1.grid(row=3,column=3,columnspan=5,sticky='e')
sugg2.grid(row=4,columnspan=10)
sugg3.grid(row=5,columnspan=10)
label30.grid(row=6,column=2)
entry30.grid(row=6,column=3)
label31.grid(row=7,column=2)
entry31.grid(row=7,column=3)
label32.grid(row=8,column=2)
entry32.grid(row=8,column=3)
label33.grid(row=9,column=2)
entry33.grid(row=9,column=3)
button17=Button(facc1,text="save",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=save2)
button17.grid(row=19, column=3,columnspan=3,sticky='w')
button18=Button(facc1,text="Reset",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=resetcomplaint)
button18.grid(row=19, column=3,columnspan=3,sticky='e')
buttn5=Button(facc1,text="go to prev page",font=('arial',20,'bold'),padx=74,pady=2,bd=4,bg="grey",command=prev5)
buttn5.grid(row=6, column=9)


fass=Frame(win)
fass.grid(row=0)
fass.grid_forget()
button19=Button(fass,text="add suggesstion",bg='black',fg='white',font=('arial',40,'bold'),padx=52,pady=2,bd=7,command=addsuggesstion1)
button19.grid(row=1,column=0)
button20=Button(fass,text="See all Suggesstion",bg='black',fg='white',font=('arial',40,'bold'),padx=52,pady=2,bd=7,command=seesuggesstion)
button20.grid(row=2,column=0)
buttns=Button(fass,text="Exit",bg='black',fg='white',font=('arial',40,'bold'),padx=52,pady=2,bd=7,command=nextpage3)
buttns.grid(row=3,column=0)

#----------------------------------------------------------------------------
def suggesstionsave():
    #ins=sqlite3.connect("admin.db")
      cusernames=d1.get()
      cemailid=d2.get()
      ccontactno=d3.get()
      csuggestion=d4.get()
      if(cusernames==""):
        messagebox.showinfo("banking management system","enter the username")
      elif(cemailid==""):
          messagebox.showinfo("banking management system","enter the emailid")
      elif(ccontactno==""):
          messagebox.showinfo("banking management system","enter the contactno")
      elif(csuggestion==""):
          messagebox.showinfo("banking management system","enter the suggestion")
      else:
          print(cusernames+" "+cemailid+" "+ccontactno+" "+csuggestion)
          ins=sqlite3.connect("admin.db")
          ins.execute("create table if not exists suggesstion(usernames char(20) not null,mails char(30) not null,contact char(20) not null,ccomplaint char(30) not null);")
          ins.execute("insert into suggesstion(usernames,mails,contact,ccomplaint) values(?,?,?,?)",(cusernames,cemailid,ccontactno,csuggestion,));
          messagebox.showinfo('Banking Project','suggesstion Save')
          ins.commit()
          show=ins.execute("select * from suggesstion")
          for row in show:
              print(row[0]+" "+row[1]+" "+row[2]+" "+row[3])

def suggesstionreset():
            d1.set("")
            d2.set("")
            d3.set("")
            d4.set("")
            
fads=Frame(win)
fads.grid(row=0)
fads.grid_forget()
label0=Label(fads,text="  SUGGESTION BOX  ",bg='black',fg='white',font=('arial',40,'bold'))
ls=Label(fads,text="")
ls1=Label(fads,text="")
ls2=Label(fads,text="")
ls3=Label(fads,text="")
label35=Label(fads,text="username",font=('arial',20,'bold'),justify='left')
entry35=Entry(fads,textvariable=d1,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label36=Label(fads,text="emailid",justify='left',font=('arial',20,'bold'))
entry36=Entry(fads,textvariable=d2,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label37=Label(fads,text="contactno",font=('arial',20,'bold'))
entry37=Entry(fads,textvariable=d3,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label38=Label(fads,text="suggesstion",font=('arial',20,'bold'))
entry38=Entry(fads,textvariable=d4,justify="right",bg="blue",bd=5,font=('arial',30,'bold'))
label0.grid(row=3,column=3,columnspan=5,sticky='e')
ls.grid(row=4,columnspan=10)
ls1.grid(row=5,columnspan=10)
label35.grid(row=6,column=2)
entry35.grid(row=6,column=3)
label36.grid(row=7,column=2)
entry36.grid(row=7,column=3)
label37.grid(row=8,column=2)
entry37.grid(row=8,column=3)
label38.grid(row=9,column=2)
entry38.grid(row=9,column=3)
ls2.grid(row=10,columnspan=10)
ls3.grid(row=11,columnspan=10)

button20=Button(fads,text="save",font=('arial',20,'bold'),padx=74,pady=2,bd=7,bg="grey",command=suggesstionsave)
button20.grid(row=18, column=3,columnspan=3,sticky='w')
button21=Button(fads,text="Reset",font=('arial',20,'bold'),padx=2,pady=2,bd=7,bg="grey",command=suggesstionreset)
button21.grid(row=20, column=3,columnspan=3,sticky='w')
button21=Button(fads,text="go to previous",font=('arial',20,'bold'),padx=35,pady=2,bd=4,bg="grey",command=prev6)
button21.grid(row=6, column=9)


win.mainloop()
