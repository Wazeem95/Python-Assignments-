S1= float(input("Please Enter the marks obtained in Physic:    "))
S2= float(input("Please Enter the marks obtained in Chemistry: "))
S3= float(input("Please Enter the marks obtained in Biology:   "))
S4= float(input("Please Enter the marks obtained in English:   "))
S5= float(input("Please Enter the marks obtained in Urdu:      "))
total_marks_Obtained=T1= (S1 + S2 + S3 + S4 + S5)
total_marks=T2=500
print("Total marks Obtained in all subjects are: ", T1)
Percentage=P= int((T1/T2)* 100)
print("Percentage: ", P)
if P>=90:
    print("Grade: A1")
elif P>=80 and P<90:
    print("Grade: A")
elif P>=70 and P<80:
    print("Grade: B")
elif P>=60 and P<70:
    print("Grade: C")
elif P>=50 and P<60:
    print("Grade: D")
else:
    print ("Fail")