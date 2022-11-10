# num1 = input("Ingresa el primer numero: ")
# num2 = input("ingresa el segundo numero: ")

# # sum of two numbers

# sum = float(num1) + float(num2)

# # display the sum

# print("La suma de {0} y {1} es {2}".format(num1, num2, sum))


# Python program to check if the input number is odd or even.

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#     print("{0} is Even".format(num))
# else:
#     print("{0} is Odd".format(num))

# Python program to check if the input year is a leap year or not

# year = int(input("Enter a year: "))
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print("{0} is a leap year".format(year))
#         else:
#             print("{0} is not a leap year".format(year))


# Python program to check if a number is positive, negative or zero

# num = float(input("Enter a number: "))

# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

# # Python program to check if a number is prime or not

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")


# # Python program to calculate year of birth

# current_year = 2022
# age = int(input("Enter your age: "))
# year_of_birth = current_year - age
# print("You were born in the year", year_of_birth)


# # python program to calculate the number of seconds in a given number of hours

# hours = int(input("Enter hours: "))
# seconds = hours * 60 * 60
# print("There are", seconds, "seconds in", hours, "hour(s)")

# # python program to calculate the number of minutes in a given number of seconds

# seconds = int(input("Enter seconds: "))
# minutes = seconds / 60
# print("There are", minutes, "minutes in", seconds, "seconds")

# # # python program to calculate the number of hours, minutes and seconds a person has lived

# age = int(input("Enter your age: "))
# seconds = age * 365 * 24 * 60 * 60
# minutes = age * 365 * 24 * 60
# hours = age * 365 * 24
# days = age * 365
# print("You have lived for", seconds, "seconds -",
#       minutes, "minutes -", hours, "hours -", days, "days")

# # python program to calculate the number of years, months and days a person has lived

# age = int(input("Enter your age: "))
# years = age
# months = age * 12
# weeks = age * 52
# days = age * 365
# print("You have lived for", years, "years -", months,
#       "months -", weeks, "weeks -", days, "days")


# # python program to calculate the number of days in a given number of years

# years = int(input("Enter years: "))
# days = years * 365
# print("There are", days, "days in", years, "year(s)")

# python program to reverse a string

# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print("The reversed string is:", reversed_string)


# python program to write a string n times

# string = input("Enter a string: ")
# n = int(input("How many times do you want to repeat the string? "))
# repeated_string = string * n
# print("The repeated string is:", repeated_string)

# python program to fetch time.is and display the time

# import time
# import datetime
# import pytz
# import requests

# url = "http://worldtimeapi.org/api/timezone/America/Costa_Rica"
# response = requests.get(url)
# data = response.json()
# time = data["datetime"]
# print("The time is:", time)

# # python program to keep showing the time until the user presses q

# import time
# import datetime
# import pytz
# import requests

# while True:
#     url = "http://worldtimeapi.org/api/timezone/America/Costa_Rica"
#     response = requests.get(url)
#     data = response.json()
#     time = data["datetime"]
#     print("The time is:", time)
#     if input("Press q to quit: ") == "q":
#         break


# python program to count slowly to 100 and print the numbers

# import time

# for i in range(1, 11):
#     print(i)
#     time.sleep(1)

#     if i == 10:
#         print("Done!")

# python program to count in reverse from 10 to 0 and print the numbers

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)

    if i == 0:
        print("Done!")
