def ShopOLAP(N, items): 
    
    d = {}
    for i in range(N):
        key,value = items[i].split()
        d[key] = d.get(key, 0) + int(value)
        
    d = {k: str(v) for k, v in d.items()}
    sorted_key_value_tuple = sorted(sorted(d.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(len(sorted_key_value_tuple)):
        res.append(' '.join(sorted_key_value_tuple[i]))
    return res