import math

#Basic
calc = lambda x, y: x + y

authors = ["William Shakespeare", "Johann Wolfgang von Goethe", "Miguel de Cervantes", "J.K. Rowling"]

authors.sort(key= lambda surname: surname.split(" ")[-1].lower())

print(authors)

print("------------------------------------------")

#Integrated functions

#Map - It takes an iterable and returns a map object, applying the function
# to each element of the iterable

radius = [1, 2, 3, 4, 5]
area = map(lambda r: math.pi * (r ** 2), radius)

print(list(area))
print(list(map(lambda r:  math.pi * (r ** 2), radius)))

print("------------------------------------------")

#Filter - It takes an iterable and returns a new filter object with only the true values

odd_numbers = list(filter(lambda x: x%2 == 0 , radius))
print(odd_numbers)

print("------------------------------------------")

countries = ["Brazil", "", "USA", "", "", "England", "Germany", "Japan", ""]

# filter_empty = filter(lambda x: len(x) > 0 , countries)
# filter_empty = filter(lambda x: x != '' , countries)
filter_empty = filter(None , countries)

print(list(filter_empty))
print("------------------------------------------")
#Reduce - It's not built-in anymore

from functools import reduce

data = [1, 2, 3, 4, 5]

res = reduce(lambda x,y: x * y, data)

print(res)
print("------------------------------------------")

#All() -> It returns true if all items of the iterable are true or if it's empty

print(all([1, 2, 3, 4, 5]))
print(all([0,1, 2, 3, 4, 5]))
print(all([]))
print(all('LF'))

names = ["Carl", "Cameron", "Cathy"]
print(all([name[0] == 'C' for name in names]))


print("------------------------------------------")

#Any() -> it returns true if any element is true. If it's empty it returns false
code = [True, False, False]
code2 = []
print(any(code))
print(any(code2))


print("------------------------------------------")

names = ["Carl", "Cameron", "Cathy"]

#Generator Vs List/Dict/Set Comprehension

#Generator - It consumes less memory because it generates an object that can be used or not.
# It does not store the result (data) in the memory right away, only the object.

#Comprehension -> Already creates the list/dict/set in the memory.

res = (x[0] == "C" for x in names )
print(res)

from sys import getsizeof

#Check the number of bytes each solution utilizes

list_comp = getsizeof([n * 10 for n in range(1000)])

set_comp = getsizeof({n * 10 for n in range(1000)})

dict_comp = getsizeof({n * 10 for n in range(1000)})

generator = getsizeof((n * 10 for n in range(1000)))

print("Consume of memory for the same task")

print(f"List comprehension: {list_comp} bytes")
print(f"Set comprehension: {set_comp} bytes")
print(f"Dict comprehension: {dict_comp} bytes")
print(f"Generator Expression: {generator} bytes")
 
gen = (x for x in range(5))

print(f"Generator object (iterable): {gen}")
print(type(gen))

for i in gen:
    print(i)


print("------------------------------------------")