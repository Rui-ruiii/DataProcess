from RandomWalk1 import RandomWalk
from matplotlib import pyplot as plt

while True:
    Rw = RandomWalk()
    Rw.fill_walk()

    #设置窗口尺寸
    plt.figure(figsize=(10,6))
    #用颜色表示路径
    point_numbers = list(range(Rw.point_number))
    plt.scatter(Rw.x_values,Rw.y_values,s=15,c=point_numbers,cmap=plt.cm.Blues)

    #突出起点和终点!!!为什么-1和1能表示起点和终点呢？
    plt.scatter(0,0,c='Green',s=40,edgecolors='none')
    plt.scatter(Rw.x_values[-1],Rw.y_values[1],c='red',s=40,edgecolors='none')

    plt.show()
    keep_running = input("Make Another Walk? (y/n):")
    if keep_running == 'n':
        break
    else:
        continue
