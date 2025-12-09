import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("demo.xlsx")


#df2 = df.groupy("市区").sum()
plt.figure(figsize=(10,5))

plt.bar(df.市区, df.台风)
plt.title("2020年各地市台风预警情况")
plt.xlabel("地市")
plt.ylabel("台风预警次数")
plt.rcParams['font.size'] = 22
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

plt.savefig("c04.03.weather2.pdf",pad_inches=0.01,bbox_inches='tight')
plt.show()