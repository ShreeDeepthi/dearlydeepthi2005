f_ref = open("original.txt","w")
n = int(input("enter len of file:"))
for i in range(n):
    number = input("enter a number:")
    f_ref.write(number+"\n")
f_ref = open("original.txt","r")
e_n = open("evennumbers.txt","w")
o_n = open("oddnumbers.txt","w")
ec=oc=0
for i in f_ref:
    if int(i)%2 == 0:
        e_n.write(i+"\n")
        ec+=1
    else:
        o_n.write(i+"\n")
        oc+=1
print(ec)
print(oc)
f_ref.close()
e_n.close()
o_n.close()
f_ref = open("original.txt","r")
e_n = open("evennumbers.txt", "r")
o_n =open("oddnumbers.txt", "r") 
print("Contents of original.txt:")
print(f_ref.read())
print("Contents of evennumbers.txt:")
print(e_n.read())
print("Contents of oddnumbers.txt:")
print(o_n.read())
f_ref.close()
e_n.close()
o_n.close()