def MaximumDiscount(N, price):
    price.sort(reverse=True)
    discount = 0
    
    if N%3 == 0 and N==3:
        return min(price)
    elif N>3:
        for i in range(N//3):
            price_1 = price[:3]
            price = price[3:]
            discount += min(price_1)
    
    return discount 
