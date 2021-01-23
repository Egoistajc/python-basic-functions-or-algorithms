target = [1.5, 2.1, 3.3, -4.7, -2.3, 0.75]
prediction = [0.5, 1.5, 2.1, -2.2, 0.1, -0.5]

error = []
for i in range(len(target)):
    error.append(target[i] - prediction[i])
squaredError = []
absError = []
for val in error:
    squaredError.append(val * val)  # target-prediction之差平方
    absError.append(abs(val))  # 误差绝对值
from math import sqrt

print("绝对平均偏差 = ", sum(absError) / len(absError))  # 平均绝对误差MAE
targetDeviation = []
targetMean = sum(target) / len(target)  # target平均值
for val in target:
    targetDeviation.append((val - targetMean) * (val - targetMean))
print("方差 = ", sum(targetDeviation) / len(targetDeviation))  # 方差
print("标准差 = ", sqrt(sum(targetDeviation) / len(targetDeviation)))  # 标准差