#py学习记录03
"""
收获:
1.实现交互，输入函数input
2.列表和元组数据类型
3.多返回值
4.列表就如同C中的数组,作为参数时,传入的是地址
5.元组和列表都可以套娃
"""

#输入函数input
"""
input_str = input("请输入内容: ")
print("您输入的内容是: " + input_str )
print("type(input) = " + str( type(input_str) ))
"""

#题1,难点在于类型转换
"""
gross_income = input("总收入是: ")
employee_salaries = input("员工工资: ")
catering = input("餐饮费: ")
travelling_expenses = input("交通费: ")
profit = ( int(gross_income) - int(employee_salaries) - int(catering) - int(travelling_expenses) ) * 0.8
print("纯利润为: " + str(profit) )
"""

#题目2
"""
def print_length():
    temp_str = input("请输入内容: ")
    length = len(temp_str)
    return length

length =  print_length()
print("len = " + str(length))
"""

#列表1
"""
print("创建列表: ")
My_list_1 = []      #只是声明是列表
My_list_2 = [1, 2, 3.14, "4.0", [5,6,7] ]
print("下标索引: ")
print( "My_list_2[2] = " + str(My_list_2[2]) )
print( "My_list_2[-1] = " + str(My_list_2[-1]) )
print( "My_list_2[-1][1] = " + str(My_list_2[-1][1]) )
print( "My_list_2 = " + str(My_list_2) )
print("切片操作: ")
print( "My_list_2[2:] = " + str(My_list_2[2:]) )
print( "My_list_2[:2] = " + str(My_list_2[:2]) )
print( "My_list_2[2:4] = " + str(My_list_2[2:4]) )
print( "My_list_2[-1][1:] = " + str(My_list_2[-1][1:]) )
print("修改列表: ")
print("My_list_2 = " +str(My_list_2) )
print("My_list_2[1] = 'hello'")
My_list_2[1] = 'hello'
print("My_list_2 = " +str(My_list_2) )
print("My_list_2[-1][1] = 'test'")
My_list_2[-1][1] = 'test'
print("My_list_2 = " +str(My_list_2) )
"""

#列表2
"""
temp = 3.0
print("测试初始化时求值:")
My_list_3 =[ 1,2, temp + 2, temp *2]
print("My_list_3 = " + str(My_list_3))
print("测试批量修改: ")
My_list_3[1:4] = [6,6,6]
print("My_list_3 = " + str(My_list_3))
print("测试合并列表: ")
My_list_3 += [7,7,7]
print("My_list_3 = " + str(My_list_3))
"""

#元组1
"""
print("创建元组: ")
My_tuple_1 = ()
My_tuple_2 = (1,)
My_tuple_3 = (1, 2.0, 3, "hello", [7,8,9])
print("My_tuple_3 = " + str(My_tuple_3))
print("下标访问: ")
print("My_tuple_3[1] = " + str(My_tuple_3[1]))
print("My_tuple_3[-2] = " + str(My_tuple_3[-2]))
print("My_tuple_3[3][1] = " + str(My_tuple_3[3][1]))
print("切片访问: ")
print("My_tuple_3[2:] = " + str(My_tuple_3[2:]))
print("My_tuple_3[:2] = " + str(My_tuple_3[:2]))
print("My_tuple_3[2:-2] = " + str(My_tuple_3[2:-2]))
print("My_tuple_3[-2][:-2] = " + str(My_tuple_3[-2][:-2]))
"""

#元组2
"""
My_tuple_4 = [1, 2, 3.0, "hello", [7,8,9]]
print("My_tuple_4 = " + str(My_tuple_4))
My_tuple_4[-1][1] = 'H'
print("My_tuple_4 = " + str(My_tuple_4))
"""

#in关键字
"""
test_list = [1, 2.0, 'T']
test_tuple = (1, 2.0, 'R')
if 'T' in test_list :
    print("列表存在’T‘")
if 'T' not in test_tuple :
    print("元组不存在‘T’")
"""

#批量赋值
"""
print("批量赋值: ")
var_1, var_2 = (1, 2.0)
print( "var_1 = " + str(var_1) + "\tvar_2 = " + str(var_2) )
var_1, var_2 = ['s', "hello"]
print( "var_1 = " + str(var_1) + "\tvar_2 = " + str(var_2) )
var_1, var_2 = 23, 'KKK'        #本质是元组
print( "var_1 = " + str(var_1) + "\tvar_2 = " + str(var_2) )
"""

#多个返回值
"""
def fun_1() :
    name = input("名字: ")
    age = input("年龄: ")
    #return (name,age)
    #return [name,age]
    return name,age

#print( fun_1() )
a,b = fun_1()
print("a = " + a + "\tb = " + b )
"""

#题目
"""
var1 = [ 33, ['我的名字', '黑羽白月'], 'hello world!']
print(var1[-1])
print(var1[1][1])
var1[-1] = 'My god!'
var1[1][1] = '拜月童子'
print(var1[-1])
print(var1[1][1])
print(var1)
"""

#地址和值
"""
def fun_1(para) :
    para = "hello"

var_1 = 'ok'
fun_1(var_1)
print(var_1)        #值传递不改变传入参数

def fun_2(para) :
    para[0] = "hello"

var_2 = ['ok',1,2,3]
fun_2(var_2)
print(var_2)        #列表如同C数组,传入的是地址,直接修改具体内容了
"""


