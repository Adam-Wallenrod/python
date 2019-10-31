file = open('result.txt', 'r')
rawData = file.readlines()
print('rawData: ', rawData)

dataList = []

for line in rawData:
    numberInt = int(line.rstrip())
    dataList = dataList + [numberInt]

print('new dataList: ', dataList)


n = len(dataList)


# Variable for storin data when making assignments
firstValue = 0
secondValue = 0
swapWasMade = False
done = False

print('before sorting: ', dataList)

while done == False:
    print('------------------------')

    for i in range(n):
        print('element: ', dataList[i])

        if (i == (n - 1)) and (swapWasMade == False):
            done = True
            print('End!!!')
            break

        if (i == (n - 1)):
            swapWasMade = False
            print('end of iteration')
            break


        if (dataList[i] > dataList[i+1]):
            firstValue = dataList[i]
            secondValue = dataList[i+1]
            dataList[i] = secondValue
            dataList[i+1] = firstValue
            swapWasMade = True
            print('swapWasMade: ', swapWasMade)


        print('i: ', i)



print('sorted data: ', dataList)

file.close()
