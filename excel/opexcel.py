# _*_ encoding:utf-8 _*_
from openpyxl import load_workbook
import re
import pandas as pd

wb = load_workbook("regularization.xlsx")
sheet = wb.active

data = pd.DataFrame(columns=['kks', 'surface', 'pnum', 'gnum'])

for row in sheet.rows:
    dic = dict()
    # row为元组数据结构,根据单元格顺序来获取相关内容
    dic['kks'] = row[0].value

    # 采用正则化表达式获取受热面名称,屏号,管号
    reg = re.search('(末级过热器|末级再热器)\w*第(\d*)屏\w*第(\d*)管', row[1].value)

    # 匹配结果为元组数据结构，根据组号来获取匹配项
    dic['surface'] = 'finish' if reg.groups()[0] == '末级过热器' else 'reheater'
    dic['pnum'] = reg.groups()[1]
    dic['gnum'] = reg.groups()[2]

    # 对DateFrame数据结构添加行
    data = data.append(dic, ignore_index=True)

# 设置kks列为index
data = data.set_index(['kks'])
print(data[data['surface']=='finish'])
