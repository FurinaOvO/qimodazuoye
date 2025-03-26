import settings
import student
import main



def reader():#读取txt中学生信息到students列表中
	with open('File/students.txt', 'r', encoding='UTF-8') as rf:
		for stu in rf:
			stu = stu.strip()
			s = stu.split(',')
			score = {'Math':s[2],'English':s[3],'Python':s[4]}
			stu = student.Student(s[0], s[1], score)
			if not settings.number_check(stu.getNum):
				main.students.append(stu)

def write():#读取学生信息存储到txt文件中
	with open('File/students.txt', 'w', encoding='UTF-8') as wr:
		for stu in main.students:
			wr.write(fm(stu))

def fm(stu):#将学生信息格式化
	name = stu.getName()
	num = stu.getNum()
	score = stu.getScore()
	math = score.get('Math')
	en = score.get('English')
	py = score.get('Python')
	return f'{name},{num},{math},{en},{py}\n'






