# initialization
F0 = 0
F1 = 1

n = input('How many Fibonacci elements you would like to display (n > 1): ')
n = int(n)


print('Selected n: ', n)


if n > 1:
    count = 0

    fibonacciSeq =  str(F0) + ' + ' + str(F1)


    while count < n - 1:
        newElement = F0 + F1
        F0 = F1
        F1 = newElement



        fibonacciSeq = fibonacciSeq + ' + '
        fibonacciSeq = fibonacciSeq + str(newElement)
        count =  count + 1

    print(fibonacciSeq)
