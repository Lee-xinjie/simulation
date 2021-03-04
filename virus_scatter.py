import numpy as np
import matplotlib.pyplot as plt
# 地图长度
length = 100
# 总人口
pop = 2000
# 初始病人数量
n = 10
# 感染半径
sd = 5
# 感染几率 50%
sr = 0.5
# 个人
class People(object):
    def __init__(self):
    	# 随机坐标  根据给定维度生成[0,1)之间的数据
        self.x = np.random.rand() * length
        self.y = np.random.rand() * length
        self.loc = np.array([self.x, self.y])
        self.color = 'g'

    # 随机运动  randn函数返回样本，具有标准正态分布
    def move(self):
        self.x += np.random.randn()
        self.y += np.random.randn()
# 人群
all_people = np.array([People() for i in range(pop)])

# 初始化患病人群
sick_people = np.random.choice(all_people, size=n, replace=False)
for p in sick_people:
    p.color = "r"
# 病毒感染函数  """如果健康人群和患病人群距离小于感染半径，则被感染"""
def affect_virus(all_people):
    sick_people = []
    healthy_people = []
    n = 0
    for p in all_people:
        if p.color == "r":
            sick_people.append(p)
            n += 1
        if p.color == "g":
            healthy_people.append(p)

    for sp in sick_people:
        for hp in healthy_people:
            dist = np.linalg.norm(sp.loc - hp.loc)
            rad = np.random.rand()
            if hp.color == "g" and dist <= sd and rad < sr:
                hp.color = "r"
                n += 1
    return n
#绘图
plt.ion()
while n < pop:
    plt.clf()

    n = affect_virus(all_people)
    plt.scatter([p.x for p in all_people], [p.y for p in all_people], c=[p.color for p in all_people], s=3)

    plt.axis([0, length, 0, length])
    plt.pause(0.1)
    print("总人数：{}，传染人数：{}".format(pop, n))

plt.ioff()
plt.show()
