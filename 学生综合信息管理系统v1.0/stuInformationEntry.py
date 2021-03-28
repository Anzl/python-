#编程逻辑：先将输入的数据存入ls，直到输入结束，最后在ls中按学号排好序后写入文件
import basicInformation
def Entering():
    fname = 'student.txt'
    fo = open(fname,"w+")
    ls = []     #主要操作列表
    ls1 = []       #临时列表
    flag = 1    #标识变量
    x = ''
    fo.write("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
    print('请输入要录入的学生信息')
    while flag==1:
        ls1 = [input("学号:"),input("姓名:"),input("性别:"),input("家庭住址:"),input("联系电话:")]
        ls.append(ls1)          #ls1保存录入的每条数据，添加到ls
        print("是否继续输入？y/n")
        x = input()
        if x == 'y':
            flag = 1
        else:
            flag = 0
    ls.sort(key=lambda x:int(x[0]),reverse=False)       #按照第一个字段学号排序
    #写入文件
    for subelement in ls:
        for element in subelement:
            fo.write(element)
            fo.write('\t')
        fo.write('\n')
    ls.clear()
    fo.close()
    print("按1返回上一层")
    x = int(input())
    if x == 1:
        basicInformation.Information()
    
    
    