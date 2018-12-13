# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:46:52 2018

@author: Helena J Arpudaraj
"""

import numpy as np
import matplotlib.pyplot as plt
import random

    
class Node(object):
    def __init__(self, name):
        self.name=name;
        self.adjacentnode=[];
        self.numOfEdges=0;


def start():
    global i;
    global totaldegree;
    i=1;
    nodeList.append(Node(i));
    i=i+1;
    nodeList[0].adjacentnode.append(nodeList[0]);
    nodeList[0].numOfEdges=1;
    totaldegree=1;
    BProb.append(1);
    DProb.append(1);
    
def Birthnode(NodeSelect):
    global i;
    global totaldegree;
    node1=Node(i);
    nodeList.append(node1);
    node1.adjacentnode.append(NodeSelect);
    node1.numOfEdges=1;        
    NodeSelect.adjacentnode.append(node1);
    NodeSelect.numOfEdges=(NodeSelect.numOfEdges)+1; 
    i=i+1;
    totaldegree=totaldegree+2;    
    numOfNodes=len(nodeList);
    for k in range (len(nodeList)):
        BProb.append((nodeList[k].numOfEdges)/(totaldegree));
        DProb.append((numOfNodes-(nodeList[k].numOfEdges))/((numOfNodes**2)-(totaldegree)));
    
def Deathnode(NodeSelected):
    global totaldegree;
    pos=nodeList.index(NodeSelected);
    nodeList.remove(NodeSelected);
    totaldegree=totaldegree-len(NodeSelected.adjacentnode);
    length=len(nodeList);
    if pos>0:
        for j in range (length):
            if NodeSelected in nodeList[j].adjacentnode:
                nodeList[j].adjacentnode.remove(NodeSelected);
                nodeList[j].numOfEdges=(nodeList[j].numOfEdges)-1;
                totaldegree=totaldegree-1;
        numOfNodes=len(nodeList);
        if numOfNodes==1:
            DProb.append(1);
            BProb.append(1);
        else:
            for k in range (len(nodeList)):
                BProb.append((nodeList[k].numOfEdges)/(totaldegree));
                DProb.append((numOfNodes-(nodeList[k].numOfEdges))/((numOfNodes**2)-(totaldegree)));
         
def CumulativeProb():
    Cumulative_BirthProb=0;
    for k in range (len(nodeList)):
        Cumulative_BirthProb=Cumulative_BirthProb+BProb[k];
        CumulativeBProb.append(Cumulative_BirthProb);
    y=random.randint(0, 10);
    y=y/10;
    for k in range (len(CumulativeBProb)):
        if CumulativeBProb[k]>=y:
            node=nodeList[k];
            return node;
        if k==(len(CumulativeBProb)-1):
            return nodeList[k];
            
    
nodeList=[];
BProb=[];
DProb=[];


start();

numOfSteps=[];
numNodes=[];
numEdges=[];

for j in range (10000):
    x=random.randint(0, 10);
    x=x/10;
    if x<=0.6:
        CumulativeBProb=[];
        NodeSelected=CumulativeProb(); 
        BProb=[];
        DProb=[];
        Birthnode(NodeSelected);
    else:
        maxpos=DProb.index(max(DProb));
        NodeSelected=nodeList[maxpos];
        BProb=[];
        DProb=[];
        Deathnode(NodeSelected);
        length=len(nodeList);
        if length==0:
            start();
    numOfSteps.append(j);
    numNodes.append(len(nodeList));
    numEdges.append(totaldegree);

    
nodeList=[];
BProb=[];
DProb=[];

start();

numOfSteps2=[];
numNodes2=[];
numEdges2=[];
    

for j in range (10000):
    x=random.randint(0, 10);
    x=x/10;
    if x<=0.9:
        CumulativeBProb=[];
        NodeSelected=CumulativeProb(); 
        BProb=[];
        DProb=[];
        Birthnode(NodeSelected);
    else:
        maxpos=DProb.index(max(DProb));
        NodeSelected=nodeList[maxpos];
        BProb=[];
        DProb=[];
        Deathnode(NodeSelected);
        length=len(nodeList);
        if length==0:
            start();
    numOfSteps2.append(j);
    numNodes2.append(len(nodeList));
    numEdges2.append(totaldegree);


     
nodeList=[];
BProb=[];
DProb=[];

start();

numOfSteps1=[];
numNodes1=[];
numEdges1=[];
    

for j in range (10000):
    x=random.randint(0, 10);
    x=x/10;
    if x<=0.75:
        CumulativeBProb=[];
        NodeSelected=CumulativeProb(); 
        BProb=[];
        DProb=[];
        Birthnode(NodeSelected);
    else:
        maxpos=DProb.index(max(DProb));
        NodeSelected=nodeList[maxpos];
        BProb=[];
        DProb=[];
        Deathnode(NodeSelected);
        length=len(nodeList);
        if length==0:
            start();
    numOfSteps1.append(j);
    numNodes1.append(len(nodeList));
    numEdges1.append(totaldegree);

plt.plot(numOfSteps,numNodes,label='p=0.6')
plt.plot(numOfSteps1,numNodes1,label='p=0.75')
plt.plot(numOfSteps2,numNodes2,label='p=0.9')
plt.xlabel('number of steps')
plt.ylabel('number of nodes')
plt.title('Graph 1')
plt.legend()
plt.show()


plt.plot(numOfSteps,numEdges,label='p=0.6')
plt.plot(numOfSteps1,numEdges1,label='p=0.75')
plt.plot(numOfSteps2,numEdges2,label='p=0.9')
plt.xlabel('number of steps')
plt.ylabel('number of edges')
plt.title('Graph 2')
plt.legend()
plt.show()

klist=[];
kdegreeNodes=[];
m=len(nodeList);
P=0;
Plist=[];

for k in range (5):
    numNodes_kdegree=0;
    for l in range (len(nodeList)):
        if nodeList[l].numOfEdges == k:
            numNodes_kdegree=numNodes_kdegree + 1;
    P=P+(numNodes_kdegree/m);
    Plist.append(P);
    klist.append(k);

klist.sort(reverse=True)
plt.loglog(klist,Plist)
plt.xlabel('k')
plt.ylabel('P`[k]')
plt.title('Graph 3')
plt.show()

print("End of Execution.... For output please view the graphs generated...")