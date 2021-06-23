def BigMinus(s1, s2):
    if len(s1) > len(s2):
        max_s = s1
        min_s = s2
    else:
        max_s = s2
        min_s = s1
    
    
    res = int(max_s[-(len(min_s)):]) - int(min_s)
    
    if res < 0:
        res = ''
    
    return max_s[:-(len(min_s))] + str(res)