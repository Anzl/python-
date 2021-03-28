#编程逻辑：先从score文件里读出数据，然后将评分加到最后一列
import Grade
def instructor():
    ls = []         #主要操作列表
    s = []          ##一个临时数组
    fname = 'score.txt'
    fout = open("品德成绩.txt","w+")
    fo = open(fname,"r")
    #程序运行后，先向文件里写入一行
    fout.write("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\t' + "品德成绩" + '\n')
    #第二行开始读
    next(fo)
    for line in fo:         #将文件里的数据读入到ls
        ls.append(line.split())
#输出一条数据并引导用户进行评分
    for i in range(len(ls)):
        print("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\n')
        for j in range(len(ls[i])):
            print(str(ls[i][j]) + '\t',end=" ")
        print("请对他进行评分(满分100)：")
#分数记录到grade里
        grade = input()
        s.append(grade)     #向s列表中添加成绩
#遍历两个列表，因为一条数据对应一个学生，所以两个列表长度相等，将对应下标的值一一对应添加到ls即可
    for i in range(len(ls)):
        for j in range(len(s)):
            if i == j:#索引相等时
                ls[i].append(s[j])

    k = 0               #格式控制变量，显示好看，作用不大
    #将数据写入文件
    for subelement in ls:
        for element in subelement:
            if k == 7:                  #格式控制语句，不用管
                fout.write('\t')
            fout.write(element)
            fout.write('\t')
            k = k + 1
        k = 0
        fout.write('\n')
    ls.clear()
    fo.close()
    
    print("按1返回上一层")
    x = int(input())
    if x == 1:
        Grade.grade()