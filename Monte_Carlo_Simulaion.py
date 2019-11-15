import numpy as numpy
import matplotlib.pyplot as plt
import math

def MonteCarloSimulation(CallorPut,S1,w1,S2,w2,K,v1,v2,r,corr,T,M):
  
  N=252
  n=T*N
  asset1=numpy.zeros([n])
  asset2=numpy.zeros([n])
  option=numpy.zeros([n])
  time=numpy.zeros([n])

  mu1=(r-0.5*v1*v1)/N
  sigma1=math.sqrt((v1*v1)/N)

  mu2=(r-0.5*v2*v2)/N
  sigma2=math.sqrt((v2*v2)/N)

  for i in range(0,n):
    time[i]=i+1;

  for i in range(0,M):
    t1=numpy.zeros([n])
    t2=numpy.zeros([n])
    t1[0]=S1
    t2[0]=S2

    for j in range(1,n):
      Rand1 = numpy.random.normal(mu1, sigma1,1)
      Rand2 = numpy.random.normal(mu2, sigma2,1)
      t1[j] = t1[j-1]*math.exp(Rand1)
      t2[j] = t2[j-1]*math.exp(corr * Rand1 + math.sqrt(1-corr*corr) * Rand2)

    asset1=asset1+t1
    asset1=asset1/2

    asset2=asset2+t2
    asset2=asset2/2

    temp=numpy.zeros([n]);
    val=numpy.zeros([n])
    for j in range(1,n):
      val[j] = w1*asset1[j-1]+w2*asset2[j-1]
      temp[j]=math.exp(-r*j/N)* max(CallorPut*(val[j] - K), 0)
    option=option+temp

  option=option/M  

  print(option[n-1])
  
  plt.figure()
  plt.plot(time,asset1,label='Asset1')
  plt.legend()
  plt.plot(time,asset2,label='Asset2')
  plt.legend()
  plt.plot(time,option,label='Option')
  plt.legend()
  plt.show()
  
  
  

CallorPut=1 #if call use 1 and if put use -1
S1=100   #Price of Stock 1
w1=0.5   #Weight of stock 1
S2=100   #Price of Stock 2
w2=0.5   #Weight of stock 2
K=100    #Strike Price
v1=0.3   #Volatility of stock 1
v2=0.3   #Volatility of stock 2
r=0.05   #Rate of Interest
corr=0.5 #Correlation co-efficient
T=3      #Time in Years
M=1000   #No. of Simulations
MonteCarloSimulation(CallorPut,S1,w1,S2,w2,K,v1,v2,r,corr,T,M)
