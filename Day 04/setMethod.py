collection=set()

collection.add(1)
collection.add(2)
collection.add(2)
collection.add(3)
collection.add("Hello")
collection.add(("nice","try"))

print(collection)

collection.remove(2)
print(collection)

collection.clear()
print(collection)

col={"hello","world","my","name","is"}
print(col.pop())
print(col.pop())
print(col.pop())


set1={1,2,3,4,5,6}
set2={5,6,7,8,9}
print(set1.union(set2))
print(set1.intersection(set2))
