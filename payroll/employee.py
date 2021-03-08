from tkinter import *

class Employee(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.btnSalary=Button(self,text='Show Salary')
		self.btnChange=Button(self,text='Change Password')
		self.btnChange.grid(row=1,column=0)
		self.btnSalary.grid(row=1,column=1)
		self.pack()
		