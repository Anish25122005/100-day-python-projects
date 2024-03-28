from random import randint
import string
import random
final_password=""
length_of_passsword=int(input("length of password(8-16):"))
if(length_of_passsword>=8 and length_of_passsword<=16):
    while len(final_password)<=length_of_passsword:
        i=str(randint(0,9))
        final_password+=i
        j=random.choice(string.ascii_letters)
        final_password+=j
        k=chr(randint(0,50))
        final_password+=k
    print(f"your password is {final_password}")
elif(length_of_passsword<8):
    print("too small")
else:
    print("limit exceeded")