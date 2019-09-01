import matplotlib.pyplot as plt

#s为尺寸指定大小
#x_value = [0,1,2,3,4,5]或者是如下的形式
x_value = list(range(0,101))
y_value = [x**3 for x in x_value]
#edgecolors表示点的边框颜色，c表示颜色，cmp表示映射较大值为深色，较小值为浅色
plt.scatter(x_value,y_value,s=40,edgecolors='None',c=y_value,cmap=plt.cm.Blues)

plt.title("Spot picture",fontsize=24)
plt.xlabel('value',fontsize=14)
plt.ylabel('Square_value',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

#设置两条坐标轴的取值范围
plt.axis([0,150,0,1500000])
plt.savefig('dateprocess2.png',bbox_inches='tight')
plt.show()

#隐藏坐标轴
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)

#保存图表
# 第一个参数是保存的文件名，这句必须在show之前使用，否则生成的图片是空白
# 第二个参数是使生成的图片紧凑，不会出现显示不全的情况
#plt.savefig('dateprocess2.png',bbox_inches='tight')