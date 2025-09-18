def add(str):
    if len(str)==0:
        return 0
    
    elif len(str)==1:
        return int(str)
    
    else:
        numbers=str.split(",")
        res=0
        for num in numbers:
            res+=int(num)
        
        return res


