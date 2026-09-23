ls=[1,4,9,16,25,36,49,64,81,100]

n=2
i=0
for e in ls:
      if(e==n):
            print("num found:",e,"at pos",i)
            break
      i+=1
            
else:
      print("no")