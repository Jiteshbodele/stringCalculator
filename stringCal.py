import re


def add(strng):
    if len(strng)==0:
        return 0
    
    elif len(strng)==1:
        return int(strng)
    
    else:
        numbers=re.split(r'[,\n]',strng)
        res=0
        for num in numbers:
            res+=int(num)
        
        return res


