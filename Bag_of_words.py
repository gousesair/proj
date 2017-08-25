import os
import string
import math
import re


class plagarism():
    def __init__(self):
        self
    def rep(self,t):
        """
        This function is used for replacing
        the special characters in the string
        """
        return re.sub('[^A-Za-z0-9\_\n]+', ' ',t)

    def frequency(self,d,dict1):
        """
        This function is used for calculating
        the frequency of the file
        """
        for i in d:
            if i==" " or i=="" or i=="\n":
                pass
            elif i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        return dict1

    def dotp(self,d1,d2):
        """
        This function is used for calculating
        the dot product of the files
        """
        L=[]
        for i in d1:
            for j in d2:
                if i==j:
                    L.append(d1[i]*d2[j])
        return sum(L)

    def modfreq(self,d):
        """
        This function is used for calculating
        the modulus frequency of the file
        """
        s=0
        for i in d:
            s+=(d[i])**2
        p=s**(1/2)
        return p
    def plag(self):
        """
        This function is used for calculating
        the plagarism of the files
        """
        path=input("Enter path:")
        a=os.listdir(path)
        os.chdir(path)
        print(a)
        for k in a:
            file1=open(k,"r")
            y=[]
            t1=file1.read()
            t1=t1.lower()
            t1=self.rep(t1)
            t1=t1.split(" ")
            dict1={}
            dict1=self.frequency(t1,dict1)
            s1=self.modfreq(dict1)
            for j in a:
                if k==j:
                    y.append(None)
                else:
                    file2=open(j,"r")
                    t2=file2.read()
                    t2=t2.lower()
                    t2=self.rep(t2)
                    t2=t2.split(" ")
                    dict2={}
                    dict2=self.frequency(t2,dict2)
                    freq=self.dotp(dict1,dict2)
                    s2=self.modfreq(dict2)
                    try:
                        if s1*s2==0:
                            raise Exception
                        else:
                            tsum=s1*s2
                            y.append(str(round(((freq/tsum)*100),2))+"%")
                    except Exception:
                        y.append("Empty")
                    file2.close()
            print(k,y)
            print("\n")
            file1.close()

"""
The main program execution starts here
"""
p=plagarism()
p.plag()
