def BiggerGreater(string):
      
    for i in range(len(string)-1,0,-1):
        
        if string[i] > string[i-1]:
            
            new_str = list(string[i-1:])
            max_str = sorted(new_str)
            elem = max_str[max_str.index(new_str[0])+1]
            
            x = new_str.index(elem)
            new_str[0],new_str[x] = new_str[x],new_str[0]
            
            res = string[:i-1] + ''.join(new_str[0]) + ''.join(sorted(new_str[1:]))
            return res 
        
    res = ''    
    return res