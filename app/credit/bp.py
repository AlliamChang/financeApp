# -*- coding:utf-8 -*-

import cPickle as pickle
import random
import math

# 参数
num = 7
m = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
var = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
w = [0] * int(math.pow(2, num))
# 记录上一步的参数
m_temp = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
var_temp = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
w_temp = [0] * int(math.pow(2, num))


# 神经网络计算违约概率 然后转换为额度
def net(x):
    # load_param()
    y = [0] * 8
    y[0] = 0.25 * x[0] + 0.25 * x[1] + 0.5 * x[2]
    y[1] = 0.17 * x[3] + 0.27 * x[4] + 0.38 * x[5] + 0.18 * x[6]
    y[2] = 0.25 * x[7] + 0.33 * x[8] + 0.42 * x[9]
    y[3] = 0.75 * x[10] + 0.25 * x[11]
    y[4] = 0.65 * x[12] + 0.35 * x[13]
    y[5] = 0.67 * x[14] + 0.33 * x[15]
    y[6] = x[16]
    # y[7] = x[17]  # 是否违约
    return round(random.uniform(1, 10), 2)
    # return round(f(y)*100)


# 高斯函数
def guass(y, i, j):
    return math.exp(-math.pow((y[i] - m[i][j]) / var[i][j], 2))


# 正则化
def normal(y, i, j):
    return guass(y, i, j) / (guass(y, i, 0) + guass(y, i, 1))


# 规则化
def rule(y, k):
    b = bin(k)
    l = len(b)
    result = 0
    for i in range(0, num):
        if i > l - 3:
            result *= normal(y, i, 0)
        else:
            result *= normal(y, i, b[l - 1 - i])

    return result


# 反模糊化 即f
def f(y):
    result = 0
    for i in range(0, int(math.pow(2, num))):
        result += w[i] * rule(y, i)
    return result


# 损失函数
def loss_func(y):
    y_input = [0] * (len(y) - 1)
    for i in range(len(y) - 1):
        y_input[i] = y[i]
    y_output = y[len(y) - 1]
    return math.pow(f(y_input) - y_output, 2) / 2


# 梯度函数 即损失函数关于参数求导 待定
# param_type 0:m 1:var 2:w
def grad_func(y, i, j, param_type):
    if param_type == 0:
        # return 0.1 * f(y) * m[i][j]
        return f(y) - w[i] * rule(y, i) + rule(y, i)
    elif param_type == 1:
        # return 0.2 * f(y) * var[i][j]
        return f(y) - w[i] * rule(y, i) + rule(y, i)
    else:
        return f(y) - w[i] * rule(y, i) + rule(y, i)


# 保存训练后参数
def dump_param():
    f1 = open('m.txt', 'wb')
    f2 = open('var.txt', 'wb')
    f3 = open('w.txt', 'wb')
    pickle.dump(m, f1)
    pickle.dump(var, f2)
    pickle.dump(w, f3)
    f1.close()
    f2.close()
    f3.close()


# 读取训练后参数
def load_param():
    f1 = open('m.txt', 'rb')
    f2 = open('var.txt', 'rb')
    f3 = open('w.txt', 'rb')
    global m, var, w, m_temp, var_temp, w_temp
    m = pickle.load(f1)
    m_temp = pickle.load(f1)
    var = pickle.load(f2)
    var_temp = pickle.load(f2)
    w = pickle.load(f3)
    w_temp = pickle.load(f3)
    f1.close()
    f2.close()
    f3.close()


# 迭代阀值，当两次迭代损失函数之差小于该阀值时停止迭代
epsilon = 0.0001
# 学习率
alpha = 0.01
# 最大迭代次数
max_iter = 100000


def bpTrain(y):
    cnt = 0
    while True:
        cnt += 1
        if cnt > max_iter:
            return
            # 用步长乘以损失函数的梯度，得到当前位置下降的距离
        # 确定是否所有的θi,梯度下降的距离都小于ε，如果小于ε则算法终止
        stop = True
        for i in range(len(m)):
            for j in range(2):
                delta = alpha * grad_func(y, i, j, 0)
                if m[i][j] - m_temp[i][j] > delta:
                    stop = False
                    break
        if stop:
            for i in range(len(var)):
                for j in range(2):
                    delta = alpha * grad_func(y, i, j, 1)
                    if var[i][j] - var_temp[i][j] > delta:
                        stop = False
                        break
        if stop:
            for i in range(len(w)):
                delta = alpha * grad_func(y, i, 0, 3)
                if w[i] - w_temp[i] > delta:
                    stop = False
                    break

        # 更新所有的θ
        if not stop:
            for i in range(len(m)):
                for j in range(2):
                    delta = alpha * grad_func(y, i, j, 0)
                    m_temp[i][j] = m[i][j]
                    m[i][j] = m[i][j] - delta

            for i in range(len(var)):
                for j in range(2):
                    delta = alpha * grad_func(y, i, j, 1)
                    var_temp[i][j] = var[i][j]
                    var[i][j] = var[i][j] - delta

            for i in range(len(w)):
                delta = alpha * grad_func(y, i, 0, 3)
                w_temp[i] = w[i]
                w[i] = w[i] - delta
        else:
            dump_param()
            return
