
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i()) # output : 
    
    
    
    
    
    
    
    
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))  
print(check(7))  




#Lamda with multiple statements
calc = lambda x, y: (x + y, x * y)   ##two expression addition and multiplication

res = calc(3, 4)
print(res)  #returns a tuple  

#output: [7,12]



#List in built one , mixed data types ,slower
#Array ---import arrays from module ,single type,faster,numeric purpose


n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n) #filter() applies this condition to each element in nums.
print(list(even)) 

#output: [2,4,6]


#########################################################################################################




a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a) 
#map() iterates through a and applies the transformation(X*2)
print(list(b))  






from functools import reduce

a = [1, 2, 3, 4]   ####1*2*3*4 ===
b = reduce(lambda x, y: x * y, a)  # x=1*y= 2 =2===>x=2 y=3 2*3 =6 ===x=6 y=4 6*4= 
#reduce() applies this operation across the list.
print(b) # output==>24



    