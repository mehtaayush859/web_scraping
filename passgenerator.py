import random

print("Welcome to Password generator..!!! ")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = input("Enter amout of password you want..!\n")
number = int(number)

length = input('Give passowrd length you want\n')
length = int(length)

print("Here are some generated passwords..!!\n")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)

    print(passwords)