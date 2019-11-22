dic = {
    'num1' : 12,
    'num2' : 15,
    'string':'Name',
    'char':'a',
    'num3' : 17,
    'num4':21,
}

sum = 0

for i in dic.values():
    if type(i) == int:
        sum +=i

print("Sum of all numeric items a dictionary is" , sum)