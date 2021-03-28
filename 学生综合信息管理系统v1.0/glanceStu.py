import basicInformation
def GlanceStudent():
    ls = []         #用来操作的列表
    fname = 'student.txt'
    fo = open(fname,"r")        #直接读取文件信息并显示
    next(fo)            #跳过第一行
    for line in fo:
        ls.append(line.split())
    print("===============================所有学生信息如下==================================")
    print("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if j == 4:              #控制显示的变量
                print('\t',end=' ')
            print(str(ls[i][j]),end='\t')
        print('\n')
    print("=============================== 已没有更多数据 ==================================")
    print("按1返回上一层")
    x = int(input())
    if x == 1:
        basicInformation.Information()