import math

#Basic
calc = lambda x, y: x + y

authors = ["William Shakespeare", "Johann Wolfgang von Goethe", "Miguel de Cervantes", "J.K. Rowling"]

authors.sort(key= lambda surname: surname.split(" ")[-1].lower())

print(authors)

print("------------------------------------------")
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
