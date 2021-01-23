from scipy.stats import kendalltau

x = [0.5, 0.4, 0.6, 0.3, 0.6, 0.2, 0.7, 0.5]
y = [0.6, 0.4, 0.4, 0.3, 0.7, 0.2, 0.5, 0.6]
print(kendalltau(x, y))

# 输出:(r, p)
# r:相关系数[-1，1]之间
# p:p值越小