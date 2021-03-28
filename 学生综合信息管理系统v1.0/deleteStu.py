#编程逻辑：先调用查询函数查询符合输入学号的学生信息，并显示出来，询问用户是否删除
#如果是，删除本条信息，在重新写入录入的信息保存到临时列表ls1，再将ls1写入主列表 ls，
# 再对ls按照学号排序后写入student文件，删除成功后提示用户删除成功
import selectStu
import glanceStu
import basicInformation
def Delete():
    ls = []             #主要操作列表
    ls1 = []            #临时列表
    fname = 'student.txt'
    index = selectStu.Select(ls,ls1,fname)      #调用查询函数
    
    print("您是否要删除本条数据？ y/n")
    x = input()         
    if x == 'y':
        del ls[index]                  #删除查询函数返回的下标为index的元素
        print("本条数据已删除")
        fo1 = open(fname,"w+")          
        ls.sort(key=lambda x:int(x[0]),reverse=False)   #按照第一个元素排序
        fo1.write("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
        for subelement in ls:
            for element in subelement:
                fo1.write(element)
                fo1.write('\t')
            fo1.write('\n')
        ls.clear()
        fo1.close()
    
    print("是否继续操作？ y/n")
    x = input()
    if x == 'y':
        Delete()        #如果是，再次调用本函数
    else:
        basicInformation.Information()
