marks=int(input("enter obtain marks out of 100 :"))
if marks>=90 and marks<=100:
    print("grade O ")
elif marks>=80 and marks<90:
    print("grade A ")
elif marks>=70 and marks<80:
    print("grade B ")
elif marks>=55 and marks<70:
    print("grade C ")
elif marks>=40 and marks<55:
    print("grade D ")
elif marks>=0 and marks<40:
    print("you fail ")
else:
    ("enter valid marks ")