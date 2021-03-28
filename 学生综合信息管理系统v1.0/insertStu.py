# import operator
#编程逻辑：
#首先将student里面的数据读到ls里，然后输入学生信息，ls1用来临时存放单条学生信息
#插入完一条数据后询问用户是否继续输入，输入完后按照学号排序重新输入student文件
import basicInformation
import glanceStu
def Insert():
    ls = []         #用来操作的列表
    ls1 = []           #临时列表
    flag = 1        #标识变量
    x = ''
    fname = 'student.txt'   
    fo = open(fname,"r")  
    next(fo)  
    for line in fo:
        ls.append(line.split())
    
    fo.close()
    print("请输入要插入的学生信息：")
    while flag == 1:
        ls1 = [input("学号:"),input("姓名:"),input("性别:"),input("家庭住址:"),input("联系电话:")]
        ls.append(ls1)              #将输入后的学生信息添加到主列表
        print("是否继续插入? y/n")      
        x = input()
        if x == 'y':
            flag = 1
        else:
            flag = 0
    ls.sort(key=lambda x:int(x[0]),reverse=False)       #按照学号排序
    #重新写入文件
    fo1 = open(fname,"w+")
    fo1.write("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
    for subelement in ls:
        for element in subelement:
            fo1.write(element)
            fo1.write('\t')
        fo1.write('\n')
    ls.clear()
    fo1.close()
    print("按1返回上一层")
    s = int(input())
    if s == 1:
        basicInformation.Information()