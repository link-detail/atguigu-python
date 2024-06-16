
if 1 == 1:
    print("hello")
match 1:
    case 1:
        print("我是1")
    case 2:
        print("我是2")
    case 3:
        print("我是3")
    case _:
        print("你是非法字符")

year = int(input("晴输入需要判断的年份==>"))

if year > 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year,"是闰年")
    else:
        print(year,"不是闰年")


else:
    print("你输入的年份有误!")