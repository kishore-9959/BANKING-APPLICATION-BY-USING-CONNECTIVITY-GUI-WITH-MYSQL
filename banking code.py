from tkinter import *
import mysql.connector
import tkinter.messagebox as msg
class bankdetails:
    def __init__(self,root):
        self.root=root
        self.root.title("kishore")
        self.root.geometry("400x400")
        self.root.config(bg="pink")
        title=Label(text="Bank Application",bg="pink",fg="black",font=("bold",20))
        title.pack()
        b1=Button(text="registration",bg="yellow",fg="black",font=("bold",15),command=self.registration)
        b1.place(x=100,y=100)
        b2=Button(text="deposite",bg="yellow",fg="black",font=("bold", 15),command=self.deposite)
        b2.place(x=100,y=200)
        b3=Button(text="withdraw",bg="yellow",fg="black",font=("bold", 15),command=self.withdraw)
        b3.place(x=100,y=300)
    def registration(self):
        self.registration=Tk()
        self.registration.title("registration")
        self.registration.geometry("400x400")
        self.registration.config(bg="yellow")
        title=Label(self.registration,text="registration",bg="yellow",fg="black",font=("bold",20))
        title.pack()
        username=Label(self.registration,text="username",bg="red",fg="black",font=("bold",15))
        username.place(x=20,y=90)
        self.username_entry=Entry(self.registration,font=("bold",15))
        self.username_entry.place(x=150,y=90)
        password=Label(self.registration,text="password",bg="red",fg="black",font=("bold",15))
        password.place(x=20,y=150)
        self.password_entry=Entry(self.registration,font=("bold",15))
        self.password_entry.place(x=150,y=150)
        accountnumber=Label(self.registration,text="accountno",bg="red",fg="black",font=("bold",15))
        accountnumber.place(x=20,y=210)
        self.accountnumber_entry=Entry(self.registration,font=("bold",15))
        self.accountnumber_entry.place(x=150,y=210)
        balance=Label(self.registration,text="balance",bg="red",fg="black",font=("bold",15))
        balance.place(x=20,y=260)
        self.balance_entry=Entry(self.registration,font=("bold",15))
        self.balance_entry.place(x=150,y=260)
        submit=Button(self.registration,text="submit",bg="blue",fg="black",font=("bold", 15),command=self.show_registration)
        submit.place(x=140,y=320)
        self.registration.mainloop()
    def show_registration(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="kanna", user="root",password="kishore@123")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        password = self.password_entry.get()
        accountnumber=self.accountnumber_entry.get()
        balance=int(self.balance_entry.get())
        mycur.execute("insert into employee (name, password,accountnumber,balance) values (%s, %s, %s,%s)", (name, password,accountnumber,balance))
        msg.showinfo("success","registration successfully")
        mydb.commit()
    def deposite(self):
        self.deposite=Tk()
        self.deposite.title("deposit")
        self.deposite.geometry("400x400")
        self.deposite.config(bg="yellow")
        title=Label(self.deposite,text="Deposit", bg="yellow", fg="black", font=("bold", 20))
        title.pack()
        username=Label(self.deposite, text="username", bg="red", fg="black", font=("bold", 15))
        username.place(x=20, y=90)
        self.username_entry = Entry(self.deposite, font=("bold", 15))
        self.username_entry.place(x=150, y=90)
        accountnumber = Label(self.deposite, text="Account no", bg="red", fg="black", font=("bold", 15))
        accountnumber.place(x=20, y=150)
        self.accountnumber_entry = Entry(self.deposite, font=("bold", 15))
        self.accountnumber_entry.place(x=150, y=150)
        deposit= Label(self.deposite, text="deposite", bg="red", fg="black", font=("bold", 15))
        deposit.place(x=20, y=210)
        self.deposit_entry = Entry(self.deposite, font=("bold", 15))
        self.deposit_entry.place(x=150, y=210)
        submit=Button(self.deposite, text="submit", bg="blue", fg="black", font=("bold", 15),command=self.show_deposit)
        submit.place(x=140,y=320)
        self.deposite.mainloop()
    def show_deposit(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="kanna", user="root",password="kishore@123")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        accountnumber = self.accountnumber_entry.get()
        deposite =int(self.deposit_entry.get())
        mycur.execute("update employee set deposite=%s where name = %s",
                      (deposite,name))
        mydb.commit()
        mycur.execute("update employee set balance = balance+%s where name = %s and accountnumber = %s",
                      (deposite, name, accountnumber))
        mydb.commit()
        mycur.execute("select * from employee where name=%s and accountnumber=%s and deposite=%s",
                      (name, accountnumber,deposite))
        c = 0
        for i in mycur:
            c = c + 1
        if c > 0:
            msg.showinfo("success", "deposit money")
        else:
            msg.showinfo("invalid", "not deposit money")

    def withdraw(self):
        self.withdraw = Tk()
        self.withdraw.title("withdraw")
        self.withdraw.geometry("400x400")
        self.withdraw.config(bg="yellow")
        title=Label(self.withdraw, text="withdraw", bg="yellow", fg="black", font=("bold", 20))
        title.pack()
        username = Label(self.withdraw,text="username", bg="red", fg="black", font=("bold", 15))
        username.place(x=20,y=90)
        self.username_entry = Entry(self.withdraw, font=("bold", 15))
        self.username_entry.place(x=150, y=90)
        accountnumber = Label(self.withdraw, text="Account no", bg="red", fg="black", font=("bold", 15))
        accountnumber.place(x=20, y=150)
        self.accountnumber_entry = Entry(self.withdraw, font=("bold", 15))
        self.accountnumber_entry.place(x=150, y=150)
        withdraw= Label(self.withdraw, text="withdraw", bg="red", fg="black", font=("bold", 15))
        withdraw.place(x=20, y=210)
        self.withdraw_entry = Entry(self.withdraw, font=("bold", 15))
        self.withdraw_entry.place(x=150, y=210)
        submit = Button(self.withdraw, text="submit", bg="blue", fg="black", font=("bold", 15),command=self.show_withdraw)
        submit.place(x=140,y=260)
        self.withdraw.mainloop()
    def show_withdraw(self):
        mydb = mysql.connector.connect(host="localhost", port=3306, database="kanna", user="root",password="kishore@123")
        mycur = mydb.cursor()
        name = self.username_entry.get()
        accountnumber = self.accountnumber_entry.get()
        withdraw=int(self.withdraw_entry.get())
        mycur.execute("update employee set withdraw=%s where name = %s",
                      (withdraw,name))
        mydb.commit()
        mycur.execute("update employee set balance =balance-%s where name = %s and accountnumber = %s and withdraw<=balance",
                      (withdraw, name, accountnumber))
        mydb.commit()
        mycur.execute("select * from employee where name=%s and accountnumber=%s and withdraw=%s and withdraw<=balance",
                      (name, accountnumber, withdraw))
        c=0
        for i in mycur:
            c=c+1
        if c>0:
            msg.showinfo("success","withdraw money")
        else:
            msg.showinfo("invalid","not withdraw money")


root=Tk()
b=bankdetails(root)
root.mainloop()