#technical test 5

def suma(n):
    try:
        if n >= 0 :
            aggregation = 0
            iterator = n
            n = [iterator, aggregation]
            return suma(n)
    except TypeError as TE:
        if n[0] != 0:
            n[1] = n[0] + n[1]
            n[0] -= 1
            return suma(n)
        else:
            return n[1]


if __name__ == '__main__':
    result = suma(5)
    print(result)