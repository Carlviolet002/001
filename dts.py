class DTS_SIS:
    def __init__(self):
        self.n = {'5':['45','45','45']}
    def stu_add(self):
        name = input('请输入姓名：')
        number = input('请输入学号：')
        age = input('请输入年龄：')
        where = input('请输入地址：')
        self.n[number] = [name, age, where]

    def chack_one(self):
        number = input('请输入学号：')
        if number in self.n.keys():
            a = self.n[number]
            print('学号：' + number, '姓名：' + a[0], '年龄：' + a[1], '住址：' + a[2])
        else:
            print('查无此人')

    def chack_all(self):
        for i in self.n.keys():
            if i in self.n.keys():
                a = self.n[i]
                print('学号：' + i, '姓名：' + a[0], '年龄：' + a[1], '住址：' + a[2],sep='\n')
            else:
                print('查无此人')
            print('-' * 30)

    def stu_change(self):
        number = input('请输入学号：')
        if number in self.n.keys():
            print('''
            a.修改姓名
            b.修改年龄
            c.修改住址
            d.退出
            ''')
            a = input()
            [name, age, where] = self.n[number]
            while a != 'd':
                match a:
                    case 'a':
                        name = input('请输入新姓名：')
                    case 'b':
                        age = input('请输入新年龄：')
                    case 'c':
                        where = input('请输入新地址：')
                self.n[number] = [name, age, where]
        else:
            print('查无此人')

    def stu_del(self):
        number = input('请输入学号：')
        del self.n[number]

    def s_choice(self):
        print('''
1.添加人员
2.查询所有人员
3.查询单个人员
4.修改人员信息
5.注销人员信息
按回车提交选项或退出''')
        match input():
            case '1':
                DTS_SIS.stu_add(self)
            case '2':
                DTS_SIS.chack_all(self)
            case '3':
                DTS_SIS.chack_one(self)
            case '4':
                DTS_SIS.stu_change(self)
            case '5':
                DTS_SIS.stu_del(self)
    def login(self):
        import time
        time_ = 0
        while input('请输入密钥：') != '114514':
            a = 2 ** time_
            print(f"密钥识别错误,请于{a}秒后重试")
            time.sleep(a)
            time_ += 1
        else:print('欢迎使用DTS学生信息管理系统')



a = DTS_SIS()
print(format('DTS学生信息管理系统','-^19'))
DTS_SIS.login(a)
DTS_SIS.s_choice(a)
print('感谢您的使用，如有建议请发邮件至：114514454545@nb.com')

