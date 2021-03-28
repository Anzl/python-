import Grade
def cam():
    ls = []         #主要操作列表
    s = []          #临时列表
    fname = 'score.txt'
    fout = open("同学评价.txt","w+")
    fo = open(fname,"r")
    fout.write("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\t' + "同学互评分" + '\n')
    next(fo)
    for line in fo:
        ls.append(line.split())
    #逐条显示并评分
    for i in range(len(ls)):
        print("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\n')
        for j in range(len(ls[i])):
            print(str(ls[i][j]) + '\t',end=" ")
            
        print("请对他进行评分(满分100)：")
        grade = input()
        s.append(grade)
#遍历两个列表，因为一条数据对应一个学生，所以两个列表长度相等，将对应下标的值一一对应添加到ls即可    
    for i in range(len(ls)):
        for j in range(len(s)):
            if i == j:#索引相等时
                ls[i].append(s[j])
#写入文件
    k = 0
    for subelement in ls:
        for element in subelement:
            if k == 7:
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
        
    