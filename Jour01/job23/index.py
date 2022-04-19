def triangle(number):
    for item in range(number ):
        ligne = number *2
        for i in range(ligne):
            if i ==  number - item - 1 :
                print('/', end = '')
            elif i == number +item  :
                print('\\', end = '')
            elif i == ligne -1:
                print(' ')
            else:
                if item == number -1:
                    print('_', end ='')
                else:
                    print(' ', end ='')


triangle(10)