from tkinter import *
from emaster import *
class Admin(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.menubar = Menu(self)
		self.mnuupdate = Menu(self.menubar, tearoff=0)
		self.mnuupdate.add_command(label="Delete" )
		self.mnuupdate.add_command(label="Change" )
	
		
		self.mnuupdate.add_separator()

		self.mnuupdate.add_command(label="Exit")
		self.menubar.add_cascade(label="Update", underline=0,menu=self.mnuupdate)

		self.mnuupgrade = Menu(self.menubar, tearoff=0)
		self.mnuupgrade.add_command(label="Salary Change" )
		self.mnuupgrade.add_command(label="Change Desig" )
	
		
		self.mnuupgrade.add_separator()

		self.mnuupgrade.add_command(label="Employee Add",command=self.addEmp)
		self.menubar.add_cascade(label="Upgrade", underline=0,menu=self.mnuupgrade)
		
		
	def addEmp(self):
		root=Tk()
		emp=EmployeeMaster(root)
		root.title('Employee Master')
		root.geometry('450x300')
		root.mainloop()