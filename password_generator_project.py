import random
characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRST0123456789!@#$%^&*_"
while(True):
    pass_length=int(input("Enter the length of password: "))
    pass_count=int(input("Enter the number of password you want:"))

    for i in range(pass_count):
        password=""
        for j in range(pass_length):
            pass_char=random.choice(characters)
            password=password+pass_char
        print("Your  password is :",password)
    repeat=input("Do you want to generate more password ? press => yes or no :")
    if( repeat=="no"):
        break
print("Thank you !")     