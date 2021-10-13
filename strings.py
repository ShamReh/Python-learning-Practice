
#multi line string
email = '''
Hi Sham

Here is my first email.

Thank you

Bob


'''

print(email)

#priniting characters by index

course = 'Python playing around'
another = course[:]
print(course[0:3])
print(another)

#formatted strings

first = "Sham"
last = "Rehman"

#concatonation
message = first + ' [' + last + "] is a software engineer"

#formatted
msg = f'{first} [{last}] is a software engineer'
print(message)
print(msg)

#String methods

course= "Python Play around"

print(len(course))
print(course.upper())
print(course.lower())

print(course.find("P"))
print(course.replace("around", 'mess'))

#boolean expression
print('Python' in course)
