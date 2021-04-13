from collections import OrderedDict
# importing the library

dict = OrderedDict()
#creating the ordered dictionary

n = int(input())
items = []
# empty list

for i in range (n): 
    *name, price = input().split()
#assigns all the first inputs to name and assigns only last input in price
    
    temp = [price]
    #creating a list called temp with first element as price
    
    
    product = " ".join(name)
    #making the first inputs as a single entity , i.e APPLE JUICE as a single
    
    if product not in items:
        items.append(product)
        dict[product] = temp
    else:
        dict[product].append(price)
    #creating the full dictionary by appending price of same element in same key
    
for i in dict:
    print(i ,sum(list(map(int, dict[i]))))
    #finally printing output as per requirement
    #dict[i]= sum(list(map(int, dict[i])))


    

        

    