def WordSearch(len, s, subs):
    
    if s=='' or subs=='':
        return []
    
    str1 = s.split()
    new_lst = []
    end = ''
    
    for i, elem in enumerate(str1):
        if elem!= str1[-1]:
            if len(str1[i])<12 and len(str1[i] + ' ' + str1[i+1])<12:
                new_lst.append(str1[i] + ' ' + str1[i+1])
                str1.remove(str1[i+1])
            elif (len(str1[i]) + 1) == 12 or (len(str1[i])) == 12:
                new_lst.append(str1[i])
                if end != '':
                    new_lst.append(end)
                    end = ''
            else:
                if end != '' and len(end + ' ' + str1[i])<=12:
                    new_lst.append(end + ' ' + str1[i])
                    end = ''
                else:    
                    new_lst.append(str1[i][:12])
                    if end != '':
                        new_lst.append(end)
                if str1[i][12:]!='':
                    end = str1[i][12:]
                    
    if end != '' and len(end + ' ' + str1[-1])<=12:
        new_lst.append(end + ' ' + str1[-1])
    else:
        new_lst.append(str1[-1])
    
    res = []
    for elem in new_lst:
        if subs in elem.split():
            res.append(1)
        else:
            res.append(0)
    
    return res