def build_star(number):
    for i in range(number):
        for j in range(0,i+1):
            print('*', end=' ')
        print()
    return


build_star(8)
