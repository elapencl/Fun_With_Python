def full_pyramid(number):
    k=number
    for i in range(number):

        for t in range(k,0,-1):
            print(' ', end=' ')
        k -= 1
        for j in range(0,2*i+1):
            print('*', end=' ')

        print(" ")

    return


full_pyramid(8)
