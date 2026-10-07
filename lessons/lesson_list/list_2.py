number = [5, 2, 7]
#////num = [3] = 100////
number.append(100)
number.insert(0, True)

b = [1, 3, 5, 6, 3.34, False]

number.extend(b)

#number.sort()
#number.reverse()
#number.pop(-1) 
number.remove(5)

#print(number.count(2))
print(len(number))