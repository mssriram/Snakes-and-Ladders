import matplotlib.pyplot as plt
import numpy as np

file = open("newdata.txt","r")

prob={1:0,
      2:0,
      3:0,
      4:0,
      5:0,
      6:0,
      7:0,
      8:0,
      9:0,
      10:0,
      11:0,
      12:0,
      13:0,
      14:0,
      15:0,
      16:0,
      17:0,
      18:0,
      19:0,
      20:0,
      21:0,
      22:0,
      23:0,
      24:0,
      25:0,
      26:0,
      27:0,
      28:0,
      29:0,
      30:0,
      }

def probability_distribution(file,prob):
    sum=0
    for i in file:
        i=int(i)
        if int(i/10) in prob.keys():
            prob[int(i/10)]=prob.get(int(i/10))+1
        sum+=i
    avg=sum/100000
    print(avg)
    x=np.array([i*10 for i in prob.keys()])
    y=np.array([i for i in prob.values()])
    plt.plot(x,y)
    plt.show()   

probability_distribution(file,prob)


