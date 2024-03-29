'''
    this is a temperature converter made using python
'''
temp=input(" you want to convert (F(farenheit to celsius)or C(celsius to farenheit)):")
if (temp.lower() =='f'):
    faren=float(input("enter temperature in farenheit:"))
    Cel=(faren-32)*(5/9)
    print(f'temperature in celsius is {Cel}')
elif (temp.lower() =='c'):
    celsius=float(input("enter temperature in celsius:"))
    faren=((9/5)*celsius) + 32
    print(f'temperature in farenheit is {faren}')
else:
    print("The program does not support that!!!")
print("thank you for using this converter")