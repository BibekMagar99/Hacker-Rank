from collections import namedtuple
# importing the named tuple library

Student = namedtuple('Student','ID MARKS NAME CLASS')
#Declaring the namedtuple with its elements

n = int(input())
#taking the integer input


items = input().split()
#taking column headings

Marks_index = items.index("MARKS")
#finding the index of "MARKS"

Avg = Student(NAME= [], MARKS =[], ID = [], CLASS = [])
#making the elements of the namedtuple lists

for i in range (n):
    values = input().split()
    #here the input values are taken
    
    Avg.MARKS.append(values[Marks_index])
#the list "MARKS" in the named tuple is being appended with with marks by 
#taking the index of MARKS which is same in the value 
    
final = list(map(int, Avg.MARKS))
#converting the elements of "MARKS" list into integers
result = sum(final)/len(final)
print(f"{result :.2f}")
