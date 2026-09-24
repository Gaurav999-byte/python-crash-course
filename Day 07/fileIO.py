# f=open("D:\Python Crash Course\Day 07\demo.txt","r")
# data=f.read()
# #data=f.read(5)
# print(data)
# print(type(data))
# f.close

# f=open("D:\Python Crash Course\Day 07\demo.txt","r")
# line=f.readline()
# print(line)
# line1=f.readline()
# print(line1)
# f.close

# f=open("D:\Python Crash Course\Day 07\demo.txt","w")
# f.write("I want to learn javascript tommoroww 123")
# f.close

f=open("D:\Python Crash Course\Day 07\demo.txt","a")
f.write("then react js")
f.write("\n after that node js")
f.close