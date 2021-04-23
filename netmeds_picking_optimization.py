import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
import numpy as np
args = sys.argv
# print(args)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
# from sklearn.metrics import accuracy_score
# import matplotlib.pyplot as plt
from math import ceil

import pandas as pd


from math import ceil
import mlrose
import numpy as np

def cust_fn(state,dist):
  su=0
  for i in range(len(state)-1):
    for j in range(len(dist)):
      if((dist[j][0]==state[i] and dist[j][1]==state[i+1]) or (dist[j][0]==state[i+1] and dist[i][0]==state[i])):
        su+=dist[j][2]
        break
  for j in range(len(dist)):
    if((dist[j][0]==len(state) and dist[j][1]==state[0]) or (dist[j][1]==len(state) and dist[j][0]==state[0])):
      su+=dist[j][2]
      break
  return su


def round_(n):
  val=(0,26)
  from math import ceil
  x=((n/26.1)//0.5)*26
  return x



df=pd.read_csv("overall.csv")
df=df.drop(columns=["Unnamed: 0"],axis=1)

k=df.values
k
new_l=[]
for i in k:
  if(i[2]==0):
    i[2]=0.5
  new_l.append(tuple(i))
dist_list=new_l

def format_(strx):
    sep = strx.split("_")
    sep = [ i.zfill(2) for i in sep]
    return "_".join(sep)



#input in the form of list of string of aisle-no_rack-no

nodes=["1_6","1_6","1_2","1_3","1_4","1_5"] if(not args) else args[1:]
req=[]

for i in range(len(nodes)):
  nodes[i]=format_(nodes[i])

  
for i in range(len(nodes)):

  for j in range(len(dist_list)):
    if((dist_list[j][0]==nodes[i]  and dist_list[j][1]  in nodes and dist_list[j][1]!=dist_list[j][0]) or  (dist_list[j][0]=="01_01" and dist_list[j][1] in nodes) ):
        req.append(dist_list[j])

lt=len(req);newr=[];count=0
code={}

 
for i in nodes:
  if(i not in code):
    code.update({i:count})
    count+=1
if("01_01" not in nodes):
  code.update({"01_01":count})

for i in range(len(req)):
  newr.append((code[req[i][0]],code[req[i][1]],req[i][2]))

fitness_dists =  mlrose.CustomFitness(cust_fn, dist=newr,problem_type="tsp")
problem_fit= mlrose.TSPOpt(length =count, fitness_fn = fitness_dists, maximize = False)
best_state, best_fitness = mlrose.genetic_alg(problem_fit, max_attempts = 10, random_state = 2)

code1={}
for i in code:
  code1.update({code[i]:i})
final_state=[]
 
best_state_updated=[]
for i in range(len(best_state)):
  best_state_updated.append(code1[best_state[i]])
  best_state[i]=code1[best_state[i]]

print("best_state {}".format(best_state_updated))
print("best_fitness :{}".format(best_fitness));rc=[];ais=[]
