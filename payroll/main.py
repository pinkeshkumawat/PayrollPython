from pymysql import *
from tkinter import *
from tkinter import messagebox as tm
from util import *
from admin import *
from employee import *
class Login(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.lblLoginid=Label(self,text='User Name')
		self.lblPassword=Label(self,text="Password")
		self.txtLoginid=Entry(self)
		self.txtPassword=Entry(self,show='*')
		self.btnLogin=Button(self,text='login',command=self.check)
		self.lblHead=Label(self,text='Payroll Login')
		
		
		self.lblHead.grid(row=0,column=0)
		
		self.lblLoginid.grid(row=2,column=0)
		self.txtLoginid.grid(row=2,column=1)
		
		self.lblPassword.grid(row=3,column=0)
		self.txtPassword.grid(row=3,column=1)
		
		self.btnLogin.grid(columnspan=2)
		self.pack()
	def check(self):
		print('Reached')
		ob=Connect()
		uid=self.txtLoginid.get()
		pwd=self.txtPassword.get()
		con=ob.conn()
		cur=con.cursor()
		i=cur.execute("select etype from users where loginid='%s' and password='%s'"%(uid,pwd))
		if i==1:
			rs=cur.fetchone()
			if rs[0]=='admin':
				root=Tk()
				my=Admin(root)		
				root.config(menu=my.menubar)
				root.title("Admin Panel")
				root.state('zoomed')
				root.mainloop()
			else:
				root=Tk()
				my=Employee(root)		
				root.title("Employee Panel")
				root.geometry('250x250')
				root.mainloop()
		con.close()
root=Tk()
ob=Login(root)
root.title('Employee Payroll')
root.geometry('220x150')
root.mainloop()