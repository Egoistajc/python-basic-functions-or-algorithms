import numpy as np
vc=[1,2,39,0,8]
vb=[1,2,38,0,8]
print(np.mean(np.multiply((vc-np.mean(vc)),(vb-np.mean(vb))))/(np.std(vb)*np.std(vc)))
#corrcoef得到相关系数矩阵（向量的相似程度）
print(np.corrcoef(vc,vb))