from  student import Student

class StudentManage(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        # 加载学生数据
        self.load_student()
        while True:
            # 显示菜单
            self.show_menu()
            # 根据用户的输入，执行不同的功能
            menu_num = int(input("请输入功能序号"))

            if menu_num == 1:
                # 添加学员
                self.add_student()
            elif menu_num == 2:
                # 删除学员
                self.del_student()
            elif menu_num == 3:
                # 查询学员
                self.search_student()
                pass
            elif menu_num == 4:
                # 修改学员
                self.mod_student()
                pass
            elif menu_num == 5:
                # 显示学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()
            elif menu_num == 0:
                # 退出
                break
            else:
                print("您的输入有误，请重新输入")

    @staticmethod
    def show_menu():
        print("1.添加学员")
        print("2.删除学员")
        print("3.查询学员")
        print("4.修改学员")
        print("5.显示学员信息")
        print("6.保存学员信息")
        print("0.退出")

    def add_student(self):
        print('-' * 50)

        name = input("请输入姓名")
        gender = input("请输入性别")
        tel = input("请输入电话号码")
        student = Student(name, gender, tel)
        self.student_list.append(student)
        print(student)
        print('-' * 50)

    def del_student(self):
        print('-' * 50)

        name = input("请输入要删除的学员的名字")
        for student in self.student_list:
            if name == student.name:
                self.student_list.remove(student)

        print('-' * 50)
        pass

    def search_student(self):
        print('-' * 50)
        print("查询学员")

        search_name = input("请输入要查询的学员的姓名")
        for student in self.student_list:
            if search_name == student.name:
                print(student)

        print('-' * 50)

    def show_student(self):
        print('-' * 50)
        print("显示学员信息")
        for student in self.student_list:
            print(student)
        print('-' * 50)

    def mod_student(self):
        print('-' * 50)
        print("修改学员信息")

        modify_name = input("请输入要修改的学员的姓名")
        for student in self.student_list:
            if modify_name == student.name:
                student.name = input("请输入姓名")
                student.gender = input("请输入性别")
                student.tel = input("请输入电话号码")
                break

    def save_student(self):
        with open("student.data", 'w') as f:
            # __dict__ ：将类的属性转换为字典
            data_list = [student.__dict__ for student in self.student_list]
            print(data_list)
            f.write(str(data_list))

    def load_student(self):
        try:
            f = open("student.data", 'r')
        except IOError:
            # 如果文件不存在，则创建文件
            f = open("student.data", 'w')
        else:
            data = f.read()
            # 将string类型数据转换为字典
            data_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in data_list]
        finally:
            f.close()
