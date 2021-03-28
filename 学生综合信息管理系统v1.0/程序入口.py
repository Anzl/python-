import mainInterface
input_file = open("user.txt", "r")
    # 定义空列表存储临时数据，将同一组数据存储在同一列表中
list_temp = []
for line in input_file:
    list_temp.append(line.split())
    # 将嵌套的列表转换成json格式的字典
dict_temp =  dict(list_temp)
input_file.close()

def register():       # 定义注册方法
    
    print("<注册模式>".center(50, "*"))
    usr = input("请输入用户名：")
    pwd = input("请输入密码：")
    if usr in dict_temp.keys():             #如果字典里已有数据，输出提示信息
        print("该用户已被注册，请重新输入新用户名！")
        register()                          #再次调用本函数
    else:
        fout = open("user.txt","a+")        #a+的方式打开，注册的时候不会覆盖
        info = [usr,pwd]                    #一个字典
        dict_temp[usr] = pwd
        print("注册成功，您的登录用户名是：%s 密码是：%s" % (usr, pwd))
        for i in info:                  #将信息写入用户文件
            fout.write(i)
            fout.write(' ')
        fout.write('\n')
        x = input("是否使用新用户名密码登录?登录请输入1，退出请输入2：")
        if x == "1":
            login()
        else:
            print("退出系统，欢迎下次使用。")
            return

def login():       # 定义登录方法

    print("<登录模式>".center(50, "*"))
    for i in range(3):
        usr = input("请输入用户名：")
        pwd = input("请输入密码：")
        if usr in dict_temp.keys():         #判断用户名是否在字典里
            if pwd == dict_temp[usr]:
                print("登录成功！")
                mainInterface.main()
                break
            else:
                print("密码输入错误，请重新输入！")
        else:
            print("用户名错误，请重新输入！")
        print("这是第%s次输入错误，还剩%s次机会。" % (i + 1, 2 - i))
    else:
        print("超过最大验证次数，登录失败！")


def main():             # 定义主函数
    print("欢迎使用学生综合信息管理系统-v1.0".center(100, "-"))
    print("注册请输入0,登录请输入1,退出请输入2".center(95, "-"))
    select = input("请选择您需要进行的操作：")
    if select == "0":
        register()     # 调用注册方法
    elif select == "1":
        login()         #调用登录方法
    elif select == "2":
        print("退出系统！欢迎再次使用。")
        return
    else:
        print("输入有误，请重新输入！")
if __name__ == '__main__':
    main()
    
    