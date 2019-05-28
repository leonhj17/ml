# _*_ encoding:utf-8 _*_
import pandas as pd
import numpy as np


class Heatsurfaceinfo:
    """存储受热面壁温测点信息"""
    def __init__(self, name=None, pnum=None, gnum=[], info=None):
        self.name = name
        self.pnum = pnum
        self.gnum = gnum
        self.info = info

    # 获取屏间管，可多管
    def getPj(self, gnum=None):
        """gnum输入list类型数据"""
        data = self.info
        return data[data.gnum.isin(gnum)]

    # 获取同屏管，可多屏
    def getTp(self, pnum=None):
        """pnum输入list类型数据"""
        data = self.info
        return data[data.pnum.isin(pnum)]

    # 获得测点温度二维数组
    def matrix(self):
        mat = np.zeros([self.gnum, self.pnum])
        for index, value in self.info.iterrows():
            mat[value.gnum-1, value.pnum-1] = value.tvalue
        return mat

    # 将数组形式的壁温写入到excel
    def matrix_to_excel(self):
        mat = self.matrix()
        df = pd.DataFrame(index=['第'+ str(i) + '管' for i in range(1,self.gnum+1)],
                          columns=['第'+ str(i) + '屏' for i in range(1,self.pnum+1)],
                          data=mat)
        from openpyxl import Workbook
        from openpyxl.utils.dataframe import dataframe_to_rows
        wb = Workbook()
        ws = wb.active
        for r in dataframe_to_rows(df, index=True, header=True):
            ws.append(r)
        wb.save('matrix.xlsx')

    # 分析屏间管中异常数据
    def pj_abnormal(self):
        pass

    def update(self):
        pass
