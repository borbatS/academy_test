def devision(a: int| float, b: int| float):
    if b == 0:
        raise ZeroDivisionError('ление на 0 невозможно')
    return a/b

def main():
    for i, j in enumerate([1, 2, 3], 0):
        try:
            d = devision(i, j)
        except ZeroDivisionError as e:
            print(e)
        else:
            print(d)


if __name__== "__main__":
    main()
