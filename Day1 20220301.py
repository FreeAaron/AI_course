#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(2+3)


# In[3]:


print(2 + 3)

print(2 3)

print(2 * 3)

print(10 / 2)

print(3 ** 2) # R 語言使用 3 ^ 2

print(10 % 4) # R 語言使用 10 %% 4


# In[5]:


print(2 + 3)

print(2-3)

print(2 * 3)

print(10 / 2)

print(3 ** 2) # R 語言使用 3 ^ 2

print(10 % 4) # R 語言使用 10 %% 4


# In[6]:


print(type(5))#'int'


# In[7]:


print(type(5))#'int'


# In[8]:


print(type(5))#'int'


# In[9]:


print(type(5))#'int'
print(type(5.5))#'float'
print(type(5+3j))#'complex'


# In[10]:


print(type(True))#'bool'print(type(flase))#'bool'


# In[13]:


print(type(5))
# '
print(type(5.5))
# '
print(type(5 + 3j))
# '
print(type(True))
print(type(False)) # '
print(1.0 == True)
#
True
print(0 == False) # True
print(1.2 + True)
# 2.2
print(3 + True * 2)
# 5


# In[15]:


print(type(5))
# '
print(type(5.5))
# '
print(type(5 + 3j))
# '
print(type(True))
print(type(False)) # '
print(1.0 == True)
#
True
print(0 == False) # True
print(1.2 + True)
# 2.2
print(3 + True * 2)
# 5


# In[17]:


my_bool= True
print(type(my_bool )) # '
print(float(my_bool )) # 1.0
print(int(my_bool )) # 1
print(complex(my_bool )) # 1+0j
print(type(str(my_bool ))) # '


# In[18]:


print(type(5))

print(type(5.5))

print(type(5 + 3j))

print(type(True))
# ' print(type(False)) # '
print(1.0 == True)

print(0 == False) # True
print(1.2 + True)
# 2.2
print(3 + True * 2)
# 5


# In[20]:


participated_group='Bid Data'
current_ttl_articles = 4
is_participating = True

my_status = [participated_group,current_ttl_articles,is_participating]

print(type(my_status[0]))
print(type(my_status[1]))
print(type(my_status[2]))


# In[22]:


participated_group="Bid Data"
current_ttl_articles = 4
is_participating = True

#建立dictionary
my_status = {"group":participated_group,"ttl_articles":current_ttl_articles,"is_participating":is_participating}

#利用鍵值選擇元素
print(type(my_status[group]))
print(type(my_status[ttl_articles]))
print(type(my_status[is_participating]))


# In[24]:


participated_group="Bid Data"
current_ttl_articles = 4
is_participating = True

#建立dictionary
my_status = {"group":participated_group,"ttl_articles":current_ttl_articles,"is_participating":is_participating}

#利用鍵值選擇元素
print(my_status[group])
print(my_status[ttl_articles])
print(my_status[is_participating])


# In[28]:


participated_group="Bid Data"
current_ttl_articles = 4
is_participating = True

#建立dictionary
#my_status = {"group":participated_group,"ttl_articles":current_ttl_articles,"is_participating":is_participating}

#利用鍵值選擇元素
print(my_status["group"])
print(my_status["ttl_articles"])
print(my_status["is_participating"])


# In[30]:


participated_group="Bid Data"
current_ttl_articles = 4
is_participating = True

#建立dictionary
my_status = {"group":participated_group,"ttl_articles":current_ttl_articles,"is_participating":is_participating}

#利用鍵值選擇元素
print(my_status["group"])
print(my_status["ttl_articles"])
print(my_status["is_participating"])


# In[31]:


import numpy as np

my_np_array = np.array([1,2,3,4])
print(my_np_array ** 2)


# In[33]:


my_2d_array = np.array([[1,3],
                       [2,4]])
print(my_2d_array ** 2)


# In[39]:


import numpy as np
ironmen = np.array([46, 8, 11, 11, 4, 56])
print(ironmen[0]) # 選出 Modern Web 組的鐵人數
print(ironmen > 10) # 哪幾組的鐵人數超過 10 人
print(ironmen[ironmen > 10]) # 超過 10 人的鐵人數

import numpy as np
ironmen_2d_array = np.array([[46, 11, 4],
[8, 11, 56]])
print(ironmen_2d_array.size) # 6
print(ironmen_2d_array.shape) # (2, 3)


# In[41]:


import pandas as pd # 引用套件並縮寫為 pd
groups = ["Modern Web", "DevOps", "Cloud", "Big Data",
"Security", "自我挑戰組"]
ironmen = [46, 8, 12, 12, 6, 58]
ironmen_dict = {"groups": groups,
"ironmen": ironmen
}
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df) # 看看資料框的外觀
print(type(ironmen_df)) # pandas.core.frame.DataFrame


# In[46]:


import pandas as pd
groups = ["Modern Web", "DevOps", "Cloud", "Big Data",
"Security", "自我挑戰組"]
ironmen = [46, 8, 12, 12, 6, 58]
ironmen_dict = {"groups": groups,
"ironmen": ironmen
}
ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df[ironmen_df.loc[:,"ironmen"] > 10])
# 選出鐵人數超過 10 的 data frame


# In[47]:


import pandas as pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen = [46, 8, 12, 12, 6, 58]

ironmen_dict = {"groups": groups,
                "ironmen": ironmen  }

ironmen_df = pd.DataFrame(ironmen_dict)

print(ironmen_df.shape) # 回傳列數與欄數
print("---")
print(ironmen_df.describe()) # 回傳描述性統計
print("---")
print(ironmen_df.head(3)) # 回傳前三筆觀測值
print("---")
print(ironmen_df.tail(3)) # 回傳後三筆觀測值
print("---")
print(ironmen_df.columns) # 回傳欄位名稱
print("---")
print(ironmen_df.index) # 回傳 index


# In[48]:


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


# In[49]:


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


# In[50]:


'hello world!'
"hello world!"


# In[51]:


'hello world!'


# In[52]:



"hello world!"


# In[53]:


print("'Welcome to Python.'")
print(type("'Welcome to Python.'"))
print('"Welcome to Python."')
print(type('"Welcome to Python."'))


# In[54]:



print('C:\some\name')  
print('C:\\some\\name')
print(r'C:\some\name') 


# In[55]:



print('C:\some\name')  


# In[56]:


print("Hello" + "World")
print("Hi" * 3)
print("Hello World"[0:7]) 
print(len("Hello World"))


# In[57]:


print("Hello World"[0:8]) 


# In[58]:


print("HelloWorld"[0:7]) 


# In[59]:


print(len("Hello"))


# In[60]:


print("Hello World"[0:0
            ]) 


# In[61]:


print("Hello World"[0:0]) 


# In[62]:


print("Hello World"[0:1]) 


# In[63]:


print("Hello World"[1:1]) 


# In[64]:


print("Hello World"[1:2]) 


# In[65]:


print("Hello World"[1:3]) 


# In[66]:


print(type(1))
print(type(1.0))
print(type(1+2j))
print(type(complex(1,2)))

print(str(0))
print(str(1.9))


# In[67]:


print(int(1.9)) 
print(int("0")) 
print(float(1))
print(type(str(0)))
print(type(str(1.9)))
print(type(int(1.9)))
print(type(int("0")))
print(type(float(1)))


# In[68]:


int("hello")


# In[69]:


int("1.1")


# In[70]:


int(1.1)


# In[71]:


print(1+2)
print(3-4)
print(5*2)
print(9/7)
print((1+3)*(2-4))
print(1+3*2-4) 
print(3**2) 
print(5//3) 
print(5%3) 


# In[72]:


print(9/7)


# In[73]:


print((1+3)*(2-4))
print(1+3*2-4) 


# In[74]:


a = 7
# 在Python裡宣告一個變數

a = 7 
print(a*3) 
# 宣告變數a
# 進行基本運算
a = a*5 
print(a)


# In[75]:


a=[1,2,3,4,5]
a


# In[76]:


a=[1,2,3,4,5]


# In[77]:


a=[1,2,3,4,5]
a


# In[78]:


a=[1,2,3,4,5]


# In[79]:


a=[1,2,3,4,5]


# In[80]:


a=[1,2,3,4,5]
a


# In[81]:


a[3]


# In[82]:


print(len(a))


# In[83]:


a.pop()
a


# In[84]:


a.pop()
a


# In[85]:


a.append(1)
a


# In[86]:


a.remove(2)
a


# In[87]:


a.sort()
a


# In[88]:


a.append(5)
a


# In[89]:


a.reverse()
a


# In[90]:


alphabet = {
    "a":"apple",
    "b":"ball",
    "c":"cat",
    "d":"dog",
    "e":"elephant"
}

print(alphabet["a"])


# In[91]:


alphabet = {
    "a":"apple",
    "b":"ball",
    "c":"cat",
    "d":"dog",
    "e":"elephant"
}

print(alphabet["a"])
print(alphabet["b"])


# In[98]:


alphabet = dict(
    a="apple",
    b="baldfsdfl",
    c="cat",
    d="dasdsadsaog",
    e="elephant"
)

print(alphabet["a"])


# In[93]:


alphabet["f"] = "frog" 
alphabet["a"] = "ant" 

print(alphabet["a"])
print(alphabet)


# In[99]:


alphabet["f"] = "frog" 
alphabet["a"] = "anasdsadsajkhkj" 

print(alphabet["a"])
print(alphabet)


# In[100]:


new_dict = {
    "e":"egg",
    "g":"good",
    "h":"hello"
}

alphabet.update(new_dict) # 更新的資料需為字典型態
print(alphabet)


# In[101]:


del alphabet["a"] 
print(alphabet)
# 刪除資料


# In[102]:


print(len(alphabet))
print(alphabet.keys())
print(alphabet.values())
print(alphabet.items())


# In[103]:


import pandas as pd
transaction = pd.read_csv('C:/Users/taylorwang/Desktop/產業尖兵教材/transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[104]:


import pandas as pd
transaction = pd.read_csv('C ‪C:\Users\maaro\Downloads\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[105]:


import pandas as pd
transaction = pd.read_csv('‪C:\Users\maaro\Downloads\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[106]:


import pandas as pd
transaction = pd.read_csv('C:\Users\maaro\Downloads\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[107]:


member = pd.DataFrame(data)
member


# In[108]:


import pandas as pd
transaction = pd.read_csv('C:/Users/maaro/Downloads/transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[109]:


import pandas as pd
transaction = pd.read_csv(' C:\Users\maaro\Downloads\transaction ().csv ')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[110]:


import pandas as pd
transaction = pd.read_csv(' C:/Users/maaro/Downloads/transaction ().csv ')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[111]:


import pandas as pd
transaction = pd.read_csv(r' C:\Users\maaro\Downloads\transaction ().csv ')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[112]:


import pandas as pd
transaction = pd.read_csv(r' C:\Users\maaro\OneDrive\桌面\transaction.csv ')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[113]:


import pandas as pd
transaction = pd.read_csv(r'‪C:\Users\maaro\OneDrive\文件\transaction.csv ')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[114]:


import pandas as pd
transaction = pd.read_csv(r'‪ C:\Users\maaro\Downloads\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[115]:


import pandas as pd
transaction = pd.read_csv('‪C:/Users/maaro/Downloads/transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[116]:


import pandas as pd
transaction = pd.read_csv(r'‪ C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[117]:


import pandas as pd
transaction = pd.read_csv('‪C:/Users/maaro/iCloudDrive/進修之路/AI/王子廌/transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[1]:


import pandas as pd
#transaction = pd.read_csv('C:/Users/taylorwang/Desktop/產業尖兵教材/transaction.csv')
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[2]:


import pandas as pd
#transaction = pd.read_csv('C:/Users/taylorwang/Desktop/產業尖兵教材/transaction.csv')
transaction = pd.read_csv(r'C:\Users\maaro\iCloudDrive\進修之路\AI\王子廌\transaction.csv')

data = {'uid':[1,2,3,4,5],
        'name':['Howard','Lily','Kai',
                'Jojo','Ivan'],
        'age':[25,21,35,18,15]}

transaction

data


# In[3]:


print(transaction)


# In[4]:


member = pd.DataFrame(data)
member


# In[5]:


print(transaction)


# In[6]:


member.head()


# In[7]:


member.info()


# In[8]:


member.shape


# In[9]:


member['name']


# In[10]:


member[ ['name','age'] ]


# In[11]:


member['age'].mean()


# In[12]:


member['age'].max()


# In[13]:


member['age'].min()


# In[14]:


member['age'].describe()


# In[15]:


member['age'].sort_values()


# In[16]:


member['age'].sort_values(ascending = False)


# In[17]:


member.sort_values(['age'])


# In[18]:


member2 = member.drop(columns=['uid'])


# In[19]:


member2


# In[20]:


transaction['product'] == 'lemon'


# In[21]:


member.values.tolist()


# In[22]:


member


# In[23]:


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


# In[24]:


# break 描述
ironmen = [49, 8, 12, 12, 6, 61]
for ironman in ironmen:
    if (ironman < 10):
        break
    else:
        print(ironman)


# In[25]:


print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看
print("\n") # 空一行方便閱讀
# continue 描述


# In[26]:


print(ironman)


# In[27]:


# continue 描述
for ironman in ironmen:
    if (ironman < 10):
        continue
    else:
        print(ironman)

print("---")
print(ironman) # 把迴圈的迭代器（iterator）或稱游標（cursor）最後的值印出來看看


# In[28]:


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


# In[29]:


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


# In[ ]:




