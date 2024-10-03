def check_list(stop_number):
    start = 0
    infinity = 10 ** 18
    result = list()
    for i in range(start, infinity):
        if (i != 0) and (i % len(str(i)) == 0):
            result.append(i)
            if len(result) == stop_number:
                return ' '.join([str(i) for i in result])



if __name__ == '__main__':
    N = input('введите N: ')
    while int(N):
        res = check_list(int(N))
        print('numbers:', res, sep='\n')
        N = input('введите N: ')
    