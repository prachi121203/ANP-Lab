sub1 = int(input("Enter marks of the first subject: "))
sub2 = int(input("Enter marks of the second subject: "))
sub3 = int(input("Enter marks of the third subject: "))
sub4 = int(input("Enter marks of the fourth subject: "))
sub5 = int(input("Enter marks of the fifth subject: "))
 
avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5
 
if avg >= 90:
    print("Grade: A")
elif avg >= 80 and avg < 90:
    print("Grade: B")
elif avg >= 70 and avg < 80:
    print("Grade: C")
elif avg >= 60 and avg < 70:
    print("Grade: D")
else:
    print("Grade: F")
