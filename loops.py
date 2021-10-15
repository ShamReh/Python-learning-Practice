
#while loops
i = 1

while i<=5:
    print('*' * i)
    i = i+1
print("Done")

#for loops
for item in ['Sham', 'Bob', 'John']:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10, 2):
    print(item)

#nested loops

for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#F shape using nested loop

numbers = [5, 2, 5, 2, 2]

for count in numbers:
    output= ''
    for x in range(count):
        output+= 'x'
    print(output)

for i in range(3):
    for j in range(4):
        print(i, "x", j, "=", i * j)

for i in range(10, 21, 2):
    print(i)