from pymysql import *
class Connect:
	def conn(self):
		con=connect(db='payroll',user='root',passwd='root',host='localhost')
		return con 