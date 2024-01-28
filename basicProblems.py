'''
problem --- 19
q: Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.


code: 
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

def getColor(l_1, l_2):
    print(f"Differenc between set one and set two is :\n {l_1.difference(l_2)}")
    print(f"Differenc between set two and set one is :\n {l_2.difference(l_1)}")

getColor(color_list_1, color_list_2)
''' 


'''
problem ---18 
q:  Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.

code: 


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
]

for num in numbers:
    if num == 237:
        print(num)
        break 
    elif num % 2 == 0:
        print(num)

''' 


'''
problem --- 17 
q: Write a Python program that concatenates all elements in a list into a string and returns it.
code: 
def getString(nums):
    result = ''
    for n in nums:
        result += str(n) 

    return result 

result = getString([4,5,6,7, 50, 45])
print(result)

''' 



'''
problem --- 16
q: Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

code: 

user_str = input("Enter a string: ")
num_of_copy = int(input("Enter number of copy(non negetive-integer: "))

def getCopy(s, n):
    tmp_str = s 
    result = ""
    if len(s) > 2:
        tmp_str = s[:2]

    for i in range(n):
        result += tmp_str 
    return result 
result = getCopy(user_str, num_of_copy)
print(result)

''' 



'''
problem --- 15
q: Write a Python program to count the number 4 in a given list.

code: 

def getFourFormList(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    return count


result = getFourFormList([4, 4,56,7,84,5,4,56,4,56,3,4, 4])
print(result)
''' 




'''
problem --- 14
q:Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

code: 
string = "//sultan"
copy = 5 

def getCopies(s, c):
    final_str = s 
    for i in range(copy-1):
        final_str += s 
    return final_str 
result = getCopies(string, copy)
print(result)
'''


'''
problem --- 13
q: Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

code: 
n1,n2,n3 = (3, 3, 3)

def getSum(n1, n2, n3):
    sum = n1 + n2 + n3 
    if(n1 == n2 and n1 == n3 and n2 == n3):
        sum = sum + sum + sum 
    return sum 

result = getSum(n1, n2, n3)
print(f"The result is: {result}")

'''

'''
problem --- 12 
q: Write a Python program to calculate the number of days between two dates.

code: 
from datetime import date 

first_date_str = input("Enter the first date(format: year, month, day): ")
last_date_str = input("Enter the first date(format: year, month, day): ")

def getDateInt(d):
    year_str, month_str, days_str = d.split(",")
    year = int(year_str)
    month = int(month_str)
    days = int(days_str)
    return date(year, month, days)

def getDays(f_date, l_date):
    dif_days = l_date - f_date 
    days = dif_days.days 
    year, reminder = divmod(days, 365)
    month, day = divmod(reminder, 30)
    return year, month, day 
    
first_date = getDateInt(first_date_str)
last_date = getDateInt(last_date_str)

year, month, days = getDays(first_date, last_date)
print(f"The difference between {first_date} and {last_date} is {year} year, {month} month and {days} days")

'''

'''
problem --- 11
q: Write a Python program that prints the calendar for a given month and year.

code: 
import calendar 
year = int(input("Enter year(integer number like 2024): "))
month = int( input("Enter month(integer number like 01): "))

def getSpecificCalender(y, m):
    print(calendar.month(y,m))

getSpecificCalender(year, month)


'''

'''
problem --- 10 
q: Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
code:
 math.sqrt.__doc__
 abs.__doc__ 
 write method_name.__doc__
 and get the description of the method 
'''


'''
problem --- 9
q: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
code: 

value_str = input("Enter the value(integer): ")
def compute(n):
    n1 = int("%s" % n)
    n2 = int("%s%s"% (n, n))
    n3 = int("%s%s%s"% (n, n, n))
    return n1 + n2 + n3
result = compute(value_str)
print(result)

'''

'''
problem --- 8
q: Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
Sample Output: The examination will start from : 11 / 12 / 2014

code: 

'''

'''
problem --- 7
q: Write a Python program to display the first and last colors from the following list.
code:
def getColours(sample_seq):
    return sample_seq[0] , sample_seq[len(sample_seq) - 1]

result = getColours(["Red","Green","White" ,"Black"])
print(result)




'''

'''
problem --- 6
q: Write a Python program that accepts a filename from the user and prints the extension of the file.
code: 
file = input("Enter the file name: ")
def getFileExtension(fileName):
    fileArray = fileName.split(".")
    tmpExtension = fileArray[len(fileArray) - 1] 
    return tmpExtension

result = getFileExtension(file)
print(f"The extension of the {file} is .{result}!!")
'''

'''
problem --- 5
q: Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
code: 
sample_seq = input("Enter the number of the sequence : ")


listOfTheSeq = sample_seq.split(",") 
newList = []
for num in listOfTheSeq:
    newList.append(num.strip())
    
print(newList)



'''


'''
problem --- 4
q: Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them

code: 
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print(lastName, firstName)

'''


'''
problem --- 3
Write a Python program that calculates the area of a circle based on the radius entered by the user.

code: 
radius = input("Enter the radius of the circle : ")
import math 
def getArea(r):
    area = math.pi * math.pow(float(r), 2)
    area = round(area, 3)
    return area
result = getArea(radius)
print(f"The area of the circle is : {result}, whose radius is {radius}")

'''


'''
problem --- 2 
Write a Python program to display the current date and time.

code:

import datetime 
current_date_time = datetime.datetime.now()
formatted_data_time = current_date_time.strftime("%Y-%M-%D %H:%M:%S")
print("current date and time:", formatted_data_time)
'''


'''
problem ---- 1
import sys 

print("python version", sys.version)
print("\n\npython version info", sys.version_info)

''' 
