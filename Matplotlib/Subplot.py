import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.suptitle('2 subplots')

sub=['maths','science','lang1','lang2']
m1=[70,90,50,60]
m2=[60,70,80,90]

plt.subplot(1,2,2)
plt.bar(sub,m1,color="c")
plt.title('Subplot 1')
plt.ylabel('marks')

plt.subplot(1,2,1)
plt.bar(sub,m2,color="m")
plt.title('subplot 2')
plt.xlabel('subjects')
plt.ylabel('marks')

plt.show()