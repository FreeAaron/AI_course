#!/usr/bin/env python
# coding: utf-8

# In[1]:


'hello world!'
"hello world!"


# In[2]:


print("'Welcome to Python.'")
print(type("'Welcome to Python.'"))
print('"Welcome to Python."')
print(type('"Welcome to Python."'))


# In[3]:


# print()及type()內建函式
# print()打印出來，type確認資料結構

print('C:\some\name')  
print('C:\\some\\name')
print(r'C:\some\name') 


# In[4]:


# \n表示開始新的一行

print("Hello" + "World")
print("Hi" * 3)
print("Hello World"[0:7]) 
print(len("Hello World"))
# 起始編號從零開始


# In[5]:


print(type(1))
print(type(1.0))
print(type(1+2j))
print(type(complex(1,2)))

print(str(0))
print(str(1.9))
print(int(1.9)) 
print(int("0")) 
print(float(1))
print(type(str(0)))
print(type(str(1.9)))
print(type(int(1.9)))
print(type(int("0")))
print(type(float(1)))
# 會無條件省略小數部分
# int("hello")則會顯示錯誤
# float("hello")或float(1+2j)則會顯示錯誤


# In[6]:


print(1+2)
print(3-4)
print(5*2)
print(9/7)
print((1+3)*(2-4))
print(1+3*2-4) 
print(3**2) 
print(5//3) 
print(5%3) 
# 電腦會自動判斷先乘除後加減
# 三的二次方
# 除法求商
# 除法求餘


# In[7]:


a = 7
# 在Python裡宣告一個變數

a = 7 
print(a*3) 
# 宣告變數a
# 進行基本運算
a = a*5 
print(a)
# 重新賦值


# In[8]:


a=[1,2,3,4,5]
a


# In[9]:


a = 10
print(a**3)


# In[10]:


a=a*5


# In[11]:


a


# In[12]:


a*3


# In[13]:


a[3]


# In[14]:


a=[1,2,3,4,5]


# In[15]:


a[4]


# In[16]:


print(len(a))


# In[17]:


a=[1,2,2,2,3,4,5]


# In[18]:


a.remove(2)
a


# In[19]:


a.remove(2)
a


# In[20]:


alphabet = {
    "a":"apple",
    "b":"ball",
    "c":"cat",
    "d":"dog",
    "e":"elephant"
}

print(alphabet["a"])


# In[21]:


alphabet = dict(
    a="apple",
    b="ball",
    c="cat",
    d="dog",
    e="elephant"
)

print(alphabet["a"])


# In[22]:


alphabet["f"] = "frog" 
alphabet["a"] = "ant" 

print(alphabet["a"])
print(alphabet)
# 新增新元素
# 更新元素


# In[23]:


new_dict = {
    "e":"egg",
    "g":"good",
    "h":"hello"
}

alphabet.update(new_dict) # 更新的資料需為字典型態
print(alphabet)


# In[24]:


del alphabet["a"] 
print(alphabet)
# 刪除資料


# In[25]:


alphabet


# In[26]:


print(len(alphabet))
print(alphabet.keys())
print(alphabet.values())
print(alphabet.items())


# In[27]:


alphabet.keys()


# In[28]:


alphabet.values()


# In[29]:


alphabet.items()


# In[30]:


import pandas as pd
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\test.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[31]:


import pandas as pd
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[32]:


member = pd.DataFrame(data)
member


# In[33]:


transaction


# In[34]:


member.head()


# In[35]:


member.info()


# In[36]:


member.shape


# In[37]:


member['name']


# In[38]:


member[ ['name','age'] ]


# In[39]:


transaction['product'] == 'lemon'


# In[40]:


[transaction['product'] == 'lemon']


# In[41]:


transaction[transaction['product'] == 'lemon']


# In[42]:


transaction


# In[43]:


transaction['product'] == 'lemon'


# In[44]:


member['age'].sort_values(ascending = False)


# In[45]:


member.sort_values(['age'])


# In[46]:


member2 = member.drop(columns=['uid'])
member2


# In[47]:


transaction['product'] == 'lemon'


# In[48]:


member.values.tolist()


# In[49]:


transaction


# In[50]:


transaction['product']


# In[51]:


transaction[transaction["product"] != "lemon"]


# In[53]:


transaction[transaction["product"] == "lemon"]


# In[54]:


transaction['product'] == 'guava	'


# In[55]:


transaction['product'] == 'guava'


# In[56]:


transaction['product'] != 'guava'


# In[57]:


transaction[transaction['product'] != 'guava']


# In[58]:


transaction[transaction["price"] > 25]


# In[59]:


transaction[transaction["price"] > 40]


# In[60]:


a=[1,2,2,3,2,4,5]

a.remove(3)
a


# In[61]:


a.remove(3)
a


# In[62]:


transaction


# In[63]:


filt = (transaction['product'] == 'organge') & (transaction['quantity'] > 4)
filt
print(transaction.loc[filt])


# In[64]:


filt


# In[65]:


transaction['product'] == 'organge'


# In[66]:


transaction['quantity'] > 4


# In[67]:


print(transaction.loc[filt])


# In[68]:


transaction


# In[70]:


print([filt])


# In[71]:


transaction.loc[filt]


# In[72]:


transaction[filt]


# In[76]:


filt = (transaction['product'] == 'organge') & (transaction['quantity'] <= 4)
filt
print(transaction.loc[filt])


# In[74]:


transaction


# In[77]:


filt


# In[81]:


transaction.loc[filt]


# In[82]:


import pandas as pd
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')
filt_value = ['banana', 'lemon', 'guava'] #想要的值
filt = transaction['product'].isin(filt_value)  #篩選欄位有filt_value串列中的資料
filt


# In[83]:


print(transaction.loc[filt])


# In[84]:


print(transaction.loc[filt,['product', 'quantity', 'price']])


# In[85]:


filt_value


# In[86]:


filt = transaction['product'].isin(filt_value)


# In[87]:


filt


# In[88]:


filt = transaction['product'](filt_value)


# In[89]:


print(transaction[filt])


# In[90]:


print(transaction[filt])


# In[91]:


print(transaction[filt,['product', 'quantity', 'price']])


# In[92]:


print(transaction.loc[filt,['product', 'quantity', 'price']])


# In[93]:


import pandas as pd
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')
filt_value = ['banana', 'lemon', 'guava'] #想要的值
filt = transaction['product'].isin(filt_value)  #篩選欄位有filt_value串列中的資料
filt


# In[94]:


print(transaction.loc[filt])


# In[95]:


print(transaction.loc[filt,['product', 'quantity', 'price']])


# In[96]:


product = transaction.groupby("product")
product 
product .size()


# In[97]:


product = transaction.groupby("product")


# In[98]:


product 


# In[99]:


product .size()


# In[100]:


product.get_group("banana")


# In[101]:


transaction


# In[102]:


import pandas as pd
import numpy as np
transaction.groupby('product').sum()


# In[103]:


transaction.groupby(['product','uid']).sum()


# In[104]:


transaction.groupby(['product','uid']).mean()


# In[105]:


import pandas as pd
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')
filt_value = ['banana', 'lemon', 'guava'] #想要的值
filt = transaction['product'].isin(filt_value)  #篩選欄位有filt_value串列中的資料
filt


# In[106]:


transaction.groupby(['product','uid']).mean()


# In[107]:


transaction.groupby('product').mean()


# In[108]:


transaction.groupby('product').sum()


# In[109]:


transaction.groupby('product').describe()


# In[110]:


transaction


# In[111]:


transaction.groupby('product').max()


# In[113]:


transaction.groupby([]'product','uid']).sum()


# In[114]:


transaction.groupby(['product','uid']).sum()


# In[115]:


transaction.groupby(['product','uid']).sum()


# In[116]:


transaction


# In[117]:


import pandas as pd
 
df = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\資料\HR_comma_sep.csv')
print(df)


# In[118]:


import pandas as pd
 
df = pd.read_csv('C:/Users/maaro/iCloudDrive/進修之路/AI/王子廌/資料/HR_comma_sep.csv')
print(df)


# In[119]:


df.groupby('left').sum()


# In[121]:


transaction.groupby(['uid']).sum()


# In[122]:


transaction.groupby(['product']).sum()


# In[123]:


df.groupby('left').sum()


# In[124]:


df.groupby('left').mean()


# In[125]:


df.groupby(['left', 'salary']).sum()
df.groupby(['left', 'salary']).mean()


# In[126]:


df.groupby(['left', 'salary']).sum()


# In[127]:


df.groupby(['left', 'salary']).mean()


# In[128]:


filt = (df['left'] == 1)
sum(filt)


# In[129]:


sum(filt)/ len(df)


# In[130]:


filt = (df['left'] == 1)
print(df.loc[filt, ['left','sales']])
a = df.loc[filt, ['left','sales']]

b = a.groupby(['sales']).sum() #計算各職位離職人數


# In[131]:


filt = (df['left'] == 0)
sum(filt)


# In[132]:


sum(filt)/ len(df)


# In[133]:


a = ['A','B','C']
for i in a:
    print(i)


# In[134]:


A


# In[135]:


print('A')


# In[136]:


a


# In[137]:


count = 0
for i in range(1,6,1):
    count += i
    print(count)


# In[138]:


for i in range(1,6,1):
    print(i)


# In[139]:


range(1,6,1):


# In[140]:


range(1,6,1)


# In[141]:


for i in range(5,0,-1):
    print(i)


# In[142]:


count = 1
for i in range(1,6,1):
    count += i
    print(count)


# In[143]:


for i in range(5,0,-1):
a


# In[144]:


for i in range(5,0,-1):
print("A")


# In[145]:


for i in range(5,0,-1):
    print(i)


# In[146]:


count = 0
for i in range(1,6,-1):
    count += i
    print(count)


# In[147]:


count = 0
for i in range(5,1,-1):
    count += i
    print(count)


# In[148]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[149]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]

    print(ironman)
print("---")


# In[150]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")


# In[151]:


print("\n") # 空一行方便閱讀

# 帶索引值的寫法
for index in list(range(len(ironmen))): # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[152]:


a = ['A','B','C']
for i in a:
    print(i)


# In[153]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看

print("\n") # 空一行方便閱讀

# 帶索引值的寫法
for index in list(range(len(ironmen))): # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[154]:


list(range(len(ironmen)))


# In[155]:


range(len(ironmen)))


# In[156]:


range(len(ironmen))


# In[157]:


if condition1: # 條件一
    statement1
elif condition2: # 條件二
    statement2
elif condition3: # 條件三
    statement3
else: # 其他情形
    statement4


# In[158]:



score = 70 # 設定成績變數

if score >= 60: # 60分以上及格
    print("及格！")
else: # 不符合以上條件的時候執行
    print("不及格！")


# In[159]:



score = 50 # 設定成績變數

if score >= 60: # 60分以上及格
    print("及格！")
else: # 不符合以上條件的時候執行
    print("不及格！")


# In[160]:


# 加入elif敘述

score = 70 # 設定成績變數

if (score > 80):
    print("A")
elif (score >= 70) & (score < 80): # 加上括號分群幫助易讀
    print("B")
elif (score >= 60) & (score < 70):
    print("C")
else:
    print("F")


# In[161]:


# 加入elif敘述

score = 70 # 設定成績變數

if (score > 80):
    print("A")
elif (score >= 70): # 加上括號分群幫助易讀
    print("B")
elif (score >= 60):
    print("C")
else:
    print("F")


# In[162]:


# 加入elif敘述

score = 60 # 設定成績變數

if (score > 80):
    print("A")
elif (score >= 70): # 加上括號分群幫助易讀
    print("B")
elif (score >= 60):
    print("C")
else:
    print("F")


# In[163]:


score = 64


# In[164]:


if (score > 80):
    print("A")
elif (score >= 70): # 加上括號分群幫助易讀
    print("B")
elif (score >= 60):
    print("C")
else:
    print("F")


# In[165]:


# break 描述
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    if (ironman < 10):
        break
    else:
        print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看
print("\n") # 空一行方便閱讀
# continue 描述
for ironman in ironmen:
    if (ironman < 10):
        continue
    else:
        print(ironman)

print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[166]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看

print("\n") # 空一行方便閱讀

# 帶索引值的寫法
for index in list(range(len(ironmen))): # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[167]:


# break 描述
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    if (ironman < 7):
        break
    else:
        print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看
print("\n") # 空一行方便閱讀
# continue 描述
for ironman in ironmen:
    if (ironman < 10):
        continue
    else:
        print(ironman)

print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[168]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看

print("\n") # 空一行方便閱讀

# 帶索引值的寫法
for index in list(range(len(ironmen))): # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[169]:


def Function_Name(Parameter):
     """
     Introduction
     """
     Main Code
     Return

Example:


# In[170]:


def Function_Name(Parameter):
     """
     Introduction
     """
     Main Code
     Return



# In[171]:


def sum_three(a,b,c):
    '''
    This function will sum all the numbers in the parameters.
    '''
    output = a + b + c
    print('sum =',output)
    return output


# In[172]:


# 呼叫函式
sum_three(3,6,9)


# In[173]:


x = 10
# Function內使用全域變數
def example():
    global x
    print(x + 5)
example()


# In[174]:


x = sum_three(3,6,9)
x


# In[175]:


# 加法
def plus(x,y):
    p = x + y
    return p


# In[176]:


def minus(x,y):
    m = x - y
    return m


# In[177]:


# 乘法
def multiply(x,y):
    mul = x * y
    return mul


# In[178]:


# 除法
def divide(x,y):
    div = x / y
    return div


# In[179]:


plus(6,3)
minus(6,3)
multiply(6,3)
divide(6,3)


# In[180]:


plus(6,3)


# In[181]:



minus(6,3)


# In[182]:



multiply(6,3)


# In[183]:


help(sum_three)


# In[184]:


Fahrenheit = (Celsius * 9/5) + 32


# In[185]:


def Celsius_to_Fahrenheit(celsius = 0):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, 'Celsius is equivalent to', fahrenheit, 'Fahrenheit')
    return fahrenheit

f = Celsius_to_Fahrenheit(40)

f


# In[186]:


Fahrenheit = (Celsius * 9/5) + 32


# In[187]:


# 不帶索引值的寫法
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    print(ironman)
print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看

print("\n") # 空一行方便閱讀

# 帶索引值的寫法
for index in list(range(len(ironmen))): # 產生出一組 0 到 5 的 list
    print(ironmen[index])
print("---")
print(index) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[188]:


import math # 要使用 pi 得引入套件 math

# 定義自訂函數
def circle_calculate(radius, area = True):
    '依據輸入的半徑與 area 參數計算圓形的面積或周長' # 單行的 docstring
    circle_area = math.pi * radius**2
    circle_circum = 2 * math.pi * radius
    if area == True:
        return circle_area
    else:
        return circle_circum

# 呼叫自訂函數
my_radius = 3
print(circle_calculate(my_radius)) # 預設回傳面積
print(circle_calculate(my_radius, area = False)) # 指定參數回傳周長


# In[189]:


import pandas as pd # 引用套件並縮寫為 pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
# 截至 2016-12-11 上午 11 時第 8 屆 iT 邦幫忙各組的鐵人分別是 54、8、18、14、6 與 65 人
ironmen = [54, 8, 18, 14, 6, 65]

ironmen_dict = {"groups": groups,
                "ironmen": ironmen
                }

ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df.dtypes) # ironmen_df 有 dtypes 屬性
ironmen_df.head(n = 3) # ironmen_df 有 head() 方法


# In[190]:


sum_three(3,6)


# In[191]:


def sum_three(a=1,b=2,c=3):
    '''
    This function will sum all the numbers in the parameters.
    '''
    output = a + b + c
    print('sum =',output)
    return output

sum_three(3,6)


# In[192]:


sum_three(3,6,3)


# In[193]:


sum_three(3,6,2)


# In[194]:


sum_three()


# In[195]:


變數範圍
x = 10
# Function內使用全域變數
def example():
    global x
    print(x + 5)
example()


# In[196]:


#變數範圍
x = 10
# Function內使用全域變數
def example():
    global x
    print(x + 5)
example()


# In[197]:


#回傳值
x = sum_three(3,6,9)
x


# In[199]:



def Celsius_to_Fahrenheit(celsius = 0):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, 'Celsius is equivalent to', fahrenheit, 'Fahrenheit')
    return fahrenheit

f = Celsius_to_Fahrenheit(40)

f


# In[200]:


celsius


# In[201]:



def Celsius_to_Fahrenheit(celsius = 0):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, 'Celsius is equivalent to', fahrenheit, 'Fahrenheit')
    return fahrenheit

f = Celsius_to_Fahrenheit(60)

f


# In[202]:


import math # 要使用 pi 得引入套件 math

# 定義自訂函數
def circle_calculate(radius, area = True):
    '依據輸入的半徑與 area 參數計算圓形的面積或周長' # 單行的 docstring
    circle_area = math.pi * radius**2
    circle_circum = 2 * math.pi * radius
    if area == True:
        return circle_area
    else:
        return circle_circum

# 呼叫自訂函數
my_radius = 3
print(circle_calculate(my_radius)) # 預設回傳面積
print(circle_calculate(my_radius, area = False)) # 指定參數回傳周長


# In[203]:


print(circle_calculate(3))


# In[204]:


import pandas as pd # 引用套件並縮寫為 pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
# 截至 2016-12-11 上午 11 時第 8 屆 iT 邦幫忙各組的鐵人分別是 54、8、18、14、6 與 65 人
ironmen = [54, 8, 18, 14, 6, 65]

ironmen_dict = {"groups": groups,
                "ironmen": ironmen
                }

ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df.dtypes) # ironmen_df 有 dtypes 屬性
ironmen_df.head(n = 3) # ironmen_df 有 head() 方法


# In[205]:


2+3


# In[206]:


2-3


# In[207]:



2*3


# In[ ]:




