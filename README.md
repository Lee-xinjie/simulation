# Simulation program of COVID-19 transmission
本次使用Python创建了一个新冠病毒在人群中传播的计算机仿真模型，并使用matplotlib绘图的程序.通过传播数据分析来评价一些疫情防治措施对遏制病毒传播的作用，并针对不同场景给出防疫建议。  

本次设计思路：人群分布设定在某一特定区域（商业中心）随机分布,人员活动则使用标准正态分布.当认为传染者和正常人的距离缩小到一定范围后,正常人就被感染。  
  
采用面向对象的方式，每个人为一个独立对象，通过遍历所有对象：更新人群移动位置），计算当前对象到其他所有人的相对距离，根据距离，感染率等因素，改变人群当前的状态（正常/患病）。  
  
+ 可以根据人口密度、防疫措施等因素更改参数，查看疫情传染效率，进而判断防疫措施的不同效果。   
```python
# 地图长度
length = 100
# 总人口
pop = 2000
# 初始病人数量
n = 10
# 传染半径
infect_distance = 5
# 传染几率 50%
infect_rate= 0.5
```
![image text](https://github.com/Lee-xinjie/simulation/blob/main/1.png)
![image text](https://github.com/Lee-xinjie/simulation/blob/main/result.png)
