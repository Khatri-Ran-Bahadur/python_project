number=[3,4,5,6]

# #### 1 Method
def square(a):
    return a**2

lists=list(map(square,number));

# #### 2 Method this is the same
lists1=list(map(lambda a:a**2,number));

#### 3 List Comprehensive method same
square_new=[i**2 for i in number]
print(square_new);

### 4 same using for loop

list_new=[]
for num in number:
    list_new.append(square(num))
print(list_new)

my_list=['absc','fhdf','dhfh']

map_length=map(len,my_list);
print(list(map_length));