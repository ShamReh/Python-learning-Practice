#multi-dimensional lists

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print(cool_animals[2][2])
print(cool_animals[0][1])

#multiple data-types in list

farm = ["Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850]

#Methods

my_fruit = ["Apple", "Banana", "Orange"]

my_fruit.append("Grapefruit")
print(my_fruit)

my_fruit.remove("Banana")
print(my_fruit)

my_fruit.pop()
print(my_fruit)

my_fruit.pop(0)
print(my_fruit)

my_fruit.insert(0, "Mango")
print(my_fruit)

my_fruit.extend(["Grapefruit", "Kiwi"])
print(my_fruit)

print(my_fruit.index("Kiwi"))

print(my_fruit.count("Orange"))

my_fruit.reverse()
print(my_fruit)

my_fruit.extend(['Avacado', 'Passionfruit'])
print(my_fruit)

my_fruit.sort()
print(my_fruit)

my_fruit.sort(key=len)
print(my_fruit)

print(", ".join(my_fruit))

#Tuples

farm = "Pepperidge Farm", ["Winnie the Moo", "Moolan"], 1850  # This is a tuple of length 3
farm_name, cool_cows, farm_size = farm
print(farm_name)

#Dictionaries

noises = {"cow" : "moo", "sheep" : "baa"}
print(noises["cow"])
noises["chicken"] = "cluck"
print(noises)

print(noises.keys())
print(tuple(noises.items()))

#sets

my_items = ["Apple", "Banana", "Apple", "Banana", "Orange"]
print(set(my_items))

#Dictionary task

books = {"The Handmaiden's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}

#Query using key: value pairs
print(books.keys())
print(books["The Handmaiden's Tale"])

#max value

numbers=[3, 6, 2, 8, 4, 10]
max= numbers[0]

for number in numbers:
    if number >max:
        max=number
print(max)

#2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]

for row in matrix:
    for item in row:
        print(item)

print(matrix[0][1])

#Duplicates removed

numbers=[2, 2, 4, 6, 3, 4, 6, 1]
uniques=[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print ( uniques)

#Unpacking

coordinates = (1,2,3)

x, y, z= coordinates

print (x)


