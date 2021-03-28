import Evaglobale
import Grade
def display():
    # Evaglobale.comprehensive()          #先调用综合成绩单函数，将数据存入文件
    ls = []                             
    fname = '综合测评成绩单.txt'
    fo = open(fname,"r")
    next(fo)            #跳过第一行
    for line in fo:     #遍历文件，将每行数据添加到ls里
        ls.append(line.split())
    print("===============================所有学生信息如下==================================")
    print("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "学习成绩排名" + '\t' + "总成绩" + '\t' + "总成绩排名" + '\n')
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if j == 6:              #规范显示
                print('\t',end=' ')
            print(str(ls[i][j]),end='\t')   #显示数据
        print('\n')
    print("=============================== 已没有更多数据 ==================================")
    print("按1返回上一层")
    x = int(input())
    if x == 1:
        Grade.grade()