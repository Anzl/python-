import Grade
def enterscorce():
    ls = []         #用来操作的列表
    score = []      #临时储存学生成绩信息的列表
    sum = 0         #三科分数总分
    flag = 1        #标识变量
    i = 0           #名次控制变量
    fname = 'score.txt'
    fo = open(fname,"w+")
    fo.write("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "排名" + '\n')
    print('请输入要录入的学生信息')
    while flag==1:
        score = [input("学号:"),input("姓名:"),input("语文成绩:"),input("数学成绩:"),input("英语成绩:")]
        sum = int(score[2]) + int(score[3]) + int(score[4])    #计算三科成绩之和
        score.append(str(sum))              #将总分添加到score列表
        ls.append(score)                    #将score添加到ls
        print("是否继续输入？y/n")           
        x = input()                         
        if x == 'y':
            flag = 1
        else:
            flag = 0
    ls.sort(key=lambda x:int(x[5]),reverse=True)            #按照总分排序为计算名次做铺垫
    for r in ls:            #r是二维列表s中的每一个一维列表
        r.append(str(i+1))  #为每个同学分配名次
        i = i+1
    ls.sort(key=lambda x:int(x[0]),reverse=False)       #按照学号排序再次写入文件
    # print(ls)
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
        Grade.grade()