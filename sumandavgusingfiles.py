f = open("Numbers.txt", "w")
N = int(input("Enter a number to know no. of elements to be written to a file: "))
for i in range(N):
    num = input(f"Enter a number{i+1}: ")
    f.write(f"{num}\n")
f.close()
f = open("Numbers.txt", "r")
sum1 = 0
for i in f:
    sum1 += int(i)
print("Sum= ", sum1)
print("Average= ", sum1/N)
f.close()


    



    