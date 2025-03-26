
import file_io
import settings

#主函数
students = []
def main():
	file_io.reader()
	control()
	file_io.write()
	pass

def control():#控制函数
	print('Welcome To Student Management System')
	print('[1]Add New Student')
	print('[2]Remove Student')
	print('[3]Modify Student Score')
	print('[4]Search Student')
	print('[5]Output All Student')
	print('[0]Exit')
	c = input('请输入选项:\n')

	match c:
		case '0':
			print('再见,已退出管理系统.\n')
			exit()
		case '1':
			settings.add_stu()
			pass
		case '2':
			settings.remove_stu()
			pass
		case '3':
			settings.modify_stu()
			pass
		case '4':
			settings.search_stu()
			pass
		case '5':
			settings.output_stu()
			pass
		case _:
			settings.return_stu()
	pass

if __name__ == '__main__':
	main()