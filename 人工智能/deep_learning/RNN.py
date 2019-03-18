#在语音识别和语言模型，机器翻译方面表现突出
#他的输入层来 x层和它上一个时刻的输出
#卷积神经网络在不同空间共享参数，循环神经网络在不同时间共享参数
#训练方法为  沿时间反响传播
#以机器翻译为列:
#带翻译的句子为ABCD
#循环神经网路第一段每一个时刻输入的分别是A，B，C，D，，然后用'_'作为带翻译句子的结束符
#从结束符开始，进行翻译，每一刻的输入就是上一次的输出

#循环神经网络向前传播过程
import numpy as np
X = [1,2]
state = [0.0,0.0]
#分开定义不同部分的权重和方便操作
w_cell_state = np.asarray([[0.1,0.2],[0.3,0.4]])
w_cell_input = np.asarray([0.5,0.6])
b_cell = np.asarray([0.1,-0.1])

#定义输出的全连接参数
w_output= np.asarray([[1.0],[2.0]])
b_output = 0.1
#按照时间顺序执行循环神经网络向前椽笔过程
for i in range(len(X)):
    #计算循环体中全连接神经网咯
    before_activation = np.dot(state,w_cell_state) + X[i] * w_cell_input + b_cell
    state = np.tanh(before_activation)

    #根据当前时刻计算最终输出
    final_output = np.dot(state,w_output) + b_output

    #输出每个时刻的信息
    print('before activation:',before_activation)
    print('state:',state)
    print('output:',final_output)

