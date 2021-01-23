import pandas as pd

#最小最大标准化
inputFile='D:\Python\PythonBasicAlgorithm\winequality-both.csv'
wine=pd.read_csv(inputFile)

#将'tpye'和'quality'字段以外的字段进行标准化
#去除'tupe'和'quality'字段
wineInd=wine[wine.columns.difference(['type','quality'])]

#min-max标准化
wineIndMinMax=(wineInd-wineInd.mean())/wineInd.std()
print(wineIndMinMax.head(5))

