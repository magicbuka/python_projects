def SynchronizingTables(N, ids, salary):
    
    ids2 = ids.copy()
    ids2.sort()
    salary.sort()
    
    d = {}
    for i, num in enumerate(ids):
        d[num] = i
    
    lst = []
    for i, num in enumerate(ids2):
        lst.append([d[num], salary[i]])
    
    lst.sort(key=lambda row: row[0])
    result = []
    for row in lst:
        result.append(row[1])
            
    return result