print("Lab-08")
print("Hassan Ahmed Inamdar 18B-080-CS, Sec-A")
print("Question 3(a)")
def even(n):
    for i in range(2,n):
        if i%2 == 0 and i%3 == 0:
            print(i,"This number is divisbile by 2 and 3.")
        elif i%2 == 0:
            print(i,"This number is divisble by 2.")
        elif i%3 == 0:
            print(i, "This number is divisible by 3")
even(17)

