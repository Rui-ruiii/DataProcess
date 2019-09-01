import matplotlib.pyplot as plt
from random import choice
class RandomWalk():
    """只有两个方法，前者设置点数等属性，后者计算所经过的所有点"""

    def __init__(self,point_number=5000):
        """初始化随机漫步的属性,指定点数（长度范围）为5000，所有的随机漫步都始于（0，0）"""
        self.point_number = point_number
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.point_number:

            #决定前进方向以及沿这个方向前进的距离,-1是左，1是右
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance
            y_direction = choice([-1,1])
            y_distance = choice([0, 1, 2, 3, 4, 5,6,7,8])
            y_step = y_direction * y_distance

            #不能原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的距离
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

#记得在定义对象的时候，类名的括号不能丢，否则会出现
# missing 1 required positional argument: 'self'的错误提示
# 再有就是如果方法的属性定义中除了self还有别的属性，那么在调用方法时，要对这个属性进行参数的定义
Rw = RandomWalk()
Rw.fill_walk()
plt.scatter(Rw.x_values,Rw.y_values,s=15)
plt.show()