#一个只供调用的函数，因用的较多，所以单独封装成了函数
import glanceStu
def Select(ls,ls1,fname):
    index = 0
    flag = 1
    x = ''
    fo = open(fname,"r")
    next(fo)
    for line in fo:
        ls.append(line.split())
    fo.close()
    sno = input("请输入学生学号：")         #按学号查询
#遍历ls，搜索与输入学号相同的记录，记录其下标存入index，找到后将标志变量设为1，
#跳出循环，否则设为0
    for subelement in ls:
        if subelement[0] == sno:
            index = ls.index(subelement)
            flag = 1
            ls1 = subelement
            break
        else:
            flag = 0
#出了循环后，判断flag状态，1为找到了，输出显示一下，否则显示查无此人，返回index
    if flag == 1:
        print(ls1)
    else:
        print("查无此人")
    return index