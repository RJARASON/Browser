import matplotlib.pyplot as plt

Activities=['School','Study','Play','Sleep','Others']
Time_spent=[6,4,1.5,8,4.5]
color=['c','g','y','m','hotpink','#32a8a8']

fig,axs=plt.subplots(nrows=2,ncols=2,figsize=(10,8))

axs[0,0].plot(Activities,Time_spent)
axs[0,0].set_title('Subplot 1 line graph')

axs[0,1].scatter(Activities,Time_spent)
axs[0,1].set_title('Subplot 2 scatter graph')

axs[1,0].bar(Activities,Time_spent)
axs[1,0].set_title('Subplot 3 bar graph')

axs[1,1].pie(Time_spent,labels=Activities,colors=colors,
             startangle=90,
             explode=(0,0.1,0.5,0.25,0.5),
             autopct='%1.1f%%')
axs[1,1].set_title('Subplot 4 pie chart')

plt.tight_layout()

plt.show()
