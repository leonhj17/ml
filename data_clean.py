# _*_ encoding:utf-8 _*_
import pandas as pd
import numpy as np

df = pd.DataFrame({'A':['a0','a1','a1','a2','a3','a4'],
                   'B':['b0','b1','b2','b2','b3',None],
                   'C':[1,2,None,3,4,5],
                   'D':[0.1,10.2,11.4,8.9,9.1,12],
                   'E':[10,19,32,25,8,None],
                   'F':['f0','f1','g2','f3','f4','f5']})

# 根据上下四分卫数来删除异常值
upper = df['D'].quantile(0.75)
lower = df['D'].quantile(0.25)
q_int = upper - lower
df[[df['D']>lower-1.5*q_int][df['D']<upper+1.5*q_int]]

# 根据字符串开头来删除异常值，注意列表表达式语法
df[[True if item.startwith('f') else False for item in df['F'].values]]

# 采用E列均值来填充空值
df.fillna(df['E'].mean())
