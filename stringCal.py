def add(str):
    if len(str)==0:
        return 0
    
    elif len(str)==1:
        return int(str)
    
    else:
        numbers=str.split(",")

        return int(numbers[0])+int(numbers[1])


