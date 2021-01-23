import pandas as pd
import numpy as np

#导入数据
inputFile='D:\Python\PythonBasicAlgorithm\winequality-both.csv'
wine=pd.read_csv(inputFile)

#将'tpye'和'quality'字段以外的字段进行标准化
#去除'tupe'和'quality'字段
wineInd=wine[wine.columns.difference(['type','quality'])]

#小数定标
wineIndNDS=wineInd/10**np.ceil(np.log10(wineInd.abs().max()))
print(wineIndNDS.head(5))

wineInd/10**np.ceil(np.log10(wineInd.abs().max()))