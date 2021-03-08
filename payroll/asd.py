from pymysql import *
from tkinter import *
class Abc(Frame):
	def __init__(self,master):
		super().__init__(master)
		
		self.tarea=Label(self)
		self.tarea.grid(row=0,column=0)
		self.btnok=Button(self,text='Show',command=self.show)
		self.btnok.grid(row=1,column=0)
		self.pack()
		
	def show(self):
		con=connect(db='payroll',user='root',passwd='root',host='localhost')
		cur=con.cursor()
		cur.execute("select * from users")
		rs=cur.fetchall()
		i=len(rs)
		t=''
		for x in range(i):
			t=t+"\n"+rs[x][0]+"\t"+rs[x][1]+"\t"+rs[x][2]
		self.tarea.config(text=t)
ro=Tk()
ob=Abc(ro)
ro.geometry('300x300')
ro.mainloop()
		
	
		