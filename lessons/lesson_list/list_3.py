n = int(input("enter the lenth : "))

i = 0

user_elm = []

while i < n:
    string = "element number" + str(i + 1) + " :"
    user_elm.append(input(string))
    i +=1
user_elm.sort()

print(user_elm      )