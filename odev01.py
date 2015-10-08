import numpy as np
import matplotlib.pyplot as plt


d = np.random.uniform(0.5, 1.5, size = 2)
u = np.random.uniform( -5, 5, size = 2)
N = np.random.normal( u[0],  d[0], 1000)
M = np.random.normal(  u[1],  d[1], 1000)

Array1 = []   
Array2 = []   
Histogram1 = [0 for x in range(41)]
Histogram2 = [0 for x in range(41)]
x = [0 for x in range(41)]
for i in range(0,41):
    x[i]=-20+i
print x

sum1 =0
Histogram1_First_Element=0
Histogram2_First_Element=0

for i in N:
     Histogram1[ 21 + int(round(N[i])) ] = Histogram1[ 21 + int(round(N[i])) ]+1
for i in M:
     Histogram2[ 21 + int(round(M[i])) ] = Histogram2[ 21 + int(round(M[i])) ]+1
    

sum1 = sum(Histogram1)
sum2 = sum(Histogram2)

for j in range(0,41):
    #print Histogram1[j]
    Histogram1[j] = Histogram1[j]/float(sum1)
    if( Histogram1[j] != 0 and Histogram1_First_Element == 0 ):
         Histogram1_First_Element = j-20
    #print Histogram1[j]
    Histogram2[j] = Histogram2[j]/float(sum2)
    if( Histogram2[j] != 0 and Histogram2_First_Element == 0 ):
         Histogram2_First_Element = j-20
    
print "Histogram1 First Element:" ,Histogram1_First_Element, "\n"
print "Histogram2 First Element:" ,Histogram2_First_Element, "\n"

print "Histogram1: \n " ,Histogram1,"\n"
print "Sum Histogram 1:" ,sum(Histogram1), "\n"
print "Histogram2: \n " ,Histogram2, "\n"
print "Sum Histogram 2:" ,sum(Histogram2), "\n"
Difference = int(abs(Histogram1_First_Element) + abs(Histogram2_First_Element))
print "Difference:" ,Difference 


ax = plt.subplot(111)
barWidth=0.5
ax.bar(x, Histogram1, width=barWidth) 
ax.bar(x, Histogram2, width=barWidth,color = 'r') 

plt.show()
