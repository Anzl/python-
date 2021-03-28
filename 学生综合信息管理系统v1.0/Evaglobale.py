#编程逻辑：
#首先分别读取同学评价、老师评价、品德成绩里面的最后一列存放到s数组里，然后提取最后一列成绩到grade数组，
#接着把grade里面的数据添加到
def comprehensive():
    ls = []         #整理数据的主要数组，存放了从同学评价文件里读取出来的每行数据
    s = []          #一个临时数组，存放从三个文本文件里读出来的每一行字段，从第二行开始读
    grade = []      #存放s数组中的最后一个字段，即对应的成绩(最后一列)
    fout = open("综合测评成绩单.txt","w+")      
    fo1 = open("同学评价.txt","r")
    fo2 = open("老师评价.txt","r")
    fo3 = open("品德成绩.txt","r")
#先向综合测评成绩单文件中写入一行提示信息，真正的数据从第二行开始
    fout.write("学号" + '\t' + "姓名" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' + "总分" + '\t' + "学习成绩排名" + '\t' + "总成绩" + '\t' + "总成绩排名" + '\n')
    next(fo1)       #跳过第一行，从第二行开始读，下同
    next(fo2)
    next(fo3)
#一个赋值函数，即将grade里的成绩分别拼接到ls数组的最后
    def valuation():
        for i in range(len(ls)):
            for j in range(len(grade)):
                if i == j:#索引相等时
                    ls[i].append(grade[j])
    for line in fo1:            #读取同学评价文件里的每行数据添加到ls
        ls.append(line.split())
    
    for line in fo2:            #读取老师评价里的每行数据添加到s
        s.append(line.split())
    for i in s:                 #提取s中的最后一列成绩添加到grade
        grade.append(i[-1])
    valuation()                 #调用赋值函数
    s = []                      #s，grade重新赋值为空数组
    grade = []
    for line2 in fo3:           #重复之前的操作读取另一个文件
        s.append(line2.split())
    for ii in s:
        grade.append(ii[-1])
    valuation()
    grade = []      #grade重新赋值为空数组  
#遍历ls，计算综合测评成绩，综合测评总分＝（考试成绩）*0.6+（同学互评分）*0.1+品德成绩*0.1+任课老师评分*0.2        
    for j in ls:
        grade.append(str(round((float(j[-5]) * 0.6) + (float(j[-3]) * 0.1) + (float(j[-2]) * 0.2) + (float(j[-1]) * 0.1))))

    valuation()
#删除同学评分，老师评分，品德成绩三项，不需写入文件
    for j in ls:
        del j[-2]
        del j[-2]
        del j[-2]
    ls.sort(key=lambda x:int(x[7]),reverse=True)        #按照综合测评总分排序
    i = 0                   #计数变量，记录排名
    for r in ls:            #r是二维列表s中的每一个一维列表
        r.append(str(i+1))
        i = i+1
    k = 0                   #用来规范格式的变量，不是很重要
    for subelement in ls:       #将数据写入文件
        for element in subelement:
            if k == 7:
                fout.write('\t')
            fout.write(element)
            fout.write('\t')
            k = k + 1
        k = 0
        fout.write('\n')
    ls.clear()
    fo1.close()
    fo2.close()
    fo3.close()
    fout.close()