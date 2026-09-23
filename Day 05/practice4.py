ls=[1,4,9,16,25,36,49,64,81,100]

num=int(input("number to search:"))

i=0
while i<len(ls):
      if(ls[i]==num):
            print(num,"found at positon ",i)
            break
      i+=1
else:
      print("not present")