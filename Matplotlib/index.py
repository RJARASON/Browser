import matplotlib.pyplot as plt

x1=['Country','Population','Yearly change','Net Change','Density','Land Area (KM)','Migrants','Fert Rates','Med Age','Urban Pop','World share']
x2=["China", "1,411,778,724", "0.03 %", "4,493,564", "12,307", "9,596,961", "7,046,433", "2.0", "38", "60.3 %", "16.56 %"]
x3=["United States", "331,883,986", "0.18 %", "596,182", "1,633", "9,525,067", "328,295", "1.8", "79", "82.4 %", "18.89 %"],

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.bar(x1, x2, color='blue')
plt.title('Population Data')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')

plt.subplot(2, 1, 2)
plt.plot(x1, x3, color='green', marker='o')
plt.title('Population Data')
plt.ylabel('Values')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()