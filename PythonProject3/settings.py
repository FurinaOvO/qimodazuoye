import time
import file_io
import main
import student


def add_stu():#添加学生信息
	name = input('请输入学生姓名:\n')
	number = input('请输入学生学号:\n')
	math = input('请输入学生数学成绩:\n')
	eng = input('请输入学生英语成绩:\n')
	py = input('请输入学生Python成绩:\n')
	score = {'Math':math,'English':eng,'Python':py}

	if number_check(number):
		print('Error,该学生已经存在，请重新输入学生信息\n')
		add_stu()
	else:
		stu = student.Student(name,number,score)
		main.students.append(stu)
		file_io.write()
		print('Success,已成功添加该学生\n')
		print('3s后返回Control Panel\n')
		time.sleep(3)
		main.control()

def number_check(number):#学号查重
	result = False
	for s in main.students:
		if number == s.getNum():
			result = True
	return  result

def searcher(mod,args):#姓名学号筛选
	if mod == 'remove':
		result = False
		for s in main.students:
			if args == s.getName() or s.getNum():
				main.students.remove(s)
				result = True
		return result
	elif mod == 'search':
		stus = []
		for s in main.students:
			if args in s.getName() or s.getNum():
				stus.append(s)
		return stus
	#后续添加其他筛选条件
	else:
		pass



def remove_stu():#删除指定学生信息
	args = input('Please input Name or Number')
	if searcher('remove', args):
		print('Success !!\n已经成功删除\n')
		file_io.write()
	else:
		print('Error !!\n删除失败,没有查找到该学生\n')
	print('3s后返回Control Panel\n')
	time.sleep(3)
	main.control()

def modify_stu():#修改学生信息
	result = False
	args = input('Please input Name or Number')
	for s in main.students:
		if args == s.getName():
			print('已查找到目标\n')
			print(s.output())
			new_name = input('Please input New Name:') or s.getName()
			new_num = input('Please input New Number:') or s.getNum()
			new_math = input('Please input New Math Score:') or s.getScore().get('Math')
			new_eng = input('Please input New English Score:') or s.getScore().get('English')
			new_py = input('Please input New Python Score:') or s.getScore().get('Python')
			s.setName(new_name)
			s.setNum(new_num)
			new_score = {'Math':new_math,'English':new_eng,'Python':new_py}
			s.setScore(new_score)
			result = True
			break
	if not result:
		print('Error!!未查找到该学生')
	print('3s后返回Control Panel\n')
	time.sleep(3)
	file_io.write()
	main.control()


def search_stu():#查找学生
	args = input('Please input Name or Number')
	stus = searcher('search', args)
	if not stus:
		print('Error !!\n没有找到符合条件的学生\n')
	else:
		print(f'Success !!\n查找到所有符合"{args}"条件的所有学生\n')
		for stu in stus:
			print(stu.output())
	print('3s后返回Control Panel\n')
	time.sleep(3)
	main.control()
	pass

def output_stu():#输出所有学生的信息
	for stu in main.students:
		print(stu.output())
	print('已输出所有学生成绩(3s后自动跳转Control Panel)\n')
	time.sleep(3)
	main.control()


def return_stu():
	print('Error!!!\n请重新输入选项(3s后自动跳转)\n')
	print('==================')
	time.sleep(3)
	main.control()