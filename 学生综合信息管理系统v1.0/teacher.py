import Grade
def tea():
    ls = []         #主要操作列表
    s = []          #临时列表
    fname = 'score.txt'
    fout = open("老师评价.txt","w+")
    fo = open(fname,"r")
    #先向文件里写入一行
    fout.write("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\t' + "任课老师评分" + '\n')
    next(fo)        #跳过第一行
    for line in fo:                     #读取出来的数据写入ls
        ls.append(line.split())
 #显示一条数据进行评分，保存到grade里，然后将分数加到s中       
    for i in range(len(ls)):
        print("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "总成绩排名" + '\n')
        for j in range(len(ls[i])):
            print(str(ls[i][j]) + '\t',end=" ") 
        print("请对他进行评分(满分100)：")
        grade = input()
        s.append(grade)
        print(s)
        
#遍历两个列表，因为一条数据对应一个学生，所以两个列表长度相等，将对应下标的值一一对应添加到ls即可    
    for i in range(len(ls)):
        for j in range(len(s)):
            if i == j:#索引相等时
                ls[i].append(s[j])
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
    