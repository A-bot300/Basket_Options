import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

#initializing
w1=0.5        
w2=0.5       
K=100         
S1=40         
sigma1=0.3 
sigma2=0.3 
r=0.05
corr=0.5
T=3
S2=40
k_=120 
M=40
L=40
N=10
ds1=5
ds2=5
dt=T/N

grid=np.empty([N+1,M+1,L+1])

#boundary conditions
for i in range(0,M+1):
  for j in range(0,L+1):
    grid[N][i][j]=max(w1*ds1*i + w2*ds2*j - K , 0)
  
for i in range(0,N+1):
  for j in range(0,M+1):
    grid[N-i][j][0]=max(w1*j*ds1-K*math.exp(-r*i),0)

for i in range(0,N+1):
  for j in range(0,L+1):
    grid[N-i][0][j]=max(w2*j*ds2-K*math.exp(-r*i),0)
    
for i in range(0,N+1):
  for j in range(0,L+1):
    grid[N-i][M][j]=max(w1*M*ds1+w2*j*ds2-K*math.exp(-r*i),0)   

for i in range(0,N+1):
  for j in range(0,M+1):
    grid[N-i][j][L]=max(w1*j*ds1+w2*L*ds2-K*math.exp(-r*i),0)   
    
    
#print(grid)  
 #backtracking to calculate stock price 
for i in range(0,N):
  for j in range(1,M):
    for k in range(1,L):
      a=0.5*sigma1*sigma1*(j*j*ds1*ds1)
      b=r*j*ds1
      c=-r
      d=0.5*sigma2*sigma2*(k*k*ds2*ds2)
      e=corr*sigma1*sigma2*j*ds1*k*ds2
      f=r*k*ds2
   
      A=(1/dt) - ((2*a)/(ds1*ds1)) + c - ((2*d)/(ds2*ds2)) 
      B=a/(ds1*ds1) + b/(2*ds1)
      C=a/(ds1*ds1) - b/(2*ds1)
      D=d/(ds2*ds2) + f/(2*ds2)
      E=d/(ds2*ds2) - f/(2*ds2)
      F=e/(4*ds1*ds2)
      
      grid[N-i-1][j][k]=dt*(A*grid[N-i][j][k] + B*grid[N-i][j+1][k] + C*grid[N-i][j-1][k] + D*grid[N-i][j][k+1] + E*grid[N-i][j][k-1] + F*(grid[N-i][j+1][k+1] + grid[N-i][j-1][k-1] - grid[N-i][j+1][k-1] - grid[N-i][j-1][k+1]))

print(grid[0][S1][S2]-k_)       
#print(grid) 
#print(A,B,C,D,E,F)
