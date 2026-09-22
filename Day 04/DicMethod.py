student={
      "name":"Gaurav",
      "age":21,
      "score":{
            "chem":98,
            "phy":97,
            "math":96
      }
}

print("Student.keys")
print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))

print("Student.Values")
print(student.values())
print(list(student.values()))

print("student.items")
pairs=list(student.items())
print(pairs)

print("student.get")
print(student.get("score1"))
print(student.get("score"))


print("student.update")
#student.update({"city":"delhi"})
#OR
new_dic={"name":"Tejas","age":22}
student.update(new_dic)
print(student)