def odometer(oksana):
    res = 0
    pred_hours = 0
    for i in range(len(oksana)):
        if i%2 == 0:
            current_hours = oksana[i+1]
            res += (oksana[i] * (current_hours - pred_hours))
            pred_hours = current_hours
    return res