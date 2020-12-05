#46. List
animals = ["Dog", "Bear", "Cat","Panda"]
for x in animals:
    print(x)
#48. Accessing elements in a list
animals = ["Dog", "Bear", "Cat","Panda"]
print(animals[1:2])
print(animals[-1])
animals[0] = "Puppy"
animals

#49. Lists Methods 1
fruits = ["orange","apple","grape", "berry"]
vegetable = ["broccoli","carrot"]

fruits.extend(vegetable)
print(fruits)

vegetable.append("bean")
print(vegetable)

fruits.sort() #default asc
print(fruits)
fruits.sort(reverse=True)
print(fruits)

fruits.count("orange")

#49. Lists Methods 2
print(fruits)
fruits.index("apple")

fruits.insert(0,"banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("orange")
print(fruits)

del vegetable
#print (vegetable)

#51. Tuple
fruits = ("grape","apple","berry")
print(fruits)

# for x in fruits:
#     print(x)
print(fruits[2])

animals = tuple(("lion","tiger","bear"))
print(animals)
print(animals[0],animals[2])

#animals[0] = "cheetah" #error --> tuple immutable

#53. Set
fruits = {"grape","orange","apple","tomato"}
type(fruits)

for x in fruits:
    print(x)

fruits = set(("grape","orange","apple","tomato"))
animals = set(("lion","bear","tiger"))
print(len(fruits))

#54 Set Method

#add()
fruits.add("mango")
print(fruits)

#update()
fruits.update(["kiwi","berry"])
print(fruits)
 
#remove()
fruits.remove("kiwi")
print(fruits)

#discard()
fruits.discard("kiwi")

#clear()
fruits.clear()
print(fruits)

#del()
del fruits