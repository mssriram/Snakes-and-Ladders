import random
from math import sqrt
import numpy as np
import time

start_time=time.time()


def Dice():
    return random.randint(1,6)

def snake(i):							#Creating the snakes on the board
    tail=random.randint(1,98)
    head=tail+snake_length[i]
    if head>98 or adjmatrix[head][tail]==1:
        return False
    else:
        for j in range(0,2):
            adjmatrix[head-j]=[2]*100
            adjmatrix[head+j]=[2]*100
        adjmatrix[head][tail]=1
        return True

    
def ladder(i):							#Creating the ladders on the board
    tail=random.randint(1,98)
    head=tail+ladder_length[i]
    if head>98 or adjmatrix[head][tail]==1:
        return False
    else:
        for j in range(0,2):
            adjmatrix[tail-j]=[2]*100
            adjmatrix[tail+j]=[2]*100
        adjmatrix[tail][head]=1
        return True


def temp_board():					#Creates a temporary board to extract the lengths of the snakes and ladders

    while len(snake_length)<snakes or len(ladder_length)<ladders:
        head=random.randint(0,100)
        tail=random.randint(0,100)
        if head-tail>min_snake and head-tail<max_snake and len(snake_length)<snakes and head-tail not in snake_length:
            snake_length.append(head-tail)
        elif tail-head>min_ladder and tail-head<max_ladder and len(ladder_length)<ladders and tail-head not in ladder_length:
            ladder_length.append(tail-head)

def Board():						#Creates the board
    for i in range(0,int(snakes)):
        while not snake(i):
            snake(i)
           #print(i)
    for i in range(0,int(ladders)):
        while not ladder(i):
            ladder(i)

def Game():						#The game is simulated
    position=0
    n=0
    while position<99:
        n+=1
        newposition = position + Dice()
        if newposition<100:
            position=newposition
        for i in range(0,100):
            if adjmatrix[position][i]==1:
                position=i
                break
    newfile.write(str(n)+'\n')
    moves.append(n)
    return n

def std_deviation(mean):				#Calculating std. deviation
    sd=[]
    for i in range(0,len(moves)):
        temp=moves[i]-mean
        sd.append(temp**2)
    std=sqrt(sum(sd)/len(sd))
    return std
    
itirations=50000	 #input("enter no. of itirations\n")    
newfile=open("newdata.txt","w")
avgfile=open("avg_len.dat","a")
avg=0
moves=[]
avg_len=[]


ladders=int(input())
snakes=int(input())

min_snake=10			#int(input())			#min, max length of the snakes and ladders
max_snake=70			#int(input())
min_ladder=10			#int(input())
max_ladder=70			#int(input())

snake_length=[]
ladder_length=[]
temp_board()

for i in range(0,int(itirations)):				#simulates the game n number of times
    adjmatrix=np.zeros(shape=(100,100))
    Board()
    avg+=Game()

snake_avg=sum(snake_length)/len(snake_length)
ladder_avg=sum(ladder_length)/len(ladder_length)
#	std=std_deviation(avg/itirations)
avgfile.write("%s\t%s\t%s\t%s\t%.2f\t%.2f\t%.3f\t%.3f\n"%(min_snake, max_snake, min_ladder, max_ladder, snake_avg, ladder_avg, avg/itirations, std))


print(avg/itirations)						#avg number of moves req to complete game

end_time=time.time()
print("execution time =  %s" %(end_time-start_time))



