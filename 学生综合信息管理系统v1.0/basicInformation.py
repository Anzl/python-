import stuInformationEntry
import mainInterface
import insertStu
import modifiedStu
import deleteStu
import glanceStu
def Information():
    print("**************************学生基本信息管理**************************")
    print("1-------------------------录入学生信息------------------------------")
    print("2-------------------------插入学生信息------------------------------")
    print("3-------------------------修改学生信息------------------------------")
    print("4-------------------------删除学生信息------------------------------")
    print("5-------------------------浏览学生信息------------------------------")
    print("0------------------------- 返回主菜单 ------------------------------")
    print("要进行的操作:")
    x = int(input())
    if x == 0:
        mainInterface.main()
    if x == 1:
        stuInformationEntry.Entering()      #录入学生信息模块
    elif x == 2:
        insertStu.Insert()          #插入学生信息模块
    elif x == 3:
        modifiedStu.Modified()      #修改学生模块
    elif x == 4:
        deleteStu.Delete()          #删除学生信息模块
    else:
        glanceStu.GlanceStudent()   #浏览学生信息模块
        