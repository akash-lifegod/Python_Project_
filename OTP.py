import random
n=random.random()
d=int(input("Enter no. of digits of OTP "))
OTP = str(n)[-d: ]
print(OTP)