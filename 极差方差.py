# -*-coding:utf-8-*-
import time;
import random;


class Math:
    # 求极差
    @staticmethod
    def range(l):
        return max(l) - min(l);


    # 求方差
    @staticmethod
    def variance(l):  # 平方的期望-期望的平方
        s1 = 0;
        s2 = 0;
        for i in l:
            s1 += i ** 2;
            s2 += i;
        return float(s1) / len(l) - (float(s2) / len(l)) ** 2;

    # 求方差2
    @staticmethod
    def variance2(l):  # 平方-期望的平方的期望
        ex = float(sum(l)) / len(l);
        s = 0;
        for i in l:
            s += (i - ex) ** 2;
        return float(s) / len(l);

    # 主函数，测试


arr = [1, 2, 3, 2, 3, 1, 4];
print(Math.range(arr))
print(Math.variance(arr) )
print(Math.variance2(arr))


