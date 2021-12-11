def MassVote(N, Votes):
    
    sum_lst = sum(Votes)
    max_lst = max(Votes)
    
    if sum_lst == 0:
        return 'no winner'
    
    perc = round((max_lst / sum_lst) * 100, 3)
    count = 0
    index = 0
    
    for i in range(len(Votes)):
        if Votes[i] == max_lst:
            count += 1
            index = i
    
    if count > 1:
        return 'no winner'
    elif perc > 50:
        return 'majority winner ' + str(index+1)
    else:
        return 'minority winner ' + str(index+1)
            
