import basicInformation
import Grade
import Query
def main():
    print("**************************学生综合信息管理系统**************************")
    print("-------------------------1.学生基本信息管理------------------------------")
    print("-------------------------2. 学生成绩管理  ------------------------------")
    print("-------------------------3.   信息查询  ------------------------------")
    print("要进行的操作:")
    x = int(input())
    if x == 1:
        basicInformation.Information()
    elif x == 2:
        Grade.grade()
    else:
        Query.querty()
if __name__ == '__main__':
    main()
        

    
    