def digital_root(n):
    sum = 0
    mystr = str(n)
    if len(mystr) == 1:
        return n
    else:
        for i in mystr:
              sum += int(i)
    if sum < 10: 
        return sum
    else:
        return digital_root(sum)