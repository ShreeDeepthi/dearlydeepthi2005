f = open("Numbers.txt","r")
sum = 0
for n in f :
    n = n.strip()
    sum = sum+int(n)
    avg = sum/int(n)*10
print(sum)
print(avg)
