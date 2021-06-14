def WordSearch(len1, s, subs):
    
    if s=='' or len1==0:
        return []
    
    str1 = s.split()
    new_lst = []
    end = ''
        
    for i, elem in enumerate(str1):
        if elem!= str1[-1]:
            
            if len(str1[i])<=len1 and len(str1[i] + ' ' + str1[i+1])<=len1:
                new_lst.append(str1[i] + ' ' + str1[i+1])
                str1.remove(str1[i+1])
            elif (len(str1[i]) + 1) == len1 or (len(str1[i])) == len1:
                new_lst.append(str1[i])
                if end != '':
                    new_lst.append(end)
                    end = ''
            else:
                if end != '' and len(end + ' ' + str1[i])<=len1:
                    new_lst.append(end + ' ' + str1[i])
                    end = ''
                else:
                    new_lst.append(str1[i][:len1])
                    if end != '':
                        new_lst.append(end)
                if str1[i][len1:]!='':
                    end = str1[i][len1:]
                    
    if end != '' and len(end + ' ' + str1[-1])<=len1:
        new_lst.append(end + ' ' + str1[-1])
    elif len(str1[-1])>len1:
        new_lst.append(str1[-1][:len1])
        new_lst.append(str1[-1][len1:])
    else:
        new_lst.append(str1[-1])
    
    if len(str1) == 1:
        new_lst = [str1[0][i:i+len1] for i in range(0, len(str1[0]), len1)] 

    res = []
    for elem in new_lst:
        if subs in elem.split():
            res.append(1)
        else:
            res.append(0)
    
    return res
