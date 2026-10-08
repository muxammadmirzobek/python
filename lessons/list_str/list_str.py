word = 'futball, baskidbol, skate'

#print(len(word), "\n ")
#print(word.count('p'))

#print(word.upper())
#print(word.lower())
#print(word.capitalize())
#print(word.find('p'))

hobbiy = word.split(", ")
for i in range(len(hobbiy)):
    hobbiy[i] = hobbiy[i].capitalize()

result = ", ".join(hobbiy)
print(result)