import pandas as pd

#导入数据
inputFile='D:\Python\PythonBasicAlgorithm\winequality-both.csv'
wine=pd.read_csv(inputFile)

#将'tpye'和'quality'字段以外的字段进行标准化
#去除'tupe'和'quality'字段
wineInd=wine[wine.columns.difference(['type','quality'])]

#z-score标准化
wineIndZScore=(wineInd-wineInd.min())/(wineInd.max()-wineInd.min())
print(wineIndZScore.head(5))