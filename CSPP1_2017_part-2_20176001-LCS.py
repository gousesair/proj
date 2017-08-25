import os
import string
import math
import re
class gouse(Exception):
    pass
    
class plagarism():
    def __init__(self):
        self
#methods
    def subs(self,f1,f2):
        s=0
        for i in range(len(f1)):
            itemp=i
            item=itemp
            for j in range(len(f2)):
                if (itemp<len(f1)):
                    if f1[itemp]==f2[j]:
                        itemp+=1
                        if (itemp-i)>s:
                            s=itemp-i
                            lcs=f1[i:itemp]
                    else:
                        itemp=item
        return lcs
    def rep(self,t):
        """
        This function is used for replacing
        the special characters in the string
        """
        t=re.sub("[^a-zA-Z0-9\_\n]+","",t)
        return t

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
            z=[]
            t1=file1.read()
            try:
                if t1=="":
                    raise gouse
                else:
                    t1=t1.lower()
                    t1=self.rep(t1)
                    for j in a:
                        if k==j:
                            y.append(None)
                            z.append(None)
                        else:
                            file2=open(j,"r")
                            t2=file2.read()
                            try:
                                if t2=="":
                                    raise gouse
                                else:
                                    t2=t2.lower()
                                    t2=self.rep(t2)
                                    ss=self.subs(t1,t2)
                                    z.append(ss)
                                    dub=len(ss)
                                    y.append(round((((dub*2)/(len(t1)+len(t2)))*100)))
                                    file2.close()
                            except gouse:
                                y.append("File Empty")
            except gouse:
                y.append("File Empty")
            print(k,y)
            print("\n")
            print(z,"\n")
            file1.close()

p=plagarism()
p.plag()
            

