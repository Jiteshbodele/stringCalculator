import re


def add(strng):
    if len(strng)==0:
        return 0
    
    elif len(strng)==1:
        return int(strng)
             
    else:

        delim=[",","\n"]
        flag=0 #to indicate whether a delimeter is modefied or not

        if strng.startswith("//"):
            delim.append(strng[2])
            flag=1
           
        if flag==1:
            newstr=strng[4:]
        else:
            newstr=strng
            
        pattrn="|".join(re.escape(d) for d in delim)
        numbers=re.split(pattrn,newstr)
        res=0
        neg=[]
        for num in numbers:
            if int(num)<0:
                neg.append(int(num))

            res+=int(num)

        if len(neg)!=0:
            raise ValueError(f"negative numbers are not allowed {','.join(map(str, neg))}")   
          
        return res



