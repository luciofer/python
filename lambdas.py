import math

#Basic
calc = lambda x, y: x + y

authors = ["William Shakespeare", "Johann Wolfgang von Goethe", "Miguel de Cervantes", "J.K. Rowling"]

authors.sort(key= lambda surname: surname.split(" ")[-1].lower())

print(authors)

print("------------------------------------------")
#Map - Returns a map object

radius = [1, 2, 3, 4, 5]
area = map(lambda r: math.pi * (r ** 2), radius)

print(list(area))
print(list(map(lambda r:  math.pi * (r ** 2), radius)))

print("------------------------------------------")