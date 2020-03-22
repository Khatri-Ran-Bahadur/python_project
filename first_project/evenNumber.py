def is_even(a):
    return a%2==0

numbers=[2,3,3,4,5,6,7,8,9,6,8,2]

#filter and map function object only one time iterate so if this object many time iterate you can canvert other form
# so you can change list or tuple etc 

print(list(filter(is_even,numbers)))
#same print this function
print(tuple(filter(is_even,numbers)))
#same lambda function
print(tuple(filter(lambda a:a%2==0,numbers)))

even=[i for i in numbers if i%2==0]
print(even);