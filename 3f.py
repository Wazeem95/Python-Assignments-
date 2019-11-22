dic = {
    'num1' : 12,
    'num2' : 15,
    'string':'Name',
    'char':'a',
    'num3' : 17,
    'num4':21,
}
check_key = input("Enter Key Name Check if exist or not")
flag = False
for i in dic.keys():
    if i == check_key:
        flag = True
        break

if flag:
    print("Given Key exist")
else:
    print("Given Key dose not exist")