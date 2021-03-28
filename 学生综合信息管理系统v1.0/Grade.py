import enterScore
import schoolmate
import teacher
import qualite
import DisplayGrade
import mainInterface
import Evaglobale
def grade():
    print("**************************学生成绩管理**************************")
    print("------------------------1.录入学生成绩------------------------------")
    print("------------------------2.同学互评  ------------------------------")
    print("------------------------3.任课老师评价------------------------------")
    print("------------------------4.辅导员评价 ------------------------------")
    print("------------------------5.学生综合信息浏览------------------------------")
    print("------------------------0.返回主菜单 ------------------------------")
    print("要进行的操作:")
    x = int(input())
    if x == 1:
        enterScore.enterscorce()            #输入学生成绩模块
    elif x == 2:
        schoolmate.cam()                    #学生互评模块
    elif x == 3:
        teacher.tea()                       #任课老师评价模块
    elif x == 4:
        qualite.instructor()                #品德成绩评价模块
    elif x == 5:
        Evaglobale.comprehensive()          #先把信息写入综合成绩单，再显示
        DisplayGrade.display()  
    else:
        mainInterface.main()            #显示所有学生成绩模块