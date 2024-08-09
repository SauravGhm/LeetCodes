result = []
path = [1,2,3]
result.append(path) #appends the references to the list 'path'
result.append(path[:]) #Appends a copy of the list 'path'

#Modify the original 'path'
path.pop()

#checking the contents of the result
print(result)

