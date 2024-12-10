# collection={}
# print(type(collection))
collection=set()
print(type(collection))
collection.add(1)
collection.add((1,2,3,4,4,))
collection.add("python")
collection.pop()
print(collection)
col={1,2,3,4,4,4,5,5,"a","w","d","water"}
print(col)
print(len(col))
print(col.pop())
print(col.pop())
set1={1,5,6,8,9,0,7,5,5,7,}
set2={3,34,5,5,66,7,8,88,3}
print(set1.union(set2))
print(set1.intersection(set2))