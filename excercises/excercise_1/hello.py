import random
s = 'Hello World!'
print(s)
x = 1988

if x == 1987:
    print(' thats right its 1987')

f = open("result.txt", "w+")


rangeStart = input("Range start: ")
rangeStartInt = int(rangeStart)
rangeEnd = input("Range end: ")
rangeEndInt =int(rangeEnd)



for i in range(10):
    randomInt = random.randint(rangeStartInt, rangeEndInt)
    f.write("%d,\n" % randomInt)
    print("Drawed number: %d\n " % randomInt)




f.close()
