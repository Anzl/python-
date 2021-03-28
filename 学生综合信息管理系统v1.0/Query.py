#编程逻辑：分别从两个文件读数据，最后将重复字段去掉合并成一条综合记录
import basicInformation
import mainInterface
def querty():
    ls = []     
    ls1 = []
    s = []
    fo1 = open('student.txt',"r")
    fo2 = open('综合测评成绩单.txt',"r")
    next(fo1)
    next(fo2)
    flag = 1
    x = ''
    for line in fo2:            #读取综合测评成绩单中数据放到ls
        ls.append(line.split())

    for line in fo1:  # 读取student表中的数据放到s
        s.append(line.split())
    for i in s:  #删除s中重复的字段（姓名，学号）
        del i[0]
        del i[0]
    #遍历两个列表
    for i in range(len(ls)):
        for j in range(len(s)):
            if i == j:  # 索引相等时
                ls[i].insert(2, s[j][0])        #为了看着美观，将性别字段插入到第三个位置
                ls[i].append(s[j][1])           #其他字段添加到最后
                ls[i].append(s[j][2])
    sno = input("请输入学生学号：")
    print("===============================您要查询的学生信息如下==================================")
    print("学号" + '\t' + "姓名" + '\t' + "性别" + '\t' + "语文" + '\t' + "数学" + '\t' + "英语" + '\t' +
      "总分" + '\t' + "学习成绩排名" + '\t' + "总成绩" + '\t' + "总成绩排名" + '\t' + "家庭住址" + '\t' + "手机号" + '\n')
    #检索与学号相同的记录
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            if str(ls[i][j]) == sno:        #如果学号匹配，则输出记录
                for k in range(len(ls[i])):
                    if (k == 8) or (k == 10) or (k == 11):      #格式规范控制
                        print('\t', end=' ')
                    print(str(ls[i][k]), end='\t')      
                print('\n')
    print("=============================== 已没有更多数据 ==================================")
    fo2.close()
    fo1.close()
    print("按1返回上一层,任意键返回主菜单")
    x = int(input())
    if x == 1:
        basicInformation.Information()
    else:
        mainInterface.main()