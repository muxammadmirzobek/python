word = "hello world !"
count = 0
for i in word:
    if i == "l":
        count += 1
        
print("count : ", count)
#/////////////////////////////////
#     <------ while ------->
#i = 5
#while i <= 15:
#    print(i)
#    i += 2
#/////////////////////////////////

for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i == 6:
        break
    print (i)
#//////////////////////////////////

found = None
for i in "hello":
    if i == "l":
        found = True
        break
    else: 
        found = False

print("javob : ", found)