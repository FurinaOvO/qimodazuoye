#定义学生类
class Student:
	def __init__(self,name,number,score):#构造方法
		self.name = name
		self.number = number
		self.score = score

	def getName(self):
		return self.name
	def getNum(self):
		return self.number
	def getScore(self):
		return self.score

	def setName(self,name):
		self.name = name
	def setNum(self,number):
		self.number = number
	def setScore(self,score):
		self.score = score

	def output(self):
		return (f'Name:{self.name}\n'
				f'Age:{self.number}\n'
				f'Math:{self.score.get('Math')}\n'
				f'English:{self.score.get('English')}\n'
				f'Python:{self.score.get('Python')}\n')
