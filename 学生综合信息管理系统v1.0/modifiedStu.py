# import operator
#编程逻辑：先调用查询函数查询符合输入学号的学生信息，并显示出来，询问用户是否修改
#如果是，删除之前的那条信息，在重新写入录入的信息保存到临时列表ls1，再将ls1写入主列表
# ls，再对ls按照学号排序后写入student文件，修改成功后提示用户修改成功
import selectStu
import glanceStu
import basicInformation
def Modified():
    ls = []         #主列表
    ls1 = []           #临时列表
    fname = 'student.txt'
    index = selectStu.Select(ls,ls1,fname)      #调用查询函数
    
    print("您是否要修改本条数据？ y/n")
    x = input()
    if x == 'y':
        del ls[index]       #删除查询到的信息
        ls1 = [input("学号:"),input("姓名:"),input("性别:"),input("家庭住址:"),input("联系电话:")]
        ls.append(ls1)      #将输入的新数据加到ls
        ls.sort(key=lambda x:int(x[0]),reverse=False)       #按照学号排序
        fo1 = open(fname,"w+")
        fo1.write("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
        #再次写入文件
        for subelement in ls:
            for element in subelement:
                fo1.write(element)
                fo1.write('\t')
            fo1.write('\n')
        ls.clear()
        fo1.close()
        print("本条数据已更新")
        print("是否继续操作？ y/n")
        x = input()
        if x == 'y':
            Modified()      #如果是，再次调用修改函数
        else:
            basicInformation.Information()      #否则返回主菜单
    print("按1返回上一层")
    x = int(input())
    if x == 1:
        basicInformation.Information()