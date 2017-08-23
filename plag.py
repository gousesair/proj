import os
import string
import math
"""
def rep(t):
    x=t
    x.replace("\n"," ")
    x=[z.strip(string.punctuation) for z in x]
    y="!~@#$%^&*()-+/*+`=[]\{}|;:'<>/?.,"
    m=0
    for i in range(len(x)):
        for j in range(len(i)):
        if i==x[m]:
            x.strip(i)
        if m<len(x):
            m+=1
        else:
            return x
    return x

"""


def frequency(d,dict1):
    for i in d:
        if i==" " or i=="" or i=="\n":
            pass
        elif i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    return dict1

def dotp(d1,d2):
    L=[]
    for i in d1:
        for j in d2:
            if i==j:
                L.append(dict1[i]*dict2[j])
    return sum(L)

def modfreq(d):
    s=0
    for i in d:
        s+=(d[i])**2
    p=s**(1/2)
    return p

path=input("Enter path:")
a=os.listdir(path)
os.chdir(path)
for k in a:
    file1=open(k,"r")
    y=[]
    t1=file1.read()
    t1=t1.lower()
    #t1.replace("\n"," ")
    t1=t1.split(" ")
    t1=[z.strip(string.punctuation) for z in t1]
    #t1=rep(t1)
    dict1={}
    dict1=frequency(t1,dict1)
    s1=modfreq(dict1)
    for j in a:
        if k==j:
            y.append(None)
        else:
            file2=open(j,"r")

            t2=file2.read()

            t2=t2.lower()
            
            #t1.replace("\n"," ")

            t2=t2.split(" ")

            t2=[z.strip(string.punctuation) for z in t2]
          
            #t2=rep(t2)
          
            dict2={}
                        
            dict2=frequency(t2,dict2)

            freq=dotp(dict1,dict2)
            
            s2=modfreq(dict2)

            tsum=s1*s2

            y.append(str(round((freq/tsum)*100))+"%")

            file2.close()
    print(y)
    print("\n")
    file1.close()

