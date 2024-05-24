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