
f_ref = open("original.txt","w")
f_ref.write("There is teacher who is Intelligent,Hard working,Freindly and Caring")
f_ref.close()
f_ref = open("original.txt","r")
paragraph = f_ref.read()
f_ref.close()
print("Original paragraph:")
print(paragraph)
f_ref = open("original.txt","w")
f_ref = open("original.txt","a")
s = paragraph.split()
print(s)
for i in s:
   k =i[ : :-1]
   x = k.capitalize()
   f_ref.write(x)
   f_ref.write(" ")
f_ref.close()
f_ref = open("original.txt","r")
print("Modified content of a file: ", f_ref.read())
f_ref.close()

