list=["a","b","c","d","e"]
idx=len(list)-1

def printi(list,idx):
      if(idx==-1):
            return 0
      printi(list,idx-1)
      print(list[idx])

printi(list,idx)